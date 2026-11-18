# Documentación electrónica SIFEN

[English](sifen-electronic-documentation.md) | [Português](sifen-electronic-documentation.pt.md) | [Español](sifen-electronic-documentation.es.md)

Usa la [skill SIFEN](../../../skills/sifen-electronic-documentation/SKILL.md) para consultar el Manual v150, las Notas 1–27 y las guías de pruebas/envío suministradas. Esta incorporación al código fuente aún no se ha publicado; una versión publicada anterior del Harness no la incluye. El snapshot declarado termina el **2026-03-09**. Las conclusiones sobre producción actual requieren verificar fuentes oficiales posteriores. La consulta local no certifica conformidad fiscal.

Desde la raíz del checkout del Harness realmente instalado, con Python 3.11+:

```sh
export SIFEN_SKILL_ROOT="$PWD/skills/sifen-electronic-documentation"
python3 "$SIFEN_SKILL_ROOT/scripts/query_rules.py" GENFE010 --include notes --context 2 --max 50
```

Los utilitarios usan la biblioteca estándar Python. La búsqueda es literal e ignora mayúsculas/minúsculas por defecto; `--regex` y `--case-sensitive` cambian esos modos. `--include` filtra rutas relativas. Sin coincidencias se devuelve éxito con un mensaje. Argumentos inválidos, corpus ausente/ilegible o una selección sin archivos fuente devuelven error. El mensaje de límite indica que puede ser necesario consultar más fuentes. Busca Notas y Manual por separado, lee el contexto y cita páginas reales; declara documentos ausentes y extracciones ambiguas.

Ejemplo de solicitud:

> Usa $sifen-electronic-documentation para explicar GENFE010 en Producción el 2026-03-09 con las fuentes locales. Cita la Nota aplicable y no modifiques archivos ni envíes documentos.

## Exportación opcional

Exporta solo cuando quieras añadir instrucciones a un proyecto elegido:

```sh
python3 "$SIFEN_SKILL_ROOT/scripts/export_agent.py" generic --destination /path/to/project
```

Plataformas: `claude`, `gemini`, `copilot`, `cursor`, `generic`. Se comprueban todas las colisiones antes de escribir; los archivos existentes causan un error sin salida parcial. `--force` sustituye explícitamente archivos de salida regulares existentes. La exportación no copia el corpus ni instala un agente nativo de Codex. Configura `SIFEN_SKILL_ROOT` en el ejecutor de destino o proporciona la ruta instalada verificada; necesita acceder a la skill y a los Standards del Harness. Los archivos generados se prueban como artefactos; no se afirma compatibilidad en ejecución con todas las versiones de IDE.

Los archivos oficiales y sus extractos conservan el idioma y los hashes. El material de autoría de la skill usa [Apache-2.0](../../../skills/sifen-electronic-documentation/LICENSE-SCOPE.md). Para el acervo oficial, consulta la [atribución a la DNIT y los términos aplicables](../../../skills/sifen-electronic-documentation/references/attribution-notice.md) y la [procedencia de las fuentes](../../../skills/sifen-electronic-documentation/references/provenance.md).

Ejecuta la validación completa con `./scripts/validate/run.sh` tras instalar `requirements-validation.txt` en el entorno Python documentado. La suite específica usa `python -m unittest discover -s tests/skills -p test_sifen_documentation.py`; no sustituye la suite completa ni la evidencia supervisada.
