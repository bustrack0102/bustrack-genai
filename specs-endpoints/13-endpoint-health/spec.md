# 13-endpoint-health — Endpoint de salud del servicio GenAI

> Repositorio: BusTrack GenAI · Endpoint: `GET /health` · Estado: Propuesto · Fecha: 2026-10-30.

## 1. Objetivo

Exponer salud del servicio para operación interna.

## 2. Contrato

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/health` |
| Autenticación | Interno; solo API/infraestructura. |
| Consumidor | API central / infraestructura |
| Estado | Propuesto |

**Parámetros / entrada:**

- Sin parámetros.

**Respuesta:**

- 200: healthy.
- 503: unhealthy.

## 3. Códigos HTTP

- 200/201: éxito.
- 400/422: validación.
- 401/403: autenticación/autorización.
- 404: recurso inexistente.
- 409: conflicto.
- 429: rate limit.
- 500: error interno sin detalles.

## 4. Validaciones

1. No exponer detalles internos.

## 5. Seguridad

- Sanitización, guardrails anti prompt injection, sin PII en prompts/logs, límites de tokens y cero secretos en Git.
- No registrar tokens, credenciales ni PII.

## 6. Criterios de aceptación

- [ ] La tarea tiene criterios verificables y evidencia asociada.
- [ ] No se declara implementado lo que no existe en código o pruebas.
- [ ] Los contratos consumidos o expuestos quedan documentados.
- [ ] `Memoria.md` refleja el estado resultante.

## 7. Dependencias

- `docs/contratos-integracion.md`
- `spec.md` de la tarea funcional asociada
