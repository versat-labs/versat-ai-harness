# Preparar o ambiente

[English](workspace-setup.md) | [Português](workspace-setup.pt.md) | [Español](workspace-setup.es.md)

Prepare o repositório em que trabalhará e confirme a versão disponível do Harness. A distribuição no workspace Versat é gerenciada por um administrador; política de instalação e acesso devem ser conferidos no seu workspace.

## Preparação

1. Obtenha acesso ao repositório alvo e leia seu README e orientações de contribuição. Clone-o com a URL real ou use um checkout existente limpo.
2. No Codex, abra esse repositório como pasta do projeto. Confirme que é a pasta principal antes de trabalhar.
3. Leia AGENTS.md e identifique a versão do Harness/provedor e o lock de Standards quando presentes. Peça ao Codex para localizar a Skill necessária e os recursos canônicos correspondentes antes de alterar arquivos.

A OpenAI documenta a seleção de pastas em [Projects and chats (inglês)](https://learn.chatgpt.com/docs/projects). Ações de preparação podem ser compartilhadas por [local environments (inglês)](https://learn.chatgpt.com/docs/environments/local-environment); configure apenas os comandos exigidos pelo seu repositório.

## Verificar e recuperar

Peça ao Codex para informar diretório de trabalho, versão do provedor e onde encontrou versat-sdd. Os caminhos devem pertencer ao projeto/provedor pretendido. Se faltar acesso ou uma Skill, pare esse fluxo e procure o responsável pelo repositório ou workspace. Não copie políticas de outra release nem presuma instalação automática. Um repositório sem metadados de identidade precisa ser classificado antes de bootstrap ou migração.

Para usar o Harness no Claude Code em vez do Codex, siga [Preparar o Claude](claude-setup.pt.md).

[Continuar para o início rápido](../quickstart.pt.md)

## Instalação candidata, atualizações exatas e recuperação

Atualização: a v0.4.0 foi publicada em 2026-11-24, e os dois catálogos do repositório agora selecionam a v0.5.0, disponível quando sua tag for criada após o merge. O restante deste parágrafo registra o estado anterior da candidata. A candidata local 0.4.0 usa o marketplace `versat` / `Versat Plugins`, preservando o plugin `versat-ai-harness`. A tag exata v0.4.0 ainda não está disponível. O proprietário informa que somente Elvis e Everton usam o Harness; ambos reinstalarão manualmente depois. O acompanhamento da main é aceito neste escopo, incluindo possível interrupção/reparo manual; pin prévio ou ensaio isolado não são requisitos para entregar o código. Identidade/sincronização nativa continuam não verificadas. Veja o [guia de transição e recuperação](marketplace-transition.pt.md).

## Ensaio legado histórico — não são instruções de transição

Os comandos e observações abaixo pertencem ao ensaio legado autorizado anteriormente. Não os execute no perfil atual nesta transição; siga os pré-requisitos da reinstalação manual posterior no guia de transição.

O proprietário escolheu uma instalação individual com o mesmo usuário da Versat para o ensaio privado. No Codex desktop 26.915.31945/build 9922, o CLI incluído instalou `versat-ai-harness@versat-internal` versão 0.4.0 em um cache local separado; os arquivos do plugin 0.3.0 do workspace permaneceram iguais. A cópia instalada correspondeu a todos os arquivos da origem e resolveu as cinco Skills e os recursos canônicos. Isso verifica a etapa de instalação privada, não acesso anônimo, release público nem toda a suíte comportamental.

Neste build macOS, os comandos observados foram:

```sh
harness_test_catalog=/absolute/path/to/reviewed-private-catalog
/Applications/Codex.app/Contents/Resources/codex plugin marketplace add "$harness_test_catalog" --json
/Applications/Codex.app/Contents/Resources/codex plugin add versat-ai-harness@versat-internal --json
```

O catálogo local revisado se chama `versat-internal` e aponta `source.path` para o candidato privado exato dentro de sua raiz; é um adaptador de teste, não substituto do marketplace versionado do repositório. Antes de executar, confirme que a entrada/cache pessoal não existe ou tem substituição explicitamente autorizada, preservando a instalação do workspace. Confira identidade, versão e caminho retornados, compare os arquivos reais e inicie um contexto sintético novo com esse provedor instalado exato. Não confunda duas instalações de mesmo nome nem use a Skill de outro provedor. Uma instalação local pode ser individual mesmo quando o usuário pertence a um workspace.

A [documentação oficial](https://developers.openai.com/plugins/build/plugins) descreve catálogos locais; o [registro de preparação](../../handoffs/harness-publication-readiness/README.md) identifica escopo observado e verificações pendentes. O contexto local compartilha permissões do usuário e não é isolamento de segurança. Primeiro uso, falhas, atualização explícita e recuperação exigem observações próprias. Uma conta externa não é necessária neste ensaio privado; a aceitação pública posterior ainda deve usar um usuário externo sem vínculo privado.

Para uma atualização explícita, registre o provedor exato anterior e o par lock/config do projeto; revise a substituição exata e compatibilidade antes de alterar o consumidor. Teste primeiro em contexto descartável. Após falha, preserve ou restaure o último par compatível verificado e registre o resultado. Acesso ausente, referência indisponível, runtime incompatível ou recursos canônicos ausentes devem interromper o fluxo, sem escolher `latest`. Consumidor com registros SDD v3 ativos deve manter provedor compatível verificado; não use tag incapaz de lê-los nem remova marcadores de versão. Publicação ou atualização do marketplace não migra consumidores por si só.

Resultado esperado: provedor selecionado e locais reais dos recursos identificados, ou pré-requisito específico marcado como não verificado. Acesso anônimo, instalação externa e recuperação após publicação continuam sendo verificações operacionais autorizadas separadamente.
