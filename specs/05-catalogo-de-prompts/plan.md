# Plan técnico — 05-catalogo-de-prompts — Catálogo de prompts

> Spec: `spec.md` · Repositorio: BusTrack GenAI · Estado: Pendiente.

## 1. Estrategia

Implementar por incrementos, conservando contratos y midiendo con pruebas antes de avanzar.

## 2. Arquitectura y componentes

- Stack objetivo: Python 3.11 + FastAPI + OpenAI API, con grounding obligatorio y guardrails.
- Componentes: componentes del repositorio afectados por la tarea.
- Tecnología: Python 3.11 + FastAPI + OpenAI API, con grounding obligatorio y guardrails.

## 3. Archivos y estructura

```text
src/prompts/ (futuro)
```

## 4. Seguridad

- Sanitización, guardrails anti prompt injection, sin PII en prompts/logs, límites de tokens y cero secretos en Git.
- Validar entradas y no registrar secretos/PII.

## 5. Riesgos

- Confundir el estado actual con el objetivo.
- Dependencias con otros repositorios no documentadas.
- Ampliar el alcance sin spec aprobada.

## 6. Estrategia de pruebas

Pruebas unitarias y de contrato cuando exista código; revisión documental mientras la tarea sea propuesta.

## 7. Trazabilidad

Cada tarea de `task.md` referencia un requisito de `spec.md`; los diagramas viven en `chart.md`.
