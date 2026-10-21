# Entrega 7 — Coleta de dados, necessidades e aspectos éticos

**Data:** 21/10/2026  
**Status:** 🟨 em andamento

## Objetivo da atividade

Planejar dados necessários para compreender usuários e requisitos de IHC, escolher técnicas adequadas e documentar instrumentos de modo que a aplicação possa ser reproduzida por pessoas diferentes.

## Para escopos de IHC derivados de TCC técnico

Quando o usuário e a interface foram propostos pela disciplina, uma prioridade da coleta é investigar se esse **cenário de uso realmente faz sentido**. Não trate o exercício de comercialização da Entrega 1 como validação de mercado.

Perguntas úteis incluem:

- esse perfil realmente realiza a atividade imaginada?
- quais ferramentas usa hoje?
- quais informações consulta?
- quais decisões toma?
- que vocabulário utiliza?
- quais parâmetros compreende e quais deveriam ser abstraídos?
- precisa de dashboard, histórico, filtros, relatórios ou comparação? Por quê?
- quais erros são frequentes e quais são críticos?
- existem papéis/permissões diferentes?
- que resultados do algoritmo/modelo seriam úteis ou difíceis de interpretar?

Quando o acesso ao perfil profissional for difícil, discuta com o docente alternativas metodológicas (especialistas próximos, dados secundários, literatura, participantes proxy) e registre as limitações. **Não esconda a limitação da amostra.**

## Hipóteses e lacunas prioritárias herdadas da Entrega 1

Antes de decidir “que dados coletar”, retome os itens `[H]` e `[?]` da Entrega 1 e o registro de hipóteses em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md). A coleta deve responder perguntas reais do projeto, e não apenas produzir um formulário porque a técnica foi solicitada.

| ID | Hipótese/lacuna | Evidência atual | Decisão que depende da resposta | Prioridade |
|---|---|---|---|---|
| H07/L05 | Quais recursos os tutores usam para buscar orientação? | A E2 descreve alternativas; o uso pelo público ainda não foi investigado. | Priorizar caminhos compatíveis com as práticas atuais. | alta |
| H06/H08 | Quais dispositivos e dificuldades influenciam essa busca? | Contextos e necessidades das personas ainda são hipóteses. | Ajustar linguagem, apresentação e interação. | alta |
| H10a/H10b/H10c | Quais critérios importam na escolha de uma clínica? | O mapa existe no TCC, mas os critérios do público permanecem abertos. | Selecionar informações relevantes para mapa e lista. | alta |
| H09/H12 | Quando voz e perguntas complementares ajudam ou dificultam o relato? | Recursos documentados no TCC, sem confirmação de utilidade com tutores. | Rever formas de entrada e complementação. | média |
| H14 | Como o tutor percebe o cadastro antes do relato urgente? | Fluxo previsto na E6; possível atrito ainda não investigado. | Rever a posição do cadastro. | alta |
| H02/H13 | Como o tutor entende uma mensagem de não emergência? | Risco de falsa segurança previsto, sem coleta concluída. | Rever texto e próximo passo. | alta |
| H03/H05/L02 | O resumo e o painel atendem à rotina da clínica? | Funcionalidades no TCC não comprovam necessidade profissional. | Investigar com profissionais nas demais contribuições; este questionário não resolve essa questão. | alta |

## Parte A — necessidades e requisitos de IHC

> **Responsabilidade:** solução individual por integrante.

### A01 — Vinicius de Castro Duarte

**Autor(a):** Vinicius de Castro Duarte — 22.224.020-2

#### Que dados coletar?

| Dado/informação | Hipótese/lacuna relacionada | Por que é necessário | Qual decisão de design pode afetar |
|---|---|---|---|
| Práticas de busca e dificuldades relatadas. | H07/L05 e H06 | Conhecer o processo atual, sem pressupor uso de chatbot. | Canais, linguagem e ajuda. |
| Dispositivo preferido e barreiras de uso. | H08/H06 | Identificar condições relevantes de interação. | Prioridade de dispositivo e apresentação. |
| Critérios para escolher uma clínica. | H10a/H10b/H10c | Distinguir proximidade, horário e disponibilidade. | Conteúdo do mapa/lista. |
| Preferência por texto/voz e motivos para interromper perguntas. | H09/H12 | Investigar utilidade percebida e esforço. | Entrada de dados e complemento do relato. |
| Expectativa sobre cadastro e interpretação de não emergência. | H14 e H02/H13 | Identificar atrito percebido e possível falsa segurança. | Posição do cadastro e mensagem de resultado. |

#### De quem coletar?

| Perfil/stakeholder | Critério de inclusão | Relação com persona/público |
|---|---|---|
| Tutores de cães ou gatos. | Ter 18 anos ou mais, participar do cuidado do animal e aceitar voluntariamente a pesquisa. | Público principal representado por P01 e P02. Recrutamento por conveniência; resultados limitados aos respondentes. |

#### Aspectos éticos

Analise voluntariedade, consentimento, minimização de dados, privacidade, riscos, gravação, anonimização, armazenamento e descarte. Não responda apenas “sim, por causa da LGPD”: explique **quais dados e riscos existem neste projeto**.

A participação será voluntária, com consentimento no início do formulário online e possibilidade de pular perguntas ou sair antes do envio. Não serão solicitados nome, e-mail, contato ou dados identificáveis do tutor, animal ou clínica; a coleta automática de e-mail será desativada. Não haverá gravações. Para reduzir exposição ou desconforto, as respostas abertas deverão omitir dados pessoais e poderão ficar em branco. As respostas terão acesso restrito à equipe, os resultados serão apresentados sem identificação e os registros individuais serão excluídos ao encerrar a atividade.


> Repita A02, A03...

## Parte B — ferramentas de coleta

> Cada integrante deve preparar uma técnica/instrumento completo. As técnicas devem ser diferentes entre si e **questionário deve estar entre as técnicas escolhidas**, conforme o enunciado da disciplina.

### Instrumento I01 — Questionário online para tutores

**Autor(a):** Vinicius de Castro Duarte — 22.224.020-2  
**Técnica:** questionário em formulário online  
**Objetivo:** Conhecer práticas e dificuldades de tutores para orientar cadastro, chat e busca de clínicas.  
**Público:** Tutores adultos de cães/gatos, relacionados a P01 e P02.

#### Procedimento padronizado de aplicação

1. Criar o formulário com o texto abaixo, desativar coleta de e-mail e exigência de login e conferir o funcionamento antes de divulgar.
2. Apresentar finalidade, cuidados com os dados e consentimento. Encerrar o formulário se a pessoa não atender aos critérios ou não aceitar participar.
3. Compartilhar o link com tutores adultos. Manter a ordem das perguntas; após o consentimento, todas serão opcionais. Não é necessário usar o VetIA.
4. Ao concluir, agradecer e permitir o envio, sem exigir respostas faltantes.
5. Reunir as respostas em acesso restrito e preparar uma síntese sem identificação, seguindo os cuidados descritos acima.

#### Instrumento

Cole aqui o questionário/roteiro completo ou forneça link **mais uma cópia textual no repositório**.

**Apresentação e consentimento**

Este formulário acadêmico busca entender como tutores procuram orientação e atendimento para cães e gatos. Participar é voluntário; você pode pular perguntas ou sair antes de enviar. Não informe dados que identifiquem pessoas, animais ou clínicas. Não haverá gravações. As respostas serão acessadas apenas pela equipe e apresentadas sem identificação; os registros individuais serão excluídos ao encerrar a atividade. Este formulário não oferece atendimento veterinário.

**Você tem 18 anos ou mais, participa do cuidado de um cão/gato e aceita participar?**

( ) Sim. ( ) Não — encerrar sem seguir para as perguntas.

**1. Quando precisa de orientação sobre a saúde do animal, a quais recursos costuma recorrer?** Marque todas as opções aplicáveis.

[ ] Ligação para clínica/profissional [ ] Mensagens [ ] Busca na internet [ ] Mapas online [ ] Redes sociais [ ] Pessoas conhecidas [ ] Chatbot/aplicativo [ ] Ida direta à clínica [ ] Outro: ____ [ ] Nunca precisei.

“Nunca precisei” deve ser marcada sozinha.

**2. Se já buscou orientação ou atendimento, qual foi a principal dificuldade, se houve?** Não identifique o animal ou a clínica. Pode responder “nenhuma” ou “não se aplica”.

Resposta curta: ____

**3. Qual dispositivo você usaria primeiro nessa busca?**

( ) Celular ( ) Computador ( ) Tablet ( ) Pediria ajuda a alguém ( ) Outro: ____ ( ) Não sei.

**4. Quais dificuldades poderiam atrapalhar o uso de um site nessa situação?** Marque todas as opções aplicáveis.

[ ] Conexão instável [ ] Cuidar do animal ao mesmo tempo [ ] Ler na tela [ ] Digitar [ ] Compreender termos [ ] Outra: ____ [ ] Nenhuma [ ] Não sei.

“Nenhuma” e “Não sei” devem ser marcadas sozinhas.

**5. Quais seriam os três critérios mais importantes para escolher uma clínica?** Marque até três.

[ ] Proximidade [ ] Confirmação de que pode receber agora [ ] Funcionamento 24 horas [ ] Capacidade de atender o tipo de caso [ ] Já conhecer a clínica [ ] Custo [ ] Outro: ____ [ ] Não sei.

“Não sei” deve ser marcada sozinha.

**6. Para relatar o que está acontecendo, você preferiria texto ou voz? Por quê? Se escolhesse voz, precisaria conferir o texto transcrito?**

Resposta curta; pode indicar “depende”, “nenhuma” ou “não sei”: ____

**7. O que faria você parar de responder às perguntas de um chat sobre o animal?**

Resposta curta; pode indicar “não sei”: ____

**8. Em uma situação urgente, como você preferiria que o cadastro fosse apresentado?**

( ) Antes de relatar o problema ( ) Depois de relatar o problema ( ) Sem preferência ( ) Outra opção: ____ ( ) Não sei.

**9. Leia esta mensagem fictícia: “Com as informações relatadas, não foi identificada indicação de emergência. Isso não é um diagnóstico. Observe a evolução e procure avaliação veterinária se houver piora, novos sinais ou dúvida.” O que você entende e qual seria seu próximo passo?**

Resposta curta: ____

**10. Há algo importante para buscar orientação ou escolher uma clínica que não perguntamos?**

Resposta opcional: ____

**Encerramento:** Obrigado pela participação. A mensagem apresentada é fictícia e não avalia a saúde do seu animal.


#### Como os dados serão analisados

As respostas fechadas serão resumidas por contagens, informando quantas pessoas responderam a cada item. Nas questões com várias escolhas, o total poderá ultrapassar o número de participantes. Respostas vazias não serão tratadas como “não”.

As respostas abertas serão agrupadas por temas, como dificuldades, linguagem, voz, cadastro e compreensão. Na questão 9, será verificado se a pessoa distingue “não foi identificada emergência” de “não precisa observar ou procurar avaliação”. Interpretações divergentes orientarão revisão do texto, sem avaliar acerto clínico.

A ligação com as hipóteses será: questões 1–2 → H07/L05; 3–4 → H08/H06; 5 → H10a/H10b/H10c; 6 → H09; 7 → H12; 8 → H14; 9 → H02/H13. A questão 10 poderá revelar necessidades não previstas. A síntese registrará o número real de respostas e as limitações da amostra por conveniência. Preferência declarada não comprova desempenho ou redução de tempo.

## Síntese

Explique quais lacunas de conhecimento sobre usuários o conjunto de técnicas pretende reduzir. Indique explicitamente quais hipóteses da Entrega 1 deverão ficar **sustentadas, refutadas ou refinadas** após a análise dos dados. Quando os dados forem coletados/analisados, atualize o histórico em `RASTREABILIDADE.md`.

Esta versão contém apenas a contribuição do Vinicius até o momento. O instrumento será um formulário online; aqui está seu planejamento e sua cópia textual, sem aplicação ou resultados declarados.

A coleta pretende refinar H07, H08, H06, H09, H10a/H10b/H10c, H12, H14 e H02/H13, além de L05. Após a análise, será indicado quais hipóteses ficaram sustentadas, refutadas ou refinadas no alcance das respostas. O questionário não comprova efeitos sobre tempo, segurança clínica ou utilidade do dashboard para profissionais. H03/H05/L02 continuam dependentes de investigação com a clínica.

O planejamento considera as personas P01/P02, as tarefas T01–T03 e os fluxos da E6, em conjunto com o [TCC](https://github.com/vinizika/tcc), sua [documentação funcional](https://github.com/vinizika/tcc/blob/main/docs/poc-utilizavel.md) e a [rastreabilidade](../RASTREABILIDADE.md). A entrega permanece em andamento, aguardando as contribuições e técnicas distintas dos demais integrantes.


## Checklist

- [x] Hipóteses/lacunas prioritárias da Entrega 1 foram revisitadas.
- [x] Se o escopo de IHC foi derivado de TCC técnico, a coleta investiga a plausibilidade do usuário, tarefa e contexto adotados.
- [x] Perguntas não pressupõem que dashboard, CRUD, filtros ou relatórios sejam necessários; investigam a necessidade.
- [x] Cada dado a coletar responde uma dúvida concreta do projeto ou justifica outra necessidade de informação.
- [x] Parte A identifica dados e perfis de coleta de forma específica.
- [x] Aspectos éticos são contextualizados para o projeto.
- [ ] Há uma técnica completa por integrante e técnicas distintas.
- [x] Questionário está incluído entre as técnicas.
- [x] Cada instrumento possui objetivo, público, procedimento e conteúdo integral.
- [x] Perguntas evitam indução e coletam apenas dados necessários.
- [x] Está claro como os dados serão analisados e usados no design.

