# AGENTS.md — Manual Operativo para Agentes de IA (BusTrack GenAI)

> Directrices operativas para agentes de IA que mantengan o desarrollen componentes en este repositorio.

---

## 1. Principios SDD
1. **Spec First:** Toda modificación de prompts, endpoints o lógica de negocio debe derivar de una especificación en `specs/`.
2. **Grounding Obligatorio:** Los prompts del sistema deben enfatizar que el modelo solo responde basándose en el contexto provisto y rechaza inventar datos.
3. **Cero Secretos:** Nunca escribir valores de API keys en código, prompts o pruebas de integración.

---

## 2. Flujo de Desarrollo
1. Diseñar o consultar la especificación en `specs/`.
2. Definir contratos de datos Pydantic en `src/api/` y plantillas en `src/prompts/`.
3. Escribir pruebas en `UnitTest/` y casos adversarios en `GuardrailTest/`.
4. Implementar la orquestación en `src/services/`.
5. Ejecutar `pytest` y actualizar `Memoria.md`.
