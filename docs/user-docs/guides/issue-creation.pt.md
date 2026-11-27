# Criar uma issue no GitHub

[English](issue-creation.md) | [Português](issue-creation.pt.md) | [Español](issue-creation.es.md)

Use a Skill `github-issue-creation` para transformar uma ideia ou um problema detectado em uma issue completa no GitHub, em um repositório da `versat-labs`. Você pode descrevê-la em inglês, português ou espanhol; a issue é sempre escrita em inglês.

## Pré-requisitos

- O Plugin do Harness instalado e o repositório de destino em uso, com o remote `origin` na `versat-labs`.
- Acesso ao GitHub pelo seu agente, por um servidor MCP do GitHub ou pelo GitHub CLI autenticado com `gh auth login`.
- Permissão de push no repositório, necessária para definir o campo de issue "Origin".
- No GitHub CLI, o escopo `project` para adicionar issues ao projeto "Portfolio" da organização: `gh auth refresh -s project`.
- Python com PyYAML, conforme o `requirements-validation.txt` do Harness.

## Experimente

```text
Use $github-issue-creation para abrir uma issue: a exportação do relatório mensal para CSV falha por timeout quando tem mais de 10.000 linhas. Deveria terminar em menos de um minuto.
```

## O que acontece

1. A Skill lê os formulários de issue do próprio repositório, ou os padrões da organização em `versat-labs/.github`: Bug report, Feature request e Chore.
2. Ela escolhe o formulário. Se a sua intenção couber em mais de um, pergunta qual você quer.
3. Ela redige o título e os campos em inglês, mantendo código, comandos e saídas de erro exatamente como você escreveu.
4. Ela pede, em uma única mensagem, qualquer campo obrigatório que não conseguiu preencher, como os passos de reprodução de um bug ou a persona de uma feature.
5. Ela pergunta o "Origin", a menos que você já o tenha informado: **Internal Idea**, para um codeowner ou membro da equipe Versat; **External suggestion**, para um contribuidor externo, cliente ou parceiro; ou **VIP Customer feature request**, para um cliente VIP que paga pelo desenvolvimento.
6. Ela mostra uma prévia com o repositório, o formulário, o título, o corpo, o tipo, o Origin e o projeto "Portfolio". Nada é criado até você confirmar. Issues em um repositório público são públicas; retire nomes de clientes ou outros dados sensíveis antes de confirmar.
7. Ela cria a issue, define o tipo e o Origin, adiciona a issue ao "Portfolio" e informa o link e o resultado de cada passo.

## Resultados e falhas

A Skill informa apenas o que o GitHub confirmou. Quando um passo posterior à criação falha, como a falta do escopo `project`, você recebe o link da issue e instruções para concluir esse passo na barra lateral da issue. Quando a própria criação falha, nenhuma issue existe e a Skill indica o pré-requisito que falta. Ela nunca tenta criar de novo por conta própria, para evitar duplicadas.

A Skill não anexa arquivos. Adicione capturas de tela no GitHub depois da criação.

## Vulnerabilidades de segurança

Não relate uma suspeita de vulnerabilidade como issue. Quando a sua descrição parecer uma, a Skill não cria nada e indica a rota privada nas [orientações de relato de segurança](https://github.com/versat-labs/.github/blob/main/SECURITY.pt.md):

- Em um repositório público, use **Security → Report a vulnerability**.
- Em um repositório privado, envie e-mail aos CODEOWNERS responsáveis pelos canais internos existentes da Versat.
- Quando a rota não estiver disponível, peça instruções privadas a um maintainer sem compartilhar detalhes.
