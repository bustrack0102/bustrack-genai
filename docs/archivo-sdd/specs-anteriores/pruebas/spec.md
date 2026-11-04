# Estrategia de pruebas

> Repositorio: BusTrack GenAI · Ruta: `specs/pruebas/` · Estado: Parcial · Fecha: 2026-10-30.

## 1. Identificador y nombre

- **ID:** `pruebas`
- **Nombre:** Estrategia de pruebas
- **Repositorio:** BusTrack GenAI

## 2. Objetivo

Definir la estrategia de pruebas de BusTrack GenAI y el criterio de evidencia.

## 3. Contexto

Stack de pruebas previsto: pytest, pytest-cov, GuardrailTest, pruebas de contrato y seguridad.

## 4. Alcance

**Incluye:**

- Pruebas unitarias, integración, contrato y seguridad.
- Datos de prueba.
- Cobertura y umbrales.
- Evidencia en CI.

**No incluye:**

- Pruebas de carga/caos no aprobadas.
- Pruebas contra producción.

## 5. Requisitos funcionales

1. Cada requisito crítico tiene prueba.
2. Las pruebas no dependen de servicios reales no controlados.
3. La cobertura se mide y reporta.
4. Los tests deben poder ejecutarse localmente.

## 6. Requisitos no funcionales

1. Documentación verificable y sin secretos.
2. Cambios incrementales y reversibles.
3. Trazabilidad spec -> tarea -> prueba.

## 7. Reglas de negocio

- OpenAI API es el proveedor objetivo. Google GenAI queda inactivo y sujeto a aprobación.
- El servicio no expone endpoints públicos; solo es consumido por la API.
- La IA solo explica y recomienda sobre datos validados por la API.

## 8. Criterios de aceptación

- [ ] Suite ejecutable en verde.
- [ ] Cobertura reportada.
- [ ] Casos de error cubiertos.
- [ ] Sin dependencia de Azure real.

## 9. Restricciones

- No ejecutar migraciones ni despliegues en esta fase.
- No cambiar el stack objetivo sin autorización.
- No incluir secretos ni PII.

## 10. Dependencias

- `constitution.md`
- specs/seguridad/

## 11. Trazabilidad

- Plan: `plan.md` · Tareas: `task.md` · Diagramas: `chart.md`.
- Estado real: `../../Memoria.md`.
- Contratos: `../../docs/contratos-integracion.md`.
