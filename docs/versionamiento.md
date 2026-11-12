# Matriz de Versionamiento SemVer — BusTrack GenAI (Requisito 11 y 15)

Ver matriz maestra unificada en `bustrack-api/docs/versionamiento.md`.

| Hito | SemVer | Prompt Catalog | Docker Tag (`bustrackacr0102`) | Contrato Interno |
|---|---|---|---|---|
| Línea Base | `0.1.0` | `v1` | `0.1.0-{sha}` | `GET /health`, `POST /recommendations` |
| **Etapa 0** | `0.2.0` | `v1` | `0.2.0-{sha}` | Dockerfile real + CD ACR + Guardrails/pytest |
| **Etapa 3** | `0.8.0` | `v2` (grounding estricto) | `0.8.0-{sha}` | Integración E2E con API + historial/feedback |
| **Etapa 4** | `0.9.0` | `v2` | `0.9.0-{sha}` | Container App interno + App Insights |
| **Etapa 5** | `1.0.0` | `v2` | `1.0.0-{sha}` | Liberación Evaluación Final |
