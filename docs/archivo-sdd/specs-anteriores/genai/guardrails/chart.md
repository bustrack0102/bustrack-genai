# Diagramas — Guardrails, seguridad y anti-alucinación

> Spec: `spec.md` · Plan: `plan.md`. Diagramas Mermaid; no representan recursos desplegados.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[Entrada] --> B[Sanitizar]
  B --> C[Detectar inyección]
  C -->|sospecha| D[Rechazar/limitar]
  C -->|ok| E[LLM]
  E --> F[Verificar grounding]
  F -->|ok| G[Responder]
  F -->|no| H[Respuesta segura]
```

## 2. Relación entre componentes

```mermaid
flowchart LR
  U[Entrada] --> S[Guardrails]
  S --> L[LLM]
  L --> G[Grounding]
  G --> R[Salida]
```

## 3. Flujo de datos / secuencia

```mermaid
sequenceDiagram
  participant A as API
  participant S as Guardrails
  participant O as OpenAI
  A->>S: contexto + petición
  S->>S: sanitizar + detectar
  S->>O: prompt seguro
  O-->>S: texto
  S->>S: verificar grounding
  S-->>A: respuesta segura o rechazo
```

## 4. Notas

No hay guardrails implementados; el diagrama es objetivo.
