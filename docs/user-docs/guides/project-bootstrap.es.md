# Iniciar un proyecto

[English](project-bootstrap.md) | [Português](project-bootstrap.pt.md) | [Español](project-bootstrap.es.md)

Usa bootstrap para un proyecto nuevo o vacío. Proporciona propósito, responsable, perfil, dominio, criticidad, tecnologías y proveedor exacto del Harness. Los repositorios existentes con contenido usan mantenimiento.

## Pruébalo

Solicitud ilustrativa; reemplaza el ID o proporciona los datos reales del proyecto:

```text
Usa $project-bootstrap en este repositorio vacío. Reutiliza el brief del producto, pregunta por la identidad faltante y presenta una estructura y contexto de producto para revisión. No crees repositorios remotos ni PRs.
```

## Resultado esperado

Espera una estructura compuesta de base/perfil, specs/product/overview.md con vacíos de evidencia, .versat/project.yaml, .versat/standards.lock exacto y un cambio SDD project-bootstrap. El índice del proveedor resuelve Standards; los usuarios no eligen un subconjunto de políticas obligatorias. Revisa las hipótesis del producto antes de tratarlas como requisitos.

## Recuperación y límites

Una estructura vacía no demuestra una aplicación utilizable. Registra las comprobaciones de ejecución no disponibles y evita guías vacías o pasos ejecutables ficticios. Si hay contenido existente en conflicto, detente y clasifica el repositorio antes de componer plantillas.

## Seguridad de repositorios públicos en GitHub

Use el [procedimiento de seguridad del proveedor exacto (inglés)](../../guides/public-repository-security.md). Prepare los archivos con `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging` y ejecute `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` desde ese proveedor. Para consumidores instalados, añada `--project-root /absolute/consumer` con el lock exacto correspondiente. Revise las diferencias y preserve checks más fuertes y conflictos de ownership; solo operaciones administrativas autorizadas aplican la configuración.

La preparación pública exige una verificación actual y completa en modo live con `public_ready: true`. Un esqueleto local, check de política, snapshot guardado o código de salida 0 aislado es insuficiente. Los permisos u observaciones ausentes siguen sin verificar. La auditoría no autoriza ediciones; el mantenimiento verifica correcciones autorizadas y nunca elige `latest` silenciosamente. Una aprobación de CODEOWNER elegible satisface la regla básica, aunque ambos hayan recibido una solicitud de review. Los contribuidores externos usan forks y PRs; el CI de forks no recibe credenciales administrativas. La publicación de releases y su adopción siguen separadas.

## Referencias

- [Skill (inglés)](../../../skills/project-bootstrap/SKILL.md)
- [Templates (inglés)](../../../project-templates/README.md)
- [Project schema (inglés)](../../../schemas/project.schema.yaml)

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
