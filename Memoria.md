# Memoria técnica — BusTrack GenAI

> Registro vivo. No se borra historial. Última actualización: 2026-10-30.

## 1. Estado real

- **Repositorio:** `bustrack-genai-main` (raíz interior; el árbol está anidado `X-main/X-main`).
- **Tecnología actual:** Python 3.11, FastAPI, OpenAI SDK, Google GenAI SDK, tiktoken, pytest (esqueleto sin código).
- **Tecnología objetivo:** Python 3.11 + FastAPI + OpenAI API, con grounding obligatorio y guardrails.
- **Git:** no hay repositorio Git local; los tags/releases no son verificables.

## 2. Funcionalidades implementadas

- Estructura src/{api,core,prompts,services} (solo .gitkeep).
- requirements.txt con FastAPI, OpenAI, Google GenAI, tiktoken, pytest, black, flake8 y Semgrep.
- Gobernanza GenAI/Python en constitution, AGENTS, Memoria y CHECKLIST.

## 3. Funcionalidades pendientes

- Todo el código del servicio: app FastAPI, endpoints internos, prompts y servicios.
- Integración OpenAI y control de costos/tokens.
- Grounding, contexto validado y explicaciones/recomendaciones.
- Guardrails contra prompt injection y alucinaciones.
- Pruebas de guardrails, integración y seguridad.
- Dockerfile, CI bloqueante y despliegue Azure.

## 4. Arquitectura actual

src/{api,core,prompts,services}; suites UnitTest, IntegrationTest, GuardrailTest, SecurityTest

## 5. Migraciones

No aplica una migración de stack en este repositorio.

## 6. Decisiones arquitectónicas

- Se adopta SDD y DevSecOps.
- La API central es la fuente autorizada de datos.
- Cosmos DB for NoSQL es la persistencia objetivo.
- ML y GenAI son servicios internos FastAPI.
- OpenAI API es el proveedor GenAI objetivo; Google GenAI queda inactivo.
- Flutter + Dart y Angular + TypeScript son los objetivos de cliente.
- No se declaran recursos Azure desplegados.

## 7. Dependencias entre repositorios

API central -> GenAI por HTTP interno; GenAI recibe contexto validado y devuelve texto fundamentado.

## 8. Problemas conocidos

- Documentación previa desalineada con el código (corregida en esta reorganización).
- Specs históricas conservadas como referencia; ver `specs/README.md`.
- Gates CI/SAST incompletos o no bloqueantes en el estado previo.
- Deuda de pruebas y despliegue documentada en cada spec.

## 9. Historial

- **2026-10-29:** estructura SDD original y primeras fases.
- **2026-10-30:** auditoría completa, corrección documental y reorganización SDD.
  Se separan specs históricas de canónicas, se corrigen afirmaciones de stack y se
  documentan migraciones, contratos y Azure propuesto.
