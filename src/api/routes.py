"""HTTP endpoints for BusTrack GenAI service (GET /health, POST /recommendations)."""

from fastapi import APIRouter, Depends, HTTPException, status
from src.core.config import load_config
from src.core.schemas import (
    HealthResponse,
    RecommendationRequest,
    RecommendationResponse,
)
from src.core.security import verify_internal_caller
from src.services.guardrails import BudgetExceededError, GuardrailViolationError
from src.services.recommendation_service import generate_recommendation

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
def get_health() -> HealthResponse:
    """Return internal service health status without exposing internal details."""
    cfg = load_config()
    return HealthResponse(
        status="healthy",
        service=cfg.service_name,
        version=cfg.service_version,
    )


@router.post(
    "/recommendations",
    response_model=RecommendationResponse,
    dependencies=[Depends(verify_internal_caller)],
    tags=["Recommendations"],
)
def post_recommendations(
    payload: RecommendationRequest,
) -> RecommendationResponse:
    """Generate a grounded route explanation from validated API context."""
    try:
        return generate_recommendation(payload)
    except GuardrailViolationError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc
    except BudgetExceededError as exc:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=str(exc),
        ) from exc
