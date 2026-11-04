# Diagramas — Autenticación interna (sin login público)

> Spec: `spec.md` · Plan: `plan.md`. Diagramas Mermaid; no representan recursos desplegados.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[API central] -->|token interno| B[Servicio]
  B -->|válido| C[Procesar]
  B -->|inválido| D[401/403]
```

## 2. Relación entre componentes

```mermaid
flowchart LR
  API[API] --> S[Servicio interno]
  S --> K[Key Vault]
```

## 3. Flujo de datos / secuencia

```mermaid
sequenceDiagram
  participant A as API
  participant S as Servicio
  A->>S: request + credencial interna
  S->>S: validar credencial
  S-->>A: respuesta
```

## 4. Notas

No hay login público; no se debe inventar uno.
