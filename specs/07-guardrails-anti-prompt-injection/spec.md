# 07-guardrails-anti-prompt-injection — Guardrails anti prompt injection

> Repositorio: BusTrack GenAI · Estado: Implementado · Fecha: 2026-11-11.

## 1. Objetivo

Detectar y neutralizar inyección de prompts y fugas de datos.

## 2. Contexto

No implementado.

## 3. Alcance

**Incluye:**

- Sanitización.
- Detección de inyección.
- Delimitación de contexto.
- Respuesta segura.

**No incluye:**

- Cambiar el stack objetivo.
- Desplegar recursos o ejecutar migraciones en esta fase.

## 4. Requisitos funcionales

1. No concatenar entrada cruda en system prompt.
2. Delimitar contexto.
3. Rechazar o limitar entradas sospechosas.
4. No filtrar claves.

## 5. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad tarea -> prueba -> evidencia.

## 6. Reglas de negocio

- OpenAI API es el proveedor objetivo. Google GenAI queda inactivo y sujeto a aprobación.
- El servicio no expone endpoints públicos; solo es consumido por la API.
- La IA solo explica y recomienda sobre datos validados por la API.

## 7. Criterios de aceptación

- [ ] La tarea tiene criterios verificables y evidencia asociada.
- [ ] No se declara implementado lo que no existe en código o pruebas.
- [ ] Los contratos consumidos o expuestos quedan documentados.
- [ ] `Memoria.md` refleja el estado resultante.

## 8. Dependencias

- `constitution.md`
- `docs/contratos-integracion.md`

## 9. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.

## Aprobación

- [x] Revisión de arquitectura y contrato realizada — fecha: 2026-11-11
- [x] CHECKLIST_PR.md validado
- [x] Sin conflicto con constitution.md
