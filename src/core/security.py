"""Internal service authentication for BusTrack GenAI."""

import hmac
from typing import Optional
from fastapi import Header, HTTPException, status
from src.core.config import load_config


def verify_internal_caller(
    x_internal_key: Optional[str] = Header(default=None, alias="X-Internal-Key"),
    authorization: Optional[str] = Header(default=None, alias="Authorization"),
) -> None:
    """Validate internal credential supplied by the central BusTrack API."""
    cfg = load_config()
    expected = cfg.internal_credential.strip()
    if not expected:
        return

    provided = ""
    if x_internal_key:
        provided = x_internal_key.strip()
    elif authorization and authorization.lower().startswith("bearer "):
        provided = authorization[7:].strip()

    if not provided:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credencial interna ausente.",
        )

    if not hmac.compare_digest(provided, expected):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Credencial interna invalida.",
        )
