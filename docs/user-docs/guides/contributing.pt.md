# Contribuir com procedência clara

[English](contributing.md) | [Português](contributing.pt.md) | [Español](contributing.es.md)

Esta é a orientação mantida para contribuir no candidato do Harness e selecionar um projeto de destino. Disponibilidade pública e adoção Apache do Harness estão pendentes. Até existirem, utilize apenas repositórios e termos autorizados; este guia não promete fork público nem instalação disponível.

## Preparar e contribuir

1. Escolha o repositório real e leia README, AGENTS e instruções de contribuição. Suas regras prevalecem sobre padrões da organização. Outros produtos mantêm termos e rotas independentes.
2. Selecione uma issue existente ou um formulário de bug, funcionalidade ou manutenção. Ao abrir uma issue ou alterar substancialmente sua definição, escreva o título e a descrição em inglês, incluindo as respostas do formulário, o resultado esperado e os passos para reproduzir o problema, quando aplicáveis. A equipe pode conversar em espanhol nos comentários. Se a discussão mudar o escopo ou os critérios de aceitação, atualize a descrição em inglês. Use o número real da issue ou da Story. Consulte o [padrão de idiomas](../../../standards/core/language.md#github-issues).
3. Identifique material próprio/de terceiros, fontes, versões, permissões e avisos. Direitos ausentes impedem aceitação. Leia [licenciamento](licensing.pt.md); a licença da ferramenta não determina termos de material independente no destino.
4. Siga a [preparação](workspace-setup.pt.md). No checkout do Harness, use Python 3.11+, instale `requirements-validation.txt` em ambiente virtual e execute `./scripts/validate/run.sh --quality-base origin/main` na raiz. Em outros projetos, use suas verificações próprias.
5. Quando repositório e permissões permitirem, use fork autorizado ou branch de trabalho e a [convenção Git](../../../standards/core/git.md). Acesso público de leitura/fork não concede escrita, merge ou release no repositório original.
6. Para mudanças materiais, siga os [três gates do SDD](sdd-with-codex.pt.md); solicite implementação explicitamente após aprovar Tasks. Inclua documentação mantida e verificações relevantes. Siga a [entrega](github-delivery.pt.md) para arquivo documental, revisão do PR e verificações finais, com autorização efetiva para operações remotas.

Resultado esperado: contribuição revisável com referências reais de issue/procedência e verificações observadas. Informe verificações indisponíveis; aprovação local não comprova proteção de branch nem aceitação.

## Termos candidatos de contribuição

Se e quando este candidato Apache for adotado, a seção 5 do [texto Apache exato](../../licensing/candidates/apache-2.0/LICENSE.txt) regerá contribuições intencionalmente submetidas para inclusão, salvo indicação explícita em contrário, conforme as definições da licença e eventual acordo separado. Este guia não acrescenta CLA, DCO ou cessão de propriedade intelectual. Até a adoção, utilize os termos efetivos do repositório/versão e esclareça ausências. A aprovação proprietária anterior e estas instruções não constituem uma licença efetiva.

## Revisão e recuperação

O mantenedor deve revisar escopo, procedência e verificações obrigatórias. CODEOWNERS identifica contatos técnicos, sem comprovar qualificação jurídica ou proteção ativa. Direitos ou revisão obrigatória ausentes impedem aceitação. Corrija falhas e obtenha novas evidências; mudanças de escopo reabrem o gate pertinente. Sem acesso, use a rota pública existente do destino sem o Harness quando apropriado, ou solicite instruções ao mantenedor visível sem divulgar informações confidenciais.

Não exponha vulnerabilidades em issues públicas; use [reporte de segurança](security-reporting.pt.md). Política canônica: [Contribution](../../../standards/core/contribution.md).

[Quickstart](../quickstart.pt.md) · [Harness](../../../README.pt.md)
