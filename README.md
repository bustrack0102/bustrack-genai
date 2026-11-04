# BusTrack GenAI — BusTrack

> Sistema de consulta y planificación de transporte público — Universidad Tecnológica de Tula-Tepeji.
> SDD + DevSecOps. Este README describe el **estado real** y la **arquitectura objetivo**.

## Estado actual

- **Tecnología real:** Python 3.11, FastAPI, OpenAI SDK, Google GenAI SDK, tiktoken, pytest (esqueleto sin código).
- **Tecnología objetivo:** Python 3.11 + FastAPI + OpenAI API, con grounding obligatorio y guardrails.
- **Implementado:** ver lista en `Memoria.md`.
- **No implementado:** ver pendientes en `Memoria.md`.
- **Recursos Azure:** no desplegados; propuesta en `azure/`.

## Qué hace este repositorio

API central -> GenAI por HTTP interno; GenAI recibe contexto validado y devuelve texto fundamentado.

## Estructura

```text
src/{api,core,prompts,services}; suites UnitTest, IntegrationTest, GuardrailTest, SecurityTest
```

## Gobernanza SDD

| Documento | Propósito |
|---|---|
| `constitution.md` | Principios inalterables del repositorio. |
| `AGENTS.md` | Instrucciones para agentes de IA. |
| `Memoria.md` | Estado real, decisiones y deuda técnica. |
| `CHECKLIST_PR.md` | Controles obligatorios de PR. |
| `specs/` | Specs canónicas (`spec.md`, `plan.md`, `task.md`, `chart.md`). |
| `docs/contratos-integracion.md` | Contratos con los demás repositorios. |
| `.opencode/` | Agentes y skills específicos. |
| `.semgrep/` | Reglas SAST reales. |
| `.github/workflows/` | CI por stack. |

## Specs por tarea

- `specs/01-configuracion-inicial-del-proyecto/` — Configuración inicial del proyecto (Parcial).
- `specs/02-arquitectura-base-fastapi/` — Arquitectura base FastAPI (Pendiente).
- `specs/03-contratos-de-contexto-validado/` — Contratos de contexto validado (Pendiente).
- `specs/04-grounding-de-recomendaciones/` — Grounding de recomendaciones (Pendiente).
- `specs/05-catalogo-de-prompts/` — Catálogo de prompts (Pendiente).
- `specs/06-generacion-de-explicaciones/` — Generación de explicaciones (Pendiente).
- `specs/07-guardrails-anti-prompt-injection/` — Guardrails anti prompt injection (Pendiente).
- `specs/08-control-de-tokens-y-costos/` — Control de tokens y costos (Pendiente).
- `specs/09-integracion-con-openai/` — Integración con OpenAI API (Pendiente).
- `specs/10-observabilidad-y-limites/` — Observabilidad y límites del servicio (Pendiente).
- `specs/11-empaquetado-docker/` — Empaquetado Docker (Pendiente).
- `specs/12-evaluacion-de-no-alucinacion/` — Evaluación de no alucinación (Pendiente).

## Specs de endpoints

- `specs-endpoints/13-endpoint-health/` — `GET /health` (Propuesto).
- `specs-endpoints/14-endpoint-recommendations/` — `POST /recommendations` (Propuesto).

## CI/CD y Azure

- `cicd/` — arquitectura del pipeline y gates.
- `azure/` — arquitectura final de despliegue (propuesta).

El historial de la organización anterior está en `docs/archivo-sdd/specs-anteriores/`.

## Comandos

```text
pip install -r requirements.txt
black --check src UnitTest IntegrationTest GuardrailTest SecurityTest && flake8 src UnitTest IntegrationTest GuardrailTest SecurityTest
pytest UnitTest IntegrationTest GuardrailTest SecurityTest
```

## Limitaciones y advertencias

- No se declara funcionalidad terminada sin código y pruebas.
- El árbol está anidado `X-main/X-main`; la raíz real es la carpeta interior.
- No hay repositorio Git local, por lo que tags/releases no son verificables.
- No hay despliegue Azure ni recursos provisionados.

## Equipo

Fátima Ximena García González, Diego Parra Cruz, José de Jesús López Islas, Melanie Joliee Bonilla Domínguez.
