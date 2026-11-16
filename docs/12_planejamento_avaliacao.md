# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** 16/11/2026  
**Status:** 🟩 concluída  
**Responsabilidade:** 1 solução por equipe

## Objetivo da atividade

Planejar a avaliação antes de executá-la, ligando perguntas de avaliação a métodos, participantes, tarefas, métricas, aspectos práticos, ética e forma de análise.

## O que está sendo avaliado

Em projetos cuja interface foi criada ou ampliada para a disciplina, o plano deve declarar explicitamente que a avaliação investiga **a qualidade da interação/protótipo**, não a validade científica ou o desempenho técnico do algoritmo/modelo do TCC.

Exemplos de perguntas:

- o DBA consegue localizar e comparar duas execuções?
- o analista entende o significado de um indicador?
- o administrador consegue alterar uma permissão sem risco de erro não percebido?
- o usuário compreende que o processamento está em andamento e consegue recuperar-se de uma falha?
- os filtros ajudam a localizar o histórico relevante?
- um relatório permite identificar a informação necessária para a decisão?

Se o protótipo utiliza dados ou resultados simulados, documente isso no plano.

A avaliação investiga **a qualidade da interação com o protótipo navegável do VetIA** (E11): se o tutor consegue relatar o caso, compreender a orientação e seus limites, encontrar atendimento, controlar o que compartilha e acompanhar a resposta da clínica. **Não** avalia a acurácia da classificação de urgência nem o desempenho do pipeline LLM/RAG, que pertencem à avaliação experimental do TCC. Se o modelo gerar uma classificação diferente da esperada para um caso fictício, isso é registrado como nota técnica para o TCC, não como problema de usabilidade.

**Real e simulado no protótipo:** a orientação automática (classificação, justificativa e perguntas complementares) é **gerada em tempo real** pelo pipeline do TCC, com "Gemini · nuvem" fixado em todas as sessões. Os casos Bob e Nina são **fictícios** e entregues em cartões. A conta `Ana (demo)` é acadêmica e compartilhada. O Hospital Veterinário Aurora e o Centro Vet Horizonte são unidades **fictícias**: o aceite e a mensagem da clínica são **simulados** por um integrante que opera `Plantão Aurora (demo)` com roteiro fixo. As clínicas do mapa são dados públicos reais, não recebem casos e não devem ser contatadas. Os limites técnicos do protótipo estão resumidos na [referência interna do TCC](referencias/tcc_documentacao_funcional.md).

## A. Método DECIDE

| Etapa | Aplicação no projeto |
|---|---|
| **D — Determine the goals** | (1) Verificar as metas MU01–MU04 da Entrega 8 com tutores, em casos fictícios; (2) encontrar problemas de interação e de comunicação nas telas D01–D42 antes de qualquer uso fora da disciplina; (3) obter evidência preliminar sobre as hipóteses H02, H11b, H12, H13, H14, H16 e H17, que dependem de observação de uso; (4) priorizar correções no protótipo, na MoLIC e nos signos. A preocupação central é a **falsa segurança** — o tutor concluir que "está tudo bem" ou que "o atendimento está garantido" —, ligada à meta de Nielsen de maior prioridade na E8, **baixa taxa de erro (35%)**, seguida de **facilidade de aprendizado (30%)**. **Limites revisitados para esta amostra e versão**, como a E8 previa: os limites de MU01 (80%), MU02 (3 min), MU03 (4/5) e MU04 (100%) são mantidos, porque não há linha de base que justifique outros valores e 3 participantes não permitem recalibrá-los; o que muda é a leitura — com n = 3, MU01 só é atendida com 3/3, qualquer falha já indica problema a investigar, e os resultados são indícios, não estimativas. MU02 é medida descontando a espera do modelo, que não depende da interface. A **facilidade de memorização** não é verificada, pois exigiria uma segunda sessão após um intervalo. |
| **E — Explore the questions** | Os objetivos foram desdobrados em 15 perguntas operacionais (QA01–QA15, seção B). Exemplos: o tutor reconta a orientação de emergência e o próximo passo sem distorcer? Percebe que "Enviado" não significa vaga confirmada? Sabe quem escreveu a mensagem recebida, o VetIA ou a equipe da clínica? Entende que "Precisamos entender melhor" não é "está tudo bem"? |
| **C — Choose the evaluation paradigm and techniques** | **Inspeção:** avaliação heurística (H1–H10 de Nielsen) por 3 avaliadores (A01 Julian, A02 Vinícius, A03 João), individual, cobrindo todas as telas e estados, inclusive o painel da clínica (F4) e estados que não entram no teste. Para reduzir o viés de autoria, cada um começa pelos fluxos que não modelou. **Observação de uso:** teste em laboratório com 3 tutores, tarefas com cenário neutro, métricas de desempenho e perguntas de reconto após as tarefas críticas, complementado por **investigação** (questionários e entrevista pós-teste). A inspeção vem primeiro: problemas de severidade 4 ou que bloqueiem as tarefas são corrigidos antes do piloto e a versão é congelada. *Think aloud* concorrente não será usado, pois altera o tempo (MU02); a verbalização é coletada logo após cada tarefa. |
| **I — Identify the practical issues** | **Participantes:** 3 finais + 1 piloto, recrutados por conveniência (Vinícius coordena), com triagem prévia. **Ambiente:** sala reservada na FEI, ~50 min por sessão. **Equipamentos:** smartphone da equipe em **modo avião com Wi-Fi** (impede ligação real a clínicas do mapa), gravação de tela com áudio, notebook do operador da clínica, cartões impressos. **Preparação:** conta `Ana (demo)` e painel `Plantão Aurora (demo)` reiniciados e permissões do navegador limpas antes de cada sessão (Julian). **Piloto:** ~2 dias antes, validando cartões, tempos, gravação e estabilidade do modelo (cada caso enviado 5 vezes). **Cronograma proposto:** 16–18/11 preparação e recrutamento; 18–20/11 inspeção individual; 21/11 consolidação e congelamento; 23/11 piloto; 24–27/11 sessões; 28/11–01/12 análise. **Responsáveis:** rodízio moderador/observador/operador — U01: Julian/Vinícius/João; U02: Vinícius/João/Julian; U03: João/Julian/Vinícius. **Riscos técnicos:** resposta do modelo diferente da esperada (seguir com o que aparecer, adaptar o reconto e marcar a situação como "não apresentada"; se a não emergência não for estável no piloto, UT06 sai); provedor lento ou fora do ar (espera descontada do tempo; > 5 min, remarcar); servidor indisponível (remarcar, sem substituir por prints); gravação falha (planilha do observador vira fonte principal). |
| **D — Decide how to deal with ethical issues** | Exercício de disciplina orientado pelos princípios das Resoluções CNS 466/2012 e 510/2016 e pela LGPD, sem comitê de ética; se o material for usado como pesquisa no TCC, o orientador será consultado. Convite informa que o cenário envolve **emergência fictícia com animal**. Termo lido e assinado antes das tarefas; **gravação de tela e voz autorizada à parte**, sem câmera no rosto. Como o texto digitado vai ao Google Gemini, só são usados casos fictícios e o participante é orientado a não escrever dados reais. Pré-teste mínimo e sem nome; IDs U01–U03; termo guardado separado das planilhas. Gravações em pasta restrita à equipe, excluídas após a análise e até 31/12/2026. Interrupção livre, sem justificativa. *Debriefing* final: a orientação é automática, pode errar e não substitui o veterinário; nenhuma mensagem foi enviada a clínicas reais. |
| **E — Evaluate, interpret and present the data** | Definições fixadas antes da coleta (seção F). Quantitativos por tarefa apresentados como contagem "x/3" e mediana e comparados às metas; recontos classificados por dois integrantes; falas codificadas por categorias predefinidas; problemas priorizados pela escala 0–4; triangulação inspeção × observação. Resultados registrados nas E13/E14 e, na matriz de rastreabilidade, como **evidência preliminar (n = 3)**, não como confirmação das hipóteses. |

## B. Perguntas de avaliação

Métodos: **heurística** (E13); **observação** (E14); **reconto** = pergunta de compreensão logo após a tarefa; **questionário**; **entrevista** pós-teste. Os IDs `Sxx` são os signos da E9: o que será observado é se cada signo comunica o que o esquema define.

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | Tutores relatam o caso fictício e obtêm uma orientação sem ajuda? | observação (UT01) | sucesso, ajuda, erro | MU01: ≥ 80% sem ajuda (com n = 3, exige 3/3) |
| QA02 | O cadastro do animal atrasa ou bloqueia o início do relato? (H14) | observação (UT01) + entrevista | ordem das ações; falas sobre obrigatoriedade; signo animal (S02) | Nenhum participante acredita que precisa cadastrar antes de relatar |
| QA03 | O tutor compreende a orientação de possível emergência e o próximo passo? (H02, H11a) | reconto CMP-1 | compatível/incompatível; signos orientação (S09), sinais considerados (S30), justificativa (S10), limites (S11), próximo passo (S12) | MU04: 3/3 compatíveis |
| QA04 | O tutor encontra uma clínica aberta e o contato em tempo aceitável? (H10a, H18) | observação (UT02) | tempo de interação; sucesso; signos região (S13), clínica (S14), horário informado (S15), contato (S16) | MU02: mediana ≤ 3 min |
| QA05 | O tutor revisa e corrige o resumo antes do envio e controla o que é compartilhado? (H16) | observação (UT03) | informação nova no resumo (S17); autorizações marcadas (S19); destinatário (S18) | 3/3 com sucesso total; nenhuma autorização contra o cenário |
| QA06 | O tutor distingue caso enviado de atendimento confirmado? | reconto CMP-2 | compatível/incompatível; signo estado do encaminhamento (S20) | MU04: 3/3 compatíveis |
| QA07 | O tutor percebe a resposta da clínica e distingue mensagem automática de mensagem da equipe? (H17) | observação (UT04) + reconto CMP-3 | localiza aceite e mensagem; atribui a origem; signos resposta da clínica (S23), origem da informação (S21), canal com a clínica (S27) | 3/3 localizam e atribuem corretamente |
| QA08 | Diante de informação insuficiente, o tutor responde sem inventar dados e entende que isso não é "está tudo bem"? (H12, H13) | observação (UT05) + reconto CMP-4 | sucesso; "não sei" quando aplicável; reconto; signos pergunta e resposta complementar (S06, S07), orientação (S09) | MU04: 3/3 compatíveis |
| QA09 | Após orientação de não emergência, o tutor sabe o que observar e quando procurar ajuda? (H13) | observação (UT06) + reconto CMP-5 | compatível/incompatível; signos limites (S11) e próximo passo (S12) | MU04: 3/3 compatíveis |
| QA10 | O tutor confia excessivamente na orientação automática? (H11b) | questionário + entrevista | confiança 1–5 cruzada com os recontos | Ninguém declara que dispensaria o veterinário em emergência ou INCERTO |
| QA11 | Os tutores ficam satisfeitos com a facilidade das tarefas? | questionário pós-tarefa | escala 1–5 da E8 | MU03: mediana ≥ 4 em cada tarefa |
| QA12 | Quais violações das 10 heurísticas existem nas telas e estados, inclusive no painel da clínica? | heurística | violações por heurística; severidade 0–4 | Severidade 4 e bloqueadores corrigidos antes do teste |
| QA13 | A interface comunica o processamento da análise e evita reenvio por falta de feedback? | heurística (H1/H9) + observação | violações; toques repetidos ou reenvio; signo estado da análise (S08) | Nenhum reenvio involuntário observado |
| QA14 | Os requisitos básicos de acessibilidade da E8 são atendidos? | heurística + verificação WCAG | contraste do texto pequeno (1.4.3), foco e teclado no painel (2.1.1, 2.4.7), estado não só por cor (1.4.1) | Pendências da E11 medidas e registradas |
| QA15 | Os participantes prefeririam relatar por voz? (H09) — exploratória | entrevista | preferência declarada; uso espontâneo do áudio | Sem critério; resultado descritivo |

Fora do escopo: H04 exige estudo comparativo com outro canal; H03/H05 dependem de profissionais da clínica.

## C. Escopo e participantes

| Item | Planejamento |
|---|---|
| Perfis | Tutores adultos de cães ou gatos, próximos de P01 (preocupação aguda, uso no celular) e de P02 (menor familiaridade com aplicativos de saúde). P03 é coberta apenas pela inspeção heurística. |
| Critérios de inclusão/exclusão | **Inclusão:** ≥ 18 anos; tutor atual ou nos últimos 2 anos de cão ou gato; usa smartphone; na amostra, ao menos 1 participante com pouca familiaridade com aplicativos de saúde e ao menos 1 que já teve preocupação com o animal fora do horário comercial (idade não é usada como indicador de familiaridade). **Exclusão:** integrantes da equipe; quem já viu o protótipo, participou da simulação da E6 (inclui o orientador) ou do grupo de foco I03 da E7, que usa cenários parecidos; médicos-veterinários e estudantes de veterinária; quem prefira não participar por perda recente ou emergência veterinária recente. |
| Nº de participantes | 3 finais (U01–U03), igual ao nº de integrantes, + 1 piloto fora da amostra. 3 avaliadores na inspeção heurística. |
| Ambiente | Presencial, laboratório (sala reservada na FEI, São Bernardo do Campo); operador da clínica fora do campo de visão do participante. |
| Dispositivo | Smartphone Android da equipe, Chrome, modo avião com Wi-Fi, gravação de tela com áudio; notebook para o painel da clínica. Na inspeção: emulação 375 × 812 (tutor) e 1366 × 768 (painel). |
| Protótipo/versão | <https://vetia.chilecentral.cloudapp.azure.com/>, congelado no dia do piloto (registrar data, commit e provedor na E14). No teste: F1 (opcional), F2, F3, F5, F6 e não emergência. Só na inspeção: F4 e os estados que a E11 lista como não prototipados (carregamento e falha da análise, recusa, confirmação de cancelamento, lista vazia, sessão expirada). As alterações da E6 seção 5 ainda não publicadas não fazem parte da versão testada. |
| Teste piloto | Com 1 pessoa que atenda aos critérios e fique fora da amostra, conduzido pela equipe toda ~2 dias antes das sessões. Validar cartões, duração, tempos-limite, gravação, reinício da conta, sinal ao operador da clínica e estabilidade das respostas do modelo (cada caso enviado 5 vezes). |

## D. Lista de tarefas de avaliação

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite (se houver) |
|---|---|---|---|---|
| UT01 | São 22h. Você cuida do Bob (cachorro, 5 anos, 22 kg). Há uns 20 minutos ele está respirando muito rápido, a língua está meio roxa e ele não quer levantar. Use o aplicativo para contar o que você está vendo no Bob e saber o que fazer. | T01, O01/O08, F1/F2; MU01; H14 | Relato enviado com os sinais do cartão e orientação exibida, sem ajuda. Cadastrar o Bob não é exigido. | 6 min de interação (espera do modelo descontada) |
| CMP-1 | "Com suas palavras: o que o aplicativo disse sobre o Bob e o que você faria agora?" | T03, O03; MU04 (emergência) | Cita urgência/risco e procurar atendimento agora. | — |
| UT02 | Você decidiu levar o Bob para atendimento. Está no Centro Universitário FEI, em São Bernardo do Campo. Encontre um lugar que esteja funcionando agora e descubra como entraria em contato com ele. Pare quando souber como faria o contato. | T02, O04, F2 (D13–D17); MU02; H10a, H18 | Seleciona clínica indicada como aberta e localiza o telefone/ação de contato. | 5 min |
| UT03 | Você ligou para o Hospital Veterinário Aurora (unidade fictícia de teste) e pediram que mandasse as informações do Bob pelo aplicativo antes de sair. Você lembra que ele vomitou uma vez por volta das 17h. Faça o hospital receber o caso do Bob sabendo também do vômito. Você prefere que o hospital não veja tudo o que foi conversado no aplicativo, só o necessário. | T02, O05, F3 (D14, D18–D22); H16 | Estado "Enviado"; resumo inclui o vômito; conversa completa não autorizada. | 6 min |
| CMP-2 | "Neste momento, o Bob já tem atendimento garantido no hospital? Como você sabe?" | O10; MU04 (envio sem confirmação) | Responde que ainda falta a resposta/aceite da clínica. | — |
| UT04 | Alguns minutos se passaram. Veja se o hospital respondeu e, se ele puder receber o Bob, avise que você já está saindo. *(Antes, o operador aceita o caso e envia a mensagem do roteiro.)* | T02, O10, F5 (D31–D35); H17 | Localiza o encaminhamento, identifica aceite e mensagem e comunica a saída. | 4 min |
| CMP-3 | "Quem escreveu a última mensagem que você leu: o aplicativo ou alguém do hospital? Como percebeu?" | H17 | Atribui à equipe do hospital e cita o sinal usado. | — |
| UT05 | Você também cuida da Nina, gata de 8 anos. Há uns dois dias ela está comendo menos e mais quieta; você não sabe direito quando começou. Use o aplicativo para saber o que fazer. Se perguntarem algo, use só o que sabe: hoje comeu metade do normal; não vomitou; não sabe se tem bebido água. | T03, O02/O03, F6 (D36–D42); H12, H13 | Envia o relato, responde à pergunta complementar (dizendo que não sabe o que não sabe) e chega à orientação final. | 8 min de interação |
| CMP-4 | "Com suas palavras: o que o aplicativo concluiu sobre a Nina e o que você faria agora?" | MU04 (INCERTO) | Falta informação; não significa que está tudo bem; procurar/observar e buscar atendimento em piora. | — |
| UT06 | Outro dia: hoje de manhã a Nina espirrou duas ou três vezes. Está comendo, brincando e se comportando como sempre. Use o aplicativo para saber se precisa fazer alguma coisa. | T03, O03; H13 | Envia o relato e chega à orientação. | 4 min de interação |
| CMP-5 | "Com suas palavras: o que você faria com a Nina a partir de agora?" | MU04 (não emergência) | Acompanhar e citar ao menos um sinal que levaria a procurar atendimento. Incompatível: "não precisa fazer nada". | — |

> Uma boa instrução descreve o objetivo do participante sem dizer **onde clicar** ou usar o rótulo exato do controle que está sendo testado.

## E. Instrumentos

- [Modelo de termo de consentimento](../instrumentos/termo_consentimento_modelo.md) — versão adaptada: [termo do teste VetIA](../instrumentos/teste_vetia_termo_consentimento.md)
- [Roteiro de teste](../instrumentos/roteiro_teste_usabilidade.md) — versão adaptada: [roteiro do moderador e do operador da clínica](../instrumentos/teste_vetia_roteiro_moderador.md), com [cartões de tarefa do participante](../instrumentos/teste_vetia_cartoes_participante.md)
- [Planilha de observação](../instrumentos/planilha_observacao_modelo.md) — versão adaptada: [planilha do teste VetIA](../instrumentos/teste_vetia_planilha_observacao.md)
- [Formulário de avaliação heurística](../instrumentos/formulario_heuristica_modelo.md) — usado sem alteração por A01–A03
- [Questionários de triagem, pré-teste, pós-tarefa e pós-teste](../instrumentos/teste_vetia_questionarios.md)

## F. Plano de análise

Defina antes dos testes:

- **sucesso total / parcial / falha:** *total* = critério atingido no tempo-limite, sem ajuda de nível 2 ou 3; *parcial* = critério atingido com uma ajuda de nível 2, ou faltando um elemento secundário (ex.: envia sem incluir o vômito; acha o contato sem conferir se está aberta); *falha* = critério não atingido no tempo-limite, abandono, ajuda de nível 3 ou mais de uma ajuda de nível 2.
- **o que conta como erro, dúvida, ajuda e abandono:** *erro* = ação que afasta do objetivo e precisa ser desfeita, ou que produz estado indesejado (abrir tela não relacionada e voltar, enviar sem a correção pedida, marcar autorização contra o cenário), classificado como navegação, entrada, interpretação ou controle de compartilhamento; *dúvida* = pausa > 10 s sem interação com hesitação verbal ou gestual (registrada como comportamento, não como erro); *ajuda* = nível 1 esclarece o cenário (não conta), nível 2 indica uma região ou conceito da interface, nível 3 indica o controle; *abandono* = participante declara que desistiria ou pede para passar à próxima tarefa. Toques repetidos ou novo envio durante o processamento são registrados como *reenvio involuntário* (QA13).
- **como tempo será medido:** pela gravação de tela, com cronômetro de apoio do observador; início quando o participante termina de ler o cartão e toca na tela, fim quando o critério é atingido ou ele declara ter terminado. *Tempo de interação* = tempo total − espera do processamento do modelo, registrada à parte. MU02 segue a E8: da abertura da busca até localizar o contato; mediana das conclusões, com falhas informadas separadamente.
- **escala de satisfação pós-tarefa:** a da E8 — "Quão satisfeito ficou com a facilidade para realizar esta tarefa?", de 1 (muito insatisfeito) a 5 (muito satisfeito), seguida de "O que tornou isso fácil ou difícil?". No pós-teste, confiança na orientação para decidir sem veterinário (1–5), analisada junto com os recontos: confiança alta + reconto incompatível indica falsa segurança.
- **como observações/falas serão codificadas:** recontos transcritos e classificados por dois integrantes independentemente como compatível, parcialmente compatível ou incompatível (só *compatível* conta para MU04; situação não exibida pelo modelo sai do denominador). Falas recebem códigos predefinidos — URG urgência, LIM limites da orientação, CNF confiança, EST estado do envio, ORI origem da mensagem, CTR controle do compartilhamento, NAV navegação, LNG linguagem, ESP espera, CAD cadastro, EMO reação emocional —, com novos códigos registrados quando surgirem. A primeira sessão é codificada pelos três juntos; as demais, pelo moderador e revisadas por outro integrante.
- **como problemas serão priorizados:** escala de severidade 0–4, a mesma da E13, considerando frequência (1/3, 2/3, 3/3), impacto e persistência. Qualquer interpretação de falsa segurança ("está tudo bem", "a vaga está garantida", "não preciso de veterinário") recebe severidade 4, mesmo com 1 participante. Problema encontrado na heurística e no teste sobe um nível de prioridade.
- **como comparar resultados às metas de usabilidade:** MU01 = sucessos totais em UT01 / 3 (atendida com 3/3); MU02 = mediana do tempo em UT02 ≤ 3:00; MU03 = mediana ≥ 4 em cada tarefa; MU04 = compatíveis / apresentados em cada situação (emergência, envio sem confirmação, INCERTO, não emergência), atendida com 100%. Resultados apresentados como contagem "x/3" na E14, com tabela por participante, consolidação por tarefa, gráfico de sucesso por tarefa e tabela MU01–MU04.

## Checklist

- [x] As seis etapas DECIDE foram contextualizadas, não apenas expandidas por sigla.
- [x] Perguntas de avaliação têm método e evidência correspondentes.
- [x] O plano distingue avaliação de IHC de avaliação técnica/científica do TCC.
- [x] Dados ou processamentos simulados no protótipo estão declarados.
- [x] Tarefas vêm de objetivos/cenários relevantes.
- [x] Critérios de sucesso foram definidos antes da coleta.
- [x] Questões práticas e éticas estão resolvidas.
- [x] Instrumentos estão prontos antes da Entrega 13/14.
- [x] Plano diz como dados serão analisados e apresentados.
