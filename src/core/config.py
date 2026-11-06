"""Environment-based configuration for BusTrack GenAI service."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceConfig:
    """Immutable configuration loaded from environment variables."""

    service_name: str
    service_version: str
    environment: str
    llm_model: str
    llm_base_url: str
    llm_credential: str
    internal_credential: str
    max_prompt_units: int
    request_timeout_seconds: float


def load_config() -> ServiceConfig:
    """Load configuration from environment without hardcoded credentials."""
    return ServiceConfig(
        service_name=os.getenv("SERVICE_NAME", "bustrack-genai"),
        service_version=os.getenv("SERVICE_VERSION", "1.0.0"),
        environment=os.getenv("ENVIRONMENT", "production"),
        llm_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        llm_base_url=os.getenv(
            "OPENAI_BASE_URL", "https://models.inference.ai.azure.com"
        ),
        llm_credential=os.getenv("OPENAI_API_KEY", ""),
        internal_credential=os.getenv("INTERNAL_SERVICE_CREDENTIAL", ""),
        max_prompt_units=int(os.getenv("MAX_PROMPT_UNITS", "2048")),
        request_timeout_seconds=float(os.getenv("REQUEST_TIMEOUT_SECONDS", "15.0")),
    )
