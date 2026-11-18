# Documentação eletrônica SIFEN

[English](sifen-electronic-documentation.md) | [Português](sifen-electronic-documentation.pt.md) | [Español](sifen-electronic-documentation.es.md)

Use a [skill SIFEN](../../../skills/sifen-electronic-documentation/SKILL.md) para consultar o Manual v150, as Notas 1–27 e as guias de testes/envio fornecidas. Esta adição ao código-fonte ainda não foi lançada; uma versão publicada anterior do Harness não a inclui. O snapshot declarado termina em **2026-03-09**. Conclusões sobre produção atual exigem verificar fontes oficiais posteriores. A consulta local não certifica conformidade fiscal.

Na raiz do checkout do Harness realmente instalado, com Python 3.11+:

```sh
export SIFEN_SKILL_ROOT="$PWD/skills/sifen-electronic-documentation"
python3 "$SIFEN_SKILL_ROOT/scripts/query_rules.py" GENFE010 --include notes --context 2 --max 50
```

Os utilitários usam a biblioteca padrão Python. A busca é literal e ignora diferenças entre maiúsculas/minúsculas por padrão; use `--regex` e `--case-sensitive` para alterar esses modos. `--include` filtra caminhos relativos. A ausência de resultados retorna sucesso com uma mensagem. Argumentos inválidos, acervo ausente/ilegível ou seleção sem arquivos-fonte retornam erro. A mensagem de limite indica que mais fontes podem precisar de consulta. Pesquise Notas e Manual separadamente, leia o contexto e cite páginas reais; informe documentos ausentes e extrações ambíguas.

Exemplo de pedido:

> Use $sifen-electronic-documentation para explicar GENFE010 em Produção em 2026-03-09, usando as fontes locais. Cite a Nota aplicável e não modifique arquivos nem envie documentos.

## Exportação opcional

Exporte somente quando quiser adicionar instruções a um projeto escolhido:

```sh
python3 "$SIFEN_SKILL_ROOT/scripts/export_agent.py" generic --destination /path/to/project
```

Plataformas: `claude`, `gemini`, `copilot`, `cursor`, `generic`. Todas as colisões são verificadas antes da escrita; arquivos existentes causam erro sem saída parcial. `--force` substitui explicitamente arquivos de saída regulares existentes. A exportação não copia o acervo nem instala um agente nativo do Codex. Configure `SIFEN_SKILL_ROOT` no executor de destino ou forneça o caminho instalado verificado; ele precisa acessar a skill e os Standards do Harness. Os arquivos gerados são testados como artefatos; não se afirma compatibilidade em execução com todas as versões de IDEs.

Os arquivos oficiais e suas extrações preservam idioma e hashes. As instruções autorais estão em inglês. Consulte a [procedência](../../../skills/sifen-electronic-documentation/references/provenance.md) para a declaração de autoria e a liberação pendente de redistribuição de terceiros. O código e a documentação autorais desta skill usam [Apache-2.0](../../../skills/sifen-electronic-documentation/LICENSE-SCOPE.md); as fontes oficiais estão excluídas. A licença do restante do repositório não muda e nenhuma release é publicada.

Execute a validação completa com `./scripts/validate/run.sh`, após instalar `requirements-validation.txt` no ambiente Python documentado. A suíte específica usa `python -m unittest discover -s tests/skills -p test_sifen_documentation.py`; ela não substitui a suíte completa nem a evidência supervisionada.
