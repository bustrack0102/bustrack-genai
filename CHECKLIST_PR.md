# CHECKLIST_PR.md — BusTrack Generative AI

> Constitución §3. 1 revisor obligatorio. Rama `main` protegida.

- [ ] Spec en `specs/` aprobada y enlazada.
- [ ] Linter y formato limpio (`flake8`, `black --check`).
- [ ] Pruebas unitarias (`UnitTest/`) en verde.
- [ ] Pruebas de integración (`IntegrationTest/`) en verde.
- [ ] Pruebas de guardrails e inyección (`GuardrailTest/`) en verde.
- [ ] Pruebas de seguridad y sanitización (`SecurityTest/`) en verde.
- [ ] Semgrep SAST sin vulnerabilidades altas ni críticas.
- [ ] Verificación de cero exposición de API keys en código, logs o fixtures.
- [ ] `Memoria.md` actualizada con decisiones y estado del modelo.
- [ ] Revisor asignado: ___________________  Fecha: ___________________
