# Refuerza la seguridad de los repositorios públicos

Bootstrap, auditoría y mantenimiento podían presentar validación local sin comprobar todas las protecciones de GitHub. Este cambio añade una política única resuelta por el índice, un verificador de solo lectura y configuración generada para revisión. Solo una evaluación live completa permite declarar preparación pública; snapshots, permisos faltantes y conflictos permanecen explícitos.

Incluye protección de main sin bypass administrativo, aprobación de un CODEOWNER elegible, invalidación de aprobaciones y revisión del último push, restricciones administrativas de branches/tags, secret scanning y push protection. Preserva checks existentes, controles más fuertes y contribución mediante fork → PR. Actualiza las tres Skills, composición y guías EN/PT/ES.

Validación: 245 pruebas, Ruff, contratos del paquete/SDD, tres escenarios supervisados con replay independiente y lectura live del Harness con comparación administrativa independiente. El defecto de nombres de campos entre protección clásica y rulesets fue corregido; intentos anteriores e interrupciones están documentados. Evidencia: `docs/validation/public-repository-security/README.md`.

Dossier único: `specs/archive/public-repository-security/`; `closure: prepared`. El preflight de entrega con `--require-archive` pasa. La configuración observada del Harness cumple los controles y conserva `structural-validation`; la verificación no cambió la cuenta activa ni escribió en GitHub.

Esta es preparación local para revisión. CI remoto, revisión humana, merge, publicación de release y adopción exacta por consumidores siguen siendo hechos separados. VERSION y pins existentes no cambian.

Revisores propuestos: los CODEOWNERS existentes. Sin Story suministrada; no se inventa identificador. Posible mensaje de squash en inglés: `Enforce public repository security across project lifecycles`.
