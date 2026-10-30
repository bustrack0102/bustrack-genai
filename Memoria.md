# Memoria técnica — BusTrack Generative AI

> Registro de experimentos de prompts, evaluación de respuestas, decisiones arquitectónicas y deuda técnica del servicio de IA Generativa.

---

## 📌 Fase GENAI-00 — Inicialización y Estructura SDD (2026-10-29)

- **Estado:** Estructura base Spec-Driven Development (SDD) creada para el servicio de IA Generativa en Python.
- **Decisión 1 (Arquitectura de Servicio):** El servicio operará de manera independiente desacoplado de la API principal, comunicándose vía HTTP interno.
- **Decisión 2 (Agnosticismo del Proveedor LLM):** El diseño soporta clientes configurables (Azure OpenAI / Gemini) mediante variables de entorno, permitiendo seleccionar el proveedor definitivo sin refactorizar la lógica de negocio.
- **Decisión 3 (Cero Alucinaciones):** El ordenamiento y filtrado de opciones lo realiza la API con datos reales; el microservicio de IA se limita a la redacción explicativa y síntesis fundamentada (*grounded explanation*).
- **Deuda Técnica Documentada:** Selección final del proveedor de IA en la nube y parametrización de cuotas/claves en fase de despliegue.
