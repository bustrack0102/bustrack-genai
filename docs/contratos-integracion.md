# Contratos de integración — BusTrack GenAI

> Vista de los contratos que este repositorio expone o consume. Solo login/logout están
> implementados en los clientes y la API; el resto es **propuesta** hasta que exista código.

## 1. Principios

- La API central es la única fuente autorizada de datos de transporte.
- Ningún cliente accede a Cosmos DB ni a ML/GenAI directamente.
- ML y GenAI son servicios internos autenticados; no exponen login público.
- Toda integración usa HTTPS, timeouts y errores tipados.
- Lo propuesto se marca como tal; no se declaran endpoints inexistentes.

## 2. Expone (solo API)

| Método | Ruta | Estado | Auth |
|---|---|---|---|
| GET | `/health` | Propuesta | Interno. |
| POST | `/recommendations` | Propuesta | Token interno / identidad administrada. |

## 3. Consume

- OpenAI API (proveedor objetivo).
- Google GenAI: inactivo, sujeto a aprobación.

## 4. Reglas

- Sin login público.
- Sin acceso a Cosmos DB.
- Grounding obligatorio sobre contexto validado por la API.

## 5. Errores uniformes

| Código | Significado |
|---|---|
| 400 | Petición mal formada. |
| 401 | Credencial ausente o inválida. |
| 403 | Sin permiso. |
| 404 | Recurso inexistente. |
| 409 | Conflicto de concurrencia/unicidad. |
| 422 | Validación de dominio/esquema. |
| 429 | Rate limit. |
| 500 | Error interno sin detalles sensibles. |
