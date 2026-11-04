# Diagramas — 14-endpoint-recommendations — Endpoint interno de recomendaciones

> Spec: `spec.md` · Plan: `plan.md`.

## 1. Flujo del endpoint

```mermaid
flowchart TD
  A[API] --> B[Token]
  B --> C[Validar contexto]
  C --> D[Prompt]
  D --> E[OpenAI]
  E --> F[Grounding]
  F --> G[Respuesta]
```

## 2. Componentes

```mermaid
flowchart LR
  C[Consumidor] --> A[Servicio]
  A --> D[(Datos)]
```

## 3. Secuencia

```mermaid
sequenceDiagram
  participant C as Consumidor
  participant S as Servicio
  C->>S: POST /recommendations
  S-->>C: respuesta
```

## 4. Notas

Diagramas de proceso; no representan recursos desplegados.
