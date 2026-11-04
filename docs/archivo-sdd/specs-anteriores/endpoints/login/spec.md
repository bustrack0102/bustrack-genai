# Autenticación interna (sin login público)

> Repositorio: BusTrack GenAI · Ruta: `specs/endpoints/login/` · Estado: Pendiente · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `endpoints/login`
- **Nombre:** Autenticación interna (sin login público)
- **Repositorio:** BusTrack GenAI

## 2. Objetivo

Documentar por qué Servicio de IA generativa no expone login público y cómo se autentica internamente.

## 3. Contexto

No expone login público; se autentica internamente y solo la API puede invocarlo.

## 4. Alcance

**Incluye:**

- Autenticación servicio-a-servicio.
- Rechazo de llamadas no autorizadas.
- Rotación de credenciales internas.

**No incluye:**

- Login de usuarios finales.
- Gestión de cuentas.
- Sesiones de navegador.

## 5. Requisitos funcionales

1. Solo la API puede invocar el servicio.
2. Rechazar peticiones sin credencial interna válida.
3. No exponer endpoints de autenticación pública.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- OpenAI API es el proveedor objetivo. Google GenAI queda inactivo y sujeto a aprobación.
- El servicio no expone endpoints públicos; solo es consumido por la API.
- La IA solo explica y recomienda sobre datos validados por la API.

## 8. Criterios de aceptación

- [ ] Petición sin credencial interna devuelve 401/403.
- [ ] Petición válida de la API es aceptada.
- [ ] No hay endpoints de login público.

## 9. Restricciones

- No implementar login genérico por copia de otro repo.

## 10. Dependencias

- API central
- `docs/contratos-integracion.md`

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
