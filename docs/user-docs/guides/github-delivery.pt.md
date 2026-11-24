# Entrega pelo GitHub

[English](github-delivery.md) | [Português](github-delivery.pt.md) | [Español](github-delivery.es.md)

Use este guia ao preparar uma mudança vinculada a uma issue para revisão humana. Você precisa da URL real da issue, instruções do repositório, escopo aprovado e ambiente de validação do projeto.

## Experimente

Pedido ilustrativo; substitua o ID ou forneça os dados reais do projeto:

```text
Use $versat-sdd para inspecionar <change-id>, preparar o resumo de entrega e identificar pré-requisitos de arquivo ou validação ausentes. Não publique PR nem faça merge.
```

## Resultado esperado

Trabalhe em uma branch seguindo a convenção Git resolvida. Mantenha rastreabilidade entre issue, requisitos e commits; não invente um ID do Shortcut. Planejamento ou trabalho incompleto é revisado em PR draft. Antes de submeter a implementação concluída, prepare o arquivo documental na mesma branch e passe no preflight de arquivo selecionado. Solicite a publicação do PR explicitamente; depois obtenha revisão humana e CI obrigatório final antes do merge.

## Recuperação e limites

Informe no PR as verificações falhas ou indisponíveis. O feedback da revisão permanece no mesmo ID; mudanças de escopo reabrem a revisão correspondente. Verifique o merge real separadamente da prontidão local. Um merge não publica uma release nem atualiza consumidores instalados.

## Segurança de repositórios públicos no GitHub

Use o [procedimento de segurança do provedor exato (inglês)](../../guides/public-repository-security.md). Prepare os arquivos com `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging` e execute `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` a partir desse provedor. Para consumidores instalados, acrescente `--project-root /absolute/consumer` com o lock exato correspondente. Revise as diferenças e preserve checks mais fortes e conflitos de ownership; somente operações administrativas autorizadas aplicam a configuração.

A prontidão pública exige uma verificação atual e completa em modo live com `public_ready: true`. Um esqueleto local, check de política, snapshot salvo ou código de saída 0 isolado é insuficiente. Permissões ou observações ausentes permanecem não verificadas. Auditoria não autoriza edições; manutenção verifica correções autorizadas e nunca escolhe `latest` silenciosamente. Uma aprovação de CODEOWNER elegível atende à regra básica, mesmo quando ambos receberam solicitação de review. Contribuidores externos usam forks e PRs; o CI de forks não recebe credenciais administrativas. Publicação de release e adoção continuam separadas.

## Referências

- [Git (inglês)](../../../standards/core/git.md)
- [SDD (inglês)](../../../sdd/README.md)
- [SDD validation (inglês)](../../../validators/sdd/README.md)

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
