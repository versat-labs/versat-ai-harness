# Versat AI Harness

[English](README.md) | [Português](README.pt.md) | [Español](README.es.md)

Fuente de verdad de Versat para desarrollo asistido por IA: un Plugin portátil con Standards, Spec Driven Development (SDD), Skills reutilizables, plantillas compuestas y validación determinista.

Para desarrolladores, revisores y mantenedores, incluidos colaboradores externos. Mantenido por Versat. @elviszoz y @evertonspohrversat son los CODEOWNERS generales y responsables de la clasificación compartida de seguridad; Elvis coordina. Main exige una aprobación elegible de CODEOWNER que no sea el autor de la PR y CI aprobada. La prueba interna de aprobación, descarte y nueva aprobación está completa. La recepción externa de reportes de seguridad sigue sin verificarse.

## Comienza aquí

[Inicio rápido: obtener un primer plan SDD](docs/user-docs/quickstart.es.md) · [Contexto del producto](docs/product/overview.es.md)

- [Preparar el entorno](docs/user-docs/guides/workspace-setup.es.md)
- [Preparar Claude](docs/user-docs/guides/claude-setup.es.md)
- [SDD con Codex](docs/user-docs/guides/sdd-with-codex.es.md)
- [Entrega mediante GitHub](docs/user-docs/guides/github-delivery.es.md)
- [Iniciar un proyecto](docs/user-docs/guides/project-bootstrap.es.md)
- [Mantener un proyecto existente](docs/user-docs/guides/project-maintenance.es.md)
- [Auditar un proyecto](docs/user-docs/guides/project-audit.es.md)
- [Revisar la arquitectura](docs/user-docs/guides/architecture-review.es.md)
- [Validación y evaluaciones](docs/user-docs/guides/validation-and-evaluations.es.md)
- [Documentación electrónica SIFEN](docs/user-docs/guides/sifen-electronic-documentation.es.md)
- [Crear una issue en GitHub](docs/user-docs/guides/issue-creation.es.md)

- [Transición del marketplace: identidades nueva y heredada](docs/user-docs/guides/marketplace-transition.es.md)

## Repositorio público; 0.5.0 en preparación

El repositorio es público y la licencia Apache-2.0 y los avisos revisados están integrados en main. La versión 0.4.0 se publicó el 2026-11-24. La versión 0.5.0 agrega soporte para Claude; su tag v0.5.0 se crea en el commit de merge después de la revisión. Las aprobaciones del texto y las evidencias históricas mantienen su alcance original.

La protección de main y la prueba interna de controles de PR fueron verificadas. Private Vulnerability Reporting está habilitado; comportamiento de fork/CI externo, recepción/confidencialidad de reportes e instalación/actualización/recuperación nativa del Plugin siguen pendientes. La pausa de escrituras terminó; el trabajo normal sigue mediante PRs protegidas.

[Notas de la candidata 0.4.0 y verificaciones pendientes (histórico)](docs/releases/0.4.0-candidate.es.md)

[Licencia](LICENSE) · [Contribución](docs/user-docs/guides/contributing.es.md) · [Reporte de seguridad](docs/user-docs/guides/security-reporting.es.md)

## Estado actual y adopción

VERSION y los tres manifiestos declaran 0.5.0. El catálogo de Codex (`.agents/plugins/marketplace.json`) y el catálogo de Claude (`.claude-plugin/marketplace.json`) seleccionan v0.5.0, disponible solo después de crear ese tag exacto; la referencia publicada más reciente es v0.4.0. Publicar una release no cambia los pins de los consumidores.

Instala en Claude Code:

```text
/plugin marketplace add versat-labs/versat-ai-harness
/plugin install versat-ai-harness@versat
```

Consulta [Preparar Claude](docs/user-docs/guides/claude-setup.es.md) para actualización, verificación y recuperación.

Los administradores gestionan importación del marketplace y política de instalación. Usa este repositorio como fuente, autentica con acceso de lectura, revisa la release exacta importada y confirma disponibilidad para los miembros. Sigue la interfaz actual de administración; la política del marketplace es AVAILABLE y no demuestra instalación automática. Los miembros pueden usar [la preparación del entorno](docs/user-docs/guides/workspace-setup.es.md).

## Estructura del repositorio y consumidores

La raíz del repositorio es el paquete Plugin. Las políticas están en standards/; capacidades en skills/; proceso en sdd/; aplicación mecánica en validators/ y CI; composición en project-templates/; contratos en schemas/; orientación de roles en agents/; conocimiento no normativo en resources/. Manifests y marketplace seleccionan recursos de la misma versión.

Los proyectos consumidores de agentes usan .agents/skills/, .codex/agents/ y workflows/. Un workflow necesita un ejecutor explícito; agents/*.md en la raíz no es registro nativo de Codex. Consulta [la arquitectura (inglés)](docs/architecture/overview.md) · [contrato de artefactos (inglés)](standards/core/agent-artifacts.md).

## Validación local

Usa Python 3.11+ en un entorno virtual desde la raíz de este repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-validation.txt
./scripts/validate/run.sh --quality-base origin/main
```

Puedes seleccionar un intérprete existente con PYTHON=/absolute/path/to/python. La entrada verifica paquete, registros SDD y regresiones de validadores/ejecución. No demuestra aprobación humana, CI remoto, merge ni comportamiento de otra aplicación. Las excepciones históricas de compatibilidad son explícitas.

## Contribuir y mantener

Usa $versat-sdd para cambios relevantes. Lee las instrucciones, revisa las tres etapas de planificación y autoriza explícitamente implementar después de Tasks. Prepara documentación viva y archivo documental en el mismo PR de entrega. Revisión del PR, verificaciones finales y merge son checkpoints distintos.

[SDD (inglés)](sdd/README.md) · [Instrucciones del repositorio (inglés)](AGENTS.md) · [ADRs (inglés)](docs/decisions/README.md) · [Versat Labs CONTRIBUTING (English)](https://github.com/versat-labs/.github/blob/main/CONTRIBUTING.md)
