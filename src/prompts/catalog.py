"""Versioned prompt catalog enforcing strict grounding and no hallucination."""

import json
from src.core.schemas import RecommendationRequest

PROMPT_VERSION = "1.0.0"

SYSTEM_PROMPT_ES = (
    "Eres el motor de recomendaciones explicables de BusTrack para la region "
    "Tula - Tepeji - Pachuca. "
    "REGLAS ESTRICTAS DE GROUNDING:\n"
    "1. Solo puedes recomendar una ruta cuyo 'rutaId' exista exactamente dentro de "
    "la lista 'rutasCandidatas' proporcionada en el contexto.\n"
    "2. Esta estrictamente prohibido inventar rutas, paradas, horarios, tarifas, "
    "empresas o tiempos de recorrido.\n"
    "3. No incluyas datos personales (PII) en la respuesta.\n"
    "4. Responde UNICAMENTE con un objeto JSON valido con las claves: "
    "'rutaRecomendadaId' (string) y 'explicacion' (string en espanol claro, "
    "mencionando empresa, tarifa y duracion del contexto validado)."
)


def build_user_prompt(payload: RecommendationRequest, sanitized_notes: str) -> str:
    """Build structured user prompt from validated route context."""
    routes_data = [
        {
            "rutaId": r.rutaId,
            "lineaNombre": r.lineaNombre,
            "empresaNombre": r.empresaNombre,
            "medioTransporte": r.medioTransporte,
            "origenNombre": r.origenNombre,
            "destinoNombre": r.destinoNombre,
            "tarifaMxn": r.tarifaMxn,
            "duracionEstimadaMin": r.duracionEstimadaMin,
            "calificacionPromedio": r.calificacionPromedio,
            "horariosDisponibles": r.horariosDisponibles[:5],
            "paradasOrdenadas": r.paradasOrdenadas[:10],
        }
        for r in payload.rutasCandidatas
    ]
    context_obj = {
        "destinoId": payload.destinoId,
        "prioridadBusqueda": payload.preferencias.prioridadBusqueda,
        "notas": sanitized_notes,
        "rutasCandidatas": routes_data,
    }
    return json.dumps(context_obj, ensure_ascii=False)
