# Entrega 6 — Prototipação em papel

**Data:** 21/10/2026  
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 solução integrada por equipe

## Objetivo da atividade

Externalizar rapidamente ideias de interação em baixa fidelidade para explorar alternativas antes de investir em detalhes visuais. O valor da atividade está no **ciclo construir → simular → observar → revisar**, não na beleza do desenho.

## 1. Escopo do protótipo

**Personas:** P01 — Camila Rocha; P02 — Roberto Nunes; P03 — Marina Lopes.  
**Cenários/tarefas cobertos:** C01/T01 e T02; C03/T03; continuidade de C02 para P03.  
**Objetivos principais:** Explorar em papel o cadastro do tutor e do pet, o relato e a orientação pelo chat, a localização de clínicas no mapa e a consulta do resumo do caso pela clínica. O cadastro não deve impedir o acesso inicial à orientação. O painel da clínica será exploratório, associado às hipóteses H03 e H05.

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

## 2. Fluxos escolhidos

| Fluxo | Tarefa/objetivo | Por que foi priorizado |
|---|---|---|
| PF01 | Cadastrar tutor e pet: informar dados do tutor, nome, espécie e idade do pet; revisar e corrigir campos. Apoio à T01. | Associar o relato ao animal correto e explorar a validação dos dados, sem bloquear a orientação inicial. |
| PF02 | Usar o chat: selecionar o pet, relatar sinais, responder às perguntas e compreender a orientação e o próximo passo. T01 e T03. | É o fluxo central da pré-triagem; deve contemplar emergência, não emergência e informação insuficiente. |
| PF03 | Achar uma clínica no mapa: usar localização ou informar região, consultar dados da unidade, selecionar e iniciar contato. T02. | Transformar a orientação em busca de atendimento, sem confundir clínica listada com disponibilidade confirmada. |
| PF04 | Consultar o dashboard da clínica: abrir um caso compartilhado com autorização, ler o resumo e informar a possibilidade de atendimento. Continuidade de C02/P03. | Explorar a continuidade tutor–clínica prevista em H03 e H05, ainda sem tarefa própria detalhada na Entrega 5. |

## 3. Telas e estados

O protótipo foi explorado em duas formas. Os cartões em papel (`P01`…) estão em [`../assets/06_prototipos/`](../assets/06_prototipos/), com versão para impressão em [`Prototipo_E6_para_impressao.pdf`](../assets/06_prototipos/Prototipo_E6_para_impressao.pdf). Esta seção registra o **protótipo navegável do VetIA** (`D01`…), publicado em <https://vetia.chilecentral.cloudapp.azure.com/> e capturado em 04/11/2026. O lado do tutor foi capturado em visão de celular (375 × 812), contexto previsto para P01 (H08); o painel da clínica, em visão de computador (1280 × 800), contexto previsto para P03.

Todos os prints usam as contas acadêmicas compartilhadas do próprio sistema (`Ana (demo)` e `Plantão Aurora (demo)`), casos fictícios e unidades marcadas como fictícias. Nenhum dado real de tutor, animal ou clínica foi usado.

### 3.1 Mapa de estados

| ID | Tela/estado | Controle que muda o estado | Fluxo | Tarefa |
|---|---|---|---|---|
| D01 | Entrada: escolha entre tutor, clínica ou conta própria | "Entrar como tutor" → D08; "Entrar como clínica" → D25 | — | — |
| D02 | Menu do tutor | Nova conversa, Meus animais, Encontrar atendimento, Encaminhamentos | — | — |
| D03 | Meus animais, vazio | "Cadastrar animal" → D04 | PF01 | apoio a T01 |
| D04–D05 | Cadastro com só nome e espécie obrigatórios | "Salvar animal" → D06/D07; "Voltar" ou "×" cancela | PF01 | apoio a T01 |
| D06 | Lista logo após salvar (continuou vazia) | reabrir a página → D07 | PF01 | apoio a T01 |
| D07 | Lista com o animal cadastrado | "Editar informações" | PF01 | apoio a T01 |
| D08 | Conversa inicial; animal opcional ("Associar animal depois") | seletor de animal; atalhos de sinais; texto ou áudio; enviar → D10 | PF02 | T01 |
| D09 | Relato digitado, botão de envio ativo | enviar → D10 | PF02 | T01 |
| D10–D12 | Resultado de **possível emergência** com sinais identificados, ação principal, justificativa e referências | "Encontrar atendimento" → D13 | PF02 | T03 |
| D13 | Encontrar atendimento, antes da busca | endereço + "Buscar" ou "Usar minha localização" → D15 | PF03 | T02 |
| D14 | Unidades fictícias para testar a continuidade | "Compartilhar caso" → D18 | PF03/PF04 | T02 |
| D15 | Mapa e lista de clínicas públicas (Google), sem filtro | "Abertas agora" → D16 | PF03 | T02 |
| D16–D17 | Mapa e lista filtrados por "Abertas agora" | "Ligar", "Rota" | PF03 | T02 |
| D18–D19 | Revisar antes de enviar: relato editável e pré-triagem automática | edição do relato | PF03 | T02 |
| D20 | Autorização pendente: "Confirmar e compartilhar" desabilitado | marcar autorização → D21 | PF03 | T02 |
| D21 | Autorização marcada | "Confirmar e compartilhar" → D22 | PF03 | T02 |
| D22–D23 | Encaminhamento **Enviado** com histórico do caso | "Cancelar envio", "Ver outras clínicas" | PF03 | T02 |
| D24 | Conversa com pessoas (tutor ↔ clínica) | "Enviar" | PF03 | T02 |
| D25 | Painel da clínica: contadores e lista de casos | selecionar caso → D26 | PF04 | continuidade C02/P03 |
| D26–D27 | Caso na clínica: relato autorizado, pré-triagem, dados do animal | "Confirmar recebimento", "Aceitar caso", "Recusar" | PF04 | continuidade C02/P03 |
| D28 | Caso **Aceito** | "Registrar chegada" | PF04 | continuidade C02/P03 |
| D29–D30 | Resposta da clínica e painel atualizado | "Enviar" | PF04 | continuidade C02/P03 |
| D31–D32 | Tutor vê o encaminhamento **Aceito** | "Estou a caminho" → D33 | PF03 | T02 |
| D33–D35 | **A caminho**: oferta de compartilhar localização, histórico e resposta da clínica | "Autorizar e compartilhar", "Cancelar envio" | PF03 | T02 |
| D36 | Nova conversa já associada ao animal anterior | seletor de animal | PF02 | T01 |
| D37–D39 | Estado **INCERTO** ("Precisamos entender melhor") com pergunta complementar | responder ou contatar clínica | PF02 | T01/T03 |
| D40 | Justificativa e referências abertas | expandir/recolher | PF02 | T03 |
| D41–D42 | Orientação após o complemento | novo relato; "Ver clínicas" | PF02 | T03 |

### 3.2 Prints

**PF01 — Cadastro do animal**

<table>
<tr>
<td align="center"><img src="../assets/06_prototipos/D01_inicio.jpg" width="180"><br><sub>D01 Entrada</sub></td>
<td align="center"><img src="../assets/06_prototipos/D02_menu_tutor.jpg" width="180"><br><sub>D02 Menu do tutor</sub></td>
<td align="center"><img src="../assets/06_prototipos/D03_meus_animais_vazio.jpg" width="180"><br><sub>D03 Meus animais vazio</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D04_cadastro_animal.jpg" width="180"><br><sub>D04 Cadastro</sub></td>
<td align="center"><img src="../assets/06_prototipos/D05_cadastro_salvar.jpg" width="180"><br><sub>D05 Campos opcionais e salvar</sub></td>
<td align="center"><img src="../assets/06_prototipos/D06_lista_apos_salvar.jpg" width="180"><br><sub>D06 Lista logo após salvar</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D07_lista_com_bob.jpg" width="180"><br><sub>D07 Lista ao reabrir</sub></td>
<td></td><td></td>
</tr>
</table>

**PF02 — Relato e orientação (possível emergência)**

<table>
<tr>
<td align="center"><img src="../assets/06_prototipos/D08_chat_inicial.jpg" width="180"><br><sub>D08 Conversa inicial</sub></td>
<td align="center"><img src="../assets/06_prototipos/D09_relato_digitado.jpg" width="180"><br><sub>D09 Relato digitado</sub></td>
<td align="center"><img src="../assets/06_prototipos/D10_resultado_topo.jpg" width="180"><br><sub>D10 Início do resultado</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D11_resultado_emergencia.jpg" width="180"><br><sub>D11 Possível emergência</sub></td>
<td align="center"><img src="../assets/06_prototipos/D12_resultado_justificativa.jpg" width="180"><br><sub>D12 Justificativa e referências</sub></td>
<td></td>
</tr>
</table>

**PF03 — Encontrar atendimento e compartilhar o caso**

<table>
<tr>
<td align="center"><img src="../assets/06_prototipos/D13_encontrar_atendimento.jpg" width="180"><br><sub>D13 Antes da busca</sub></td>
<td align="center"><img src="../assets/06_prototipos/D14_unidades_ficticias.jpg" width="180"><br><sub>D14 Unidades fictícias</sub></td>
<td align="center"><img src="../assets/06_prototipos/D15_mapa_todas.jpg" width="180"><br><sub>D15 Sem filtro</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D16_mapa_abertas_agora.jpg" width="180"><br><sub>D16 Abertas agora (mapa)</sub></td>
<td align="center"><img src="../assets/06_prototipos/D17_lista_abertas_agora.jpg" width="180"><br><sub>D17 Abertas agora (lista)</sub></td>
<td align="center"><img src="../assets/06_prototipos/D18_revisar_envio.jpg" width="180"><br><sub>D18 Revisar antes de enviar</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D19_revisar_pretriagem.jpg" width="180"><br><sub>D19 Pré-triagem no envio</sub></td>
<td align="center"><img src="../assets/06_prototipos/D20_autorizacao_pendente.jpg" width="180"><br><sub>D20 Autorização pendente</sub></td>
<td align="center"><img src="../assets/06_prototipos/D21_autorizacao_marcada.jpg" width="180"><br><sub>D21 Autorização marcada</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D22_encaminhamento_enviado.jpg" width="180"><br><sub>D22 Enviado</sub></td>
<td align="center"><img src="../assets/06_prototipos/D23_historico_caso.jpg" width="180"><br><sub>D23 Histórico</sub></td>
<td align="center"><img src="../assets/06_prototipos/D24_mensagem_tutor.jpg" width="180"><br><sub>D24 Mensagem do tutor</sub></td>
</tr>
</table>

**PF04 — Painel da clínica**

<table>
<tr>
<td align="center"><img src="../assets/06_prototipos/D25_painel_clinica.jpg" width="280"><br><sub>D25 Painel</sub></td>
<td align="center"><img src="../assets/06_prototipos/D26_clinica_resumo_caso.jpg" width="280"><br><sub>D26 Resumo do caso</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D27_clinica_acoes.jpg" width="280"><br><sub>D27 Ações da clínica</sub></td>
<td align="center"><img src="../assets/06_prototipos/D28_clinica_caso_aceito.jpg" width="280"><br><sub>D28 Caso aceito</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D29_clinica_resposta.jpg" width="280"><br><sub>D29 Resposta ao tutor</sub></td>
<td align="center"><img src="../assets/06_prototipos/D30_painel_atualizado.jpg" width="280"><br><sub>D30 Painel atualizado</sub></td>
</tr>
</table>

**PF03 (continuação) — Tutor recebe a confirmação**

<table>
<tr>
<td align="center"><img src="../assets/06_prototipos/D31_tutor_encaminhamentos.jpg" width="180"><br><sub>D31 Encaminhamentos</sub></td>
<td align="center"><img src="../assets/06_prototipos/D32_tutor_aceito.jpg" width="180"><br><sub>D32 Aceito</sub></td>
<td align="center"><img src="../assets/06_prototipos/D33_tutor_a_caminho.jpg" width="180"><br><sub>D33 A caminho</sub></td>
</tr>
<tr>
<td align="center"><img src="../assets/06_prototipos/D34_tutor_localizacao_historico.jpg" width="180"><br><sub>D34 Localização e histórico</sub></td>
<td align="center"><img src="../assets/06_prototipos/D35_tutor_resposta_clinica.jpg" width="180"><br><sub>D35 Resposta da clínica</sub></td>
<td></td>
</tr>
</table>

**PF02 — Relato e orientação (informação insuficiente)**

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

**Data:** 30/10/2026 · **Versão:** protótipo navegável publicado · **Análise:** Gemini (nuvem), padrão do sistema · **Condução:** equipe.

A navegação seguiu as situações S01 e S02 do roteiro em [`instrumentos_simulacao.md`](../assets/06_prototipos/instrumentos_simulacao.md), com os casos fictícios de Bob (P01) e Nina (P02), percorrendo o caminho principal de cada caso, e não todas as telas do sistema. As mensagens do tutor foram escritas pela equipe; **as respostas do sistema citadas abaixo são as que o protótipo efetivamente produziu**, conferidas nos prints. Como a equipe conhece as telas, este walkthrough identifica problemas de fluxo e de estado, mas **não substitui a simulação com uma pessoa externa** pedida no enunciado, que continua pendente (ver Checklist). Não houve gravação de vídeo; os prints indicados entre parênteses são o registro.

### 4.1 Caso 1 — Bob, possível emergência (S01)

Com Bob já cadastrado, o tutor abriu uma nova conversa e escreveu: "O Bob está respirando muito rápido faz uns 20 minutos e a língua dele está com uma cor estranha, meio roxa. Ele está deitado e não quer levantar." (D09). O sistema respondeu que os sinais precisavam de avaliação veterinária agora, listou os sinais que identificou no relato (respiração rápida, língua roxa, não quer levantar) e mostrou o cartão **"Procure atendimento agora"**, com o botão "Encontrar atendimento" (D10–D11). No celular, porém, o cartão apareceu cortado: o seletor "Análise por" e o aviso sobre o Gemini ficam fixos na parte de baixo, ocupam cerca de metade da tela, e foi preciso rolar para chegar à ação principal (D10).

Ao tocar "Encontrar atendimento", o tutor buscou pela região da FEI. Sem filtro, os primeiros resultados foram um atendimento a domicílio fechado naquele momento e um pet shop (D15). Só depois de marcar "Abertas agora" um hospital veterinário 24 h, aberto e a 0,5 km, apareceu em primeiro lugar, com o aviso de que aquela é uma informação pública, sem encaminhamento pela plataforma (D16–D17).

Para testar a continuidade do caso, o tutor compartilhou o relato com o Hospital Veterinário Aurora, uma unidade fictícia do ambiente acadêmico. Antes do envio, o sistema mostrou o relato para revisão e só liberou "Confirmar e compartilhar" depois que a autorização foi marcada, lembrando que o envio não confirma uma vaga (D18–D21). Com o caso enviado, o tutor perguntou à clínica se podiam receber Bob (D22–D24).

No painel da clínica, o caso chegou com o relato autorizado pelo tutor e a pré-triagem identificada como "não é diagnóstico". Junto veio também a instrução dirigida ao tutor ("Procure um veterinário imediatamente, sem esperar"), que não faz sentido para a equipe que recebe o caso (D26). A clínica aceitou o caso e respondeu que podia receber Bob pela entrada do pronto-atendimento (D28–D29).

De volta ao celular, o encaminhamento aparecia como "Aceito", mas o texto principal continuava o mesmo de antes ("Você pode acompanhar a resposta da clínica…"); a confirmação só ficava clara ao rolar até a conversa (D32, D35). Ao tocar "Estou a caminho", o botão "Cancelar envio" passou a ocupar o mesmo lugar, já destacado, o que facilitaria cancelar o encaminhamento com um segundo toque (D33).

### 4.2 Caso 2 — Nina, informação insuficiente (S02)

Ao tocar "Nova conversa", o seletor já veio com Bob e o título "Como Bob está hoje?"; foi preciso trocar para "Associar animal depois" antes de relatar o caso de outro animal (D36). O tutor escreveu: "Minha gata Nina está comendo menos faz uns dois dias e está diferente, mais quieta. Não sei direito quando isso começou." (D37). O sistema respondeu que ainda faltavam informações para orientar a urgência e que isso não significa que esteja tudo bem, mostrou o cartão **"Precisamos entender melhor"**, reforçou que tudo bem responder que não sabe e perguntou "Quanto ele comeu em relação ao habitual?", tratando a gata no masculino (D38–D39).

O tutor respondeu: "Acho que menos da metade do normal, mas não tenho certeza. Ela não vomitou." A nova resposta repetiu a mesma abertura e o mesmo cartão. Os sinais identificados continuaram "comendo menos; mais quieta", sem a informação acrescentada, e a orientação final foi entrar em contato com uma clínica e procurar atendimento se houver piora (D41–D42).

### 4.3 Observações

| Observação | Tela/ação | Evidência | Consequência para o design |
|---|---|---|---|
| O resultado de emergência é claro e leva a uma ação. | D11 | Cartão "Procure atendimento agora" com instrução e botão "Encontrar atendimento". | Atende T03 e o desfecho de emergência. Manter. |
| No celular, o seletor "Análise por" e o aviso sobre o Gemini ficam fixos e ocupam cerca de metade da tela. | D10 | O cartão de resultado aparece cortado e exige rolagem; os termos "Gemini · nuvem" e "Ollama" não são explicados ao tutor. | Em emergência, a ação principal fica fora da vista, e o vocabulário contraria H06. Recolher o seletor após o primeiro envio ou levá-lo para configurações, com um aviso curto de privacidade. |
| Sem filtro, a busca prioriza um atendimento a domicílio fechado e um pet shop. | D15 | Ordem dos dois primeiros resultados. | Em emergência, o tutor pode perder tempo. Vir com "Abertas agora" ligado quando o resultado for emergência e destacar unidades 24 h (H10a/H10b). |
| A lista distingue informação pública de encaminhamento. | D17 | "Informações públicas · sem encaminhamento pela plataforma". | Evita confundir clínica listada com vaga confirmada (RC09). Manter. |
| O envio exige autorização explícita e avisa que não garante vaga. | D18–D21 | Botão desabilitado até marcar a autorização; aviso "O envio não confirma uma vaga". | Atende RC06 e a separação entre envio e confirmação. Manter. |
| O resumo enviado à clínica inclui a instrução dirigida ao tutor. | D26 | "Procure um veterinário imediatamente, sem esperar" no painel da clínica. | Mistura destinatários e confunde a origem da mensagem (H17). Mostrar à clínica apenas a classificação e o motivo. |
| Com o caso aceito, o tutor vê o selo "Aceito", mas o texto não muda. | D32 | Continua "Você pode acompanhar a resposta da clínica…". | A confirmação mais importante do fluxo fica só num selo pequeno. Trocar o texto para "A clínica confirmou que pode receber Bob". |
| Ao tocar "Estou a caminho", "Cancelar envio" assume a mesma posição e já destacado. | D32 → D33 | Posição dos botões antes e depois. | Risco de cancelar o encaminhamento em situação de pressa. Afastar "Cancelar envio" e pedir confirmação. |
| "Nova conversa" mantém o animal da conversa anterior. | D36 | Seletor com Bob ao iniciar o relato sobre Nina. | Risco de associar o relato ao animal errado. Iniciar sem animal ou perguntar qual animal. |
| O estado INCERTO comunica que falta informação e não equivale a "está tudo bem". | D38 | "Isso não significa que esteja tudo bem"; "tudo bem responder que não sabe". | Atende H13 e evita falsa segurança. Manter. |
| A pergunta complementar trata a gata como "ele". | D39 | "Quanto ele comeu…" após "Minha gata Nina…". | Reduz a sensação de ser compreendido. Usar o gênero do relato ou forma neutra ("o animal"). |
| Depois do complemento, a resposta repete o texto anterior e não reflete o que foi informado. | D41–D42 | Sinais identificados sem "menos da metade" nem "não vomitou"; mesma abertura e mesmo cartão. | O tutor não percebe que a resposta foi considerada e pode repetir ou abandonar (H12). Mostrar o que mudou e atualizar os sinais. |

## 5. Alterações após a simulação

As alterações abaixo são **decisões de revisão** derivadas do walkthrough. Ainda não foram implementadas no protótipo publicado; a coluna "Depois" descreve a próxima versão.

| Antes | Problema | Depois | Justificativa |
|---|---|---|---|
| Seletor de modelo e aviso fixos acima da caixa de texto (D10). | Ocupam metade da tela do celular e escondem a ação principal do resultado. | Aviso de privacidade curto no primeiro envio; escolha de processamento em configurações. | Ação principal visível em emergência (T03); linguagem simples (H06). |
| Busca de clínicas sem filtro (D15). | Prioriza unidade fechada e pet shop. | "Abertas agora" ligado por padrão quando o resultado for emergência; 24 h destacadas. | Reduz o tempo até achar atendimento adequado (T02, H10a/H10b). |
| Resumo da clínica com a instrução dirigida ao tutor (D26). | Destinatários misturados. | Clínica vê apenas a classificação e o motivo. | Origem clara das mensagens (H17). |
| Selo "Aceito" com texto genérico (D32). | Confirmação da clínica pouco visível. | Mensagem explícita: "A clínica confirmou que pode receber Bob", com a resposta da equipe em destaque. | Distinguir envio de confirmação, decisão já registrada na E5. |
| "Cancelar envio" na posição do botão "Estou a caminho" (D33). | Toque acidental pode cancelar o encaminhamento. | Botão de cancelar afastado, em estilo secundário e com confirmação. | Prevenção de erro em situação de pressa (P01). |
| Nova conversa herda o animal anterior (D36). | Relato pode ser associado ao animal errado. | Nova conversa começa em "Associar animal depois" ou pergunta qual animal. | Evita dados errados no caso e no resumo. |
| Pergunta complementar com gênero errado (D39). | Linguagem distante do tutor. | Gênero do relato ou forma neutra. | Linguagem simples (H06). |
| Resposta ao complemento igual à anterior (D41). | Tutor não vê efeito da sua resposta. | Mostrar sinais atualizados e o que ainda falta. | Progresso deve refletir informação nova, não número de mensagens (E5, T01; H12). |

Mantidos sem alteração: cartão de emergência com ação direta, estado INCERTO sem falsa segurança (H13), aviso de informação pública na lista de clínicas e autorização explícita antes do envio.

## Checklist

- [x] O protótipo cobre tarefas relevantes da Entrega 5.
- [x] Cada tela/estado pode ser justificado por uma tarefa, decisão ou informação necessária.
- [x] O projeto não criou dashboard/CRUD/login apenas para parecer “completo”. O painel da clínica (PF04) é exploratório e está ligado a H03/H05.
- [x] Telas/estados estão numerados e navegáveis na documentação.
- [x] Há pelo menos uma simulação/walkthrough documentado. Walkthrough da equipe (seção 4); a simulação com pessoa externa ainda está pendente.
- [x] Críticas não foram apenas listadas: geraram decisão de revisão.
- [ ] O protótipo continua em baixa fidelidade; detalhes visuais não mascaram problemas de fluxo. Os cartões em papel são de baixa fidelidade; o protótipo navegável é de alta fidelidade, e por isso o walkthrough se concentrou em fluxo e estados.
