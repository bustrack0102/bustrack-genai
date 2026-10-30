# BusTrack · Generative AI — Spec-Driven GenAI Service

> Microservicio de Explicación y Recomendación Generativa — **Universidad Tecnológica de Tula-Tepeji**
> Desarrollado con **Spec-Driven Development (SDD)** y asegurado bajo prácticas de **DevSecOps** desde el día uno.

---

## 👥 Equipo de Desarrollo (BusTrack)
* **Fátima Ximena García González**
* **Diego Parra Cruz**
* **José De Jesús López Islas**
* **Melanie Joliee Bonilla Domínguez**

---

## 📋 Resumen del Repositorio
Este repositorio contiene el microservicio de **Inteligencia Artificial Generativa** de BusTrack. Su función es proporcionar recomendaciones contextuales y explicaciones en lenguaje natural para orientar a los usuarios en la selección de opciones de transporte, empresas y rutas adecuadas a su destino, con base exclusiva en **calificaciones reales, opiniones recopiladas y datos verificados**.

* **Metodología:** Spec-Driven Development (SDD) basada en especificaciones en `/specs`.
* **Diseño Anti-Alucinación (Grounding):** La IA generativa solo redacta y explica opciones previamente filtradas y calculadas con datos reales por la API. No inventa rutas, precios, empresas ni destinos que no existan en el sistema.
* **Seguridad y DevSecOps:** Guardrails contra Prompt Injection, sanitización de entradas, SAST con Semgrep y CI con GitHub Actions.

---

## 🏛️ Componentes de Gobernanza y SDD

| Componente | Ruta | Propósito |
|---|---|---|
| **Constitución (Fuente de verdad)** | `constitution.md` (espejo en `.specify/memory/constitution.md`) | Principios éticos, límites de inferencia y reglas no negociables de IA |
| **Manual operativo para Agentes** | `AGENTS.md` | Directrices para agentes de IA que mantengan o extiendan prompts y servicios |
| **Especificaciones (Specs)** | `specs/` | Historias y entregables de IA (`000-base-genai`, `001-sentiment-analyzer`, `002-recommendation-explainer`, etc.) |
| **Plantillas SDD** | `.specify/templates/` (y `specs/_template.md`) | Plantillas oficiales para nuevas especificaciones de GenAI |
| **Agentes y Habilidades IA** | `.opencode/agents/` y `.opencode/skills/` | Configuración de agentes OpenCode / WARP |
| **Seguridad SAST** | `.semgrep/semgrep.yaml` | Reglas de análisis estático de código |
| **Checklist de PR** | `CHECKLIST_PR.md` | Validación estricta previa a la integración de cambios |
| **Memoria técnica** | `Memoria.md` | Registro de experimentos con prompts, costos de inferencia y deuda técnica |

---

## 🧪 Estructura del Código y Pruebas

```text
bustrack-genai/
├── src/
│   ├── api/          # Endpoints FastAPI para generación y análisis semántico
│   ├── core/         # Configuración del proveedor de LLM (Azure OpenAI / Gemini)
│   ├── prompts/      # Plantillas de prompts versionadas y tipadas
│   └── services/     # Orquestación de inferencia y verificación de hechos (Grounding)
├── UnitTest/         # Validación de formateo de prompts, parsers y esquemas
├── IntegrationTest/  # Pruebas de integración del microservicio HTTP
├── GuardrailTest/    # Validación contra inyección de prompts y jailbreaks
└── SecurityTest/     # Verificación de autenticación y sanitización de inputs
```

---

## 🚀 Integración Continua (CI)
El workflow `.github/workflows/ci-pr.yml` valida formateo (`black`), estilo (`flake8`), seguridad (`semgrep`), pruebas de integración y guardrails (`pytest`) en cada Pull Request.
