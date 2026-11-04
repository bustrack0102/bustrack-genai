# Contratos y grounding de datos validados

> Repositorio: BusTrack GenAI · Ruta: `specs/genai/contratos-grounding/` · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `genai/contratos-grounding`
- **Nombre:** Contratos y grounding de datos validados
- **Repositorio:** BusTrack GenAI

## 2. Objetivo

Especificar contratos internos y grounding obligatorio del servicio GenAI.

## 3. Contexto

La IA solo puede explicar/recomendar sobre datos validados por la API.

## 4. Alcance

**Incluye:**

- Contrato de entrada con contexto validado.
- Contrato de salida con texto fundamentado.
- Referencias a datos de origen.
- Rechazo de contexto incompleto.

**No incluye:**

- Generar datos de transporte.
- Consultar Cosmos directamente.
- Sustituir a la API.

## 5. Requisitos funcionales

1. Toda recomendación referencia datos de entrada.
2. Si falta contexto, no se inventa: se responde con limitación.
3. El texto no incluye datos ausentes del contexto.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- OpenAI API es el proveedor objetivo. Google GenAI queda inactivo y sujeto a aprobación.
- El servicio no expone endpoints públicos; solo es consumido por la API.
- La IA solo explica y recomienda sobre datos validados por la API.

## 8. Criterios de aceptación

- [ ] Contrato documentado.
- [ ] Contexto vacío produce respuesta segura.
- [ ] Salida incluye referencias.
- [ ] Pruebas de grounding.

## 9. Restricciones

- No declarar implementación existente.
- No inventar endpoints.

## 10. Dependencias

- docs/contratos-integracion.md
- specs/genai/prompts-recomendaciones/

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
