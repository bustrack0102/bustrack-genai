# Diagramas — Contratos y grounding de datos validados

> Spec: `spec.md` · Plan: `plan.md`. Diagramas Mermaid; no representan recursos desplegados.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[Contexto API] --> B{¿Completo?}
  B -->|no| C[Respuesta limitada]
  B -->|sí| D[Prompt]
  D --> E[LLM]
  E --> F[Verificar grounding]
  F -->|ok| G[Respuesta]
  F -->|no| C
```

## 2. Relación entre componentes

```mermaid
flowchart LR
  API[API] --> G[GenAI]
  G --> O[OpenAI]
  API --> DB[(Cosmos)]
```

## 3. Flujo de datos / secuencia

```mermaid
sequenceDiagram
  participant A as API
  participant G as GenAI
  participant O as OpenAI
  A->>G: contexto validado
  G->>O: prompt + contexto
  O-->>G: texto
  G->>G: verificar grounding
  G-->>A: explicación + referencias
```

## 4. Notas

No hay implementación ni llamadas a OpenAI activas.
