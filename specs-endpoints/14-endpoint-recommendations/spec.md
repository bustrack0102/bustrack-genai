# 14-endpoint-recommendations — Endpoint interno de recomendaciones

> Repositorio: BusTrack GenAI · Endpoint: `POST /recommendations` · Estado: Implementado · Fecha: 2026-11-11.

## 1. Objetivo

Recibir contexto validado y devolver recomendaciones/explicaciones fundamentadas.

## 2. Contrato

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/recommendations` |
| Autenticación | Token interno o identidad administrada; sin login público. |
| Consumidor | API central |
| Estado | Implementado |

**Parámetros / entrada:**

- Body: contexto validado de rutas/horarios/tarifas y preferencias.

**Respuesta:**

- 200: texto + referencias.
- 401/403: sin credencial interna.
- 422: contexto inválido.
- 429: límite de uso.

## 3. Códigos HTTP

- 200/201: éxito.
- 400/422: validación.
- 401/403: autenticación/autorización.
- 404: recurso inexistente.
- 409: conflicto.
- 429: rate limit.
- 500: error interno sin detalles.

## 4. Validaciones

1. Contexto validado por la API.
2. Límite de tokens.
3. Sin PII.

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

## Aprobación

- [x] Revisión de arquitectura y contrato realizada — fecha: 2026-11-11
- [x] CHECKLIST_PR.md validado
- [x] Sin conflicto con constitution.md
