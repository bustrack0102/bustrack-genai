"""Integration tests for GET /health and POST /recommendations endpoints."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_endpoint_returns_healthy() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "healthy"
    assert body["service"] == "bustrack-genai"
    assert "X-Correlation-ID" in response.headers


def test_recommendations_endpoint_returns_grounded_response() -> None:
    payload = {
        "userId": "USR-001",
        "destinoId": "DST-UTTT",
        "preferencias": {
            "prioridadBusqueda": "menor_tiempo",
            "idioma": "es-MX",
            "notasAdicionales": "Viaje matutino hacia la universidad",
        },
        "rutasCandidatas": [
            {
                "rutaId": "RUT-001-IDA",
                "lineaNombre": "Tula - Pachuca",
                "empresaId": "EMP-AVM",
                "empresaNombre": "Autotransportes Valle del Mezquital (AVM)",
                "medioTransporte": "autobus",
                "origenNombre": "Central de Autobuses de Tula",
                "destinoNombre": "Central de Autobuses de Pachuca",
                "tarifaMxn": 60.0,
                "duracionEstimadaMin": 95,
                "calificacionPromedio": 4.5,
                "horariosDisponibles": ["06:30", "08:00"],
                "paradasOrdenadas": [
                    "PAR-TULA-01",
                    "PAR-ATIT-02",
                    "PAR-AJAC-03",
                    "PAR-PACH-04",
                ],
            }
        ],
    }
    response = client.post("/recommendations", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["rutaRecomendadaId"] == "RUT-001-IDA"
    assert "RUT-001-IDA" in data["rutasEvaluadas"]
    assert data["criterios"]["tarifaMxn"] == 60.0
    assert "RUT-001-IDA" in data["explicacion"]
