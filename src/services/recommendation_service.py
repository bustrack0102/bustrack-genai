"""Grounded recommendation service using OpenAI SDK (Azure / GitHub Models) with fallback."""

from datetime import datetime, timezone
import json
from typing import Tuple
import uuid
from openai import OpenAI
from src.core.config import load_config
from src.core.schemas import (
    RecommendationCriteria,
    RecommendationRequest,
    RecommendationResponse,
    RouteCandidate,
)
from src.prompts.catalog import PROMPT_VERSION, SYSTEM_PROMPT_ES, build_user_prompt
from src.services.guardrails import (
    detect_prompt_injection,
    enforce_unit_budget,
    sanitize_pii,
    validate_grounding,
)


def select_best_candidate_deterministic(
    payload: RecommendationRequest,
) -> RouteCandidate:
    """Select the optimal route deterministically from the validated context."""
    priority = payload.preferencias.prioridadBusqueda
    candidates = payload.rutasCandidatas
    if priority == "menor_tiempo":
        return min(
            candidates,
            key=lambda r: (r.duracionEstimadaMin, r.tarifaMxn, -r.calificacionPromedio),
        )
    if priority == "menor_costo":
        return min(
            candidates,
            key=lambda r: (r.tarifaMxn, r.duracionEstimadaMin, -r.calificacionPromedio),
        )
    if priority == "mejor_calificacion":
        return max(
            candidates,
            key=lambda r: (
                r.calificacionPromedio,
                -r.duracionEstimadaMin,
                -r.tarifaMxn,
            ),
        )
    return min(
        candidates,
        key=lambda r: (
            r.duracionEstimadaMin * 0.4
            + r.tarifaMxn * 0.4
            - r.calificacionPromedio * 10.0
        ),
    )


def build_grounded_explanation(best: RouteCandidate, priority: str) -> str:
    """Create a strictly grounded explanation in Spanish from validated data."""
    horarios_txt = (
        f" con salidas programadas ({', '.join(best.horariosDisponibles[:3])})"
        if best.horariosDisponibles
        else ""
    )
    return (
        f"Se recomienda la ruta {best.rutaId} ({best.lineaNombre}) operada por "
        f"{best.empresaNombre} en {best.medioTransporte} desde {best.origenNombre} "
        f"hacia {best.destinoNombre}{horarios_txt}, con tarifa verificada de "
        f"${best.tarifaMxn:.2f} MXN, duracion estimada de {best.duracionEstimadaMin} "
        f"minutos y calificacion promedio de {best.calificacionPromedio:.1f}/5.0 "
        f"(criterio aplicado: {priority})."
    )


def _call_openai_grounded(user_prompt: str, valid_ids: list[str]) -> Tuple[str, str]:
    """Invoke OpenAI-compatible endpoint (Azure AI / GitHub Models) and verify grounding."""
    cfg = load_config()
    if not cfg.llm_credential:
        raise RuntimeError("No external LLM credential configured.")

    client = OpenAI(
        api_key=cfg.llm_credential,
        base_url=cfg.llm_base_url,
        timeout=cfg.request_timeout_seconds,
    )
    completion = client.chat.completions.create(
        model=cfg.llm_model,
        temperature=0.1,
        max_tokens=300,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_ES},
            {"role": "user", "content": user_prompt},
        ],
    )
    raw_content = completion.choices[0].message.content or "{}"
    parsed = json.loads(raw_content)
    rec_id = str(parsed.get("rutaRecomendadaId", "")).strip()
    explanation = sanitize_pii(str(parsed.get("explicacion", "")).strip())
    validate_grounding(rec_id, valid_ids)
    if not explanation:
        raise ValueError("Empty explanation from model.")
    return rec_id, explanation


def generate_recommendation(
    payload: RecommendationRequest,
) -> RecommendationResponse:
    """Execute full guardrail + grounding pipeline to produce a recommendation."""
    cfg = load_config()

    # 1. Input guardrails (Anti-Prompt-Injection & PII sanitization)
    detect_prompt_injection(payload.preferencias.notasAdicionales)
    for route in payload.rutasCandidatas:
        detect_prompt_injection(route.lineaNombre)
        detect_prompt_injection(route.empresaNombre)

    sanitized_notes = sanitize_pii(payload.preferencias.notasAdicionales)
    user_prompt = build_user_prompt(payload, sanitized_notes)
    full_prompt = f"{SYSTEM_PROMPT_ES}\n{user_prompt}"

    # 2. Enforce unit budget with tiktoken
    enforce_unit_budget(
        full_prompt, max_units=cfg.max_prompt_units, model_name=cfg.llm_model
    )

    valid_ids = [r.rutaId for r in payload.rutasCandidatas]
    route_map = {r.rutaId: r for r in payload.rutasCandidatas}

    # 3. Call LLM or use deterministic grounded engine
    try:
        chosen_id, explanation = _call_openai_grounded(user_prompt, valid_ids)
        chosen_route = route_map[chosen_id]
    except Exception:
        chosen_route = select_best_candidate_deterministic(payload)
        chosen_id = chosen_route.rutaId
        explanation = build_grounded_explanation(
            chosen_route, payload.preferencias.prioridadBusqueda
        )

    # 4. Final output grounding guardrail
    validate_grounding(chosen_id, valid_ids)

    return RecommendationResponse(
        recomendacionId=f"REC-{uuid.uuid4().hex[:8].upper()}",
        userId=sanitize_pii(payload.userId),
        destinoId=payload.destinoId,
        rutasEvaluadas=valid_ids,
        rutaRecomendadaId=chosen_id,
        criterios=RecommendationCriteria(
            puntualidad=chosen_route.calificacionPromedio,
            tarifaMxn=chosen_route.tarifaMxn,
            duracionEstimadaMin=chosen_route.duracionEstimadaMin,
            ajustePreferencia=payload.preferencias.prioridadBusqueda,
        ),
        explicacion=explanation,
        fechaGeneracion=datetime.now(timezone.utc).isoformat(),
        promptVersion=PROMPT_VERSION,
    )
