# 01-configuracion-inicial-del-proyecto — Configuración inicial del proyecto

> Repositorio: BusTrack GenAI · Estado: Parcial · Fecha: 2026-10-30.

## 1. Objetivo

Dejar el servicio Python/FastAPI configurable, con dependencias y estructura reproducible.

## 2. Contexto

Existe requirements.txt y carpetas src/{api,core,prompts,services} con solo .gitkeep; no hay código.

## 3. Alcance

**Incluye:**

- requirements.txt.
- Estructura src/.
- Configuración por entorno.
- Comandos de lint/test.

**No incluye:**

- Cambiar el stack objetivo.
- Desplegar recursos o ejecutar migraciones en esta fase.

## 4. Requisitos funcionales

1. Instalación reproducible.
2. Sin secretos en el repositorio.
3. Configuración por entorno.
4. Comandos documentados.

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
