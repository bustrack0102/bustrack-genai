---
version: 1.0.0
ratified: 2026-10-29
last_amended: 2026-10-29
status: active
source_of_truth: .specify/memory/constitution.md
mirror: ./constitution.md
methodology: SDD
project: BusTrack - Generative AI
team:
  - Fátima Ximena García González
  - Diego Parra Cruz
  - José De Jesús López Islas
  - Melanie Joliee Bonilla Domínguez
institution: Universidad Tecnológica de Tula-Tepeji
---

# Constitución — BusTrack Generative AI

> Rector técnico del microservicio de IA Generativa. Ante conflicto con otro artefacto, **manda esta constitución**.
> Filosofía madre: la IA no inventa; solo explica y sintetiza hechos verificados con datos reales del sistema.

## 1. Propósito y alcance

- Microservicio en Python (FastAPI) para generar recomendaciones y síntesis explicadas de opciones de viaje y opiniones de usuarios.
- Inferencia basada en contexto real provisto por `bustrack-api` (rutas existentes, tarifas actuales, empresas activas y valoraciones registradas).
- Toda funcionalidad se deriva de especificaciones formales en `/specs`.

## 2. Principios no negociables

1. **Anti-Alucinación y Grounding Estricto**:
   - Prohibido que el modelo sugiera empresas, tarifas o rutas que no hayan sido suministradas explícitamente en el payload de contexto.
   - Si no existen rutas u opciones válidas para un destino, el servicio debe responder indicando la ausencia de datos en lugar de inventar alternativas.
2. **Seguridad contra Inyección de Prompts**:
   - Toda entrada de usuario (opiniones, comentarios, consultas) debe sanitizarse antes de incrustarse en los prompts de inferencia.
   - Las pruebas en `GuardrailTest/` deben validar la resistencia a manipulaciones (*jailbreaks*, instrucciones de escape del rol del sistema).
3. **Protección de Credenciales**:
   - Las API Keys del proveedor de LLM (Azure OpenAI, Gemini, etc.) jamás se almacenan en código ni se exponen en logs o respuestas de error.
4. **Respuesta Estructurada**:
   - Todas las salidas generadas deben cumplir con contratos y esquemas Pydantic para un consumo seguro por la API principal.
5. **Control de Costos**:
   - Implementación de límites de longitud de tokens y almacenamiento en caché de respuestas idénticas para mitigar consumo excesivo de cuota.
6. **Bitácora en Memoria**:
   - Los cambios de prompts, modelos base y lecciones aprendidas se documentan en `Memoria.md`.

## 3. Gobernanza SDD y DevSecOps

- Cada PR debe cumplir la lista de comprobación de `CHECKLIST_PR.md`.
- CI configurado en `.github/workflows/` con `pytest`, `flake8` y escaneo SAST con Semgrep.
