# Preparar o Claude

[English](claude-setup.md) | [Português](claude-setup.pt.md) | [Español](claude-setup.es.md)

Instale o Versat AI Harness no Claude Code (terminal, desktop ou web) pelo marketplace do repositório, mantenha-o em uma release exata e verifique qual provider a sessão usa.

## Pré-requisitos

- Claude Code 2.1.277 ou posterior; execute `claude --version`.
- Acesso de leitura a `github.com/versat-labs/versat-ai-harness` (público).
- A release desejada existe como tag Git. Os dois catálogos do repositório selecionam `v<VERSION>`; o suporte ao Claude começa na 0.5.0, que só pode ser instalada depois que a tag `v0.5.0` for criada no commit de merge. Tags anteriores não têm catálogo do Claude.

## Instalar

Em uma sessão do Claude Code:

```text
/plugin marketplace add versat-labs/versat-ai-harness
/plugin install versat-ai-harness@versat
```

Pelo terminal, os comandos equivalentes são:

```sh
claude plugin marketplace add versat-labs/versat-ai-harness
claude plugin install versat-ai-harness@versat
```

O marketplace se chama `versat`. Sua única entrada instala `versat-ai-harness` deste repositório na tag exata selecionada pelo catálogo. Inicie uma nova sessão depois de instalar.

## Atualizar

Por padrão, o Claude não atualiza automaticamente marketplaces de terceiros. Escolha uma opção:

- Ativar a atualização automática: execute `/plugin`, abra **Marketplaces**, selecione `versat` e ative a atualização automática.
- Atualizar explicitamente: `claude plugin marketplace update versat` e depois `claude plugin update versat-ai-harness@versat`.

Uma atualização leva a instalação para a tag selecionada pelo catálogo atual. Ela não altera nenhum lockfile de projeto; os projetos adotam uma nova release do Harness por uma migração revisada.

## Verificar

1. `claude plugin list` mostra `versat-ai-harness@versat` habilitado, com a versão esperada.
2. Em uma nova sessão, peça: “Usando a Skill versat-sdd, informe a VERSION do Harness e os caminhos de sdd/process.md e standards/index.yaml que você resolveu.” Os caminhos devem estar dentro do diretório do plugin instalado e a VERSION deve coincidir com a versão instalada.
3. O plugin fornece sete Skills e nenhum subagente. Os arquivos Markdown do diretório `agents/` do pacote são orientações de papéis para leitura explícita, não subagentes do Claude.

Se uma Skill estiver ausente ou resolver arquivos de outro local, pare e corrija a instalação antes de executar um fluxo.

## Instruções do projeto

Os projetos Versat mantêm suas regras no `AGENTS.md`. O Claude lê o `CLAUDE.md`; o Agent Artifact Standard exige um `CLAUDE.md` cujo único conteúdo é `@AGENTS.md`, para que o Claude carregue as mesmas regras. Projetos novos o recebem do template base; projetos existentes o adotam pela [manutenção de projeto](project-maintenance.pt.md), e a [auditoria de projeto](project-audit.pt.md) aponta um arquivo ausente ou divergente. Não coloque regras no `CLAUDE.md`.

## Recuperação

- Fixar uma release exata: `claude plugin marketplace remove versat`, depois `claude plugin marketplace add versat-labs/versat-ai-harness#v0.5.0` (ou uma tag posterior) e reinstale. Tags anteriores à v0.5.0 não têm catálogo do Claude. Nunca selecione um branch ou `latest`.
- Uma atualização com falha só preserva a última release verificada se ela estiver fixada; registre a falha e informe os mantenedores.
- Um projeto com registros SDD v3 ativos precisa de um provider compatível com v3 (0.3.0 ou posterior).

## Estado da verificação

Os arquivos de marketplace e plugin passam no `claude plugin validate` e no validador de pacote do Harness. A instalação a partir de um catálogo local de teste foi exercitada em uma configuração isolada durante a preparação da release. A instalação pelo GitHub em `v0.5.0`, a atualização automática e a atualização explícita ainda não foram observadas; trate-as como não verificadas até o acompanhamento da release registrá-las.
