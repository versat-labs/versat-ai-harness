# Versat AI Harness

[English](README.md) | [Português](README.pt.md) | [Español](README.es.md)

Fuente de verdad de Versat para desarrollo asistido por IA: un Plugin portátil con Standards, Spec Driven Development (SDD), Skills reutilizables, plantillas compuestas y validación determinista.

Para quienes desarrollan, revisan y mantienen proyectos, incluidos contribuidores externos cuando acceso y términos aplicables estén disponibles. Mantenido por Versat; los CODEOWNERS generales y responsables de triaje de seguridad son @elviszoz y @evertonspohrversat, con coordinación de Elvis. La política exige una aprobación elegible de quien no abrió la PR. La elegibilidad sigue el CODEOWNERS de la rama base; esta preparación local no activa controles en GitHub ni demuestra entrega de reportes de seguridad. Consulte el [handoff actual](docs/handoffs/harness-publication-blockers/README.md).

## Comienza aquí

[Inicio rápido: obtener un primer plan SDD](docs/user-docs/quickstart.es.md) · [Contexto del producto](docs/product/overview.es.md)

- [Preparar el entorno](docs/user-docs/guides/workspace-setup.es.md)
- [SDD con Codex](docs/user-docs/guides/sdd-with-codex.es.md)
- [Entrega mediante GitHub](docs/user-docs/guides/github-delivery.es.md)
- [Iniciar un proyecto](docs/user-docs/guides/project-bootstrap.es.md)
- [Mantener un proyecto existente](docs/user-docs/guides/project-maintenance.es.md)
- [Auditar un proyecto](docs/user-docs/guides/project-audit.es.md)
- [Revisar la arquitectura](docs/user-docs/guides/architecture-review.es.md)
- [Validación y evaluaciones](docs/user-docs/guides/validation-and-evaluations.es.md)
- [Documentación electrónica SIFEN](docs/user-docs/guides/sifen-electronic-documentation.es.md)

## Preparación de la publicación en curso

La licencia Apache-2.0 y los avisos aprobados están aplicados en esta rama local de entrega. La integración en main y la distribución pública siguen pendientes; 0.4.0 no es una release disponible. La [aprobación del texto](docs/licensing/candidates/apache-2.0/APPROVAL.md) permanece como revisión histórica sin cambios. Consulte [licencias](docs/user-docs/guides/licensing.es.md), [contribución](docs/user-docs/guides/contributing.es.md), [reporte de seguridad](docs/user-docs/guides/security-reporting.es.md) y la [resolución actual de pendientes](docs/handoffs/harness-publication-blockers/README.md).

La secuencia aprobada en GitHub Free mantiene privadas la preparación y la revisión; después exige autorización separada para hacer público el repositorio y proteger/verificar main inmediatamente, en un máximo de 15 minutos. Las verificaciones reales de controles, reporte y uso externo preceden cualquier release posterior. La secuencia está preparada, no ejecutada; consulte el [handoff operativo actual](docs/handoffs/harness-publication-blockers/README.md).

## Estado actual y adopción

VERSION y manifiestos ahora declaran el candidato local 0.4.0. Su catálogo en el repositorio selecciona v0.4.0, que no debe importarse como release disponible antes de crear y verificar esa etiqueta exacta bajo autorización separada. Las instalaciones existentes y referencias de consumidores permanecen iguales; la referencia publicada anterior es v0.3.0.

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
