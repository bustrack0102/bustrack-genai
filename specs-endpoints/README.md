# Specs de endpoints — BusTrack GenAI

> Contratos HTTP que este repositorio expone o consume. Cada endpoint tiene
> `spec.md`, `plan.md`, `task.md` y `chart.md`. La numeración continúa después
> de la última tarea de `../specs/`.

## Endpoints

| ID | Método y ruta | Nombre | Estado |
|---|---|---|---|
| `13-endpoint-health` | `GET /health` | Endpoint de salud del servicio GenAI | Propuesto |
| `14-endpoint-recommendations` | `POST /recommendations` | Endpoint interno de recomendaciones | Propuesto |

## Reglas

- Diferenciar endpoints implementados de propuestos.
- No inventar endpoints ni métodos.
- Cada endpoint declara autenticación, validaciones, códigos HTTP y pruebas.
