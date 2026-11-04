# Cierre de sesión / revocación interna

> Repositorio: BusTrack GenAI · Ruta: `specs/endpoints/logout/` · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `endpoints/logout`
- **Nombre:** Cierre de sesión / revocación interna
- **Repositorio:** BusTrack GenAI

## 2. Objetivo

Documentar la revocación de credenciales internas de Servicio de IA generativa.

## 3. Contexto

No expone login público; se autentica internamente y solo la API puede invocarlo.

## 4. Alcance

**Incluye:**

- Revocación de credencial interna.
- Rotación.
- Errores y reintentos.

**No incluye:**

- Logout de usuario final.

## 5. Requisitos funcionales

1. Permitir rotar/revocar la credencial interna.
2. No dejar credenciales en logs.
3. Rechazar credenciales revocadas.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- OpenAI API es el proveedor objetivo. Google GenAI queda inactivo y sujeto a aprobación.
- El servicio no expone endpoints públicos; solo es consumido por la API.
- La IA solo explica y recomienda sobre datos validados por la API.

## 8. Criterios de aceptación

- [ ] Credencial revocada deja de funcionar.
- [ ] No hay logout de usuario final.
- [ ] Sin secretos en logs.

## 9. Restricciones

- No ejecutar migraciones ni despliegues en esta fase.
- No cambiar el stack objetivo sin autorización.
- No incluir secretos ni PII.

## 10. Dependencias

- API central
- `docs/contratos-integracion.md`

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
