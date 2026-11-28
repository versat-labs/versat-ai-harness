# Preparar Claude

[English](claude-setup.md) | [Português](claude-setup.pt.md) | [Español](claude-setup.es.md)

Instala Versat AI Harness en Claude Code (terminal, escritorio o web) desde el marketplace del repositorio, mantenlo en una release exacta y verifica qué provider usa tu sesión.

## Requisitos previos

- Claude Code 2.1.277 o posterior; ejecuta `claude --version`.
- Acceso de lectura a `github.com/versat-labs/versat-ai-harness` (público).
- La release deseada existe como tag de Git. Ambos catálogos del repositorio seleccionan `v<VERSION>`; el soporte para Claude empieza en 0.5.0, que solo se puede instalar después de crear el tag `v0.5.0` en su commit de merge. Los tags anteriores no tienen catálogo de Claude.

## Instalar

En una sesión de Claude Code:

```text
/plugin marketplace add versat-labs/versat-ai-harness
/plugin install versat-ai-harness@versat
```

Desde una terminal, los comandos equivalentes son:

```sh
claude plugin marketplace add versat-labs/versat-ai-harness
claude plugin install versat-ai-harness@versat
```

El marketplace se llama `versat`. Su única entrada instala `versat-ai-harness` desde este repositorio en el tag exacto que selecciona el catálogo. Inicia una nueva sesión después de instalar.

## Actualizar

Claude no actualiza automáticamente los marketplaces de terceros por defecto. Elige una opción:

- Activar la actualización automática: ejecuta `/plugin`, abre **Marketplaces**, selecciona `versat` y activa la actualización automática.
- Actualizar explícitamente: `claude plugin marketplace update versat` y luego `claude plugin update versat-ai-harness@versat`.

Una actualización lleva la instalación al tag que selecciona el catálogo actual. No cambia ningún lockfile de proyecto; los proyectos adoptan una nueva release del Harness mediante una migración revisada.

## Verificar

1. `claude plugin list` muestra `versat-ai-harness@versat` habilitado con la versión esperada.
2. En una nueva sesión, pide: “Usando la Skill versat-sdd, informa la VERSION del Harness y las rutas de sdd/process.md y standards/index.yaml que resolviste.” Las rutas deben estar dentro del directorio del plugin instalado y la VERSION debe coincidir con la versión instalada.
3. El plugin proporciona siete Skills y ningún subagente. Los archivos Markdown del directorio `agents/` del paquete son orientación de roles para lectura explícita, no subagentes de Claude.

Si falta una Skill o resuelve archivos de otra ubicación, detente y corrige la instalación antes de ejecutar un flujo.

## Instrucciones del proyecto

Los proyectos Versat mantienen sus reglas en `AGENTS.md`. Claude lee `CLAUDE.md`; el Agent Artifact Standard exige un `CLAUDE.md` cuyo único contenido sea `@AGENTS.md`, para que Claude cargue las mismas reglas. Los proyectos nuevos lo reciben de la plantilla base; los existentes lo adoptan mediante el [mantenimiento de proyectos](project-maintenance.es.md), y la [auditoría de proyectos](project-audit.es.md) informa un archivo ausente o divergente. No pongas reglas en `CLAUDE.md`.

## Recuperación

- Fijar una release exacta: `claude plugin marketplace remove versat`, luego `claude plugin marketplace add versat-labs/versat-ai-harness#v0.5.0` (o un tag posterior) y reinstala. Los tags anteriores a v0.5.0 no tienen catálogo de Claude. Nunca selecciones una rama ni `latest`.
- Una actualización fallida solo conserva la última release verificada si la mantienes fijada; registra la falla e infórmala a los mantenedores.
- Un proyecto con registros SDD v3 activos necesita un provider compatible con v3 (0.3.0 o posterior).

## Estado de la verificación

Los archivos de marketplace y plugin pasan `claude plugin validate` y el validador de paquete del Harness. La instalación desde un catálogo local de prueba se ejercitó en una configuración aislada durante la preparación de la release. La instalación desde GitHub en `v0.5.0`, la actualización automática y la actualización explícita aún no se han observado; trátalas como no verificadas hasta que el seguimiento de la release las registre.
