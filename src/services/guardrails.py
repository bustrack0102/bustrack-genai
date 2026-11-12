"""Guardrails against prompt injection, PII leakage, budget excess, and hallucination."""

import re
from typing import List, Optional
import tiktoken

INJECTION_PATTERNS = [
    re.compile(r"ignora\s+(todas\s+)?(las\s+)?instrucciones", re.IGNORECASE),
    re.compile(r"ignore\s+(all\s+)?(previous\s+)?instructions", re.IGNORECASE),
    re.compile(r"system\s*prompt", re.IGNORECASE),
    re.compile(r"olvida\s+tu\s+rol", re.IGNORECASE),
    re.compile(r"actua\s+como", re.IGNORECASE),
    re.compile(r"jailbreak", re.IGNORECASE),
]

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_REGEX = re.compile(r"\b(?:\+?52[-.\s]?)?(?:\d{2,3}[-.\s]?){2}\d{4}\b")


class GuardrailViolationError(ValueError):
    """Raised when an input or output violates a safety or grounding guardrail."""


class BudgetExceededError(ValueError):
    """Raised when the prompt exceeds the configured unit budget."""


def detect_prompt_injection(text: Optional[str]) -> None:
    """Raise GuardrailViolationError if prompt injection patterns are detected."""
    if not text:
        return
    for pattern in INJECTION_PATTERNS:
        if pattern.search(text):
            raise GuardrailViolationError(
                "Entrada rechazada por guardrail anti-prompt-injection."
            )


def sanitize_pii(text: Optional[str]) -> str:
    """Mask email addresses and phone numbers before sending text to an LLM."""
    if not text:
        return ""
    masked = EMAIL_REGEX.sub("[CORREO_OCULTO]", text)
    masked = PHONE_REGEX.sub("[TELEFONO_OCULTO]", masked)
    return masked.strip()


def count_prompt_units(text: str, model_name: str = "gpt-4o-mini") -> int:
    """Count prompt units using tiktoken with safe fallback."""
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def enforce_unit_budget(
    text: str, max_units: int, model_name: str = "gpt-4o-mini"
) -> int:
    """Verify that the prompt size stays within the allowed budget."""
    used = count_prompt_units(text, model_name=model_name)
    if used > max_units:
        raise BudgetExceededError(
            f"El contexto excede el limite permitido ({used} > {max_units})."
        )
    return used


def validate_grounding(recommended_route_id: str, valid_route_ids: List[str]) -> None:
    """Ensure the recommended route ID belongs to the validated route candidates."""
    if recommended_route_id not in valid_route_ids:
        raise GuardrailViolationError(
            f"Alucinacion bloqueada: ruta '{recommended_route_id}' fuera del contexto."
        )


ROUTE_CODE_PATTERN = re.compile(r"\bRUT-[A-Z0-9-]+\b", re.IGNORECASE)
URL_PATTERN = re.compile(r"https?://\S+", re.IGNORECASE)
UUID_PATTERN = re.compile(
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
    re.IGNORECASE,
)


def validate_explanation_grounding(
    explanation: str,
    valid_route_ids: List[str],
) -> None:
    """Block hallucinated route codes, external URLs, or unmasked PII inside prose."""
    if not explanation or not explanation.strip():
        raise GuardrailViolationError("Explicacion vacia rechazada por guardrail.")

    if URL_PATTERN.search(explanation):
        raise GuardrailViolationError(
            "Alucinacion bloqueada: URL externa no autorizada en explicacion."
        )

    valid_upper = {rid.upper() for rid in valid_route_ids}
    for match in ROUTE_CODE_PATTERN.findall(explanation):
        if match.upper() not in valid_upper:
            raise GuardrailViolationError(
                f"Alucinacion bloqueada: codigo '{match}' ausente del catalogo."
            )

    explanation_without_uuids = UUID_PATTERN.sub("[UUID]", explanation)
    if EMAIL_REGEX.search(explanation) or PHONE_REGEX.search(explanation_without_uuids):
        raise GuardrailViolationError(
            "Guardrail PII: la explicacion no debe contener datos personales."
        )
