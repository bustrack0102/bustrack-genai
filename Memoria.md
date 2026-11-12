# Memoria técnica — BusTrack GenAI

> Registro vivo. No se borra historial. Última actualización: 2026-11-05.

## 1. Estado real

- **Repositorio:** `bustrack-genai`
- **Tecnología actual:** Python 3.11+, FastAPI, OpenAI SDK (`gpt-4o-mini` vía Azure AI / GitHub Models con fallback determinista), `tiktoken`, `pytest`.
- **Tecnología objetivo:** Python 3.11 + FastAPI + OpenAI API, con grounding obligatorio y guardrails.
- **Git:** conectado a `https://github.com/bustrack0102/bustrack-genai.git`.

## 2. Funcionalidades implementadas

- Estructura completa `src/{api,core,prompts,services}` implementada y operativa:
  - `src/main.py`: App FastAPI, middleware `X-Correlation-ID` y manejadores de errores uniformes.
  - `src/core/{config.py,schemas.py,security.py}`: Configuración por entorno, esquemas Pydantic v2 validados y autenticación interna (`X-Internal-Key` / `Bearer`).
  - `src/prompts/catalog.py`: Catálogo versionado (`v1.0.0`) con reglas estrictas de grounding sobre `rutasCandidatas`.
  - `src/services/guardrails.py`: Detector anti-prompt-injection, sanitizador anti-PII (correos/teléfonos), control de presupuesto de tokens (`tiktoken`) y validador anti-alucinación (`rutaRecomendadaId` en `rutasEvaluadas`).
  - `src/services/recommendation_service.py`: Integración con OpenAI SDK (`gpt-4o-mini`) sobre Azure y motor determinista fundamentado de respaldo.
  - `src/api/routes.py`: Endpoints `GET /health` (`spec-13`) y `POST /recommendations` (`spec-14`).
- `Dockerfile` multietapa con usuario no-root (`appuser`) y `HEALTHCHECK` (`spec-11`).
- Suites de pruebas automatizadas en `UnitTest`, `GuardrailTest`, `IntegrationTest` y `SecurityTest`.

## 3. Funcionalidades pendientes

- Integración en vivo con el consumo HTTP desde `bustrack-api` en ambiente productivo.

## 4. Arquitectura actual

`src/{api,core,prompts,services}`; suites `UnitTest`, `IntegrationTest`, `GuardrailTest`, `SecurityTest`.

## 5. Migraciones

No aplica una migración de stack en este repositorio.

## 6. Decisiones arquitectónicas

- Se adopta SDD y DevSecOps.
- La API central es la fuente autorizada de datos.
- ML y GenAI son servicios internos FastAPI.
- OpenAI SDK (`gpt-4o-mini` vía Azure / GitHub Models) es el proveedor GenAI activo con respaldo determinista fundamentado.
- Ninguna recomendación puede referenciar un `rutaId` fuera de `rutasCandidatas`.

## 7. Dependencias entre repositorios

API central -> GenAI por HTTP interno; GenAI recibe contexto validado y devuelve texto fundamentado compatible con `BusTrackDB.recomendacionesIA`.

## 8. Problemas conocidos

- Ninguno bloqueante.

## 9. Historial

- **2026-10-29:** estructura SDD original y primeras fases.
- **2026-10-30:** auditoría completa, corrección documental y reorganización SDD.
- **2026-11-05:** implementación completa de FastAPI (`GET /health`, `POST /recommendations`), guardrails anti-prompt-injection, sanitización PII, control de tokens con `tiktoken`, validación de grounding, `Dockerfile` y suites `UnitTest`, `GuardrailTest`, `IntegrationTest` y `SecurityTest`.
- **2026-11-11:** alineación SDD y puerta automática en CI (`docs/endpoints.md` actualizado a `/health` y `/recommendations`, bloques `## Aprobación` y `checklists/pr.md` en `specs/` y `specs-endpoints/`, `scripts/check_sdd.ps1` validando `SDD-OK` en `.github/workflows/ci-pr.yml`).
- **2026-11-11 (Etapa 0 — v0.2.0 SemVer y CD ACR real):** agregada `docs/versionamiento.md` y reemplazado `az container restart` en `.github/workflows/cd-azure.yml` por build/push de `Dockerfile` a `bustrackacr0102` + despliegue real con `INTERNAL_SERVICE_CREDENTIAL`. Verificado local: `pytest -q` (11/11), `check_sdd.ps1` (`SDD-OK`).
