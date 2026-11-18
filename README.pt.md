# Versat AI Harness

[English](README.md) | [Português](README.pt.md) | [Español](README.es.md)

Fonte de verdade da Versat para desenvolvimento assistido por IA: um Plugin portátil com Standards, Spec Driven Development (SDD), Skills reutilizáveis, templates compostos e validação determinística.

Para quem desenvolve, revisa e mantém projetos, incluindo contribuidores externos quando acesso e termos aplicáveis estiverem disponíveis. Mantido pela Versat; os contatos de revisão dos componentes governados são @elviszoz e @evertonspohrversat em .github/CODEOWNERS.

## Comece aqui

[Início rápido: obter um primeiro plano SDD](docs/user-docs/quickstart.pt.md) · [Contexto do produto](docs/product/overview.pt.md)

- [Preparar o ambiente](docs/user-docs/guides/workspace-setup.pt.md)
- [SDD com Codex](docs/user-docs/guides/sdd-with-codex.pt.md)
- [Entrega pelo GitHub](docs/user-docs/guides/github-delivery.pt.md)
- [Iniciar um projeto](docs/user-docs/guides/project-bootstrap.pt.md)
- [Manter um projeto existente](docs/user-docs/guides/project-maintenance.pt.md)
- [Auditar um projeto](docs/user-docs/guides/project-audit.pt.md)
- [Revisar a arquitetura](docs/user-docs/guides/architecture-review.pt.md)
- [Validação e avaliações](docs/user-docs/guides/validation-and-evaluations.pt.md)
- [Documentação eletrônica SIFEN](docs/user-docs/guides/sifen-electronic-documentation.pt.md)

## Preparação da publicação em andamento

A direção pública Apache-2.0 foi aprovada. O [candidato concreto](docs/licensing/candidates/apache-2.0/APPROVAL.md) tem aprovação do texto e não foi adotado. O repositório continua privado; 0.4.0 é um candidato futuro, não uma versão disponível. Veja [licenciamento](docs/user-docs/guides/licensing.pt.md), [contribuição](docs/user-docs/guides/contributing.pt.md), [reporte de segurança](docs/user-docs/guides/security-reporting.pt.md) e o [estado da preparação](docs/handoffs/harness-publication-readiness/README.md).

## Estado atual e adoção

VERSION declara 0.3.0. O marketplace seleciona a tag exata v0.3.0; verifique a tag e seu conteúdo antes da distribuição. Execução de consumidores e avaliações supervisionadas da fonte atual são explicitamente não lançadas. Mudar a fonte ou fazer merge não atualiza Plugins instalados nem pins de consumidores. Adote outra release exata por uma mudança revisada.

Administradores gerenciam importação do marketplace e política de instalação. Use este repositório como fonte, autentique com acesso de leitura, revise a release exata importada e confirme disponibilidade aos membros. Siga a interface atual de administração; a política do marketplace é AVAILABLE e não comprova instalação automática. Os membros podem usar [a preparação do ambiente](docs/user-docs/guides/workspace-setup.pt.md).

## Estrutura do repositório e dos consumidores

A raiz do repositório é o pacote Plugin. Políticas ficam em standards/; capacidades em skills/; processo em sdd/; aplicação mecânica em validators/ e CI; composição em project-templates/; contratos em schemas/; orientações de papéis em agents/; conhecimento não normativo em resources/. Manifests e marketplace selecionam recursos da mesma versão.

Projetos consumidores de agentes usam .agents/skills/, .codex/agents/ e workflows/. Um workflow precisa de executor explícito; agents/*.md na raiz não é registro nativo do Codex. Consulte [a arquitetura (inglês)](docs/architecture/overview.md) · [contrato de artefatos (inglês)](standards/core/agent-artifacts.md).

## Validação local

Use Python 3.11+ em ambiente virtual a partir da raiz deste repositório:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-validation.txt
./scripts/validate/run.sh
```

Um interpretador existente pode ser selecionado com PYTHON=/absolute/path/to/python. A entrada verifica pacote, registros SDD e regressões de validadores/execução. Não comprova aprovação humana, CI remoto, merge nem comportamento de outra aplicação. Exceções históricas de compatibilidade são explícitas.

## Contribuir e manter

Use $versat-sdd para mudanças relevantes. Leia as instruções, revise as três etapas de planejamento e autorize explicitamente a implementação após Tasks. Prepare documentação viva e arquivo documental no mesmo PR de entrega. Revisão do PR, verificações finais e merge são checkpoints distintos.

[SDD (inglês)](sdd/README.md) · [Instruções do repositório (inglês)](AGENTS.md) · [ADRs (inglês)](docs/decisions/README.md) · [Versat Labs CONTRIBUTING (English)](https://github.com/versat-labs/.github/blob/main/CONTRIBUTING.md)
