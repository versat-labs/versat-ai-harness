# Iniciar um projeto

[English](project-bootstrap.md) | [Português](project-bootstrap.pt.md) | [Español](project-bootstrap.es.md)

Use bootstrap para um projeto novo ou vazio. Informe propósito, responsável, perfil, domínio, criticidade, tecnologias e provedor exato do Harness. Repositórios existentes com conteúdo usam manutenção.

## Experimente

Pedido ilustrativo; substitua o ID ou forneça os dados reais do projeto:

```text
Use $project-bootstrap neste repositório vazio. Reaproveite o briefing do produto, pergunte sobre a identidade ausente e apresente uma estrutura e contexto de produto para revisão. Não crie repositórios remotos nem PRs.
```

## Resultado esperado

Espere uma estrutura composta de base/perfil, specs/product/overview.md com lacunas de evidência, .versat/project.yaml, .versat/standards.lock exato e uma mudança SDD project-bootstrap. O índice do provedor resolve Standards; usuários não escolhem um subconjunto das políticas obrigatórias. Revise hipóteses do produto antes de tratá-las como requisitos.

## Recuperação e limites

Uma estrutura vazia não comprova uma aplicação utilizável. Registre verificações de runtime indisponíveis e evite guias vazios ou passos executáveis fictícios. Conteúdo existente conflitante exige parar e classificar o repositório antes de compor templates.

## Segurança de repositórios públicos no GitHub

Use o [procedimento de segurança do provedor exato (inglês)](../../guides/public-repository-security.md). Prepare os arquivos com `python scripts/bootstrap/public_security.py --output /tmp/public-security-staging` e execute `python validators/security/validate.py --repository owner/repository --live --output /tmp/public-security-report.json` a partir desse provedor. Para consumidores instalados, acrescente `--project-root /absolute/consumer` com o lock exato correspondente. Revise as diferenças e preserve checks mais fortes e conflitos de ownership; somente operações administrativas autorizadas aplicam a configuração.

A prontidão pública exige uma verificação atual e completa em modo live com `public_ready: true`. Um esqueleto local, check de política, snapshot salvo ou código de saída 0 isolado é insuficiente. Permissões ou observações ausentes permanecem não verificadas. Auditoria não autoriza edições; manutenção verifica correções autorizadas e nunca escolhe `latest` silenciosamente. Uma aprovação de CODEOWNER elegível atende à regra básica, mesmo quando ambos receberam solicitação de review. Contribuidores externos usam forks e PRs; o CI de forks não recebe credenciais administrativas. Publicação de release e adoção continuam separadas.

## Referências

- [Skill (inglês)](../../../skills/project-bootstrap/SKILL.md)
- [Templates (inglês)](../../../project-templates/README.md)
- [Project schema (inglês)](../../../schemas/project.schema.yaml)

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
