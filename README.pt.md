# Versat AI Harness

[English](README.md) | [Português](README.pt.md) | [Español](README.es.md)

Fonte de verdade da Versat para desenvolvimento assistido por IA: um Plugin portátil com Standards, Spec Driven Development (SDD), Skills reutilizáveis, templates compostos e validação determinística.

Para quem desenvolve, revisa e mantém projetos, incluindo contribuidores externos. Mantido pela Versat. @elviszoz e @evertonspohrversat são os CODEOWNERS gerais e responsáveis pela triagem compartilhada; Elvis coordena. A main exige uma aprovação elegível de CODEOWNER que não abriu a PR e CI aprovada. O teste interno de aprovação, descarte e nova aprovação foi concluído. O recebimento externo de relatos de segurança permanece não verificado.

## Comece aqui

[Início rápido: obter um primeiro plano SDD](docs/user-docs/quickstart.pt.md) · [Contexto do produto](docs/product/overview.pt.md)

- [Preparar o ambiente](docs/user-docs/guides/workspace-setup.pt.md)
- [Preparar o Claude](docs/user-docs/guides/claude-setup.pt.md)
- [SDD com Codex](docs/user-docs/guides/sdd-with-codex.pt.md)
- [Entrega pelo GitHub](docs/user-docs/guides/github-delivery.pt.md)
- [Iniciar um projeto](docs/user-docs/guides/project-bootstrap.pt.md)
- [Manter um projeto existente](docs/user-docs/guides/project-maintenance.pt.md)
- [Auditar um projeto](docs/user-docs/guides/project-audit.pt.md)
- [Revisar a arquitetura](docs/user-docs/guides/architecture-review.pt.md)
- [Validação e avaliações](docs/user-docs/guides/validation-and-evaluations.pt.md)
- [Documentação eletrônica SIFEN](docs/user-docs/guides/sifen-electronic-documentation.pt.md)
- [Criar uma issue no GitHub](docs/user-docs/guides/issue-creation.pt.md)

- [Transição do marketplace: identidades nova e legada](docs/user-docs/guides/marketplace-transition.pt.md)

## Repositório público; 0.5.0 em preparação

O repositório está público e a licença Apache-2.0 e os avisos revisados estão integrados na main. A versão 0.4.0 foi lançada em 2026-11-24. A versão 0.5.0 adiciona suporte ao Claude; sua tag v0.5.0 é criada no commit de merge após a revisão. As aprovações de texto e evidências históricas mantêm seu escopo original.

A proteção da main e o teste interno de controles de PR foram verificados. Private Vulnerability Reporting está habilitado; comportamento de fork/CI externo, recebimento/confidencialidade de relatos e instalação/atualização/recuperação nativa do Plugin permanecem pendentes. A pausa de escritas terminou; o trabalho normal segue por PRs protegidas.

[Notas da candidata 0.4.0 e verificações pendentes (histórico)](docs/releases/0.4.0-candidate.pt.md)

[Licença](LICENSE) · [Contribuição](docs/user-docs/guides/contributing.pt.md) · [Reporte de segurança](docs/user-docs/guides/security-reporting.pt.md)

## Estado atual e adoção

VERSION e os três manifests declaram 0.5.0. O catálogo do Codex (`.agents/plugins/marketplace.json`) e o catálogo do Claude (`.claude-plugin/marketplace.json`) selecionam v0.5.0, disponível somente depois que essa tag exata for criada; a referência lançada mais recente é v0.4.0. Publicar uma release não altera pins de consumidores.

Instale no Claude Code:

```text
/plugin marketplace add versat-labs/versat-ai-harness
/plugin install versat-ai-harness@versat
```

Consulte [Preparar o Claude](docs/user-docs/guides/claude-setup.pt.md) para atualização, verificação e recuperação.

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
./scripts/validate/run.sh --quality-base origin/main
```

Um interpretador existente pode ser selecionado com PYTHON=/absolute/path/to/python. A entrada verifica pacote, registros SDD e regressões de validadores/execução. Não comprova aprovação humana, CI remoto, merge nem comportamento de outra aplicação. Exceções históricas de compatibilidade são explícitas.

## Contribuir e manter

Use $versat-sdd para mudanças relevantes. Leia as instruções, revise as três etapas de planejamento e autorize explicitamente a implementação após Tasks. Prepare documentação viva e arquivo documental no mesmo PR de entrega. Revisão do PR, verificações finais e merge são checkpoints distintos.

[SDD (inglês)](sdd/README.md) · [Instruções do repositório (inglês)](AGENTS.md) · [ADRs (inglês)](docs/decisions/README.md) · [Versat Labs CONTRIBUTING (English)](https://github.com/versat-labs/.github/blob/main/CONTRIBUTING.md)
