# Teste VetIA — Roteiro do moderador e do operador da clínica

Plano: [Entrega 12](../docs/12_planejamento_avaliacao.md). Leia as falas **como estão escritas**, para que as três sessões sejam comparáveis.

**Duração prevista:** ~50 min (abertura 8 · pré-teste 3 · tarefas 30 · pós-teste 7 · encerramento 2).

## 1. Antes da sessão (checklist — 1 h antes)

**Aparelho de teste (smartphone da equipe)**

- [ ] Bateria > 80%, brilho alto, notificações silenciadas.
- [ ] **Modo avião ativado e Wi-Fi ligado** (impede ligação real a clínicas do mapa).
- [ ] Chrome com dados e **permissões do site limpos** (localização volta a ser pedida).
- [ ] Protótipo aberto em <https://vetia.chilecentral.cloudapp.azure.com/>, na tela de entrada (D01), deslogado.
- [ ] Gravação de tela com áudio do microfone testada (iniciar só após o consentimento).

**Conta e dados**

- [ ] Conta `Ana (demo)` reiniciada: sem animais, sem conversas anteriores, sem encaminhamentos (responsável: Julian).
- [ ] Painel `Plantão Aurora (demo)` sem casos pendentes.
- [ ] Provedor de análise em **"Gemini · nuvem"**.
- [ ] Fluxo completo testado com o caso do Bob: orientação aparece e envio ao Hospital Aurora funciona.

**Materiais**

- [ ] 2 vias do termo de consentimento, caneta.
- [ ] Cartões 0–6 impressos, em ordem, virados para baixo.
- [ ] Questionários e planilha de observação com o ID do participante (U01/U02/U03).
- [ ] Cronômetro do observador; água.

**Operador da clínica (notebook)**

- [ ] Logado como `Plantão Aurora (demo)` no painel, fora do campo de visão do participante.
- [ ] Mensagem de resposta copiada (seção 6).
- [ ] Celular por perto para receber o sinal do moderador.

## 2. Abertura (ler)

> "Obrigado por vir. Meu nome é ___ e esse é ___, que vai fazer anotações. Estamos testando um aplicativo, ainda em fase de protótipo, que ajuda tutores de cães e gatos a entender se o que o animal está apresentando pode ser grave e qual o próximo passo.
>
> Quero deixar claro: **estamos avaliando o aplicativo, não você.** Se algo for difícil, é um problema do aplicativo, e isso é exatamente o que queremos descobrir.
>
> O aplicativo gera orientações automáticas de verdade, mas todas as situações de hoje são inventadas. Não vamos avaliar se a orientação está clinicamente certa — isso é estudado em outra parte do trabalho. Queremos ver como é usar o aplicativo.
>
> Algumas situações envolvem um animal passando mal. Se em algum momento você não quiser continuar, é só dizer, sem precisar explicar."

Entregar o termo, ler em voz alta, responder dúvidas. Perguntar **separadamente**:

> "Você autoriza a gravação da tela do celular e da sua voz? Não gravamos o seu rosto. Se preferir, fazemos só com anotações."

Assinatura → iniciar a gravação (se autorizada) → dizer o ID em voz alta ("Sessão U0_, data ___").

## 3. Pré-teste

Aplicar o bloco **Pré-teste** de [`teste_vetia_questionarios.md`](teste_vetia_questionarios.md).

## 4. Instruções gerais (ler)

> "Vou te dar alguns cartões, um de cada vez. Cada um descreve uma situação. Faça o que faria na vida real usando o aplicativo neste celular. Pode reler o cartão quando quiser. Avise quando achar que terminou.
>
> Enquanto você faz, eu vou ficar mais em silêncio e não vou poder dizer onde tocar — isso faz parte do teste. Depois de cada situação, vou fazer uma ou duas perguntas rápidas.
>
> Use só as informações dos cartões. **Não escreva nomes, endereços ou dados reais**, porque o texto é enviado para um serviço de inteligência artificial."

Entregar o **Cartão 0**, deixar ler e entregar o celular na tela D01.

## 5. Tarefas

Para cada tarefa: entregar o cartão → observador marca o início quando o participante tocar na tela → observar sem ajudar → marcar o fim → perguntas de compreensão (quando houver) → escala pós-tarefa → "O que tornou isso fácil ou difícil?".

| Tarefa | Cartão | Logo depois da tarefa | O moderador **pode** esclarecer (nível 1) | O moderador **não deve** dizer |
|---|---|---|---|---|
| UT01 | 1 | **CMP-1:** "Com suas palavras: o que o aplicativo disse sobre o Bob e o que você faria agora?" | quem é o Bob; que pode escrever como falaria | "entre como tutor", "cadastre o animal", "use o chat", nome de qualquer botão |
| UT02 | 2 | — | onde fica a FEI; que não precisa ligar | "Encontrar atendimento", "Abertas agora", "use o mapa" |
| UT03 | 3 | **CMP-2:** "Neste momento, o Bob já tem atendimento garantido no hospital? Como você sabe?" → em seguida, **enviar o sinal ao operador** | que o Hospital Aurora é fictício e é o único que recebe casos pelo app | "Compartilhar caso", "Confirmar e compartilhar", "edite o resumo", "desmarque a caixa" |
| UT04 | 4 (entregar só depois que o operador confirmar o envio, ou após 1 min) | **CMP-3:** "Quem escreveu a última mensagem que você leu: o aplicativo ou alguém do hospital? Como percebeu?" | que alguns minutos se passaram | "Encaminhamentos", "Estou a caminho", "abra o menu" |
| UT05 | 5 | **CMP-4:** "Com suas palavras: o que o aplicativo concluiu sobre a Nina e o que você faria agora?" | que a Nina é outro animal, não o Bob | "Nova conversa", "responda à pergunta", "pode dizer que não sabe" |
| UT06 | 6 | **CMP-5:** "Com suas palavras: o que você faria com a Nina a partir de agora?" | — | — |

**Ajudas** (registrar nível na planilha):

- Nível 1 — esclarecer o cenário: permitido, não conta como ajuda.
- Nível 2 — só depois de 2 min de travamento **e** pedido do participante: "Onde você imagina que isso estaria?" e, se necessário, "Talvez haja algo no menu / no alto da tela". Conta como ajuda.
- Nível 3 — indicar o controle: só quando o tempo-limite estourar e a tarefa seguinte depender desta (UT03 → UT04). A tarefa é falha.

**Tempos-limite** (tempo de interação, espera do modelo descontada): UT01 6 min · UT02 5 min · UT03 6 min · UT04 4 min · UT05 8 min · UT06 4 min. Ao estourar: "Obrigado, vamos para a próxima situação."

**Durante a espera da análise:** não comentar. Observador anota toques repetidos ou reenvio.

**Se a orientação exibida for diferente da esperada** (ex.: Bob não aparece como possível emergência): não comentar; seguir a tarefa; adaptar o reconto ao que apareceu; anotar "nota técnica TCC" na planilha.

**Se o discador abrir** em UT02: "Pode voltar ao aplicativo", e anotar como comportamento.

## 6. Roteiro do operador da clínica (UT04)

Ao receber o sinal do moderador (após CMP-2):

1. No painel `Plantão Aurora (demo)`, abrir o caso do Bob.
2. **Aceitar** o caso.
3. Enviar exatamente esta mensagem:

   > Boa noite! Podemos receber o Bob agora. Venha direto pela entrada do pronto-atendimento.

4. Avisar o moderador ("ok") pelo celular.
5. Se o participante enviar mensagem ou marcar que está a caminho, **não responder** (a tarefa termina na comunicação da saída).
6. Não recusar o caso nem enviar outras mensagens. O estado "recusado" não é testado nesta rodada.

## 7. Pós-teste

Aplicar o bloco **Pós-teste** de [`teste_vetia_questionarios.md`](teste_vetia_questionarios.md) (escala de confiança + entrevista curta).

## 8. Encerramento e *debriefing* (ler)

> "Terminamos. Muito obrigado. Algumas informações importantes:
>
> As orientações que você viu são automáticas, de um projeto acadêmico, e **podem errar**. Elas **não substituem um veterinário**. Numa situação real com seu animal, procure atendimento.
>
> O Hospital Aurora não existe, e nenhuma mensagem foi enviada para clínicas reais.
>
> Seus dados aparecem só como U0_. A gravação fica numa pasta restrita da equipe e será apagada depois da análise, até o fim do semestre. Ficou alguma dúvida?"

Parar a gravação → conferir que a planilha está completa → transferir a gravação para a pasta restrita **no mesmo dia** → guardar o termo assinado separado das planilhas → reiniciar conta e aparelho para a próxima sessão.

## 9. Logo após a sessão (moderador + observador, 10 min)

- Registrar as 3 observações mais marcantes e qualquer desvio do roteiro.
- Anotar a classificação que o modelo exibiu em UT01, UT05 e UT06.
- Anotar problemas técnicos (lentidão, erro, servidor).
