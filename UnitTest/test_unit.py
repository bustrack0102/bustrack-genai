"""Unit tests for schemas, deterministic selection, and prompt catalog."""

import pytest
from pydantic import ValidationError
from src.core.schemas import (
    RecommendationRequest,
    RouteCandidate,
    UserPreferences,
)
from src.prompts.catalog import PROMPT_VERSION, build_user_prompt
from src.services.recommendation_service import select_best_candidate_deterministic


def _sample_candidates() -> list[RouteCandidate]:
    return [
        RouteCandidate(
            rutaId="RUT-001-IDA",
            lineaNombre="Tula - Pachuca",
            empresaId="EMP-AVM",
            empresaNombre="AVM",
            medioTransporte="autobus",
            origenNombre="Central Tula",
            destinoNombre="Central Pachuca",
            tarifaMxn=60.0,
            duracionEstimadaMin=95,
            calificacionPromedio=4.5,
            horariosDisponibles=["06:30", "08:00"],
            paradasOrdenadas=["PAR-TULA-01", "PAR-ATIT-02", "PAR-PACH-04"],
        ),
        RouteCandidate(
            rutaId="RUT-002-IDA",
            lineaNombre="Tula - Pachuca Economico",
            empresaId="EMP-LUSA",
            empresaNombre="LUSA",
            medioTransporte="autobus",
            origenNombre="Central Tula",
            destinoNombre="Central Pachuca",
            tarifaMxn=48.0,
            duracionEstimadaMin=120,
            calificacionPromedio=4.1,
            horariosDisponibles=["07:00"],
            paradasOrdenadas=["PAR-TULA-01", "PAR-AJAC-03", "PAR-PACH-04"],
        ),
    ]


def test_deterministic_selection_by_priority() -> None:
    req_fast = RecommendationRequest(
        userId="USR-001",
        destinoId="DST-UTTT",
        preferencias=UserPreferences(prioridadBusqueda="menor_tiempo"),
        rutasCandidatas=_sample_candidates(),
    )
    best_fast = select_best_candidate_deterministic(req_fast)
    assert best_fast.rutaId == "RUT-001-IDA"

    req_cheap = RecommendationRequest(
        userId="USR-001",
        destinoId="DST-UTTT",
        preferencias=UserPreferences(prioridadBusqueda="menor_costo"),
        rutasCandidatas=_sample_candidates(),
    )
    best_cheap = select_best_candidate_deterministic(req_cheap)
    assert best_cheap.rutaId == "RUT-002-IDA"


def test_duplicate_route_ids_rejected() -> None:
    dup = _sample_candidates()[0]
    with pytest.raises(ValidationError):
        RecommendationRequest(
            userId="USR-001",
            destinoId="DST-UTTT",
            rutasCandidatas=[dup, dup],
        )


def test_prompt_catalog_builds_valid_json() -> None:
    req = RecommendationRequest(
        userId="USR-001",
        destinoId="DST-UTTT",
        rutasCandidatas=_sample_candidates(),
    )
    prompt_str = build_user_prompt(req, "Sin notas")
    assert "RUT-001-IDA" in prompt_str
    assert PROMPT_VERSION == "1.0.0"
