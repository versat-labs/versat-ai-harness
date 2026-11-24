# Manter um projeto existente

[English](project-maintenance.md) | [Português](project-maintenance.pt.md) | [Español](project-maintenance.es.md)

Use manutenção para upgrades ou divergências em um repositório existente. Informe identidade/lockfile atual, release alvo explícita, adaptações locais e comandos de validação mantidos.

## Experimente

Pedido ilustrativo; substitua o ID ou forneça os dados reais do projeto:

```text
Use $project-maintenance para comparar este repositório com a release alvo exata do Harness que forneci. Preserve mudanças locais, apresente conflitos de migração e um plano de rollback, e não publique mudanças remotas.
```

## Resultado esperado

Espere um diff revisável de snapshots de Standards, templates, referências de capacidades e metadados. Classifique os artefatos do consumidor antes de movê-los. Preserve wrappers e testes próprios. Valide com o provedor alvo; registre a versão exata adotada e os resultados de integração.

## Recuperação e limites

Se nenhum alvo foi fornecido, resolva-o antes de alterar pins; nunca use latest. Apresente conflitos em vez de sobrescrevê-los. Reverta configurações e referências do provedor em conjunto e execute a suíte original restaurada.

## Segurança de repositórios públicos no GitHub

Use o [procedimento de segurança do provedor exato (inglês)](../../guides/public-repository-security.md). Prepare os arquivos com `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging` e execute `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` a partir desse provedor. Para consumidores instalados, acrescente `--project-root /absolute/consumer` com o lock exato correspondente. Revise as diferenças e preserve checks mais fortes e conflitos de ownership; somente operações administrativas autorizadas aplicam a configuração.

A prontidão pública exige uma verificação atual e completa em modo live com `public_ready: true`. Um esqueleto local, check de política, snapshot salvo ou código de saída 0 isolado é insuficiente. Permissões ou observações ausentes permanecem não verificadas. Auditoria não autoriza edições; manutenção verifica correções autorizadas e nunca escolhe `latest` silenciosamente. Uma aprovação de CODEOWNER elegível atende à regra básica, mesmo quando ambos receberam solicitação de review. Contribuidores externos usam forks e PRs; o CI de forks não recebe credenciais administrativas. Publicação de release e adoção continuam separadas.

## Referências

- [Skill (inglês)](../../../skills/project-maintenance/SKILL.md)
- [Changelog (inglês)](../../../CHANGELOG.md)
- [Migration (inglês)](../../../project-templates/README.md)

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
