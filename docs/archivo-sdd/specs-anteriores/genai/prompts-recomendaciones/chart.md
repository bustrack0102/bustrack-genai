# Diagramas — Prompts, recomendaciones y explicaciones

> Spec: `spec.md` · Plan: `plan.md`. Diagramas Mermaid; no representan recursos desplegados.

## 1. Flujo funcional

```mermaid
flowchart LR
  C[Contexto] --> P[Prompt versionado]
  P --> L[OpenAI]
  L --> O[Salida]
  O --> V[Validar grounding]
```

## 2. Relación entre componentes

```mermaid
flowchart TD
  API[API] --> S[Servicio]
  S --> P[Prompt]
  P --> O[OpenAI]
  S --> T[tiktoken]
```

## 3. Flujo de datos / secuencia

```mermaid
sequenceDiagram
  participant A as API
  participant G as GenAI
  participant O as OpenAI
  A->>G: opciones + contexto
  G->>G: render prompt
  G->>O: completion
  O-->>G: texto
  G-->>A: texto + refs
```

## 4. Notas

Google GenAI no se usa; queda documentado como inactivo.
