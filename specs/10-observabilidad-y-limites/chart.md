# Diagramas — 10-observabilidad-y-limites — Observabilidad y límites del servicio

> Spec: `spec.md` · Plan: `plan.md`.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[Petición] --> B{¿Límite?}
  B -->|no| C[413/422]
  B -->|sí| D[Procesar]
  D --> E[Métricas]
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
