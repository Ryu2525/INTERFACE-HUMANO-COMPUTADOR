# Entrega 6 — Prototipação em papel

**Data:** 21/10/2026  
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 solução integrada por equipe

## Objetivo da atividade

Externalizar rapidamente ideias de interação em baixa fidelidade para explorar alternativas antes de investir em detalhes visuais. O valor da atividade está no **ciclo construir → simular → observar → revisar**, não na beleza do desenho.

## 1. Escopo do protótipo

**Personas:** P01 — Camila Rocha; P02 — Roberto Nunes.  
**Cenários/tarefas cobertos:** C01/T01 e T03; C03/T01 e T03.  
**Objetivo principal:** Explorar a **tela de conversa** do VetIA, onde o tutor relata os sinais do animal, responde às perguntas complementares e compreende a orientação e o próximo passo. A análise se concentra no que o tutor escreve e no que o sistema responde em cada desfecho: possível emergência e informação insuficiente (INCERTO).

O cadastro do animal, a busca de clínicas, o compartilhamento do caso e o painel da clínica continuam previstos no projeto (E5 e E9), mas ficam fora desta iteração do protótipo.

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

A tela de conversa combina **entrada de dados** (relato e respostas do tutor) com **resultado com explicação** (orientação, justificativa e limites).

## 2. Fluxo escolhido

| Fluxo | Tarefa/objetivo | Por que foi priorizado |
|---|---|---|
| PF02 | Usar o chat: escolher se associa um animal, relatar os sinais, responder às perguntas e compreender a orientação e o próximo passo. T01 e T03. | É o fluxo central da pré-triagem e concentra os riscos do recorte: perder ou distorcer o relato, gerar falsa segurança e não transformar a orientação em ação. |

## 3. Telas e estados

Os estados abaixo são da tela de conversa do protótipo navegável do VetIA, publicado em <https://vetia.chilecentral.cloudapp.azure.com/> e capturado em 04/11/2026 em visão de celular (375 × 812), contexto previsto para P01 e P02 (H08). Os prints usam a conta acadêmica compartilhada do sistema (`Ana (demo)`) e casos fictícios; nenhum dado real de tutor ou animal foi usado.

### 3.1 Mapa de estados da conversa

| ID | Estado | Controle que muda o estado | Tarefa |
|---|---|---|---|
| D08 | Conversa vazia: pergunta "O que está acontecendo?", animal opcional ("Associar animal depois"), atalhos de sinais, seletor "Análise por", campo de texto e áudio | escrever ou gravar o relato; escolher o animal | T01 |
| D09 | Relato escrito, botão de envio ativo | enviar → D10 | T01 |
| D10 | Resposta iniciada: acolhimento e "Sinais identificados no relato" | rolar → D11 | T03 |
| D11 | Cartão de **possível emergência**: "Procure atendimento agora" e próximos passos | "Encontrar atendimento" | T03 |
| D12 | Abaixo do cartão: "Ver justificativa original da análise" e referências | expandir/recolher | T03 |
| D36 | Nova conversa já associada ao animal da conversa anterior | seletor de animal | T01 |
| D37 | Relato de outro animal enviado; resposta iniciada | rolar → D38 | T01/T03 |
| D38 | Cartão **"Precisamos entender melhor"** (INCERTO) | rolar → D39 | T03 |
| D39 | Pergunta complementar abaixo do cartão | responder no campo de texto → D41 | T01 |
| D40 | Justificativa e referências abertas | expandir/recolher | T03 |
| D41 | Resposta do sistema após o complemento | rolar → D42 | T03 |
| D42 | Orientação final do estado INCERTO | novo relato; "Ver clínicas" | T03 |

### 3.2 Prints da tela de conversa

**Caso 1 — possível emergência**

<table>
<tr>
<td align="center"><img src="../assets/06_prototipos/D08_chat_inicial.jpg" width="180"><br><sub>D08 Conversa vazia</sub></td>
<td align="center"><img src="../assets/06_prototipos/D09_relato_digitado.jpg" width="180"><br><sub>D09 Relato escrito</sub></td>
<td align="center"><img src="../assets/06_prototipos/D10_resultado_topo.jpg" width="180"><br><sub>D10 Início da resposta</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D11_resultado_emergencia.jpg" width="180"><br><sub>D11 Possível emergência</sub></td>
<td align="center"><img src="../assets/06_prototipos/D12_resultado_justificativa.jpg" width="180"><br><sub>D12 Justificativa e referências</sub></td>
<td></td>
</tr>
</table>

**Caso 2 — informação insuficiente**

<table>
<tr>
<td align="center"><img src="../assets/06_prototipos/D36_nova_conversa_animal_anterior.jpg" width="180"><br><sub>D36 Nova conversa com animal anterior</sub></td>
<td align="center"><img src="../assets/06_prototipos/D37_incerto_relato.jpg" width="180"><br><sub>D37 Relato e início da resposta</sub></td>
<td align="center"><img src="../assets/06_prototipos/D38_incerto_cartao.jpg" width="180"><br><sub>D38 Precisamos entender melhor</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D39_pergunta_complementar.jpg" width="180"><br><sub>D39 Pergunta complementar</sub></td>
<td align="center"><img src="../assets/06_prototipos/D40_justificativa_referencias.jpg" width="180"><br><sub>D40 Justificativa e referências</sub></td>
<td align="center"><img src="../assets/06_prototipos/D41_resposta_apos_complemento.jpg" width="180"><br><sub>D41 Após o complemento</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D42_orientacao_final.jpg" width="180"><br><sub>D42 Orientação final</sub></td>
<td></td><td></td>
</tr>
</table>

## 4. Simulação

Realize uma simulação com uma pessoa que não participou da elaboração dessas telas.

**Data:** 04/11/2026 · **Versão:** protótipo navegável publicado · **Análise:** Gemini (nuvem), padrão do sistema · **Condução:** equipe.

A conversa foi usada com dois casos fictícios do roteiro em [`instrumentos_simulacao.md`](../assets/06_prototipos/instrumentos_simulacao.md): Bob, de P01 (situação S01), e Nina, de P02 (situação S02). As mensagens do tutor foram escritas pela equipe; **as respostas do sistema citadas abaixo são as que o protótipo efetivamente produziu**, conferidas nos prints. Como a equipe conhece as telas, este walkthrough identifica problemas de fluxo e de comunicação, mas **não substitui a simulação com uma pessoa externa** pedida no enunciado, que continua pendente (ver Checklist). Não houve gravação de vídeo; os prints indicados entre parênteses são o registro.

### 4.1 Caso 1 — Bob, possível emergência (S01)

A conversa abre perguntando "O que está acontecendo?" e explicando que o tutor não precisa saber o nome do problema. Abaixo aparecem atalhos como "Mudou o comportamento" e "Parou de comer", o seletor "Análise por" (Gemini ou Ollama) com um aviso de que o relato será enviado ao Google Gemini, e o campo de texto com a opção de áudio (D08).

Com Bob associado à conversa, o tutor escreveu: "O Bob está respirando muito rápido faz uns 20 minutos e a língua dele está com uma cor estranha, meio roxa. Ele está deitado e não quer levantar." (D09). O sistema respondeu que os sinais precisavam de avaliação veterinária agora e listou os sinais que identificou no relato: respiração rápida, língua roxa, não quer levantar (D10). Em seguida veio o cartão **"Procure atendimento agora"**, com a instrução de procurar um veterinário imediatamente, de não esperar outra resposta no chat e de avisar a clínica sem atrasar a saída, além do botão "Encontrar atendimento" (D11).

No celular, porém, o cartão apareceu cortado. O seletor "Análise por", o aviso sobre o Gemini e o campo de texto ficam fixos na parte de baixo e ocupam cerca de metade da tela, e foi preciso rolar para chegar à ação principal (D10–D11). Logo abaixo do cartão ficam a justificativa e as referências, recolhidas (D12).

### 4.2 Caso 2 — Nina, informação insuficiente (S02)

Ao tocar "Nova conversa", o seletor já veio com Bob e o título mudou para "Como Bob está hoje?". Foi preciso trocar para "Associar animal depois" antes de relatar o caso de outro animal (D36).

O tutor escreveu: "Minha gata Nina está comendo menos faz uns dois dias e está diferente, mais quieta. Não sei direito quando isso começou." (D37). O sistema respondeu que ainda faltavam informações para orientar a urgência com segurança e que isso não significa que esteja tudo bem. Mostrou o cartão **"Precisamos entender melhor"**, recomendou procurar atendimento na dúvida, reforçou que tudo bem responder que não sabe e lembrou que, se houver piora, o tutor pode contatar uma clínica sem concluir a conversa (D38). Em seguida perguntou "Quanto ele comeu em relação ao habitual?", tratando a gata no masculino (D39).

Ao abrir a justificativa, o tutor leu que faltavam informações sobre vômito, apatia intensa e tempo sem comer. As referências mostravam três títulos de artigos científicos em inglês e a linha "Modelo: gemini · gemini-3.5-flash-lite" (D40).

O tutor respondeu à pergunta: "Acho que menos da metade do normal, mas não tenho certeza. Ela não vomitou." A nova resposta repetiu a mesma abertura e o mesmo cartão. Os sinais identificados continuaram "comendo menos; mais quieta", sem a informação acrescentada (D41), e a orientação final foi entrar em contato com uma clínica e procurar atendimento se houver piora, com a possibilidade de enviar novas observações (D42).

### 4.3 Observações

| Observação | Tela/ação | Evidência | Consequência para o design |
|---|---|---|---|
| A conversa aceita relato em linguagem comum e não exige associar um animal. | D08 | "Não precisa saber o nome do problema"; seletor "Associar animal depois". | Mantém o cadastro fora do caminho urgente (H14) e respeita o vocabulário do tutor (H06). Manter. |
| O resultado de emergência é claro e leva a uma ação. | D11 | Cartão "Procure atendimento agora" com instruções e botão "Encontrar atendimento". | Atende T03 no desfecho de emergência. Manter. |
| Os sinais identificados repetem as palavras do tutor. | D10 | "Respirando muito rápido; língua roxa; não quer levantar". | Permite ao tutor conferir se foi entendido. Manter. |
| No celular, o seletor "Análise por", o aviso e o campo de texto ficam fixos e ocupam cerca de metade da tela. | D10–D11 | O cartão de resultado aparece cortado e exige rolagem até a ação principal. | Em emergência, a ação principal fica fora da vista. Recolher o seletor após o primeiro envio ou levá-lo para configurações, mantendo um aviso curto de privacidade. |
| A escolha entre "Gemini · nuvem" e "Modelo local · Ollama" aparece para o tutor. | D08 | Termos técnicos sem explicação para o público leigo. | Contraria a linguagem simples prevista em H06. Usar um padrão e explicar a escolha em termos do que acontece com os dados. |
| "Nova conversa" mantém o animal da conversa anterior. | D36 | Seletor com Bob e título "Como Bob está hoje?" ao iniciar o relato sobre Nina. | Risco de associar o relato ao animal errado. Iniciar sem animal ou perguntar qual animal. |
| O estado INCERTO comunica que falta informação e não equivale a "está tudo bem". | D38 | "Isso não significa que esteja tudo bem"; "tudo bem responder que não sabe". | Atende H13 e evita falsa segurança. Manter. |
| A pergunta complementar trata a gata como "ele". | D39 | "Quanto ele comeu…" após "Minha gata Nina…". | Reduz a sensação de ser compreendido. Usar o gênero do relato ou forma neutra ("o animal"). |
| Referências em inglês e nome técnico do modelo ficam visíveis ao tutor. | D40 | Títulos de artigos e "gemini-3.5-flash-lite". | Vocabulário inadequado para o público (H06). Mostrar ao tutor a base em português simples e deixar os detalhes técnicos em um modo detalhado. |
| Depois do complemento, a resposta repete o texto anterior e não reflete o que foi informado. | D41–D42 | Sinais sem "menos da metade" nem "não vomitou"; mesma abertura e mesmo cartão. | O tutor não percebe que a resposta foi considerada e pode repetir ou abandonar (H12). Mostrar o que mudou e atualizar os sinais. |

## 5. Alterações após a simulação

As alterações abaixo são **decisões de revisão** derivadas do walkthrough. Ainda não foram implementadas no protótipo publicado; a coluna "Depois" descreve a próxima versão da tela de conversa.

| Antes | Problema | Depois | Justificativa |
|---|---|---|---|
| Seletor de modelo, aviso e campo de texto fixos ocupando metade da tela (D10). | Escondem a ação principal do resultado no celular. | Aviso de privacidade curto no primeiro envio; escolha de processamento em configurações; área fixa reduzida ao campo de texto. | Ação principal visível em emergência (T03); linguagem simples (H06). |
| Nova conversa herda o animal anterior (D36). | Relato pode ser associado ao animal errado. | Nova conversa começa em "Associar animal depois" ou pergunta qual animal. | Evita dados errados na análise e no resumo. |
| Pergunta complementar com gênero fixo (D39). | Linguagem distante do relato. | Gênero do relato ou forma neutra. | Linguagem simples e sensação de ser compreendido (H06). |
| Referências em inglês e nome do modelo visíveis (D40). | Vocabulário técnico para o tutor. | Explicação em português simples; referências técnicas em um modo detalhado. | Linguagem simples (H06). |
| Resposta ao complemento igual à anterior (D41). | Tutor não vê efeito da sua resposta. | Mostrar os sinais atualizados, o que mudou e o que ainda falta. | Progresso deve refletir informação nova, não número de mensagens (E5, T01; H12). |

Mantidos sem alteração: relato em linguagem comum sem cadastro obrigatório (H14), sinais identificados com as palavras do tutor, cartão de emergência com ação direta e estado INCERTO sem falsa segurança (H13).

## Checklist

- [x] O protótipo cobre tarefas relevantes da Entrega 5. A tela de conversa cobre T01 e T03.
- [x] Cada tela/estado pode ser justificado por uma tarefa, decisão ou informação necessária.
- [x] O projeto não criou dashboard/CRUD/login apenas para parecer “completo”.
- [x] Telas/estados estão numerados e navegáveis na documentação.
- [x] Há pelo menos uma simulação/walkthrough documentado. Walkthrough da equipe (seção 4); a simulação com pessoa externa ainda está pendente.
- [x] Críticas não foram apenas listadas: geraram decisão de revisão.
- [ ] O protótipo continua em baixa fidelidade; detalhes visuais não mascaram problemas de fluxo. O protótipo navegável é de alta fidelidade, e por isso o walkthrough se concentrou em fluxo e comunicação.
