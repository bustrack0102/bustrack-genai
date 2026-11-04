# Arquitectura Azure propuesta

> Repositorio: BusTrack GenAI · Ruta: `specs/azure/` · Estado: Propuesta · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `azure`
- **Nombre:** Arquitectura Azure propuesta
- **Repositorio:** BusTrack GenAI

## 2. Objetivo

Documentar la arquitectura Azure objetivo de Servicio de IA generativa sin declarar recursos desplegados.

## 3. Contexto

Servicio propuesto: Azure Container Apps o App Service Linux con contenedor FastAPI + Key Vault + Application Insights. Ningún recurso está desplegado.

## 4. Alcance

**Incluye:**

- Servicio recomendado y responsabilidad.
- Configuración y variables.
- Secretos y conectividad.
- Monitoreo, escalabilidad y costos estimados.

**No incluye:**

- Provisionar recursos.
- Publicar credenciales.
- Afirmar despliegue existente.

## 5. Requisitos funcionales

1. Identificar cada recurso y su responsabilidad.
2. Documentar variables de entorno.
3. Definir gestión de secretos y conectividad.
4. Definir monitoreo y escalabilidad.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- OpenAI API es el proveedor objetivo. Google GenAI queda inactivo y sujeto a aprobación.
- El servicio no expone endpoints públicos; solo es consumido por la API.
- La IA solo explica y recomienda sobre datos validados por la API.

## 8. Criterios de aceptación

- [ ] El documento distingue propuesta de estado real.
- [ ] Variables y secretos listados.
- [ ] Monitoreo y escalabilidad definidos.
- [ ] No hay afirmaciones de despliegue.

## 9. Restricciones

- No ejecutar migraciones ni despliegues en esta fase.
- No cambiar el stack objetivo sin autorización.
- No incluir secretos ni PII.

## 10. Dependencias

- `docs/contratos-integracion.md`
- specs/seguridad/

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
