# Plan técnico — Guardrails, seguridad y anti-alucinación

> Spec: `spec.md` · Repositorio: BusTrack GenAI · Estado: Pendiente.

## 1. Estrategia técnica

Documentar el estado actual y el objetivo; implementar por incrementos con pruebas y sin romper contratos.

## 2. Arquitectura propuesta

- Stack objetivo: Python 3.11 + FastAPI + OpenAI API, con grounding obligatorio y guardrails.
- Componentes: Componentes del repositorio afectados por la spec.
- Tecnologías: FastAPI + OpenAI + reglas propias.

## 3. Componentes afectados

- Componentes del repositorio afectados por la spec

## 4. Estructura de archivos

```text
src/services/guardrails.py, GuardrailTest/
```

## 5. Dependencias

- specs/genai/contratos-grounding/
- specs/seguridad/

## 6. Consideraciones de seguridad

- Sanitización, guardrails anti prompt injection, sin PII en prompts/logs, límites de tokens y cero secretos en Git.

- Validar entradas y no registrar secretos/PII.

## 7. Riesgos

- Confundir el estado actual con el objetivo.
- Documentación genérica o desalineada.
- Dependencias entre repos no documentadas.

## 8. Estrategia de pruebas

Revisión de coherencia documental y, cuando exista código, pruebas unitarias, de contrato y seguridad.

## 9. Trazabilidad

Cada tarea de `task.md` referencia un requisito de `spec.md`. Los diagramas están en `chart.md`.
