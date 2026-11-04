# Guardrails, seguridad y anti-alucinación

> Repositorio: BusTrack GenAI · Ruta: `specs/genai/guardrails/` · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `genai/guardrails`
- **Nombre:** Guardrails, seguridad y anti-alucinación
- **Repositorio:** BusTrack GenAI

## 2. Objetivo

Especificar guardrails contra prompt injection, fuga de datos y alucinaciones.

## 3. Contexto

El servicio manejará entradas de usuario indirectas y datos de la API.

## 4. Alcance

**Incluye:**

- Sanitización de entrada.
- Detección de prompt injection/jailbreak.
- Límites de tokens y tiempo.
- Verificación de grounding.
- Manejo seguro de errores.

**No incluye:**

- Filtrar contenido por criterios no documentados.
- Garantizar verdad absoluta.
- Registrar PII.

## 5. Requisitos funcionales

1. La entrada nunca se concatena cruda en el system prompt.
2. El contexto se delimita y valida.
3. Si no hay datos, no se inventa.
4. Los errores no filtran internals.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- OpenAI API es el proveedor objetivo. Google GenAI queda inactivo y sujeto a aprobación.
- El servicio no expone endpoints públicos; solo es consumido por la API.
- La IA solo explica y recomienda sobre datos validados por la API.

## 8. Criterios de aceptación

- [ ] Suite GuardrailTest ejecutable.
- [ ] Casos de inyección cubiertos.
- [ ] Grounding verificado.
- [ ] Sin fugas de claves.

## 9. Restricciones

- No declarar guardrails implementados.
- No inventar modelos de moderación.

## 10. Dependencias

- specs/genai/contratos-grounding/
- specs/seguridad/

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
