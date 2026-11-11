# Endpoints — BusTrack GenAI (FastAPI interno)

> Fuente de contratos internos del servicio GenAI. Ningún cliente público (Flutter/React) accede directamente; solo la API central consume estos endpoints.

| Método | Ruta | Auth | Rate | Códigos | Spec |
|---|---|---|---|---|---|
| GET | `/health` | Interno | — | 200/503 | 13-endpoint-health |
| POST | `/recommendations` | X-Internal-Key / Bearer | — | 200/401/403/422/429/500 | 14-endpoint-recommendations |
