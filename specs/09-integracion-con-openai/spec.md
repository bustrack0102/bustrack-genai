# 09-integracion-con-openai — Integración con OpenAI API

> Repositorio: BusTrack GenAI · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Objetivo

Integrar OpenAI como proveedor activo con manejo de errores y timeouts.

## 2. Contexto

No hay integración; Google GenAI queda inactivo.

## 3. Alcance

**Incluye:**

- Cliente OpenAI.
- Modelo.
- Timeouts.
- Reintentos controlados.

**No incluye:**

- Cambiar el stack objetivo.
- Desplegar recursos o ejecutar migraciones en esta fase.

## 4. Requisitos funcionales

1. Clave solo en entorno/Key Vault.
2. Timeout y reintento acotados.
3. Errores sin internals.
4. Sin PII en prompts.

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
