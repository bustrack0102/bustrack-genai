# Specs por tarea — BusTrack GenAI

> Cada carpeta numerada representa una tarea o funcionalidad concreta y contiene
> `spec.md`, `plan.md`, `task.md` y `chart.md`. Las categorías técnicas generales
> ya no viven aquí: CI/CD está en `../cicd/` y Azure en `../azure/`.
> El historial se conserva en `../docs/archivo-sdd/specs-anteriores/`.

## Tareas

| ID | Tarea | Estado |
|---|---|---|
| `01-configuracion-inicial-del-proyecto` | Configuración inicial del proyecto | Parcial |
| `02-arquitectura-base-fastapi` | Arquitectura base FastAPI | Pendiente |
| `03-contratos-de-contexto-validado` | Contratos de contexto validado | Pendiente |
| `04-grounding-de-recomendaciones` | Grounding de recomendaciones | Pendiente |
| `05-catalogo-de-prompts` | Catálogo de prompts | Pendiente |
| `06-generacion-de-explicaciones` | Generación de explicaciones | Pendiente |
| `07-guardrails-anti-prompt-injection` | Guardrails anti prompt injection | Pendiente |
| `08-control-de-tokens-y-costos` | Control de tokens y costos | Pendiente |
| `09-integracion-con-openai` | Integración con OpenAI API | Pendiente |
| `10-observabilidad-y-limites` | Observabilidad y límites del servicio | Pendiente |
| `11-empaquetado-docker` | Empaquetado Docker | Pendiente |
| `12-evaluacion-de-no-alucinacion` | Evaluación de no alucinación | Pendiente |

## Reglas

- No crear carpetas vacías ni specs genéricas para completar la estructura.
- No dividir una tarea en varias specs ni agrupar funcionalidades independientes.
- Una tarea pasa a `Implementado` solo con código y pruebas verificables.
- Los endpoints se documentan aparte, en `../specs-endpoints/`.
