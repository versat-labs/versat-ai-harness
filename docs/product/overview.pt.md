# Visão geral do produto

[English](overview.md) | [Português](overview.pt.md) | [Español](overview.es.md)

## Produto e responsabilidade

Versat AI Harness ajuda desenvolvedores, revisores e mantenedores a transformar intenções em mudanças revisadas e rastreáveis. A Versat o mantém; @elviszoz e @evertonspohrversat são contatos técnicos em CODEOWNERS. O público pretendido inclui desenvolvedores externos. O repositório continua privado durante a preparação da distribuição pública.

## Problema, trabalho e público

Um contribuidor precisa identificar o projeto correto, preparar seu primeiro plano SDD, compreender os gates humanos e fornecer evidências atuais. As instruções mantidas devem explicar esses passos sem gravações privadas ou vínculo com a organização. Acesso real à ferramenta/repositório é um pré-requisito separado; este documento não o concede.

A necessidade original de onboarding da equipe Versat está registrada na [Issue #22](https://github.com/versat-labs/versat-ai-harness/issues/22), histórico entregue cujo acesso acompanha a visibilidade do repositório. É procedência, não pré-requisito para usar este guia. Frequência e custo dessa necessidade ainda não foram medidos; valide-os com a equipe após o primeiro uso. Isso motiva a documentação atual sem alegar novas evidências de mercado.

## Solução e valor

Um Plugin versionado na raiz reúne Standards canônicos, ciclo SDD, cinco Skills, templates compostos e validação determinística. Apoia bootstrap, mudanças, manutenção, auditoria e revisão arquitetural. Decisões mais claras e verificações reproduzíveis são benefícios pretendidos; ganhos de produtividade e redução de defeitos precisam ser medidos.

## Origem e limites atuais

Os [ADRs](../decisions/README.md) registram decisões de pacote e processo. O código atual contém validação SDD v3 e execução explícita de testes ainda não lançadas, além da tag 0.3.0. VERSION/manifests agora declaram o candidato local de entrega 0.4.0; seu catálogo referencia v0.4.0 sem criar ou ativar essa release. Identidade do marketplace, cópias instaladas e pins dos consumidores permanecem iguais.

O [candidato Apache](../licensing/candidates/apache-2.0/APPROVAL.md) tem aprovação real do texto e sua licença e avisos estão aplicados localmente; integração na main e distribuição pública continuam pendentes. Termos de terceiros e licenças de material independente no projeto de destino permanecem separados. Confidencialidade, controles reais e verificação por usuários externos ainda limitam a prontidão pública. O Harness não fornece publicação automática, atualizações automáticas ou motor operacional de workflows. Validação estrutural não autentica aprovação humana nem comprova comportamento, CI remoto ou merge.

## Aplicabilidade e alternativas

O público pretendido se amplia além da equipe Versat sem alterar modelos de outros produtos. Não foram estabelecidos preço externo, comissão, dimensionamento de mercado ou retorno financeiro. Alternativas incluem instruções dispersas, checklists por projeto e assistência genérica de programação. O Harness reúne políticas por contexto e gates/evidências explícitos; é uma escolha de integração, não superioridade de mercado comprovada.

## Escala e responsabilidade

Versões exatas e templates compostos apoiam adoção em vários projetos. Revisão humana, traduções, compatibilidade do cliente e acesso continuam sendo restrições. Meça conclusão do onboarding, tempo até um primeiro plano revisado e dúvidas de suporte antes de afirmar valor. Proteja registros confidenciais; ensaio privado não comprova acesso anônimo. Diretórios de teste novos compartilham permissões e não são isolamento de segurança.

Instruções acessíveis e multilíngues podem reduzir barreiras de participação. Uso de modelos e avaliações repetidas consomem recursos; meça seu impacto antes de afirmar ganhos ambientais.

## Verificações abertas e próximo passo

Instalação, atualização, recuperação e resultados operacionais públicos devem ser observados antes de divulgar essas capacidades para o candidato. Contexto ausente permanece não verificado. Use [quickstart](../user-docs/quickstart.pt.md), [preparação](../user-docs/guides/workspace-setup.pt.md) e [estado da preparação](../handoffs/harness-publication-readiness/README.md). Release público e adoção por cada consumidor exigem decisões explícitas separadas.
