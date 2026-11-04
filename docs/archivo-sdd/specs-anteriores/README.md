# Specs — BusTrack GenAI

> Catálogo canónico. Cada spec contiene `spec.md`, `plan.md`, `task.md` y `chart.md`.
> Las specs históricas se conservan como referencia y **no** rigen el desarrollo.

## Specs canónicas

| ID | Nombre | Estado |
|---|---|---|
| `00-fundamentos` | 00 — Fundamentos y gobernanza SDD | Implementado |
| `01-configuracion` | 01 — Configuración del entorno | Parcial |
| `02-arquitectura` | 02 — Arquitectura y límites del servicio | Parcial |
| `endpoints/login` | Autenticación interna (sin login público) | Pendiente |
| `endpoints/logout` | Cierre de sesión / revocación interna | Pendiente |
| `integraciones` | Integraciones con el ecosistema BusTrack | Parcial |
| `seguridad` | Seguridad y privacidad | Parcial |
| `pruebas` | Estrategia de pruebas | Parcial |
| `cicd` | CI/CD y gates de calidad | Parcial |
| `azure` | Arquitectura Azure propuesta | Propuesta |
| `genai/contratos-grounding` | Contratos y grounding de datos validados | Pendiente |
| `genai/prompts-recomendaciones` | Prompts, recomendaciones y explicaciones | Pendiente |
| `genai/guardrails` | Guardrails, seguridad y anti-alucinación | Pendiente |

## Historial

- `_archivo-plantilla-dotnet/` contiene la plantilla .NET importada por error desde la API; no aplica a este stack.

## Reglas

- No copiar specs de otro stack.
- Toda spec nueva debe declarar objetivo, alcance, requisitos, criterios de aceptación y dependencias.
- Una spec solo pasa a `Implementado` con código y pruebas verificables.
- `Memoria.md` es la fuente del estado real.
