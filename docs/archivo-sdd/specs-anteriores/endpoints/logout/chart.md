# Diagramas — Cierre de sesión / revocación interna

> Spec: `spec.md` · Plan: `plan.md`. Diagramas Mermaid; no representan recursos desplegados.

## 1. Flujo funcional

```mermaid
flowchart TD
  A[API] --> B[Servicio]
  B --> C{Credencial vigente}
  C -->|sí| D[Procesar]
  C -->|no| E[401/403]
```

## 2. Relación entre componentes

```mermaid
flowchart LR
  API[API] --> S[Servicio]
  S --> KV[Key Vault]
```

## 3. Flujo de datos / secuencia

```mermaid
sequenceDiagram
  participant A as API
  participant S as Servicio
  A->>S: request + credencial
  S->>S: validar vigencia
  S-->>A: resultado
```

## 4. Notas

No aplica sesión de usuario; se documenta la credencial de servicio.
