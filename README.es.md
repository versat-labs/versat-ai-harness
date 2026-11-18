# Versat AI Harness

[English](README.md) | [Português](README.pt.md) | [Español](README.es.md)

Fuente de verdad de Versat para desarrollo asistido por IA: un Plugin portátil con Standards, Spec Driven Development (SDD), Skills reutilizables, plantillas compuestas y validación determinista.

Para quienes desarrollan, revisan y mantienen proyectos, incluidos contribuidores externos cuando acceso y términos aplicables estén disponibles. Mantenido por Versat; los contactos de revisión de componentes gobernados son @elviszoz y @evertonspohrversat en .github/CODEOWNERS.

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

La dirección pública Apache-2.0 está aprobada. El [candidato concreto](docs/licensing/candidates/apache-2.0/APPROVAL.md) tiene aprobación del texto y no está adoptado. El repositorio sigue privado; 0.4.0 es un candidato futuro, no una versión disponible. Consulte [licencias](docs/user-docs/guides/licensing.es.md), [contribución](docs/user-docs/guides/contributing.es.md), [reporte de seguridad](docs/user-docs/guides/security-reporting.es.md) y el [estado de preparación](docs/handoffs/harness-publication-readiness/README.md).

## Estado actual y adopción

VERSION declara 0.3.0. El marketplace selecciona la etiqueta exacta v0.3.0; verifica la etiqueta y su contenido antes de distribuir. La ejecución de consumidores y evaluaciones supervisadas del código actual son explícitamente no publicadas. Cambiar el código o hacer merge no actualiza Plugins instalados ni pins de consumidores. Adopta otra release exacta mediante un cambio revisado.

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
./scripts/validate/run.sh
```

Puedes seleccionar un intérprete existente con PYTHON=/absolute/path/to/python. La entrada verifica paquete, registros SDD y regresiones de validadores/ejecución. No demuestra aprobación humana, CI remoto, merge ni comportamiento de otra aplicación. Las excepciones históricas de compatibilidad son explícitas.

## Contribuir y mantener

Usa $versat-sdd para cambios relevantes. Lee las instrucciones, revisa las tres etapas de planificación y autoriza explícitamente implementar después de Tasks. Prepara documentación viva y archivo documental en el mismo PR de entrega. Revisión del PR, verificaciones finales y merge son checkpoints distintos.

[SDD (inglés)](sdd/README.md) · [Instrucciones del repositorio (inglés)](AGENTS.md) · [ADRs (inglés)](docs/decisions/README.md) · [Versat Labs CONTRIBUTING (English)](https://github.com/versat-labs/.github/blob/main/CONTRIBUTING.md)
