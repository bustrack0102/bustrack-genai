# Plan técnico — 14-endpoint-recommendations — Endpoint interno de recomendaciones

> Spec: `spec.md` · Endpoint: `POST /recommendations` · Estado: Propuesto.

## 1. Estrategia

Definir contrato, esquema de entrada/salida, validaciones y pruebas antes de implementar.

## 2. Diseño

- Stack objetivo: Python 3.11 + FastAPI + OpenAI API, con grounding obligatorio y guardrails.
- Componentes: controlador/router, servicio, repositorio o cliente HTTP.
- Tecnología: Python 3.11 + FastAPI + OpenAI API, con grounding obligatorio y guardrails.

## 3. Archivos

```text
src/api/routes.py, src/services/generation.py (futuro), specs/04-grounding-de-recomendaciones/
```

## 4. Seguridad

- Sanitización, guardrails anti prompt injection, sin PII en prompts/logs, límites de tokens y cero secretos en Git.
- Validar entradas y no registrar secretos/PII.

## 5. Errores

- Respuesta uniforme sin stack traces ni detalles internos.
- Registrar correlación sin datos sensibles.

## 6. Pruebas

Pruebas de contrato, validación, autenticación y errores cuando el endpoint exista; casos definidos mientras sea propuesto.

## 7. Riesgos

- Contrato desalineado con el consumidor.
- Errores no cubiertos.
- Exposición de datos sensibles.
