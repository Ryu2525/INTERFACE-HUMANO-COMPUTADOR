# Entrega 6 — Prototipação em papel

**Data:** 21/10/2026  
**Status:** 🟩 concluída
**Responsabilidade:** 1 solução integrada por equipe

## Objetivo da atividade

Externalizar rapidamente ideias de interação em baixa fidelidade para explorar alternativas antes de investir em detalhes visuais. O valor da atividade está no **ciclo construir → simular → observar → revisar**, não na beleza do desenho.

## 1. Escopo do protótipo

**Persona:** P01 — Camila Rocha.  
**Cenário/tarefas cobertos:** C01/T01, T03 e T02.  
**Objetivo principal:** Explorar o caminho de uma **possível emergência** no VetIA: o tutor relata os sinais no chat, compreende a orientação, toca no botão de emergência, encontra uma clínica no mapa e confirma o envio do caso.

O cadastro do animal, o estado de informação insuficiente e o painel da clínica continuam previstos no projeto (E5 e E9), mas ficam fora desta iteração.

## 1.1 Possíveis famílias de interface

Escolha apenas o que for coerente com tarefas e cenários. Para TCCs técnicos, o protótipo pode explorar:

- **dashboard** para monitoramento e tomada de decisão;
- **configuração/parametrização** para preparar algoritmo/modelo/processo;
- **entrada/seleção de dados** com validação;
- **acompanhamento de execução** com progresso, fila, cancelamento e recuperação;
- **relatório/resultados** com explicação, gráficos e exportação;
- **histórico** com busca, filtros, ordenação e detalhes;
- **comparação** entre execuções, versões, algoritmos ou períodos;
- **administração** de usuários, papéis, permissões ou entidades do domínio;
- **auditoria/logs** traduzidos para o perfil;
- **alertas/ocorrências** com ação de resposta.

> Não desenhe todas essas telas por obrigação. O objetivo da baixa fidelidade é experimentar a **estrutura da interação** necessária para as tarefas priorizadas.

O caminho explorado combina **entrada de dados** (relato no chat), **resultado com explicação** (orientação de emergência) e **alerta com ação de resposta** (botão que leva ao atendimento).

## 2. Fluxos escolhidos

| Fluxo | Tarefa/objetivo | Por que foi priorizado |
|---|---|---|
| PF02 | Usar o chat: relatar os sinais e compreender a orientação de possível emergência. T01 e T03. | É o início da pré-triagem; na emergência, a orientação precisa virar ação imediata. |
| PF03 | Encontrar atendimento: abrir o mapa a partir do botão de emergência, escolher uma veterinária e confirmar o envio do caso. T02. | Fecha o caminho da emergência, sem confundir clínica listada com vaga confirmada. |

## 3. Telas e estados

Os estados abaixo são do protótipo navegável do VetIA, publicado em <https://vetia.chilecentral.cloudapp.azure.com/>, em visão de celular (375 × 812), contexto previsto para P01 (H08). Os prints foram capturados pela equipe em 04/11/2026 com um caso fictício de dificuldade respiratória (Bob, de P01) e mostram os mesmos estados percorridos na simulação da seção 4. Usam a conta acadêmica compartilhada do sistema (`Ana (demo)`); nenhum dado real de tutor, animal ou clínica foi usado.

### 3.1 Mapa de estados

| ID | Estado | Controle que muda o estado | Fluxo | Tarefa |
|---|---|---|---|---|
| D08 | Conversa vazia: "O que está acontecendo?", animal opcional, atalhos de sinais, campo de texto e áudio | escrever ou gravar o relato | PF02 | T01 |
| D09 | Relato escrito, botão de envio ativo | enviar → D10 | PF02 | T01 |
| D10 | Resposta iniciada: acolhimento e "Sinais identificados no relato" | rolar → D11 | PF02 | T03 |
| D11 | Cartão de **possível emergência**: "Procure atendimento agora" e botão de emergência | "Encontrar atendimento" → D13 | PF02 | T03 |
| D13 | Encontrar atendimento, antes da busca | endereço + "Buscar" ou "Usar minha localização" → D15 | PF03 | T02 |
| D15 | Mapa e lista de clínicas próximas | "Abertas agora" → D17; "Ligar"; "Rota" | PF03 | T02 |
| D17 | Lista filtrada por "Abertas agora" | "Ligar"; "Rota" | PF03 | T02 |
| D14 | Veterinárias habilitadas para receber o caso (ambiente acadêmico) | "Compartilhar caso" → D18 | PF03 | T02 |
| D18–D19 | Revisar antes de enviar: relato editável, pré-triagem e destino | edição do relato | PF03 | T02 |
| D20 | Autorização pendente: "Confirmar e compartilhar" desabilitado | marcar autorização → D21 | PF03 | T02 |
| D21 | Autorização marcada | "Confirmar e compartilhar" → D22 | PF03 | T02 |
| D22–D23 | Caso **Enviado**, com histórico | "Cancelar envio"; "Ver outras clínicas" | PF03 | T02 |

No protótipo, as clínicas reais do mapa oferecem apenas "Ligar" e "Rota"; o envio do caso é feito às veterinárias habilitadas da seção acadêmica (D14), que funcionam como unidades de teste.

### 3.2 Prints

**PF02 — Chat e orientação de emergência**

<table>
<tr>
<td align="center"><img src="../assets/06_prototipos/D08_chat_inicial.jpg" width="180"><br><sub>D08 Conversa vazia</sub></td>
<td align="center"><img src="../assets/06_prototipos/D09_relato_digitado.jpg" width="180"><br><sub>D09 Relato escrito</sub></td>
<td align="center"><img src="../assets/06_prototipos/D10_resultado_topo.jpg" width="180"><br><sub>D10 Início da resposta</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D11_resultado_emergencia.jpg" width="180"><br><sub>D11 Botão de emergência</sub></td>
<td></td><td></td>
</tr>
</table>

**PF03 — Mapa e envio do caso**

<table>
<tr>
<td align="center"><img src="../assets/06_prototipos/D13_encontrar_atendimento.jpg" width="180"><br><sub>D13 Antes da busca</sub></td>
<td align="center"><img src="../assets/06_prototipos/D15_mapa_todas.jpg" width="180"><br><sub>D15 Mapa e lista</sub></td>
<td align="center"><img src="../assets/06_prototipos/D17_lista_abertas_agora.jpg" width="180"><br><sub>D17 Abertas agora</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D14_unidades_ficticias.jpg" width="180"><br><sub>D14 Veterinárias para envio</sub></td>
<td align="center"><img src="../assets/06_prototipos/D18_revisar_envio.jpg" width="180"><br><sub>D18 Revisar antes de enviar</sub></td>
<td align="center"><img src="../assets/06_prototipos/D19_revisar_pretriagem.jpg" width="180"><br><sub>D19 Pré-triagem no envio</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D20_autorizacao_pendente.jpg" width="180"><br><sub>D20 Autorização pendente</sub></td>
<td align="center"><img src="../assets/06_prototipos/D21_autorizacao_marcada.jpg" width="180"><br><sub>D21 Autorização marcada</sub></td>
<td align="center"><img src="../assets/06_prototipos/D22_encaminhamento_enviado.jpg" width="180"><br><sub>D22 Caso enviado</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D23_historico_caso.jpg" width="180"><br><sub>D23 Histórico do caso</sub></td>
<td></td><td></td>
</tr>
</table>

## 4. Simulação

Realize uma simulação com uma pessoa que não participou da elaboração dessas telas.

**Participante:** U01 — orientador do TCC, que não participou da criação das interfaces.  
**Data:** {{26/10/2026}} · **Versão:** protótipo navegável publicado 

### 4.1 Tarefa

O participante usou o protótipo diretamente, a partir do chat, com um caso fictício de possível emergência: um cachorro que comeu chocolate.

### 4.2 O que aconteceu

U01 começou pelo chat e relatou que o cachorro tinha comido chocolate. O sistema identificou o relato como **possível emergência** e mostrou o cartão de emergência com o botão "Encontrar atendimento" (estados D10–D11).

Ele tocou no botão e foi levado à tela de atendimento, com o mapa e a lista de clínicas (D13–D15). Ali selecionou uma veterinária habilitada para receber o caso (D14), passou pela tela de revisão e confirmou o envio (D18–D22). O caso foi enviado.

**Resultado:** tarefa concluída, do relato ao envio do caso para a veterinária.

**Comentários do participante:** {{registrar aqui o que o orientador comentou durante ou depois do teste, se houver}}.

### 4.3 Observações

| Observação | Tela/ação | Evidência | Consequência para o design |
|---|---|---|---|
| O chat classificou o relato de ingestão de chocolate como possível emergência. | D10–D11 | Cartão de emergência apresentado a U01 após o relato. | O desfecho de emergência foi acionado por um caso diferente dos usados pela equipe. Manter. |
| O botão de emergência levou direto à busca de atendimento. | D11 → D13 | U01 tocou no botão e chegou ao mapa sem passos intermediários. | Liga a orientação à ação (T03 → T02), como previsto em H18. Manter. |
| U01 encontrou uma veterinária e concluiu o envio. | D14 → D22 | Caso enviado ao final da simulação. | O caminho de compartilhamento é completável por quem não conhece as telas. Manter a autorização explícita antes do envio. |

Os prints das mesmas telas, analisados pela equipe, mostraram ainda os pontos abaixo, que não foram relatados por U01, mas afetam o mesmo caminho:

| Observação | Tela | Evidência | Consequência para o design |
|---|---|---|---|
| No celular, o seletor "Análise por", o aviso sobre o Gemini e o campo de texto ficam fixos e ocupam cerca de metade da tela. | D10–D11 | O cartão de emergência aparece cortado e exige rolagem até o botão. | Em emergência, a ação principal pode ficar fora da vista. |
| Sem filtro, a busca mostra primeiro uma unidade fechada e um pet shop. | D15 | Ordem dos dois primeiros resultados. | Em emergência, o tutor pode perder tempo (H10a/H10b). |
| O envio exige autorização e avisa que não garante vaga. | D20–D21 | Botão desabilitado até marcar a autorização; aviso "O envio não confirma uma vaga". | Separa envio de confirmação (RC06). Manter. |
| O rótulo da pré-triagem aparece sem acento ("EMERGENCIA"). | D19 | Texto na revisão antes do envio. | Valor interno exposto ao tutor. |

## 5. Alterações após a simulação

As alterações abaixo são **decisões de revisão** a partir da simulação e da análise das mesmas telas. Ainda não foram implementadas no protótipo publicado; a coluna "Depois" descreve a próxima versão.

| Antes | Problema | Depois | Justificativa |
|---|---|---|---|
| Seletor de modelo, aviso e campo de texto fixos ocupando metade da tela (D10–D11). | O botão de emergência pode ficar fora da vista no celular. | Área fixa reduzida ao campo de texto; ao chegar uma resposta de emergência, rolar até o cartão e manter "Encontrar atendimento" visível. | Ação principal visível em emergência (T03; H18). |
| Busca de clínicas sem filtro (D15). | Prioriza unidade fechada e pet shop. | "Abertas agora" ligado por padrão quando a busca vem do botão de emergência; unidades 24 h destacadas. | Reduz o tempo até achar atendimento adequado (T02; H10a/H10b). |
| Rótulo "EMERGENCIA" na revisão do envio (D19). | Termo interno, diferente do mostrado no chat. | Mesmo rótulo do chat: "Possível emergência". | Consistência entre chat e envio. |

Mantidos sem alteração: classificação e cartão de emergência com botão de ação, passagem direta do botão para o mapa e autorização explícita antes do envio.

## Checklist

- [x] O protótipo cobre tarefas relevantes da Entrega 5. O caminho cobre T01, T03 e T02.
- [x] Cada tela/estado pode ser justificado por uma tarefa, decisão ou informação necessária.
- [x] O projeto não criou dashboard/CRUD/login apenas para parecer “completo”.
- [x] Telas/estados estão numerados e navegáveis na documentação.
- [x] Há pelo menos uma simulação/walkthrough documentado. Simulação com o orientador (U01), que não participou da criação das telas.
- [x] Críticas não foram apenas listadas: geraram decisão de revisão.
- [ ] O protótipo continua em baixa fidelidade; detalhes visuais não mascaram problemas de fluxo. O protótipo navegável é de alta fidelidade.
