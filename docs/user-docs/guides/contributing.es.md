# Contribuir con procedencia clara

[English](contributing.md) | [Português](contributing.pt.md) | [Español](contributing.es.md)

Esta es la guía mantenida para contribuir al candidato del Harness y seleccionar un proyecto de destino. La disponibilidad pública y adopción Apache del Harness están pendientes. Hasta que existan, use únicamente repositorios y términos autorizados; esta guía no promete forks públicos ni instalación disponible.

## Preparar y contribuir

1. Seleccione el repositorio real y lea README, AGENTS e instrucciones de contribución. Sus reglas prevalecen sobre los valores de la organización. Otros productos conservan términos y rutas independientes.
2. Seleccione una issue existente o un formulario de error, funcionalidad o mantenimiento. Al abrir una issue o modificar sustancialmente su definición, escriba en inglés el título y la descripción, incluidas las respuestas del formulario, el resultado esperado y los pasos para reproducir el problema, cuando correspondan. El equipo puede conversar en español en los comentarios. Si la conversación cambia el alcance o los criterios de aceptación, actualice la descripción en inglés. Use el número real de la issue o Story. Consulte el [estándar de idiomas](../../../standards/core/language.md#github-issues).
3. Identifique material propio/de terceros, fuentes, versiones, permisos y avisos. Los derechos faltantes impiden aceptación. Lea [licencias](licensing.es.md); la licencia de la herramienta no determina términos del material independiente de destino.
4. Siga la [preparación](workspace-setup.es.md). En el checkout del Harness use Python 3.11+, instale `requirements-validation.txt` en un entorno virtual y ejecute `./scripts/validate/run.sh --quality-base origin/main` desde la raíz. En otros proyectos use sus verificaciones propias.
5. Cuando el repositorio y los permisos lo permitan, use un fork autorizado o rama de trabajo y la [convención Git](../../../standards/core/git.md). El acceso público de lectura/fork no concede escritura, merge ni release en el repositorio original.
6. Para cambios materiales, siga las [tres aprobaciones SDD](sdd-with-codex.es.md); solicite implementación explícitamente después de aprobar Tasks. Incluya documentación mantenida y verificaciones relevantes. Siga la [entrega](github-delivery.es.md) para archivo documental, revisión del PR y verificaciones finales, con autorización efectiva de operaciones remotas.

Resultado esperado: contribución revisable con referencias reales de issue/procedencia y verificaciones observadas. Declare verificaciones no disponibles; un resultado local no demuestra protección de ramas ni aceptación.

## Términos candidatos de contribución

Si y cuando este candidato Apache se adopte, la sección 5 del [texto Apache exacto](../../licensing/candidates/apache-2.0/LICENSE.txt) regirá las contribuciones enviadas intencionalmente para inclusión, salvo indicación expresa en contrario, conforme a las definiciones de la licencia y cualquier acuerdo separado. Esta guía no agrega CLA, DCO ni cesión de propiedad intelectual. Hasta la adopción, use los términos efectivos del repositorio/versión y aclare cualquier ausencia. La aprobación propietaria anterior y estas instrucciones no constituyen una licencia efectiva.

## Revisión y recuperación

El mantenedor debe revisar alcance, procedencia y verificaciones obligatorias. CODEOWNERS identifica contactos técnicos, sin demostrar cualificación jurídica ni protección activa. Derechos o revisión obligatoria faltantes impiden aceptación. Corrija fallos y obtenga evidencia nueva; los cambios de alcance reabren la aprobación pertinente. Sin acceso, use la ruta pública existente del destino sin el Harness cuando proceda, o pida instrucciones al mantenedor visible sin divulgar información confidencial.

No exponga vulnerabilidades en issues públicas; use [reporte de seguridad](security-reporting.es.md). Política canónica: [Contribution](../../../standards/core/contribution.md).

[Quickstart](../quickstart.es.md) · [Harness](../../../README.es.md)
