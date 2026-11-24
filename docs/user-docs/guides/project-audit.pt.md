# Auditar um projeto

[English](project-audit.md) | [Português](project-audit.pt.md) | [Español](project-audit.es.md)

Use uma auditoria para avaliar conformidade, prontidão ou divergências. Prepare instruções, .versat/project.yaml, .versat/standards.lock, especificações ativas e o provedor selecionado. Isso é mais amplo que uma revisão comum de código.

## Experimente

Pedido ilustrativo; substitua o ID ou forneça os dados reais do projeto:

```text
Use $project-audit para avaliar este repositório conforme o perfil declarado e os Standards resolvidos. Informe evidências, gravidade e opções de correção. Não altere arquivos.
```

## Resultado esperado

Espere achados que distingam conformidade verificada, não conformidade e verificação indisponível, com contratos afetados e próximos passos concretos. A validação determinística fornece evidência limitada; a revisão qualitativa também considera segurança, testes/evals, documentação, operações e perfil/criticidade.

## Recuperação e limites

Identidade ou contexto do provedor ausentes são lacunas explícitas, não evidência de conformidade. Pedir auditoria não autoriza correção. Use manutenção ou uma mudança SDD para tratar achados aprovados.

## Segurança de repositórios públicos no GitHub

Use o [procedimento de segurança do provedor exato (inglês)](../../guides/public-repository-security.md). Prepare os arquivos com `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging` e execute `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` a partir desse provedor. Para consumidores instalados, acrescente `--project-root /absolute/consumer` com o lock exato correspondente. Revise as diferenças e preserve checks mais fortes e conflitos de ownership; somente operações administrativas autorizadas aplicam a configuração.

A prontidão pública exige uma verificação atual e completa em modo live com `public_ready: true`. Um esqueleto local, check de política, snapshot salvo ou código de saída 0 isolado é insuficiente. Permissões ou observações ausentes permanecem não verificadas. Auditoria não autoriza edições; manutenção verifica correções autorizadas e nunca escolhe `latest` silenciosamente. Uma aprovação de CODEOWNER elegível atende à regra básica, mesmo quando ambos receberam solicitação de review. Contribuidores externos usam forks e PRs; o CI de forks não recebe credenciais administrativas. Publicação de release e adoção continuam separadas.

## Referências

- [Skill (inglês)](../../../skills/project-audit/SKILL.md)
- [Standards index (inglês)](../../../standards/index.yaml)
- [Validators (inglês)](../../../validators/README.md)

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
