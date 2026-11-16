# Entrega 8 — Ciclo de vida e engenharia de usabilidade

**Data:** 21/10/2026 (revisada em 16/11/2026 após feedback do professor)  
**Status:** 🟩 concluída  
**Responsabilidade:** 1 solução por equipe

## Objetivo da atividade

Transformar o conhecimento acumulado sobre usuários, tarefas, plataforma e contexto em princípios e **metas de usabilidade verificáveis**, mantendo o caráter iterativo do projeto.

## Delimitação do sistema interativo

Antes das características da plataforma, separe:

| Camada | O que pertence ao projeto | O que será avaliado em IHC |
|---|---|---|
| contribuição técnica do TCC | Pré-triagem com LLM/RAG, base veterinária, API e classificação de relatos. | desempenho técnico não é substituído pelo teste de IHC |
| camada de interação da disciplina | Cadastro do tutor/pet, chat, orientação, mapa e continuidade com a clínica. | compreensão, eficácia, eficiência, satisfação, erros, acessibilidade etc. |
| integrações/dados simulados | Na E6, telas em papel e casos, respostas e clínicas fictícios; na aplicação, serviços de IA/mapas e unidades acadêmicas identificadas. | A simulação avalia a interação; envio simulado não confirma atendimento real nem valida a classificação clínica. |

Em um protótipo de disciplina, é aceitável simular processamento ou resultados quando a implementação técnica não estiver integrada, desde que isso seja declarado e a simulação seja suficiente para avaliar a interação.

## 1. Características da plataforma

| Característica | Descrição | Consequência para IHC |
|---|---|---|
| Software | Aplicação web React integrada ao backend do TCC. | Manter navegação e linguagem consistentes entre cadastro, chat e atendimento. |
| Hardware/dispositivos | Navegador em celular ou computador; microfone opcional para voz. | Adaptar o conteúdo à tela e permitir relato por texto sem microfone. |
| Capacidades | Cadastro de pets, chat por texto/voz, histórico, mapa, encaminhamento e painel da clínica, conforme documentação do TCC. | Permitir revisar informações e distinguir mensagem automática de resposta profissional. |
| Restrições | Pré-triagem acadêmica; dados de horário e proximidade não comprovam capacidade de atendimento. | Explicar limites, tratar informação insuficiente e orientar confirmação com a clínica. |
| Conectividade/latência | IA e mapas dependem de serviços e conexão; podem ocorrer falhas ou indisponibilidade. | Mostrar espera e erro, preservar o relato e oferecer retentativa ou busca manual de região. |
| Segurança/privacidade | Contas de tutor/clínica, compartilhamento autorizado e contas acadêmicas compartilhadas. | Explicitar destino e conteúdo do envio; usar dados fictícios nas contas acadêmicas. |
| Volume de dados/histórico | Pets, conversas e encaminhamentos; volume de uso ainda não medido. | Identificar animal, data e estado; avaliar busca/filtros somente se a consulta ao histórico exigir. |
| Tempo de processamento | A análise pode demorar conforme provedor e infraestrutura; sem tempo fixo garantido. | Informar processamento e falha, evitando envio repetido por falta de feedback. |
| Papéis/permissões | Tutor gerencia seus casos; clínica acessa encaminhamentos autorizados para sua unidade; administração controla o vínculo institucional. | Diferenciar acessos e impedir ações ou exposição de casos de outra unidade. |

## 2. Princípios gerais do projeto

Inclua apenas normas, leis, padrões e princípios realmente relevantes, explicando **como** afetam o projeto. Não transforme esta seção em lista de links.

Os princípios estão organizados em dois grupos, como pede a atividade: **direcionados ao negócio** (leis, normas, ISO/ABNT e regras de negócio que o sistema precisa respeitar) e **direcionados à interface** (padrões de interação, guidelines e regras de outros sistemas que orientam como a interação é desenhada).

O **contexto de uso** — tutores adultos de cães/gatos, com diferentes familiaridades digitais, possivelmente sob pressão (hipótese das personas, Entregas 1/3) — não é um princípio: é uma **entrada** da análise, que já aparece nas características da plataforma (seção 1) e nas metas (seção 3). Por isso saiu desta tabela.

### 2.1 Princípios direcionados ao negócio

| Princípio/norma | Aplicabilidade ao contexto | Decisão/requisito decorrente | Fonte |
|---|---|---|---|
| LGPD | Cadastro, contato, localização e o relato do tutor podem identificar pessoas; o relato é enviado a um provedor de IA externo quando o Gemini é escolhido. | Solicitar apenas dados necessários, explicar uso e compartilhamento antes do envio ao provedor e à clínica, restringir acesso por papel; nas avaliações, usar casos fictícios. | [Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) |
| Limite legal e ético da orientação a distância | A telemedicina veterinária só pode ser exercida por médico-veterinário inscrito no conselho; mesmo a teleorientação feita por profissional proíbe definir diagnóstico ou conduta terapêutica, e o atendimento presencial é o padrão de referência. Uma pré-triagem automática, sem veterinário, fica ainda mais aquém disso. | A interface **não** apresenta diagnóstico, doença provável nem tratamento; comunica apenas possível urgência, motivos, limites e próximo passo; repete que a orientação automática pode errar e não substitui o veterinário; oferece o caminho para atendimento presencial em todos os desfechos. | Resolução CFMV nº 1.465/2022 (telemedicina veterinária), art. 4º e 5º |
| Usabilidade como norma | A definição de usabilidade adotada no projeto (eficácia, eficiência e satisfação em um contexto de uso especificado) vem da norma, e não de preferências da equipe. | As metas da seção 3 dizem sempre para quem, em que tarefa e em que contexto são medidas. | ABNT NBR ISO 9241-11 |
| Acessibilidade em aplicativos móveis | O uso previsto é principalmente pelo celular (H08); a norma brasileira trata de área de toque, nomes de botões, controle e interação em apps nativos, híbridos e web apps. | Áreas de toque adequadas, botões com nome compreensível, estados não dependentes só de cor; verificar na inspeção da E13. | ABNT NBR 17060:2022 |
| Regra de negócio — consentimento antes do compartilhamento | O TCC só envia resumo revisado, relato original e análise automática à clínica após consentimento; a conversa completa exige autorização separada. | Revisão e autorização explícitas antes do envio; duas autorizações distintas; o que vai para a clínica fica visível para o tutor. | [Referência interna do TCC](referencias/tcc_documentacao_funcional.md), seção 7 |
| Regra de negócio — envio não é vaga | Só unidades verificadas recebem casos; proximidade e horário vindos do mapa não comprovam capacidade de atendimento. | Distinguir envio, visualização, aceite e recusa; orientar confirmação com a clínica; nunca tratar envio como atendimento garantido. | [Referência interna do TCC](referencias/tcc_documentacao_funcional.md), seções 2, 6 e 7 |
| Regra de negócio — falha não é orientação | Falhas do provedor ou de cota não podem virar resultado clínico. | Estado de falha distinto de qualquer classificação, com relato preservado e nova tentativa. | [Referência interna do TCC](referencias/tcc_documentacao_funcional.md), seção 3 |

### 2.2 Princípios direcionados à interface

| Princípio/padrão | Aplicabilidade ao contexto | Decisão/requisito decorrente | Fonte |
|---|---|---|---|
| Acessibilidade web | Leitura, navegação e interpretação em diferentes dispositivos e por teclado (painel da clínica). | Usar texto além de cor, contraste legível, rótulos nos campos e foco visível na navegação por teclado. | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), critérios 1.4.1, 1.4.3, 2.1.1, 2.4.7 e 3.3.2 |
| Feedback e visibilidade do estado do sistema | Relato, processamento e encaminhamento possuem estados diferentes; a análise roda em segundo plano, sem tempo garantido. | Informar espera e falha, mostrar o estado da análise separado da urgência e o estado do encaminhamento com data e hora. | Heurística 1 de Nielsen; princípio "Visibilidade e reconhecimento" (Barbosa e Silva, 2010) |
| Projeto para erros e recuperação | Erros de relato, envio errado e interpretação insegura têm consequência real. | Permitir correção antes do envio, cancelar envio, explicar o que ocorreu e como seguir; nunca transformar falha em resultado. | Heurísticas 5 e 9 de Nielsen; "Projeto para erros" (Barbosa e Silva, 2010) |
| Equilíbrio entre controle e liberdade | O tutor precisa decidir o que compartilhar e poder sair do fluxo de perguntas para agir. | Saída clara para buscar atendimento em qualquer ponto; cadastro do animal opcional; autorizações desmarcadas por padrão. | Heurística 3 de Nielsen; "Equilíbrio entre controle e liberdade do usuário" (Barbosa e Silva, 2010) |
| Conteúdo relevante e expressão adequada | Tutor leigo, possivelmente sob estresse, lendo no celular. | Frases curtas, sem termos técnicos, rótulos sem ambiguidade; uma ação principal por tela. | Heurística 8 de Nielsen; "Conteúdo relevante e expressão adequada" (Barbosa e Silva, 2010) |
| Regras de outros sistemas — conversa | Tutores já relatam problemas por mensagens (E2). | Relato livre em formato de conversa, com origem de cada mensagem identificada e áudio como alternativa. | Análise de concorrência e análogos (E2: aplicativos de mensagem) |
| Regras de outros sistemas — mapa com lista | Padrão conhecido para encontrar estabelecimentos próximos (E2). | Mapa combinado com lista, com distância, horário, telefone e rota, e filtro de abertos. | Análise de concorrência e análogos (E2: serviços de mapas) |

## 3. Metas de usabilidade

Usabilidade deve ser discutida **no contexto de uso**. Metas quantitativas devem dizer o que será medido, em qual tarefa, com qual população e qual limite será considerado aceitável.

### 3.1 Metas qualitativas

| Meta | Para quem/tarefa | Evidência desejada | Justificativa |
|---|---|---|---|
| Compreender orientação e limites. | P01/P02; T03. | Recontar o resultado e o próximo passo, distinguindo não emergência de ausência de cuidado e INCERTO de não emergência. | Evitar falsa segurança; H02/H13. |
| Relatar e corrigir informações com controle. | P01/P02; T01. | Informar um caso fictício e corrigir o que foi entendido. | Preservar fidelidade e reduzir retrabalho. |
| Distinguir clínica localizada de atendimento confirmado. | P01; T02. | Explicar o estado do contato e o que falta confirmar. | Listagem, envio e aceitação não são equivalentes. |

### 3.2 Metas quantitativas

As metas abaixo são critérios iniciais de projeto, ainda não resultados medidos. Serão verificadas com tutores adultos de cães/gatos, em tarefas fictícias T01–T03, com instruções e dispositivo registrados. A amostra e a versão avaliadas serão definidas no planejamento da Entrega 12. Os limites de 80%, 3 minutos e 4/5 são referências iniciais de autonomia, esforço e satisfação, sem linha de base medida; poderão ser revistos com justificativa após as primeiras avaliações. A compreensão recebe critério mais rigoroso pelo risco de falsa segurança.

| ID | Dimensão | Métrica | Tarefa/escopo | Meta | Como medir | Justificativa |
|---|---|---|---|---|---|---|
| MU01 | eficácia | taxa de conclusão sem ajuda | T01 | ≥ 80% | Observar se registra, confere e envia o relato fictício; dividir conclusões sem ajuda pelo total de participantes da tarefa. | O fluxo central deve ser executável com autonomia. |
| MU02 | eficiência | tempo mediano | T02 | ≤ 3 minutos de interação | Cronometrar da abertura da busca até selecionar uma clínica e localizar o contato, sem ajuda; pausar durante espera de serviço ou troca de telas pelo mediador. Calcular a mediana das conclusões e informar também as falhas. | Limitar esforço para encontrar o próximo passo; não medir deslocamento nem tempo de resposta da clínica. |
| MU03 | satisfação | escala pós-tarefa | T01–T03 | mediana ≥ 4 em escala de 1 a 5 | Após cada tarefa: “Quão satisfeito ficou com a facilidade para realizar esta tarefa?”, de 1 (muito insatisfeito) a 5 (muito satisfeito); calcular a mediana por tarefa. | Registrar a percepção de facilidade junto do desempenho observado. |
| MU04 | compreensão | proporção de interpretações compatíveis | T03 e estado final de T02 | 100% dos participantes em cada situação apresentada | Pedir reconto de mensagens fictícias de não emergência, INCERTO e envio sem confirmação. Contar quem distingue necessidade de acompanhamento, falta de informação e ausência de aceite da clínica; registrar cada situação separadamente. | Interpretações de falsa segurança ou atendimento garantido exigem revisão. |

### 3.3 Priorização das metas (se exigida na disciplina)

Se o professor solicitar porcentagens que somem 100%, trate-as como **peso de prioridade**, não como métrica de usabilidade.

A priorização é feita sobre as **cinco metas de usabilidade de Nielsen**. As métricas MU01–MU04 da seção 3.2 continuam valendo como estão: a última coluna só indica qual métrica do projeto ajuda a verificar cada meta de Nielsen. Eficácia e compreensão são métricas próprias do projeto, não metas de Nielsen.

| Meta de Nielsen | Peso de prioridade | Justificativa no contexto do VetIA | Como será verificada (seção 3.2 e E12–E14) |
|---|---:|---|---|
| Baixa taxa de erro | 35% | Os erros mais graves deste sistema não são cliques errados, mas interpretações: tomar não emergência ou INCERTO por "está tudo bem", ou envio por vaga garantida (H02/H13). Também pesam o envio do caso sem a correção pretendida e o compartilhamento além do autorizado. É a meta ligada ao risco de falsa segurança. | MU04 (interpretações compatíveis) e contagem de erros por tarefa na E14. |
| Facilidade de aprendizado | 30% | O tutor costuma usar o sistema pela primeira vez justamente no momento da preocupação, sem tempo para aprender. A primeira utilização precisa dar certo sem ajuda. | MU01 (conclusão sem ajuda no primeiro uso) e ajudas registradas na E14. |
| Eficiência | 15% | Em possível emergência, cada minuto conta para encontrar atendimento, mas a eficiência não pode vir à custa da revisão do que é compartilhado. | MU02 (tempo para localizar uma clínica e o contato). |
| Facilidade de memorização | 10% | O uso é esporádico: o tutor pode voltar meses depois e não lembrar do fluxo. Peso menor porque, para uso raro, uma interface fácil de aprender cobre boa parte da necessidade. | Não medida nas E12–E14, que têm uma sessão por participante; seria preciso uma segunda sessão após um intervalo. Registrada como limitação. |
| Satisfação do usuário | 10% | Importa para o tutor voltar a usar e confiar no caminho, mas satisfação alta não compensa interpretação insegura. | MU03 (escala pós-tarefa). |
| **Total** | **100%** | | |

## 4. Como o ciclo será iterado

Explique que artefatos serão revisitados após protótipos e avaliações.

O projeto segue o **Ciclo de Vida de Engenharia de Usabilidade** (Mayhew, 1999), apresentado no material da aula. O modelo tem três grandes momentos: **análise de requisitos**, que produz o conhecimento sobre usuários, tarefas e plataforma e termina em princípios e metas; **projeto, testes e desenvolvimento**, em três níveis — modelo conceitual, padrões de tela e projeto detalhado —, cada um com avaliação antes de passar ao seguinte; e **instalação**, com retorno dos usuários. A iteração acontece dentro de cada nível (projetar → avaliar → revisar até atingir as metas) e entre níveis, quando uma avaliação revela problema de uma fase anterior.

| Fase do ciclo | O que a fase pede | Onde está no projeto | Estado |
|---|---|---|---|
| **Análise de requisitos** — perfil do usuário | Características, conhecimentos e contexto dos usuários. | E1 (público, hipóteses), E3 (personas P01–P03, mapa de empatia), E7 (coleta planejada). | Proto-personas; coleta da E7 pendente de aplicação. |
| Análise de requisitos — análise contextual de tarefas | Como os usuários fazem hoje e o que precisam fazer. | E2 (alternativas e concorrentes), E4 (cenários de problema), E5 (HTA, GOMS, CTT de T01–T03). | Modelado; sem observação de campo. |
| Análise de requisitos — capacidades e restrições da plataforma | O que a tecnologia permite e limita. | Seção 1 desta entrega. | Concluído. |
| Análise de requisitos — princípios gerais de projeto | Normas, leis e guidelines aplicáveis. | Seção 2 desta entrega (negócio e interface). | Concluído. |
| Análise de requisitos — metas de usabilidade | Metas qualitativas e quantitativas e sua prioridade. | Seção 3 desta entrega (MU01–MU04 e prioridade das metas de Nielsen). | Concluído; limites revistos na E12. |
| Análise de requisitos — guia de estilo | Registro das decisões para manter consistência. | Esta entrega (princípios e metas) + regras do sistema visual da E11 + esquema de signos da E9. | Parcial: consolidado ao longo das entregas, não em documento único. |
| **Nível 1** — projeto do modelo conceitual (projeto essencial) | Organização da interação, sem detalhes de tela. | E9 (cenários de interação, mapa de objetivos, signos), E10 (MoLIC). | Concluído; revisado após feedback. |
| Nível 1 — protótipo e avaliação do modelo conceitual | Testar a lógica antes de investir em telas. | E6 (protótipo em papel e simulação com U01). | Uma simulação realizada; ajustes registrados. |
| **Nível 2** — padrões de projeto de tela | Componentes, cores, tipografia e comportamento padronizados. | E11, seção "Sistema visual e consistência". | Definido. |
| Nível 2 — protótipo e avaliação dos padrões | Verificar padrões com inspeção e usuários. | E11 (protótipo navegável) avaliado por inspeção heurística na E13. | Planejado na E12. |
| **Nível 3** — projeto detalhado da interface | Todas as telas e estados. | E11 (telas D01–D42). | Estados de erro ainda faltando (E11). |
| Nível 3 — avaliação iterativa | Testes com usuários contra as metas. | E12 (planejamento), E13 (inspeção), E14 (observação de usuários). | Planejado. |
| **Instalação** — retorno dos usuários | Coletar retorno do uso real. | Fora do escopo da disciplina; a incorporação ao TCC depende da equipe e do orientador. | Não se aplica nesta etapa. |

**Como a iteração acontece no projeto:** a coleta da E7 pode refinar o perfil do usuário e as tarefas (volta à análise de requisitos). A simulação da E6 já ajustou fluxos e mensagens no nível 1. Nas Entregas 12–14, as metas desta seção são verificadas; um problema de compreensão leva de volta ao modelo conceitual (E9/E10), um problema de padrão de tela leva ao nível 2 e um problema pontual de tela ao nível 3. As decisões e seus vínculos são registrados em [`RASTREABILIDADE.md`](../RASTREABILIDADE.md), onde MU01–MU04 já estão ligadas às tarefas, aos fluxos e às perguntas de avaliação.

A necessidade do painel da clínica permanece vinculada a H03/H05 e à investigação com profissionais; qualquer meta relacionada ao painel é condicional a esse resultado.

Base: [resumo interno da documentação funcional do TCC](referencias/tcc_documentacao_funcional.md); Entregas 1, 3, 5, 6 e 7; Barbosa e Silva (2010); Mayhew, D. J. *The Usability Engineering Lifecycle*. Morgan Kaufmann, 1999.

## Checklist

- [x] Capacidades e restrições têm impacto de IHC explicitado.
- [x] Está claro o limite entre contribuição técnica do TCC e camada interativa da disciplina.
- [x] Resultados/processamento simulados no protótipo foram explicitados.
- [x] Metas de usabilidade avaliam a interação, não substituem métricas técnicas do TCC.
- [x] Normas/princípios estão contextualizados, não apenas copiados.
- [x] Metas quantitativas são mensuráveis e associadas a tarefas/público.
- [x] Eficácia, eficiência e satisfação são consideradas quando pertinentes.
- [x] Metas poderão ser verificadas nas Entregas 12–14.

