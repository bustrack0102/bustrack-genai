# Diagramas — 07-guardrails-anti-prompt-injection — Guardrails anti prompt injection

> Spec: `spec.md` · Plan: `plan.md`.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[Entrada] --> B[Sanitizar]
  B --> C[Detectar]
  C -->|sospecha| D[Rechazar]
  C -->|ok| E[LLM]
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
