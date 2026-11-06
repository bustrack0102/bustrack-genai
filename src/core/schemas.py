"""Validated Pydantic contracts for BusTrack GenAI service."""

from typing import List, Literal, Optional
from pydantic import BaseModel, Field, field_validator


class RouteCandidate(BaseModel):
    """Validated route candidate supplied by the central BusTrack API."""

    rutaId: str = Field(..., min_length=2, max_length=64)
    lineaNombre: str = Field(..., min_length=2, max_length=120)
    empresaId: str = Field(..., min_length=2, max_length=64)
    empresaNombre: str = Field(..., min_length=2, max_length=120)
    medioTransporte: str = Field(..., min_length=2, max_length=64)
    origenNombre: str = Field(..., min_length=2, max_length=120)
    destinoNombre: str = Field(..., min_length=2, max_length=120)
    tarifaMxn: float = Field(..., ge=0.0, le=5000.0)
    duracionEstimadaMin: int = Field(..., ge=1, le=1440)
    calificacionPromedio: float = Field(default=4.0, ge=0.0, le=5.0)
    horariosDisponibles: List[str] = Field(default_factory=list)
    paradasOrdenadas: List[str] = Field(default_factory=list)


class UserPreferences(BaseModel):
    """User search preferences without PII."""

    prioridadBusqueda: Literal[
        "menor_tiempo", "menor_costo", "mejor_calificacion", "equilibrado"
    ] = "equilibrado"
    idioma: str = Field(default="es-MX", max_length=16)
    notasAdicionales: Optional[str] = Field(default=None, max_length=280)


class RecommendationRequest(BaseModel):
    """Input payload for POST /recommendations."""

    userId: str = Field(..., min_length=2, max_length=64)
    destinoId: str = Field(..., min_length=2, max_length=64)
    preferencias: UserPreferences = Field(default_factory=UserPreferences)
    rutasCandidatas: List[RouteCandidate] = Field(..., min_length=1, max_length=20)

    @field_validator("rutasCandidatas")
    @classmethod
    def ensure_unique_routes(
        cls, candidates: List[RouteCandidate]
    ) -> List[RouteCandidate]:
        seen = set()
        for item in candidates:
            if item.rutaId in seen:
                raise ValueError(f"Duplicate rutaId in context: {item.rutaId}")
            seen.add(item.rutaId)
        return candidates


class RecommendationCriteria(BaseModel):
    """Explainable decision criteria stored in BusTrackDB.recomendacionesIA."""

    puntualidad: float = Field(..., ge=0.0, le=5.0)
    tarifaMxn: float = Field(..., ge=0.0)
    duracionEstimadaMin: int = Field(..., ge=1)
    ajustePreferencia: str


class RecommendationResponse(BaseModel):
    """Output payload aligned with BusTrackDB.recomendacionesIA collection."""

    recomendacionId: str
    userId: str
    destinoId: str
    rutasEvaluadas: List[str]
    rutaRecomendadaId: str
    criterios: RecommendationCriteria
    explicacion: str
    fechaGeneracion: str
    promptVersion: str


class HealthResponse(BaseModel):
    """Output payload for GET /health."""

    status: Literal["healthy", "unhealthy"]
    service: str
    version: str
