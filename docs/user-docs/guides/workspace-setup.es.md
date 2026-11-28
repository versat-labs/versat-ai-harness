# Preparar el entorno

[English](workspace-setup.md) | [Português](workspace-setup.pt.md) | [Español](workspace-setup.es.md)

Prepara el repositorio en el que trabajarás y confirma la versión disponible del Harness. La distribución en el workspace Versat la gestiona un administrador; verifica allí la política de instalación y el acceso.

## Preparación

1. Obtén acceso al repositorio destino y lee su README y pautas de contribución. Clónalo con la URL real o usa un checkout existente limpio.
2. En Codex, abre ese repositorio como carpeta del proyecto. Confirma que sea la carpeta principal antes de trabajar.
3. Lee AGENTS.md e identifica la versión del Harness/proveedor y el lock de Standards cuando existan. Pide a Codex localizar la Skill necesaria y los recursos canónicos correspondientes antes de modificar archivos.

OpenAI documenta la selección de carpetas en [Projects and chats (inglés)](https://learn.chatgpt.com/docs/projects). Las acciones de preparación pueden compartirse mediante [local environments (inglés)](https://learn.chatgpt.com/docs/environments/local-environment); configura solo los comandos requeridos por tu repositorio.

## Verificar y recuperar

Pide a Codex informar directorio de trabajo, versión del proveedor y dónde encontró versat-sdd. Las rutas deben pertenecer al proyecto/proveedor previsto. Si falta acceso o una Skill, detén ese flujo y consulta al responsable del repositorio o workspace. No copies políticas de otra release ni supongas instalación automática. Un repositorio sin metadatos de identidad requiere clasificación antes de bootstrap o migración.

Para usar el Harness en Claude Code en lugar de Codex, sigue [Preparar Claude](claude-setup.es.md).

[Continuar al inicio rápido](../quickstart.es.md)

## Instalación candidata, actualizaciones exactas y recuperación

Actualización: la v0.4.0 se publicó el 2026-11-24, y ambos catálogos del repositorio ahora seleccionan la v0.5.0, disponible cuando se cree su tag después del merge. El resto de este párrafo registra el estado anterior de la candidata. La candidata local 0.4.0 usa el marketplace `versat` / `Versat Plugins`, conservando el plugin `versat-ai-harness`. La etiqueta exacta v0.4.0 aún no está disponible. El propietario informa que solo Elvis y Everton usan el Harness; ambos reinstalarán manualmente después. Se acepta el seguimiento de main para este alcance, incluida posible interrupción/reparación manual; no se exige fijación previa ni ensayo aislado para entregar el código. Identidad/sincronización nativa siguen sin verificar. Consulte la [guía de transición y recuperación](marketplace-transition.es.md).

## Ensayo heredado histórico — no son instrucciones de transición

Los comandos y observaciones siguientes pertenecen al ensayo heredado autorizado anteriormente. No los ejecute en el perfil actual para esta transición; siga los prerrequisitos de la reinstalación manual posterior en la guía de transición.

El propietario eligió una instalación individual con el mismo usuario de Versat para el ensayo privado. En Codex desktop 26.915.31945/build 9922, el CLI incluido instaló `versat-ai-harness@versat-internal` versión 0.4.0 en una caché local separada; los archivos del plugin 0.3.0 del workspace permanecieron iguales. La copia instalada coincidió con todos los archivos de origen y resolvió las cinco Skills y recursos canónicos. Esto verifica la instalación privada, no acceso anónimo, release pública ni toda la suite de comportamiento.

En este build macOS, los comandos observados fueron:

```sh
harness_test_catalog=/absolute/path/to/reviewed-private-catalog
/Applications/Codex.app/Contents/Resources/codex plugin marketplace add "$harness_test_catalog" --json
/Applications/Codex.app/Contents/Resources/codex plugin add versat-ai-harness@versat-internal --json
```

El catálogo local revisado se llama `versat-internal` y apunta `source.path` al candidato privado exacto dentro de su raíz; es un adaptador de prueba, no sustituto del marketplace versionado del repositorio. Antes de ejecutar, confirme que la entrada/caché personal no existe o tiene sustitución explícitamente autorizada, preservando la instalación del workspace. Compruebe identidad, versión y ruta devueltas, compare archivos reales e inicie un contexto sintético nuevo con ese proveedor instalado exacto. No confunda dos instalaciones del mismo nombre ni use la Skill de otro proveedor. Una instalación local puede ser individual aunque el usuario pertenezca a un workspace.

La [documentación oficial](https://developers.openai.com/plugins/build/plugins) describe catálogos locales; el [registro de preparación](../../handoffs/harness-publication-readiness/README.md) identifica alcance observado y verificaciones pendientes. El contexto local comparte permisos del usuario y no es aislamiento de seguridad. Primer uso, fallos, actualización explícita y recuperación necesitan observaciones propias. Una cuenta externa no es necesaria para este ensayo privado; la aceptación pública posterior aún requiere un usuario externo sin pertenencia privada.

Para una actualización explícita, registre el proveedor exacto anterior y el par lock/config del proyecto; revise la sustitución exacta y compatibilidad antes de modificar al consumidor. Pruebe primero en contexto descartable. Tras un fallo, conserve o restaure el último par compatible verificado y registre el resultado. Acceso ausente, referencia no disponible, runtime incompatible o recursos canónicos faltantes deben detener el flujo, sin elegir `latest`. Un consumidor con registros SDD v3 activos debe conservar un proveedor compatible verificado; no use etiquetas incapaces de leerlos ni elimine marcadores de versión. Publicación o actualización del marketplace no migra consumidores por sí sola.

Resultado esperado: proveedor seleccionado y ubicaciones reales de recursos identificados, o un requisito específico declarado sin verificar. Acceso anónimo, instalación externa y recuperación tras publicación siguen siendo verificaciones operativas autorizadas separadamente.
