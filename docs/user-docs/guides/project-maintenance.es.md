# Mantener un proyecto existente

[English](project-maintenance.md) | [Português](project-maintenance.pt.md) | [Español](project-maintenance.es.md)

Usa mantenimiento para actualizaciones o desviaciones en un repositorio existente. Proporciona identidad/lockfile actual, release destino explícita, adaptaciones locales y comandos de validación mantenidos.

## Pruébalo

Solicitud ilustrativa; reemplaza el ID o proporciona los datos reales del proyecto:

```text
Usa $project-maintenance para comparar este repositorio con la release destino exacta del Harness que proporcioné. Conserva los cambios locales, presenta conflictos de migración y un plan de rollback, y no publiques cambios remotos.
```

## Resultado esperado

Espera un diff revisable de snapshots de Standards, plantillas, referencias de capacidades y metadatos. Clasifica los artefactos del consumidor antes de moverlos. Conserva wrappers y pruebas propios. Valida con el proveedor destino; registra la versión exacta adoptada y los resultados de integración.

## Recuperación y límites

Si no se proporcionó un destino, resuélvelo antes de cambiar pins; nunca uses latest. Expón los conflictos en lugar de sobrescribirlos. Revierte configuración y referencias del proveedor juntas y ejecuta la suite original restaurada.

## Seguridad de repositorios públicos en GitHub

Use el [procedimiento de seguridad del proveedor exacto (inglés)](../../guides/public-repository-security.md). Prepare los archivos con `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging` y ejecute `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` desde ese proveedor. Para consumidores instalados, añada `--project-root /absolute/consumer` con el lock exacto correspondiente. Revise las diferencias y preserve checks más fuertes y conflictos de ownership; solo operaciones administrativas autorizadas aplican la configuración.

La preparación pública exige una verificación actual y completa en modo live con `public_ready: true`. Un esqueleto local, check de política, snapshot guardado o código de salida 0 aislado es insuficiente. Los permisos u observaciones ausentes siguen sin verificar. La auditoría no autoriza ediciones; el mantenimiento verifica correcciones autorizadas y nunca elige `latest` silenciosamente. Una aprobación de CODEOWNER elegible satisface la regla básica, aunque ambos hayan recibido una solicitud de review. Los contribuidores externos usan forks y PRs; el CI de forks no recibe credenciales administrativas. La publicación de releases y su adopción siguen separadas.

## Referencias

- [Skill (inglés)](../../../skills/project-maintenance/SKILL.md)
- [Changelog (inglés)](../../../CHANGELOG.md)
- [Migration (inglés)](../../../project-templates/README.md)

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
