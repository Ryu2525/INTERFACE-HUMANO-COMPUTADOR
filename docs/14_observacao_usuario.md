# Entrega 14 — Avaliação de usabilidade por observação de usuários

**Data:** 18/11/2026  
**Status:** 🟩 concluída  
**Responsabilidade:** solução consolidada por equipe. O número de participantes finais observados deve ser igual ao número de integrantes, conforme o modelo da disciplina; recomenda-se que cada integrante seja responsável por conduzir/analisar ao menos um participante.

## Objetivo da atividade

Observar usuários representativos realizando tarefas reais ou realisticamente simuladas para identificar problemas de eficácia, eficiência, compreensão e satisfação que não podem ser inferidos apenas por inspeção.

> **Participantes finais não devem ser membros da equipe.** Um integrante pode participar do teste piloto apenas para validar roteiro/equipamentos, sem contar na amostra final.

### Quando o usuário é um perfil profissional especializado

Em TCCs técnicos, o público pode ser DBA, analista, pesquisador, administrador, técnico ou outro especialista. Priorize participantes que possuam relação real com as tarefas. Se não for possível recrutar o perfil ideal, qualquer participante aproximado/proxy deve ser **justificado previamente e tratado como limitação**; não apresente o resultado como equivalente ao de especialistas reais.

O teste avalia a **interação com o protótipo**. Não é necessário que o participante valide o desempenho científico do algoritmo. Resultados simulados podem ser usados quando declarados e coerentes com a tarefa.

Tarefas podem envolver, por exemplo, interpretar um dashboard, configurar uma análise, encontrar uma execução no histórico usando filtros, comparar resultados, gerar relatório, revisar alerta ou administrar permissões.

## A. Fluxograma do processo — equipe

![Fluxograma](../assets/14_testes/fluxograma_avaliacao.svg)

O fluxograma deve representar, no mínimo: planejamento → recrutamento → consentimento → preparação → execução das tarefas/observação → pós-teste → consolidação/análise → recomendações.

## B. Procedimento de preparação e execução — equipe

### Passo 1 — Objetivos e versão avaliada

**Versão/commit/Figma:** [VetIA](https://vetia.chilecentral.cloudapp.azure.com/), versão mais recente do site em 18/11/2026.  
**Metas de usabilidade relacionadas:** MU01 (≥ 80% sem ajuda em UT01), MU02 (mediana ≤ 3 min em UT02), MU03 (mediana ≥ 4/5 por tarefa) e MU04 (100% de recontos compatíveis por situação crítica).

### Passo 2 — Participantes

| ID | Perfil | Critérios que justificam participação | Integrante responsável |
|---|---|---|---|
| U01 | faixa 18–29, tutora de dois cães, usa aplicativos de serviços todos os dias | Faixa 18–29, alta familiaridade com apps, perfil próximo de P01 | Julian (moderador) |
| U02 | faixa 30–44, tutora de um gato, já precisou de atendimento fora do horário comercial | Faixa 30–44, familiaridade média, experiência de urgência noturna, perfil próximo de P01 | Vinícius (moderador) |
| U03 | faixa 45–59, tutora de uma cadela idosa, quase nunca usa apps de saúde | Faixa 45–59, baixa familiaridade, perfil próximo de P02 | João (moderador) |

### Passo 3 — Consentimento e privacidade

- Termo/registro de consentimento: [termo de consentimento do teste](../instrumentos/teste_vetia_termo_consentimento.md).
- Gravação de tela/áudio/vídeo: não houve gravação.
- Forma de anonimização: IDs `U01`, `U02` e `U03`.
- Local e período de armazenamento: pasta restrita da equipe até o fim do semestre.

### Passo 4 — Teste piloto

**Data:** 18/11/2026. O piloto e as sessões ocorreram na mesma data, antes das datas propostas na E12.  
**O que foi validado:** Roteiro, duração, entendimento das instruções e funcionamento do protótipo.  
**Mudanças após piloto:** A abertura foi encurtada, a instrução de compartilhamento de UT03 ficou mais explícita e a planilha passou a registrar separadamente a espera pela resposta do sistema.

### Passo 5 — Tarefas

| ID | Cenário/instrução apresentada | Critério de sucesso | Métricas | Ligação com modelo |
|---|---|---|---|---|
| UT01 | "São 22h. Bob, cão de 5 anos, 22 kg, respirando muito rápido há 20 min, língua meio roxa, não quer levantar. Use o aplicativo para contar o que está vendo e saber o que fazer." | Relato com os sinais e orientação de emergência exibida, sem ajuda | sucesso, tempo, erros, ajudas, satisfação, CMP-1 | T01 · F1/F2 |
| UT02 | "Você está na FEI, em São Bernardo. Encontre um lugar funcionando agora e descubra como entraria em contato." | Unidade indicada como aberta selecionada e telefone ou ação de contato localizados | sucesso, tempo (MU02), erros, satisfação | T02 · F2 |
| UT03 | "A atendente do Hospital Aurora pediu as informações pelo aplicativo. O Bob vomitou às 17h. Faça o hospital receber o caso sabendo do vômito, sem ver tudo o que foi conversado." | Resumo corrigido com o vômito, status de envio exibido, conversa completa desmarcada | sucesso, tempo, erros de controle, satisfação, CMP-2 | T02 · F3 |
| UT04 | "Veja se o hospital respondeu e, se puder receber o Bob, avise que já está saindo." | Encaminhamento, aceite e mensagem localizados, com saída comunicada pelo botão “Estou a caminho” ou por mensagem. | sucesso, tempo, erros, satisfação, CMP-3 | T02 · F5 |
| UT05 | "Nina, gata de 8 anos, comendo menos e mais quieta há dois dias; comeu metade do normal, não vomitou, não sabe se bebeu água. Use o aplicativo para saber o que fazer." | Envio, resposta apenas com dados disponíveis e chegada à orientação | sucesso, tempo, erros, satisfação, CMP-4 | T03 · F6 |
| UT06 | "Outro dia. Nina espirrou duas ou três vezes, mas come, brinca e se comporta como sempre. Use o aplicativo para saber se precisa fazer algo." | Relato enviado e orientação de não emergência lida | sucesso, tempo, erros, satisfação, CMP-5 | T03 |

### Passo 6 — Protocolo do moderador

1. Receber participante e explicar que **o produto está sendo avaliado, não a pessoa**.
2. Obter consentimento.
3. Aplicar perfil pré-teste mínimo necessário.
4. Ler instruções padronizadas.
5. Observar sem ensinar o caminho; registrar pedidos de ajuda separadamente.
6. Se usar *think aloud*, explicar e aplicar de forma consistente.
7. Após cada tarefa, registrar satisfação/SEQ ou escala definida.
8. Fazer pós-teste/entrevista breve.
9. Encerrar e explicar uso dos dados.

## C. Resultados — por participante

### U01 — faixa 18–29, alta familiaridade, perfil próximo de P01

| Tarefa | Grau de sucesso | Erros | Tipos de erro/dificuldade | Ajudas | Tempo | Satisfação | Evidência/observação |
|---|---|---:|---|---:|---|---|---|
| UT01 | total | 1 | E (digitação: "respirano") | 0 | 01:52 | 5 | Corrigiu sozinha; hesitação de 14 s antes de tocar no resultado. CMP-1 compatível. |
| UT02 | total | 0 | — | 0 | 01:18 | 5 | Leu o horário em voz alta: "aberto até 23h, ó o telefone" |
| UT03 | total | 0 | — | 0 | 03:11 | 4 | Incluiu o vômito no resumo; desmarcou a conversa completa. CMP-2 compatível. |
| UT04 | total | 0 | — | 0 | 01:34 | 5 | Usou o botão de estado "Estou a caminho". CMP-3 compatível. |
| UT05 | total | 0 | — | 0 | 03:02 | 4 | Respondeu "não sei" sobre a água sem hesitar. CMP-4 compatível. |
| UT06 | total | 0 | — | 0 | 01:26 | 5 | "É só espirro, então é acompanhar". CMP-5 compatível. |

**Link da gravação (se autorizado):** não se aplica.  
**Resposta pós-teste:** Confiança 4/5. Relatou dúvida entre as duas autorizações.

### U02 — faixa 30–44, familiaridade média, perfil próximo de P01

| Tarefa | Grau de sucesso | Erros | Tipos de erro/dificuldade | Ajudas | Tempo | Satisfação | Evidência/observação |
|---|---|---:|---|---:|---|---|---|
| UT01 | total | 1 | E (digitação: horário trocado) | 0 | 02:24 | 4 | Corrigiu após reler o cartão. CMP-1 compatível. |
| UT02 | total | 0 | — | 0 | 02:05 | 4 | Conferiu o horário antes de abrir o cartão da unidade |
| UT03 | parcial | 1 | C (manteve a conversa completa marcada) | N2 | 04:36 | 3 | "Deixa marcada, vai que precisa". CMP-2 compatível. |
| UT04 | total | 0 | — | 0 | 01:12 | 5 | Localizou o aceite na lista de encaminhamentos, leu a mensagem e acionou “Estou a caminho”. CMP-3 compatível. |
| UT05 | parcial | 1 | Navegação (dificuldade para sair da conversa) | N2 | 05:19 | 3 | Respondeu "não sei" sobre água, mas precisou o início. CMP-4 parcial. |
| UT06 | total | 0 | — | 0 | 01:58 | 4 | Leu a orientação em voz alta, sem dificuldade. CMP-5 compatível. |

**Link da gravação (se autorizado):** não se aplica.  
**Resposta pós-teste:** Confiança 3/5. Relatou dúvida sobre onde corrigir o resumo e quais informações seriam enviadas.

### U03 — faixa 45–59, baixa familiaridade, perfil próximo de P02

| Tarefa | Grau de sucesso | Erros | Tipos de erro/dificuldade | Ajudas | Tempo | Satisfação | Evidência/observação |
|---|---|---:|---|---:|---|---|---|
| UT01 | total | 0 | — | N1 | 03:38 | 4 | Pediu confirmação do enunciado uma vez. CMP-1 compatível. |
| UT02 | parcial | 1 | I (não conferiu o horário no cartão da unidade) | N2 | 03:47 | 4 | Escolheu a primeira unidade da lista |
| UT03 | falha | 1 | C (enviou com a conversa completa e sem o vômito) | N2 ×2, N3 no limite de 06:00 | 06:04 | 2 | Não reconheceu o resumo como área editável. CMP-2 compatível. “O caso foi enviado, mas o atendimento ainda não está confirmado. Preciso esperar o hospital aceitar ou responder.” |
| UT04 | total | 0 | — | 0 | 02:48 | 4 | Localizou o aceite, reconheceu a mensagem da clínica e avisou pelo chat que estava saindo. CMP-3 compatível. |
| UT05 | total | 1 | E (apagou e reescreveu o relato duas vezes) | 0 | 04:41 | 4 | Respondeu "não sei" sobre a água. CMP-4 compatível. |
| UT06 | total | 0 | — | 0 | 02:19 | 4 | Leu a orientação devagar, em voz baixa. CMP-5 compatível. |

**Link da gravação (se autorizado):** não se aplica.  
**Resposta pós-teste:** Confiança 3/5. Relatou dificuldade com as duas autorizações e sugeriu simplificar o envio.

## D. Consolidação por tarefa

| Tarefa | Taxa de sucesso | Tempo típico | Erros recorrentes | Satisfação | Meta atendida? | Problemas prioritários |
|---|---:|---|---|---|---|---|
| UT01 | 3/3 (100%) · 3/3 sem ajuda na execução | 02:24 | 2 E (digitação, corrigidos) | 4 | MU01 sim · MU03 sim | Nenhum crítico; relato digitado sob pressão gera erro de digitação |
| UT02 | 2 totais + 1 parcial (100% de conclusão) | 01:42 | 1 I (horário não conferido) | 4 | MU02 sim (01:42 ≤ 03:00) · MU03 sim | Horário da unidade passou despercebido em uma ficha |
| UT03 | 1 total + 1 parcial + 1 falha (66,7% de conclusão) | 03:11 | 2 C (conversa completa mantida), 1 ausência de correção do resumo | 3 | MU03 não · CMP-2: 3/3 compatíveis | Hierarquia das duas autorizações; resumo não reconhecido como editável |
| UT04 | 3/3 (100%) | 01:34 | Nenhum erro registrado | 5 | MU03 sim | U03 avisou pelo chat. A ação “Estou a caminho” pode ganhar destaque. |
| UT05 | 2 totais + 1 parcial (100% de conclusão) | 03:52 | 1 dificuldade de navegação e 1 reescrita | 4 | MU03 sim · CMP-4: 2/3 compatíveis | Dificuldade para sair da conversa e dúvida sobre quanto detalhar |
| UT06 | 3/3 (100%) · 3/3 sem ajuda na execução | 01:58 | 0 | 4 | MU03 sim | Nenhum |

## E. Achados e recomendações

| ID | Achado | Evidência (quant. + qual.) | Impacto | Recomendação | Artefatos a revisar |
|---|---|---|---|---|---|
| AU01 | O estado de espera após o envio tem pouco destaque (HC04). | Inspeção E13. CMP-2: 3/3 compatíveis no teste. | Risco de interpretação a acompanhar. | Manter o rótulo de espera junto ao status até o aceite. | Signos, MoLIC F5, protótipo D22 |
| AU02 | As duas autorizações têm peso visual equivalente e a opcional vem antes da obrigatória | 2/3 mantiveram a conversa completa marcada; U02: "deixa marcada, vai que precisa"; U01 desmarcou após ler as duas; U03 marcou as duas sem decidir | Exposição de conteúdo além do pretendido, não reversível após leitura; severidade 3 | Autorização obrigatória primeiro, conversa completa como opção explícita e desmarcada, com resumo do que será enviado | Signos, MoLIC F3, Figma D19–D21 |
| AU03 | O resumo do envio não é reconhecido como área editável | U03 não incluiu o vômito mesmo após duas ajudas N2; U02 voltou ao resumo só após N2; U01 editou sem ajuda | Elemento principal de UT03 perdido; severidade 3 | Marcar o resumo com indicação de que o resumo é editável ("toque para corrigir") e campo dedicado a informação nova | Protótipo D18, signos, MoLIC F3 |
| AU04 | Há dificuldade de navegação durante a complementação do relato. | U02 pediu ajuda para sair da conversa. U03 reescreveu o relato por considerá-lo curto. | Pode aumentar o esforço para concluir a interação. | Verificar a orientação sobre como avançar e sobre a suficiência dos dados informados. | Signos, MoLIC F6, protótipo D38–D39 |
| AU05 | O horário de funcionamento no cartão da unidade é lido como informação secundária | U03 selecionou a primeira unidade sem ler o horário, resolvido só com N2; U01 e U02 leram em voz alta | Seleção de unidade fechada em situação de urgência; severidade 3 | Destacar o estado aberto/fechado como selo no topo do cartão e esmaecer unidades fechadas | Signos, MoLIC F2, protótipo D17 |
| AU06 | O botão de estado "Estou a caminho" compete com o campo de mensagem aberto | U03 concluiu UT04 pelo chat. U01 e U02 usaram o botão. | O aviso chega à clínica, mas o chat não aciona a atualização estruturada do estado. Severidade 2. | Ancorar a ação de estado acima do campo de mensagem e recolher o campo quando o aceite chega | Protótipo D32–D33, MoLIC F5 |

## F. Comparação com a avaliação heurística

| Problema | Detectado na heurística? | Detectado por usuários? | O que aprendemos |
|---|---|---|---|
| HC02 · recebimento e aceite pouco distintos no painel | Sim (A02-V02) | Fora do escopo das tarefas de tutor | O painel foi operado pela equipe. A interpretação pelo tutor foi avaliada em tarefas próprias. |
| HC03 · hierarquia das autorizações pouco clara | sim (A02-V03) | sim (AU02) | Convergência direta. A inspeção previu a confusão e as sessões mostraram que o padrão é manter a caixa marcada por precaução, não por decisão |
| HC04 · espera por resposta perde destaque após o envio | Sim (A01-V01) | CMP-2 compatível nas três fichas | A inspeção indica um risco. O reconto desta rodada foi compatível nos três casos. |
| HC05 · alcance do cancelamento após o aceite | sim (A01-V02) | não — nenhuma tarefa de cancelamento na rodada | Permanece como risco de inspeção, sem confirmação comportamental |
| HC06 · seletor de provedor ocupa espaço da conversa | Sim (A01-V03) | Sem evidência suficiente | O seletor ficou oculto durante o teste. |
| AU03 · resumo não reconhecido como editável | não | sim | Apareceu só na observação: a inspeção tratou o resumo como correto por apresentar um campo de texto |
| AU05 · horário lido como decoração | não | sim | Apareceu só na observação, e apenas no perfil de baixa familiaridade |
| AU06 · botão de estado compete com o campo de mensagem | não | sim | Apareceu só na observação, no perfil de baixa familiaridade |

## G. Conclusão

A conclusão deve responder:

1. Quais metas de usabilidade foram atingidas?
2. Quais problemas foram recorrentes e com quais perfis/tarefas?
3. O que surpreendeu a equipe?
4. Quais mudanças são prioritárias?
5. Que limitações do teste impedem generalizações amplas?

1. MU01 foi atingida com 3/3 sucessos sem ajuda. MU02 foi atingida com mediana de 01:42. MU03 foi atingida em cinco tarefas e ficou abaixo da meta em UT03, com mediana de 3/5. MU04 ficou abaixo da meta em CMP-4, com dois recontos compatíveis e um parcial. CMP-2 teve 3/3 respostas compatíveis.
2. Em UT03, duas participantes mantiveram a opção de compartilhar a conversa completa. U03, com menor familiaridade, também teve dificuldade para localizar o horário e perceber a ação de estado.
3. U03 entendeu que o atendimento dependia de confirmação apesar da falha em UT03.
4. Dar destaque à edição do resumo e distinguir as autorizações obrigatória e opcional.
5. A amostra de três participantes limita a generalização. A falta de gravação limita a conferência dos tempos e das falas.

## Checklist

- [x] Número de participantes finais atende ao enunciado.
- [x] Participantes são representativos do público e não são membros da equipe.
- [x] Se foram usados participantes proxy, a justificativa e a limitação estão explícitas. **Não se aplica.**
- [x] O teste avalia a interação; não confunde usabilidade do protótipo com desempenho técnico do TCC.
- [x] Tarefas administrativas/analíticas usadas no teste são rastreáveis a objetivos e cenários.
- [x] Há consentimento e anonimização.
- [x] Foi realizado teste piloto.
- [x] Tarefas têm critérios de sucesso definidos antes do teste.
- [x] Moderadores não ensinaram o caminho durante a tarefa. A indicação direta em UT03 ocorreu no limite de tempo e a tarefa foi registrada como falha.
- [x] Resultados estão separados por usuário e por tarefa.
- [x] Foram registrados sucesso, erros, ajudas, tempo e satisfação quando aplicáveis.
- [x] Conclusão combina evidência quantitativa e qualitativa.
- [x] Achados geram recomendações e atualização da [rastreabilidade](../RASTREABILIDADE.md#vínculos-da-entrega-14).
