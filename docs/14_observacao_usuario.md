# Entrega 14 — Avaliação de usabilidade por observação de usuários

**Data da execução:** 18/11/2026  
**Revisão após o feedback do professor:** 22/11/2026  
**Status:** 🟩 concluída  
**Responsabilidade:** solução consolidada pela equipe; um participante final por integrante, cada integrante moderando uma sessão.

## Objetivo da atividade

Observar tutores realizando tarefas realisticamente simuladas no protótipo do VetIA para identificar problemas de eficácia, eficiência, compreensão e satisfação que a inspeção da E13 não consegue prever. O teste avalia a **interação com o protótipo**, não a acurácia da classificação de urgência do TCC: quando o modelo responde diferente do esperado, isso é registrado como nota técnica para o TCC, não como problema de usabilidade ([E12](12_planejamento_avaliacao.md#o-que-está-sendo-avaliado)).

**O que mudou nesta revisão:** medianas de UT02, UT03 e UT05 recalculadas e propagadas para a conclusão e para a matriz; regra de contagem de ajudas explicitada para MU01; protocolo realmente executado descrito no Passo 6; uso de *think aloud* esclarecido; todos os instrumentos vinculados; registro de versão, piloto e ausência de gravação; AU01 reclassificado como risco não confirmado; AU04 com decisão concreta e severidade; critério de UT04 alinhado a AU06; comparação com HC07–HC09 completada; conclusão e limitações aprofundadas.

## A. Fluxograma do processo — equipe

![Fluxograma do processo como executado](../assets/14_testes/fluxograma_avaliacao.svg)

O fluxograma mostra o processo **como foi executado** em 18/11: a inspeção não encontrou problema de grau 4 nem bloqueador, por isso a versão não foi alterada antes do piloto; não houve gravação e o cronômetro do observador foi a fonte dos tempos. As caixas tracejadas são decisões previstas no plano (desistência do participante, servidor fora do ar, correção de bloqueador, gravação) que não precisaram ser acionadas nesta rodada. Fonte editável: [`fluxograma_avaliacao.dot`](../assets/14_testes/fluxograma_avaliacao.dot).

## B. Procedimento de preparação e execução — equipe

### Passo 1 — Objetivos e versão avaliada

**Versão avaliada:** [VetIA](https://vetia.chilecentral.cloudapp.azure.com/), versão publicada em 18/11/2026, provedor de análise fixado em **Gemini · nuvem** nas três sessões.  
**Commit do protótipo implantado:** não registrado. A versão é identificada pela URL e pela data (18/11/2026); nenhuma versão nova foi publicada entre as capturas de 04/11 e o teste (E13, seção 2).  
**Congelamento:** a versão foi considerada congelada no início do piloto, em 18/11, e não mudou entre o piloto e a última sessão.  
**Correções entre a inspeção e o teste:** nenhuma. O plano da E12 só exigia corrigir antes do piloto problemas de severidade 4 ou que bloqueassem as tarefas, e a E13 não registrou nenhum dos dois. Por isso o teste avaliou uma versão com problemas de grau 3 já conhecidos (HC02, HC03, HC04 e HC07). Isso foi útil para verificar se esses problemas apareciam com pessoas, mas significa que nenhuma correção da inspeção foi testada. A única diferença de apresentação registrada entre as capturas da E13 e as sessões é que o seletor de provedor ficou oculto durante o teste (ver HC06 na seção F).

**Metas de usabilidade relacionadas (E8):** MU01 (≥ 80% sem ajuda em UT01), MU02 (mediana ≤ 3 min em UT02), MU03 (mediana ≥ 4/5 por tarefa) e MU04 (100% de recontos compatíveis por situação crítica).

### Passo 2 — Participantes

| ID | Perfil | Critérios que justificam a participação | Integrante responsável |
|---|---|---|---|
| U01 | faixa 18–29, tutora de dois cães, usa aplicativos de serviços todos os dias | Faixa 18–29, alta familiaridade com apps, perfil próximo de P01 | Julian (moderador) |
| U02 | faixa 30–44, tutora de um gato, já precisou de atendimento fora do horário comercial | Faixa 30–44, familiaridade média, experiência de urgência noturna, perfil próximo de P01 | Vinícius (moderador) |
| U03 | faixa 45–59, tutora de uma cadela idosa, quase nunca usa apps de saúde | Faixa 45–59, baixa familiaridade, perfil próximo de P02 | João (moderador) |

**Triagem e perfil.** Os três responderam à triagem de recrutamento de [`teste_vetia_questionarios.md`](../instrumentos/teste_vetia_questionarios.md) (seção 1): ≥ 18 anos, tutor atual de cão ou gato, uso de smartphone, não veterinário nem estudante de veterinária, nunca viu o VetIA nem participou de atividades do projeto. Nenhum é integrante da equipe. Do pré-teste, só ficou registrado o que aparece no perfil acima (faixa etária, animal, familiaridade com apps e, para U02, experiência de urgência fora do horário comercial); as demais respostas não foram guardadas (ver Passo 3). O tipo de celular do participante não foi registrado porque as sessões usaram o smartphone Android da equipe, igual para todos.

**Recrutamento por conveniência:** os participantes são amigos e familiares dos integrantes. Isso facilitou a agenda, mas pode deixar as notas de satisfação mais generosas e é registrado como limitação na conclusão.

### Passo 3 — Consentimento e privacidade

- Termo de consentimento: [termo do teste](../instrumentos/teste_vetia_termo_consentimento.md), lido em voz alta e assinado antes das tarefas.
- Gravação de tela e áudio: **não houve gravação**, por decisão da equipe, para simplificar as sessões. O plano da E12 previa gravação e já definia o que fazer sem ela: a planilha do observador passa a ser a fonte principal. A decisão é registrada como desvio do plano e como limitação na seção G.
- Anonimização: IDs `U01`, `U02` e `U03`; o termo assinado não tem ligação com o código do participante.
- Armazenamento: os termos assinados ficam com a equipe até o fim do semestre (31/12/2026); as planilhas e questionários não foram guardados depois da transcrição.

**Quem mediu e como.** Em cada sessão o observador do rodízio da E12 (U01: Vinícius; U02: João; U03: Julian) cronometrou cada tarefa com o cronômetro de apoio previsto no roteiro, do toque inicial até o critério atingido ou a declaração de término, e anotou à parte a espera pela resposta do modelo, que foi descontada. Sem gravação, cada medida depende de uma única fonte:

| Medida | Fonte única nesta rodada | O que isso significa |
|---|---|---|
| Tempo de interação | cronômetro do observador, menos a espera anotada | Precisão de segundos é a leitura do cronômetro, sem conferência posterior; erro de alguns segundos no início ou no desconto da espera é possível. As medianas devem ser lidas com essa margem. |
| Hesitação (ex.: 14 s de U01) | cronômetro do observador | Indício, não medida conferida. |
| Falas citadas | anotação manual do observador durante a sessão | Podem ser aproximadas; não há transcrição de áudio. |
| Recontos CMP | resposta anotada pelo moderador na folha do questionário e classificada no dia por dois integrantes | Dependem da qualidade da anotação; como as folhas não foram guardadas, a classificação não pode ser reconferida. |
| Sucesso, erros e ajudas | planilha do observador, revisada pelo moderador logo após a sessão | Duas pessoas conferiram, mas sem possibilidade de rever a ação. |

**Dados brutos.** As planilhas de observação e os questionários preenchidos nas sessões **não foram guardados**. Os números e falas da seção C são a transcrição que a equipe fez no mesmo dia, a partir dessas anotações, e não podem ser conferidos por terceiros nem pela própria equipe. Isso é tratado como limitação na seção G.

### Passo 4 — Teste piloto

**Data:** 18/11/2026, antes da primeira sessão, no mesmo dia das sessões (o plano previa cerca de dois dias de intervalo).  
**Participante do piloto:** um integrante da equipe, fora da amostra final. O plano da E12 previa uma pessoa de fora que atendesse aos critérios; com a agenda concentrada em 18/11, a equipe usou um integrante só para validar roteiro, cartões, tempos e equipamento. Como ele já conhecia o protótipo, o piloto não serve para prever dificuldades de compreensão (ver seção G).  
**Intervalo entre o piloto e a primeira sessão:** o piloto foi feito logo antes da primeira sessão, no mesmo dia.  
**O que foi validado:** roteiro, duração, entendimento dos cartões e funcionamento do protótipo (orientação gerada e envio ao Hospital Aurora fictício).  
**Duração do piloto:** cerca de 30 min, menos que os ~50 min previstos no roteiro (a soma dos tempos-limite das tarefas é 33 min). Como o integrante já conhecia o protótipo, esse tempo não representa uma sessão com um participante novo. Nas sessões finais, a soma dos tempos de interação das seis tarefas foi de 12:23 (U01), 17:34 (U02) e 23:17 (U03), sem contar abertura, questionários, recontos e espera do modelo.  
**Mudanças após o piloto:** a abertura foi encurtada; a instrução de compartilhamento do cartão 3 ficou mais explícita (o texto exato usado depois do piloto não foi guardado; o arquivo de cartões mostra a versão anterior ao piloto); a planilha passou a registrar separadamente a espera pela resposta do modelo.  
**Desvio do plano:** a E12 previa inspeção (18–20/11), consolidação e congelamento (21/11), piloto (23/11) e sessões (24–27/11). Tudo foi executado em 18/11. Motivo: agenda dos participantes, que só tinham disponibilidade nesse dia. Consequências: o piloto não pôde medir a duração com folga para ajustes maiores, e nenhum problema da inspeção foi corrigido antes do teste (ver Passo 1).

### Passo 5 — Tarefas

Cartões entregues ao participante: [`teste_vetia_cartoes_participante.md`](../instrumentos/teste_vetia_cartoes_participante.md). A coluna de cenário resume cada cartão; o texto integral está no arquivo. Os critérios de sucesso são os da E12, definidos antes do teste.

| ID | Cenário/instrução apresentada | Critério de sucesso | Métricas | Ligação com modelo |
|---|---|---|---|---|
| UT01 | "São 22h. Bob, cão de 5 anos, 22 kg, respirando muito rápido há 20 min, língua meio roxa, não quer levantar. Use o aplicativo para contar o que está vendo e saber o que fazer." | Relato com os sinais e orientação de emergência exibida, sem ajuda de nível 2 ou 3 | sucesso, tempo, erros, ajudas, satisfação, CMP-1 | T01 · F1/F2 |
| UT02 | "Você está na FEI, em São Bernardo. Encontre um lugar funcionando agora e descubra como entraria em contato." | Unidade indicada como aberta selecionada e telefone ou ação de contato localizados | sucesso, tempo (MU02), erros, satisfação | T02 · F2 |
| UT03 | "A atendente do Hospital Aurora pediu as informações pelo aplicativo. O Bob vomitou às 17h. Faça o hospital receber o caso sabendo do vômito, sem ver tudo o que foi conversado." | Resumo corrigido com o vômito, status de envio exibido, conversa completa desmarcada | sucesso, tempo, erros de controle, satisfação, CMP-2 | T02 · F3 |
| UT04 | "Veja se o hospital respondeu e, se puder receber o Bob, avise que já está saindo." | Encaminhamento, aceite e mensagem localizados, com saída comunicada pelo botão "Estou a caminho" ou por mensagem | sucesso, tempo, erros, satisfação, CMP-3 | T02 · F5 |
| UT05 | "Nina, gata de 8 anos, comendo menos e mais quieta há dois dias; comeu metade do normal, não vomitou, não sabe se bebeu água. Use o aplicativo para saber o que fazer." | Envio, resposta apenas com dados disponíveis e chegada à orientação | sucesso, tempo, erros, satisfação, CMP-4 | T03 · F6 |
| UT06 | "Outro dia. Nina espirrou duas ou três vezes, mas come, brinca e se comporta como sempre. Use o aplicativo para saber se precisa fazer algo." | Relato enviado e orientação de não emergência lida | sucesso, tempo, erros, satisfação, CMP-5 | T03 |

**Sobre o critério de UT04.** O critério da E12 aceita o botão de estado ou uma mensagem, porque a tarefa mede se o tutor consegue avisar a clínica. Ele foi mantido como estava, para não reinterpretar o teste depois de ver o resultado. Por isso U03, que avisou pelo chat, teve sucesso total. O efeito colateral (o estado estruturado "A caminho" não é atualizado quando o aviso vai pelo chat) é registrado à parte em AU06. Numa próxima rodada, se o estado estruturado for o que importa, o critério deve exigir o botão.

### Passo 6 — Protocolo do moderador (como executado)

O roteiro completo, com as falas lidas, está em [`teste_vetia_roteiro_moderador.md`](../instrumentos/teste_vetia_roteiro_moderador.md). As três sessões seguiram esse roteiro; o resumo abaixo descreve o que foi feito e os desvios estão listados ao final.

1. **Antes do participante chegar (1 h antes):** o moderador conferiu o checklist do roteiro: celular em modo avião com Wi-Fi, permissões do site limpas, protótipo aberto na tela de entrada, conta `Ana (demo)` sem animais, conversas nem encaminhamentos, painel `Plantão Aurora (demo)` sem casos pendentes e provedor em "Gemini · nuvem". O operador da clínica ficou no notebook, fora do campo de visão.
2. **Recepção e abertura:** o moderador se apresentou, apresentou o observador e leu a abertura (versão encurtada após o piloto), que diz que **o aplicativo está sendo avaliado, não a pessoa**, que as situações são inventadas, que a correção clínica da orientação não está em avaliação e que a pessoa pode parar a qualquer momento sem explicar o motivo.
3. **Consentimento:** o termo foi entregue, lido em voz alta e assinado. Não houve gravação, por decisão da equipe (ver Passo 3).
4. **Pré-teste:** perguntas do bloco de pré-teste, aplicadas oralmente e anotadas sem nome.
5. **Instruções gerais:** leitura do texto da seção 4 do roteiro: um cartão por vez, fazer o que faria na vida real, pode reler o cartão, avisar quando terminar, o moderador fica em silêncio e não diz onde tocar, não escrever dados reais porque o texto vai para um serviço de IA.
6. **Cada tarefa:** o moderador entregou o cartão e esperou a leitura; o observador iniciou o cronômetro no primeiro toque. Durante a tarefa, o moderador não comentou nem respondeu sobre a interface. Ajudas seguiram a política do roteiro: **N1** (esclarecer o cenário, por exemplo quem é o Bob) era permitida e não conta como ajuda; **N2** ("Onde você imagina que isso estaria?") só depois de 2 min de travamento e de pedido do participante; **N3** (indicar o controle) só quando o tempo-limite estourava e a tarefa seguinte dependia desta, e então a tarefa conta como falha. Ao fim, o moderador fez o reconto CMP correspondente, a escala de satisfação 1–5 e a pergunta "O que tornou isso fácil ou difícil?". Em UT03, após o CMP-2, o moderador enviou o sinal ao operador, que aceitou o caso e enviou a mensagem fixa do roteiro antes de UT04.
7. **Pós-teste:** escala de confiança 1–5 e entrevista curta do bloco de pós-teste.
8. **Encerramento e debriefing:** leitura do texto final: as orientações são automáticas, podem errar e não substituem o veterinário; o Hospital Aurora não existe e nenhuma mensagem foi enviada a clínicas reais; os dados aparecem só como U01–U03.
9. **Logo após a sessão:** moderador e observador revisaram a planilha, anotaram as três observações mais marcantes, a classificação exibida pelo modelo em UT01, UT05 e UT06 e desvios do roteiro. A conta e o aparelho foram reiniciados para a sessão seguinte.

**Desvios do roteiro na execução:** abertura encurtada e instrução do cartão 3 mais explícita (ambos após o piloto); gravação não realizada, por decisão da equipe. Outros desvios eventuais não podem ser listados, porque as planilhas não foram guardadas.

**Think aloud.** Conforme decidido na E12, os participantes **não** foram instruídos a pensar em voz alta durante as tarefas, para não distorcer o tempo usado em MU02. A verbalização foi coletada **logo após cada tarefa**, pela pergunta "O que tornou isso fácil ou difícil?" e pelo reconto. As falas registradas durante as tarefas ("aberto até 23h, ó o telefone" de U01; a leitura em voz baixa de U03) foram **espontâneas** e anotadas como comportamento. Como falar em voz alta pode atrasar um pouco a interação, os tempos dessas tarefas podem estar levemente acima do que seriam em silêncio; isso entra nas limitações.

### Passo 7 — Instrumentos usados

| Instrumento | Arquivo | Uso |
|---|---|---|
| Termo de consentimento | [`teste_vetia_termo_consentimento.md`](../instrumentos/teste_vetia_termo_consentimento.md) | Antes das tarefas, duas vias |
| Triagem, pré-teste, pós-tarefa e pós-teste | [`teste_vetia_questionarios.md`](../instrumentos/teste_vetia_questionarios.md) | Recrutamento, início da sessão, após cada tarefa e no final |
| Cartões de tarefa | [`teste_vetia_cartoes_participante.md`](../instrumentos/teste_vetia_cartoes_participante.md) | Um cartão por tarefa |
| Roteiro do moderador e do operador | [`teste_vetia_roteiro_moderador.md`](../instrumentos/teste_vetia_roteiro_moderador.md) | Falas lidas, política de ajuda, roteiro do operador da clínica |
| Planilha de observação | [`teste_vetia_planilha_observacao.md`](../instrumentos/teste_vetia_planilha_observacao.md) | Uma por participante, preenchida pelo observador |

## C. Resultados — por participante

Ajudas: N1 = esclarecimento do cenário, que **não conta como ajuda** (E12, seção F); N2 = indicação de região ou conceito da interface; N3 = indicação do controle. Tempos = tempo de interação, com a espera do modelo descontada.

### U01 — faixa 18–29, alta familiaridade, perfil próximo de P01

| Tarefa | Grau de sucesso | Erros | Tipos de erro/dificuldade | Ajudas | Tempo | Satisfação | Evidência/observação |
|---|---|---:|---|---|---|---|---|
| UT01 | total | 1 | E (digitação: "respirano") | — | 01:52 | 5 | Corrigiu sozinha; hesitação de 14 s antes de tocar no resultado. CMP-1 compatível. |
| UT02 | total | 0 | — | — | 01:18 | 5 | Leu o horário em voz alta, espontaneamente: "aberto até 23h, ó o telefone" |
| UT03 | total | 0 | — | — | 03:11 | 4 | Incluiu o vômito no resumo; desmarcou a conversa completa. CMP-2 compatível. |
| UT04 | total | 0 | — | — | 01:34 | 5 | Usou o botão de estado "Estou a caminho". CMP-3 compatível. |
| UT05 | total | 0 | — | — | 03:02 | 4 | Respondeu "não sei" sobre a água sem hesitar. CMP-4 compatível. |
| UT06 | total | 0 | — | — | 01:26 | 5 | "É só espirro, então é acompanhar". CMP-5 compatível. |

**Link da gravação:** não houve gravação (Passo 3).  
**Resposta pós-teste:** confiança 4/5. Relatou dúvida entre as duas autorizações.

### U02 — faixa 30–44, familiaridade média, perfil próximo de P01

| Tarefa | Grau de sucesso | Erros | Tipos de erro/dificuldade | Ajudas | Tempo | Satisfação | Evidência/observação |
|---|---|---:|---|---|---|---|---|
| UT01 | total | 1 | E (digitação: horário trocado) | — | 02:24 | 4 | Corrigiu após reler o cartão. CMP-1 compatível. |
| UT02 | total | 0 | — | — | 02:05 | 4 | Conferiu o horário antes de abrir o cartão da unidade |
| UT03 | parcial | 1 | C (manteve a conversa completa marcada) | N2 | 04:36 | 3 | Incluiu o vômito no resumo só depois da ajuda N2 e manteve a conversa completa marcada: "Deixa marcada, vai que precisa". Classificada como parcial (ver nota na seção D). CMP-2 compatível. |
| UT04 | total | 0 | — | — | 01:12 | 5 | Localizou o aceite na lista de encaminhamentos, leu a mensagem e acionou "Estou a caminho". CMP-3 compatível. |
| UT05 | parcial | 1 | N (dificuldade para sair da conversa) | N2 | 05:19 | 3 | Respondeu "não sei" sobre a água, mas precisou de ajuda N2 para sair da conversa. CMP-4 parcialmente compatível. |
| UT06 | total | 0 | — | — | 01:58 | 4 | Leu a orientação em voz alta, espontaneamente, sem dificuldade. CMP-5 compatível. |

**Link da gravação:** não houve gravação (Passo 3).  
**Resposta pós-teste:** confiança 3/5. Relatou dúvida sobre onde corrigir o resumo e quais informações seriam enviadas.

### U03 — faixa 45–59, baixa familiaridade, perfil próximo de P02

| Tarefa | Grau de sucesso | Erros | Tipos de erro/dificuldade | Ajudas | Tempo | Satisfação | Evidência/observação |
|---|---|---:|---|---|---|---|---|
| UT01 | total | 0 | — | N1 (não conta) | 03:38 | 4 | Pediu confirmação do enunciado uma vez (esclarecimento do cenário). CMP-1 compatível. |
| UT02 | parcial | 1 | I (não conferiu o horário no cartão da unidade) | N2 | 03:47 | 4 | Escolheu a primeira unidade da lista |
| UT03 | falha | 1 | C (enviou com a conversa completa e sem o vômito) | N2 ×2, N3 no limite de 06:00 | 06:04 | 2 | Não reconheceu o resumo como área editável. CMP-2 compatível: "O caso foi enviado, mas o atendimento ainda não está confirmado. Preciso esperar o hospital aceitar ou responder." |
| UT04 | total | 0 | — | — | 02:48 | 4 | Localizou o aceite, reconheceu a mensagem da clínica e avisou pelo chat que estava saindo. Sucesso total pelo critério da E12; o estado estruturado "A caminho" não foi atualizado (ver AU06). CMP-3 compatível. |
| UT05 | total | 1 | E (apagou e reescreveu o relato duas vezes) | — | 04:41 | 4 | Respondeu "não sei" sobre a água. CMP-4 compatível. |
| UT06 | total | 0 | — | — | 02:19 | 4 | Leu a orientação devagar, em voz baixa. CMP-5 compatível. |

**Link da gravação:** não houve gravação (Passo 3).  
**Resposta pós-teste:** confiança 3/5. Relatou dificuldade com as duas autorizações e sugeriu simplificar o envio.

### Recontos: critério de compatibilidade

Cada reconto foi classificado no dia por dois integrantes, com o critério da E12 (seção D). Só "compatível" conta para MU04. As respostas literais não foram guardadas, com exceção da resposta de U03 ao CMP-2, transcrita na ficha; por isso a classificação não pode ser reconferida.

| Reconto | Critério de "compatível" (E12) | Resultado |
|---|---|---|
| CMP-1 (Bob, emergência) | Cita urgência ou risco e procurar atendimento agora | 3/3 compatíveis |
| CMP-2 (envio sem confirmação) | Diz que ainda falta a resposta ou o aceite da clínica | 3/3 compatíveis; U03: "O caso foi enviado, mas o atendimento ainda não está confirmado. Preciso esperar o hospital aceitar ou responder." |
| CMP-3 (origem da mensagem) | Atribui a mensagem à equipe do hospital e cita o sinal usado | 3/3 compatíveis |
| CMP-4 (Nina, INCERTO) | Falta informação; não significa que está tudo bem; observar e procurar atendimento em piora | 2/3 compatíveis; U02 parcialmente compatível |
| CMP-5 (não emergência) | Acompanhar e citar ao menos um sinal que levaria a procurar atendimento | 3/3 compatíveis. A fala de U01 durante UT06 ("É só espirro, então é acompanhar") não cita sinal de alerta. A ficha a registra como observação de UT06; sem a folha original, não é possível saber se foi a resposta ao reconto nem reconferir a classificação. |

## D. Consolidação por tarefa

**Como foram calculados.** *Taxa de sucesso* = contagem x/3. *Tempo típico* = **mediana** dos três tempos de interação (com três valores, o valor do meio), e não média; em UT03 a mediana inclui o tempo da falha, interrompida no limite. *Satisfação* = mediana das três notas. *Sem ajuda* = sem ajuda de nível 2 ou 3, porque a E12 (seção F) define que o nível 1 apenas esclarece o cenário e não conta como ajuda; essa regra foi fixada antes do teste e é aplicada igual em todas as tarefas.

**Caso de U02 em UT03.** A participante precisou de uma ajuda N2 **e** deixou um elemento do critério de fora (a conversa completa marcada). A E12 define parcial como "uma ajuda N2 ou um elemento secundário faltando" e falha como "critério não atingido no tempo-limite, abandono, ajuda N3 ou mais de uma ajuda N2", mas não prevê a combinação das duas condições. A equipe manteve **parcial** porque nenhuma condição de falha ocorreu: não houve abandono, ajuda N3 nem segunda ajuda N2, e o caso foi enviado dentro do tempo com o vômito incluído. Mesmo assim, o problema da conversa completa entra na contagem de erros (C) e sustenta o achado AU02. Numa próxima rodada, a regra deve dizer explicitamente o que fazer nessa combinação.

| Tarefa | Taxa de sucesso | Sem ajuda (N2/N3) | Tempo típico (mediana · mín–máx) | Erros recorrentes | Satisfação (mediana) | Meta atendida? | Problemas prioritários |
|---|---:|---:|---|---|---|---|---|
| UT01 | 3/3 totais (100%) | 3/3 | 02:24 · 01:52–03:38 | 2 E (digitação, corrigidos) | 4 | MU01 sim · MU03 sim | Nenhum crítico; relato digitado sob pressão gera erro de digitação |
| UT02 | 2 totais + 1 parcial (100% de conclusão) | 2/3 | 02:05 · 01:18–03:47 | 1 I (horário não conferido) | 4 | MU02 sim (02:05 ≤ 03:00) · MU03 sim | Horário da unidade passou despercebido em uma sessão (AU05) |
| UT03 | 1 total + 1 parcial + 1 falha (66,7% de conclusão) | 1/3 | 04:36 · 03:11–06:04 | 2 C (conversa completa mantida), 1 ausência de correção do resumo | 3 | MU03 não · CMP-2: 3/3 compatíveis | Hierarquia das duas autorizações (AU02); resumo não reconhecido como editável (AU03) |
| UT04 | 3/3 totais (100%) | 3/3 | 01:34 · 01:12–02:48 | Nenhum erro registrado | 5 | MU03 sim · CMP-3: 3/3 compatíveis | U03 avisou pelo chat; estado estruturado não atualizado (AU06) |
| UT05 | 2 totais + 1 parcial (100% de conclusão) | 2/3 | 04:41 · 03:02–05:19 | 1 dificuldade de navegação e 1 reescrita | 4 | MU03 sim · CMP-4: 2/3 compatíveis | Dificuldade para sair da conversa e dúvida sobre quanto detalhar (AU04) |
| UT06 | 3/3 totais (100%) | 3/3 | 01:58 · 01:26–02:19 | 0 | 4 | MU03 sim · CMP-5: 3/3 compatíveis | Nenhum |

### Metas MU01–MU04

| Meta | Critério (E8/E12) | Resultado verificado | Situação |
|---|---|---|---|
| MU01 | ≥ 80% sem ajuda em UT01; com n = 3, exige 3/3 | 3/3 sem ajuda de nível 2 ou 3. U03 recebeu um esclarecimento N1, que pela regra da E12 não conta como ajuda. | Atingida |
| MU02 | Mediana ≤ 3:00 em UT02 | Mediana 02:05 (01:18; 02:05; 03:47). Margem de 55 s; a sessão mais lenta (U03, 03:47) ficou acima do limite. | Atingida, com margem menor do que a informada na versão anterior (01:42, valor que não existe nas fichas) |
| MU03 | Mediana ≥ 4 em cada tarefa | 4, 4, **3**, 5, 4, 4 | Atingida em 5 de 6 tarefas; não atingida em UT03 |
| MU04 | 100% de recontos compatíveis em cada situação | CMP-1 3/3 · CMP-2 3/3 · CMP-3 3/3 · CMP-4 **2/3** · CMP-5 3/3 | Não atingida em CMP-4 (INCERTO). Pela regra da E12 para resultados ambíguos com n = 3, 2/3 é tratado como meta não atingida e problema a corrigir (AU04), com nova verificação depois da correção. |

## E. Achados e recomendações

| ID | Achado | Evidência (quant. + qual.) | Severidade e impacto | Recomendação | Artefatos a revisar |
|---|---|---|---|---|---|
| AU01 | **Risco não confirmado.** A inspeção apontou que o estado de espera após o envio perde destaque (HC04). | CMP-2: 3/3 compatíveis; U03 explicou com as próprias palavras que o atendimento ainda dependia do aceite. Nenhum participante interpretou "Enviado" como vaga. A pergunta usada ("atendimento garantido?") era indutiva, o que enfraquece essa evidência. | Sem severidade de uso nesta rodada (não observado). HC04 mantém o grau 3 da inspeção, porque o reconto valeu para um único cenário. | Manter "Enviado · aguardando resposta da clínica" junto ao selo até o aceite, como a E13 recomenda, e verificar de novo numa próxima rodada. | Signos S20, MoLIC M01.C14, protótipo D22 |
| AU02 | As duas autorizações têm peso visual equivalente e a opcional vem antes da obrigatória | 2/3 mantiveram a conversa completa marcada; U02: "deixa marcada, vai que precisa"; U01 desmarcou após ler as duas; U03 marcou as duas sem decidir | 3 — exposição de conteúdo além do pretendido, não reversível após a leitura pela clínica | Autorização obrigatória primeiro, conversa completa como opção explícita e desmarcada, com resumo do que será enviado | Signos S19, MoLIC M01.C13, protótipo D19–D21 |
| AU03 | O resumo do envio não é reconhecido como área editável | U03 não incluiu o vômito mesmo após duas ajudas N2; U02 voltou ao resumo só após N2; U01 editou sem ajuda | 3 — elemento principal de UT03 perdido | Marcar o resumo como editável ("toque para corrigir") e oferecer campo dedicado a informação nova | Protótipo D18, signo S17, MoLIC M01.C13 |
| AU04 | No estado de informação insuficiente, o participante não encontra como sair da conversa nem sabe quanto detalhar | U02 precisou de ajuda N2 para sair da conversa (UT05 parcial, CMP-4 parcial). U03 apagou e reescreveu o relato duas vezes por achá-lo curto. | 2 — 2/3 com dificuldade; não impede concluir, mas aumenta o esforço e coincide com o único reconto não compatível da rodada | (1) Na orientação final de informação insuficiente (D42), mostrar no próprio cartão duas ações como botões: "Ver clínicas" e "Nova conversa", em vez de depender do link do rodapé e do menu ☰. (2) Abaixo da pergunta complementar, mostrar "Responda só o que sabe; uma frase basta" junto do atalho "Não sei" (HC08). | Signos S06/S12, MoLIC M03.C01/C06, protótipo D38–D42 |
| AU05 | O horário de funcionamento no cartão da unidade é lido como informação secundária | U03 selecionou a primeira unidade sem ler o horário, resolvido só com N2; U01 e U02 leram em voz alta | 3 — seleção de unidade fechada em situação de urgência | Destacar o estado aberto/fechado como selo no topo do cartão e esmaecer unidades fechadas | Signo S15, MoLIC M01.C09, protótipo D15–D17 |
| AU06 | O botão de estado "Estou a caminho" compete com o campo de mensagem aberto | U03 concluiu UT04 pelo chat (sucesso total pelo critério); U01 e U02 usaram o botão | 2 — o aviso chega à clínica, mas o chat não atualiza o estado estruturado "A caminho" | Ancorar a ação de estado acima do campo de mensagem e recolher o campo quando o aceite chega | Protótipo D32–D33, MoLIC M01.C14 |

**O que será implementado.** Nenhuma das recomendações foi implementada no protótipo nesta rodada; como a E14 é a última entrega da disciplina, todas ficam como trabalho futuro. Ordem de prioridade para a próxima iteração: (1) AU02, porque envolve privacidade e convergiu com a inspeção (HC03); (2) AU05, porque leva à escolha de unidade fechada em urgência; (3) AU03; depois AU04 e AU06 (severidade 2).

## F. Comparação com a avaliação heurística

| Problema | Detectado na heurística? | Detectado por usuários? | O que aprendemos |
|---|---|---|---|
| HC02 · recebimento e aceite pouco distintos no painel | Sim (A02-V02) | Fora do teste: nenhuma tarefa com profissionais da clínica | O painel foi operado pela equipe com roteiro fixo. O problema continua só como resultado de inspeção e entra como limitação na seção G. |
| HC03 · hierarquia das autorizações pouco clara | Sim (A02-V03) | Sim (AU02) | Convergência direta. A inspeção previu a confusão; as sessões mostraram que o padrão é manter a caixa marcada por precaução, não por decisão. Pela regra da E12, sobe um nível de prioridade. |
| HC04 · espera por resposta perde destaque após o envio | Sim (A01-V01) | Não confirmado (AU01) | CMP-2 compatível nas três sessões. O risco permanece, mas não foi observado neste cenário. |
| HC05 · alcance do cancelamento após o aceite | Sim (A01-V02) | Não testado | Nenhuma tarefa de cancelamento nesta rodada. Permanece como risco de inspeção. |
| HC06 · seletor de provedor ocupa espaço da conversa | Sim (A01-V03) | Sem evidência | O seletor ficou oculto durante o teste, então a condição inspecionada não foi apresentada aos participantes. |
| HC07 · animal anterior em destaque ao começar outro caso | Sim (A03-V01) | Sem evidência suficiente | Em UT05 os participantes começaram o caso da Nina depois do Bob, mas a planilha não tinha item para registrar o animal associado, e nenhuma ficha relata o relato da Nina ligado ao Bob. Não dá para afirmar que o problema não ocorreu. |
| HC08 · "Não sei" sem opção visível junto da pergunta | Sim (A03-V02) | Não confirmado | 3/3 responderam "não sei" sobre a água digitando livremente. A ausência do atalho não impediu a resposta neste cenário, que já dizia no cartão o que a pessoa não sabia. |
| HC09 · referência ambígua ao animal na pergunta complementar | Sim (A03-V03) | Sem evidência | O texto da pergunta é gerado pelo modelo e pode variar entre sessões; as fichas não registram a formulação exibida. |
| AU03 · resumo não reconhecido como editável | Não | Sim | Apareceu só na observação: a inspeção tratou o resumo como correto por apresentar um campo de texto. |
| AU04 · saída e quantidade de detalhe no estado INCERTO | Não na E13 original; relacionado a HC08 e a HC15 (D41, marcado na E11 e graduado só na revisão da E13) | Sim | Apareceu só na observação. A inspeção olhou a pergunta complementar, mas não o que o tutor faz depois da orientação final. |
| AU05 · horário lido como decoração | Parcialmente: a E11 já marcava D15 ("mapa e lista sem filtro") como problema, mas a E13 original não o graduou | Sim | Apareceu só na observação, no perfil de baixa familiaridade. A revisão da E13 registra D15 como HC13. |
| AU06 · botão de estado compete com o campo de mensagem | Não | Sim | Apareceu só na observação, no perfil de baixa familiaridade. |

Os problemas acrescentados na revisão da E13 (HC10–HC16) foram graduados depois do teste. Dois convergem com achados desta rodada: HC13 (D15, lista sem filtro começando por unidade fechada) com AU05, e HC15 (D41, resposta após o complemento sem mostrar o que foi incorporado) com AU04. Os demais não tinham tarefa correspondente.

## G. Conclusão

**1. Quais metas de usabilidade foram atingidas?** MU01 foi atingida: 3/3 concluíram UT01 sem ajuda de nível 2 ou 3 (U03 recebeu só um esclarecimento de cenário, N1, que pela regra da E12 não conta). MU02 foi atingida com mediana de 02:05 em UT02, abaixo do limite de 03:00, mas com margem de 55 s e com uma sessão (U03, 03:47) acima do limite. MU03 foi atingida em cinco das seis tarefas e ficou abaixo em UT03 (mediana 3/5). MU04 não foi atingida em CMP-4: dois recontos compatíveis e um parcialmente compatível na situação de informação insuficiente; CMP-1, CMP-2, CMP-3 e CMP-5 tiveram 3/3 compatíveis.

**2. Quais problemas foram recorrentes e com quais perfis/tarefas?** O resultado mais importante do teste é **UT03, com 66,7% de conclusão e mediana de 04:36**: é a tarefa de compartilhamento, a mais sensível à privacidade, e duas das três participantes mantiveram a conversa completa autorizada. UT05 é a segunda tarefa mais lenta (mediana 04:41) e concentra o único reconto não compatível. U03, de menor familiaridade com apps, concentra boa parte dos problemas: falha em UT03, parcial em UT02, horário ignorado e aviso de saída pelo chat. U02 teve dificuldade em UT03 e UT05. U01 não teve dificuldade relevante.

**3. O que surpreendeu a equipe?** Primeiro, U03 falhou em UT03 e mesmo assim explicou corretamente que o atendimento ainda dependia do aceite: errar a tarefa não significou entender errado o estado do envio, o que mostra que eficácia e compreensão precisam ser medidas separadamente. Segundo, o problema de privacidade mais grave (AU02) apareceu como **precaução** ("vai que precisa"), não como erro de leitura, o que muda a solução: não basta explicar melhor, é preciso que a opção opcional pareça opcional. Terceiro, três problemas de severidade 2–3 (AU03, AU05, AU06) só apareceram com pessoas, e a inspeção tinha considerado bom justamente o resumo editável.

**4. Quais mudanças são prioritárias?** (1) Separar visualmente a autorização obrigatória da opcional e mostrar o que será enviado (AU02/HC03). (2) Tornar o resumo visivelmente editável (AU03). (3) Destacar aberto/fechado no topo do cartão da unidade (AU05/HC13). (4) Dar ações claras de saída no estado de informação insuficiente (AU04).

**5. Que limitações do teste impedem generalizações amplas?**

- **Amostra de três pessoas**, recrutadas por conveniência entre amigos e familiares dos integrantes (o que pode deixar as avaliações mais gentis): os resultados são indícios, não estimativas. Uma única pessoa muda qualquer proporção em 33 pontos.
- **Só o perfil tutor.** Nenhum profissional de clínica participou; o painel (F4) e HC02 ficaram fora, e qualquer conclusão sobre ele continua exploratória até a investigação de H03/H05.
- **Sem gravação (decisão da equipe) e sem as folhas originais**: tempos, hesitações, falas e recontos dependem só da transcrição feita pela equipe no dia; as planilhas e questionários não foram guardados, então nem terceiros nem a própria equipe podem reconferir os números da seção C ou a classificação dos recontos.
- **Uma sessão por participante**: a facilidade de memorização não foi medida.
- **Cenários simulados**, em laboratório, sem estresse real nem animal presente; o contexto de urgência em casa (H08) não foi reproduzido.
- **Resposta do modelo variável** entre sessões: a formulação das perguntas complementares e da orientação pode ter mudado de uma pessoa para outra.
- **Verbalização espontânea** registrada em algumas tarefas pode ter alongado levemente os tempos dessas tarefas.
- **Formulação de CMP-2**: nas sessões foi usada a pergunta "o Bob já tem atendimento garantido no hospital?", que já sugere o conceito testado e admite resposta sim/não. O resultado 3/3 pode estar inflado; a E12 revisada troca a pergunta por uma formulação aberta para próximas rodadas. Pelo mesmo motivo, a instrução do cartão 3 sobre não mostrar toda a conversa pode ter indicado o caminho, embora 2/3 tenham mantido a autorização mesmo assim.
- **Piloto e sessões no mesmo dia**, sem correção prévia dos problemas da inspeção: o teste mediu a versão com HC02–HC07 em aberto.
- **Piloto feito por um integrante da equipe**, que já conhecia o protótipo: validou roteiro e equipamento, mas não antecipou dificuldades de quem usa o aplicativo pela primeira vez.
- **Diferença entre perfis**: os resultados de U03 pesam muito na leitura de UT02, UT03 e UT04; com três pessoas não é possível separar o efeito da interface do efeito da familiaridade.
- **H13 (falsa segurança após não emergência)**: CMP-5 teve 3/3 compatíveis, mas em um único cenário e uma única forma de apresentar a orientação.

## Checklist

- [x] Número de participantes finais atende ao enunciado.
- [x] Participantes são representativos do público e não são membros da equipe.
- [x] Se foram usados participantes proxy, a justificativa e a limitação estão explícitas. **Não se aplica.**
- [x] O teste avalia a interação; não confunde usabilidade do protótipo com desempenho técnico do TCC.
- [x] Tarefas usadas no teste são rastreáveis a objetivos e cenários.
- [x] Há consentimento e anonimização.
- [x] Foi realizado teste piloto (no mesmo dia e com um integrante da equipe, registrado como desvio).
- [x] Tarefas têm critérios de sucesso definidos antes do teste.
- [x] Moderadores não ensinaram o caminho durante a tarefa. A indicação direta em UT03 ocorreu no limite de tempo e a tarefa foi registrada como falha.
- [x] Resultados estão separados por usuário e por tarefa.
- [x] Foram registrados sucesso, erros, ajudas, tempo e satisfação quando aplicáveis.
- [x] Medianas recalculadas a partir das fichas e regra de ajuda explicitada.
- [x] Todos os instrumentos usados estão vinculados.
- [x] Conclusão combina evidência quantitativa e qualitativa.
- [x] Achados geram recomendações e atualização da [rastreabilidade](../RASTREABILIDADE.md#vínculos-da-entrega-14).
