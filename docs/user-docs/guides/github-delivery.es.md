# Entrega mediante GitHub

[English](github-delivery.md) | [Português](github-delivery.pt.md) | [Español](github-delivery.es.md)

Usa esta guía al preparar un cambio vinculado a una issue para revisión humana. Necesitas la URL real de la issue, instrucciones del repositorio, alcance aprobado y entorno de validación del proyecto.

## Pruébalo

Solicitud ilustrativa; reemplaza el ID o proporciona los datos reales del proyecto:

```text
Usa $versat-sdd para inspeccionar <change-id>, preparar el resumen de entrega e identificar prerrequisitos de archivo o validación faltantes. No publiques un PR ni hagas merge.
```

## Resultado esperado

Trabaja en una rama según la convención Git resuelta. Mantén trazabilidad entre issue, requisitos y commits; no inventes un ID de Shortcut. La planificación o el trabajo incompleto se revisan en un PR draft. Antes de presentar la implementación completa, prepara el archivo documental en la misma rama y supera el preflight de archivo seleccionado. Solicita explícitamente la publicación del PR; después obtén revisión humana y CI obligatorio final antes del merge.

## Recuperación y límites

Informa en el PR las verificaciones fallidas o no disponibles. Los comentarios de revisión permanecen con el mismo ID; los cambios de alcance reabren la revisión correspondiente. Verifica el merge real por separado de la preparación local. Un merge no publica una release ni actualiza consumidores instalados.

## Seguridad de repositorios públicos en GitHub

Use el [procedimiento de seguridad del proveedor exacto (inglés)](../../guides/public-repository-security.md). Prepare los archivos con `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging` y ejecute `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` desde ese proveedor. Para consumidores instalados, añada `--project-root /absolute/consumer` con el lock exacto correspondiente. Revise las diferencias y preserve checks más fuertes y conflictos de ownership; solo operaciones administrativas autorizadas aplican la configuración.

La preparación pública exige una verificación actual y completa en modo live con `public_ready: true`. Un esqueleto local, check de política, snapshot guardado o código de salida 0 aislado es insuficiente. Los permisos u observaciones ausentes siguen sin verificar. La auditoría no autoriza ediciones; el mantenimiento verifica correcciones autorizadas y nunca elige `latest` silenciosamente. Una aprobación de CODEOWNER elegible satisface la regla básica, aunque ambos hayan recibido una solicitud de review. Los contribuidores externos usan forks y PRs; el CI de forks no recibe credenciales administrativas. La publicación de releases y su adopción siguen separadas.

## Referencias

- [Git (inglés)](../../../standards/core/git.md)
- [SDD (inglés)](../../../sdd/README.md)
- [SDD validation (inglés)](../../../validators/sdd/README.md)

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
