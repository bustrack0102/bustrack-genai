# 02-arquitectura-base-fastapi — Arquitectura base FastAPI

> Repositorio: BusTrack GenAI · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Objetivo

Definir la app FastAPI: routers, configuración, errores y arranque.

## 2. Contexto

No hay código FastAPI.

## 3. Alcance

**Incluye:**

- App y routers.
- Configuración.
- Errores uniformes.
- Arranque y health.

**No incluye:**

- Cambiar el stack objetivo.
- Desplegar recursos o ejecutar migraciones en esta fase.

## 4. Requisitos funcionales

1. Separar api/core/prompts/services.
2. Configuración por entorno.
3. Errores sin internals.
4. Health check.

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
