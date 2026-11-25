# Auditar un proyecto

[English](project-audit.md) | [Português](project-audit.pt.md) | [Español](project-audit.es.md)

Usa una auditoría para evaluar cumplimiento, preparación o desviaciones. Prepara instrucciones, .versat/project.yaml, .versat/standards.lock, especificaciones activas y el proveedor seleccionado. Es más amplio que una revisión de código habitual.

## Pruébalo

Solicitud ilustrativa; reemplaza el ID o proporciona los datos reales del proyecto:

```text
Usa $project-audit para evaluar este repositorio según su perfil declarado y los Standards resueltos. Informa evidencia, gravedad y opciones de corrección. No modifiques archivos.
```

## Resultado esperado

Espera hallazgos que distingan cumplimiento verificado, incumplimiento y verificación no disponible, con contratos afectados y próximos pasos concretos. La validación determinista aporta evidencia limitada; la revisión cualitativa también considera seguridad, pruebas/evals, documentación, operaciones y perfil/criticidad.

## Recuperación y límites

La identidad o el contexto del proveedor faltantes son vacíos explícitos, no evidencia de cumplimiento. Pedir una auditoría no autoriza corregir. Usa mantenimiento o un cambio SDD para tratar hallazgos aprobados.

## Seguridad de repositorios públicos en GitHub

Use el [procedimiento de seguridad del proveedor exacto (inglés)](../../guides/public-repository-security.md). Prepare los archivos con `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging` y ejecute `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` desde ese proveedor. Para consumidores instalados, añada `--project-root /absolute/consumer` con el lock exacto correspondiente. Revise las diferencias y preserve checks más fuertes y conflictos de ownership; solo operaciones administrativas autorizadas aplican la configuración.

La preparación pública exige una verificación actual y completa en modo live con `public_ready: true`. Un esqueleto local, check de política, snapshot guardado o código de salida 0 aislado es insuficiente. Los permisos u observaciones ausentes siguen sin verificar. La auditoría no autoriza ediciones; el mantenimiento verifica correcciones autorizadas y nunca elige `latest` silenciosamente. Una aprobación de CODEOWNER elegible satisface la regla básica, aunque ambos hayan recibido una solicitud de review. Los contribuidores externos usan forks y PRs; el CI de forks no recibe credenciales administrativas. La publicación de releases y su adopción siguen separadas.

## Referencias

- [Skill (inglés)](../../../skills/project-audit/SKILL.md)
- [Standards index (inglés)](../../../standards/index.yaml)
- [Validators (inglés)](../../../validators/README.md)

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
