# Prompts, recomendaciones y explicaciones

> Repositorio: BusTrack GenAI · Ruta: `specs/genai/prompts-recomendaciones/` · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `genai/prompts-recomendaciones`
- **Nombre:** Prompts, recomendaciones y explicaciones
- **Repositorio:** BusTrack GenAI

## 2. Objetivo

Especificar prompts versionados y generación de recomendaciones/explicaciones fundamentadas.

## 3. Contexto

No existen prompts ni servicios.

## 4. Alcance

**Incluye:**

- Plantillas versionadas.
- Variables de contexto.
- Recomendaciones.
- Explicaciones en lenguaje natural.
- Control de tokens/costos.

**No incluye:**

- Sustituir datos de la API.
- Incluir PII.
- Usar Google GenAI como proveedor activo.

## 5. Requisitos funcionales

1. Los prompts solo reciben datos validados.
2. La salida debe ser explicable y referenciada.
3. No se inventan opciones.
4. Se controla el costo por tokens.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- OpenAI API es el proveedor objetivo. Google GenAI queda inactivo y sujeto a aprobación.
- El servicio no expone endpoints públicos; solo es consumido por la API.
- La IA solo explica y recomienda sobre datos validados por la API.

## 8. Criterios de aceptación

- [ ] Prompt versionado y documentado.
- [ ] Variables obligatorias validadas.
- [ ] Salida con referencias.
- [ ] Pruebas de no alucinación.

## 9. Restricciones

- No declarar prompts implementados.
- No usar datos reales en ejemplos.

## 10. Dependencias

- specs/genai/contratos-grounding/
- specs/genai/guardrails/

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
