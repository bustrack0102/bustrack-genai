# Diagramas — 04-grounding-de-recomendaciones — Grounding de recomendaciones

> Spec: `spec.md` · Plan: `plan.md`.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[Contexto] --> B[LLM]
  B --> C[Verificar]
  C -->|ok| D[Respuesta]
  C -->|no| E[Fallback]
```

## 2. Componentes

```mermaid
flowchart LR
  C[Cliente] --> A[Servicio]
  A --> D[(Datos)]
```

## 3. Secuencia

```mermaid
sequenceDiagram
  participant D as Dev
  participant C as CI
  D->>C: push
  C-->>D: lint + pruebas
```

## 4. Notas

Diagramas de proceso; no representan recursos desplegados.
