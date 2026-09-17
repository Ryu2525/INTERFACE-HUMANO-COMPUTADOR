# Entrega 4 — Cenários de análise/problema

**Data:** 17/09/2026  
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 solução completa por integrante

## Objetivo da atividade

Descrever situações atuais em que o usuário tenta alcançar um objetivo e encontra dificuldades. O cenário de análise/problema deve tornar visível **o contexto, os atores, as ações e as rupturas**, sem antecipar a interface que será projetada.

> **Regra central:** cenário de problema é a “história do problema”. Se o texto já diz “o sistema mostra”, “o aplicativo resolve” ou descreve botões/telas futuras, provavelmente está misturando problema com solução.

Sempre que possível, o cenário deve aprofundar uma **situação concreta já registrada na Entrega 1**.

### Quando o TCC não possuía interface

O cenário continua sendo uma história de **problema/atividade humana**, não uma história do futuro sistema. Descreva como o profissional realiza hoje uma atividade semelhante ou como lida atualmente com dados, resultados, configurações, logs, decisões e limitações que o tema do TCC pretende apoiar.

Exemplo: em vez de “o DBA abre o novo dashboard e executa o algoritmo”, descreva “o DBA precisa investigar uma consulta lenta, reúne informações em ferramentas distintas, compara planos manualmente e tem dificuldade para estimar o impacto de uma mudança”.

A interface da disciplina aparecerá somente depois, nos cenários de interação.

Se o integrante escolher um novo problema/situação, explique por que ele passou a ser relevante e indique a evidência que motivou sua inclusão.

## Cenário C01 — Compreensão da gravidade e busca de orientação durante uma possível emergência veterinária noturna

**Autor(a):** Julian Ryu Takeda — 22.224.030-1  
**Persona(s) relacionada(s):** P01  
**Necessidade relacionada:** R01  
**Situação concreta da Entrega 1 relacionada:** seção 4.5 e H01  
**Hipóteses ainda presentes:** H01, H02, H04, H06, H07 e H08

### 1. Cenário inicial

Durante a madrugada, Camila percebe que Bob, seu cão, está ofegante, mais quieto do que o normal e com a língua em uma coloração diferente. Ela está sozinha em casa, precisa continuar observando o animal e não possui conhecimento veterinário para avaliar se os sinais podem esperar até a manhã seguinte ou se exigem deslocamento imediato até um hospital veterinário. Camila tenta organizar mentalmente o que mudou, quando os sinais começaram e como descrevê-los, mas não conhece os termos clínicos correspondentes.

Sem conseguir contato profissional imediato, ela faz buscas pelo celular usando palavras cotidianas, alterna entre páginas com explicações de diferentes níveis de detalhe e credibilidade e tenta comparar as descrições encontradas com o estado de Bob. Algumas informações parecem alarmantes, enquanto outras sugerem apenas observação, e Camila não sabe quais fontes considerar confiáveis. Ao mesmo tempo, precisa decidir se chama alguém para ajudá-la, como transportará Bob e para qual clínica poderá ir. A dificuldade de interpretar as informações aumenta sua ansiedade e prolonga a tomada de decisão. Se subestimar a gravidade, poderá atrasar o atendimento; se interpretar sinais inespecíficos como confirmação de uma emergência, poderá realizar um deslocamento desnecessário e aumentar ainda mais sua preocupação.

### 2. Questões de refinamento

Use os tipos de questões/taxonomia definidos na aula. As perguntas devem revelar informações **ainda ausentes** do cenário, não repetir o que já foi respondido.

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q1 | Quais palavras Camila utiliza para descrever a alteração respiratória e a mudança de coloração, e quais sinais ela consegue observar sem orientação profissional? | A linguagem utilizada e a capacidade de observação influenciam a forma como ela busca informação e comunica o caso. | Entrevistas com tutores e atividade de descrição de casos simulados, sem exigir terminologia clínica. |
| Q2 | Quais alternativas Camila considera antes de decidir pelo deslocamento e em que ordem tenta utilizá-las? | É necessário compreender seu planejamento atual, os pontos de hesitação e as dependências entre busca, contato, transporte e escolha da clínica. | Entrevistas semiestruturadas e mapeamento retrospectivo da jornada de tutores. |
| Q3 | Quais recursos e limitações estão presentes durante a madrugada, como apoio de outra pessoa, iluminação, conexão e meio de transporte? | O ambiente pode facilitar ou dificultar a observação do animal, a busca de orientação e a execução da decisão. | Investigação contextual, questionário e entrevistas com tutores. |
| Q4 | Que indícios Camila utiliza para julgar se uma orientação encontrada é confiável e se já possui informação suficiente para agir? | O cenário ainda não explica como ela avalia as fontes nem quando considera encerrada a busca. | Entrevistas e teste exploratório com fontes atualmente disponíveis. |

### 3. Cenário refinado

Reescreva o cenário incorporando as respostas. Marque o conteúdo novo de forma consistente (por exemplo, `**[NOVO: ...]**`).

Durante a madrugada, Camila percebe que Bob, seu cão, está ofegante, mais quieto do que o normal e com a língua em uma coloração diferente. Ela está sozinha em casa, precisa continuar observando o animal e não possui conhecimento veterinário para avaliar se os sinais podem esperar até a manhã seguinte ou se exigem deslocamento imediato até um hospital veterinário. **[NOVO: Camila descreve o que vê com expressões como “respirando muito rápido”, “sem querer levantar” e “língua meio roxa”, sem saber quais detalhes são clinicamente relevantes (Q1, hipótese H06).]**

Sem conseguir contato profissional imediato, ela faz buscas pelo celular usando essas mesmas palavras cotidianas. **[NOVO: Primeiro compara resultados de busca, depois tenta telefonar para uma clínica conhecida e, caso não consiga resposta, considera pedir ajuda a um familiar para transportar Bob (Q2, hipótese H07).]** Ela alterna entre páginas com explicações de diferentes níveis de detalhe e credibilidade e tenta comparar as descrições encontradas com o estado do animal. Algumas informações parecem alarmantes, enquanto outras sugerem apenas observação. **[NOVO: A pouca iluminação, a atenção dividida entre o celular e Bob, a ausência de outra pessoa em casa e a incerteza sobre transporte tornam a busca mais difícil (Q3, hipótese H08).]** Camila também precisa decidir para qual clínica poderá ir e se o local está funcionando naquele horário. **[NOVO: Ela tende a confiar mais em conteúdos que identificam uma instituição ou um profissional, mas não possui critérios suficientes para comparar recomendações conflitantes e continua buscando confirmação (Q4, hipótese H07).]** A dificuldade de interpretar as informações aumenta sua ansiedade e prolonga a tomada de decisão. Se subestimar a gravidade, poderá atrasar o atendimento; se interpretar sinais inespecíficos como confirmação de uma emergência, poderá realizar um deslocamento desnecessário e aumentar ainda mais sua preocupação.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | Camila, tutora de Bob e responsável pela decisão inicial; um familiar e a clínica aparecem como possíveis atores de apoio. |
| Objetivo(s) | Compreender a possível gravidade dos sinais e decidir se precisa procurar atendimento imediato. |
| Contexto | Residência durante a madrugada, possível ausência de apoio imediato e atenção dividida entre observar o animal e procurar orientação. |
| Recursos/informações | Celular, mecanismos de busca, páginas on-line, telefone de clínica, observações sobre os sinais de Bob e possível ajuda de um familiar. |
| Ações | Observar Bob, descrever os sinais, pesquisar termos, comparar páginas, telefonar, procurar ajuda e avaliar alternativas de atendimento. |
| Problemas/rupturas | Diferença entre linguagem leiga e clínica, informações divergentes, dificuldade para avaliar a credibilidade das fontes, falta de contato imediato e pressão emocional. |
| Consequências | Possível atraso em um caso grave, deslocamento desnecessário, comunicação incompleta com a clínica e aumento da ansiedade. |

### 5. Implicações para as próximas entregas

As tarefas de observar e relatar sinais, compreender uma orientação, decidir o próximo passo e procurar atendimento merecem análise. Ainda precisam ser coletadas informações sobre como tutores descrevem sinais respiratórios, quais fontes consultam, quais critérios usam para confiar em uma orientação e como as condições do ambiente afetam a sequência de ações. As hipóteses relacionadas devem permanecer abertas, pois o cenário não constitui validação empírica.

## Cenário C02 — Recebimento fragmentado de informações antes da chegada de um possível caso emergencial

**Autor(a):** Vinícius de Castro Duarte — 22.224.020-2  
**Persona(s) relacionada(s):** P03  
**Necessidade relacionada:** R05  
**Situação concreta da Entrega 1 relacionada:** seções 3.2, 4.3 e 5.4; atividade A06  
**Hipóteses ainda presentes:** H03 e H05

### 1. Cenário inicial

Marina é médica-veterinária plantonista em um hospital veterinário que atende durante a noite. Enquanto acompanha outros animais, uma atendente recebe a ligação de um tutor preocupado com um cão que apresenta dificuldade para respirar. O tutor relata os sinais sem uma ordem definida, alternando observações atuais, informações do histórico e dúvidas sobre o que deve fazer. A atendente registra parte do relato enquanto também precisa responder a outras pessoas e verificar com a equipe se existe possibilidade de receber o animal.

Quando a informação chega a Marina, alguns dados estão distribuídos entre anotações, uma conversa por telefone e uma mensagem encaminhada. Ela tenta identificar rapidamente quais sinais foram observados diretamente pelo tutor, quando começaram, como evoluíram e quais dados ainda não foram informados. Como o relato foi recontado por outra pessoa, Marina não consegue distinguir com segurança o que foi dito originalmente, o que foi resumido e o que resultou da interpretação de quem recebeu a ligação.

Antes de orientar a atendente sobre a continuidade do contato, Marina interrompe outra atividade, pede que algumas perguntas sejam repetidas ao tutor e verifica com a equipe a capacidade de atendimento naquele momento. A troca adicional aumenta o tempo necessário para organizar o caso e pode levar o tutor a repetir informações sob estresse. Se um sinal importante não for transmitido ou se a possibilidade de atendimento for presumida sem confirmação, a preparação da equipe e a decisão do tutor poderão ser prejudicadas.

### 2. Questões de refinamento

Use os tipos de questões/taxonomia definidos na aula. As perguntas devem revelar informações **ainda ausentes** do cenário, não repetir o que já foi respondido.

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q1 | Quem normalmente recebe o primeiro contato do tutor e quem decide se a unidade possui condições de receber o caso? | O alcance do objetivo depende dos papéis, das responsabilidades e da passagem de informação entre os profissionais. | Entrevistas com atendentes e médicos-veterinários de clínicas ou hospitais com plantão. |
| Q2 | Quais dados mínimos Marina precisa conhecer para compreender o relato inicial e preparar a continuidade do atendimento? | O cenário precisa distinguir informação essencial, informação complementar e dados cuja ausência exige novo contato. | Literatura e protocolos veterinários utilizados no TCC, seguidos de validação em entrevistas com profissionais. |
| Q3 | Por quais canais as informações chegam, como são registradas e quais outras atividades competem pela atenção da equipe? | A fragmentação pode decorrer dos recursos utilizados, das interrupções e da organização do trabalho. | Observação contextual autorizada e entrevistas sobre o fluxo real de plantão. |
| Q4 | Como Marina verifica a origem, a completude e a atualidade das informações antes de utilizá-las na preparação do atendimento? | É necessário entender como a profissional identifica lacunas e evita tratar uma interpretação de terceiros como dado confirmado. | Entrevistas com profissionais e análise dos registros utilizados pelas clínicas. |
| Q5 | O que muda no fluxo quando a unidade não pode receber o animal ou quando o estado relatado se agrava durante o contato? | Esses eventos alteram o objetivo imediato, os atores envolvidos e as informações que precisam ser comunicadas ao tutor. | Entrevistas baseadas em incidentes críticos e análise de procedimentos da unidade. |

### 3. Cenário refinado

Reescreva o cenário incorporando as respostas. Marque o conteúdo novo de forma consistente (por exemplo, `**[NOVO: ...]**`).

Marina é médica-veterinária plantonista em um hospital veterinário que atende durante a noite. Enquanto acompanha outros animais, uma atendente recebe a ligação de um tutor preocupado com um cão que apresenta dificuldade para respirar. **[NOVO: A atendente realiza o primeiro registro e consulta Marina, que avalia as informações clínicas disponíveis; a confirmação sobre a capacidade de atendimento também depende da situação operacional da unidade (Q1, hipótese H05).]**

O tutor relata os sinais sem uma ordem definida, alternando observações atuais, informações do histórico e dúvidas sobre o que deve fazer. **[NOVO: Marina procura identificar espécie, idade, sinais observados, início e evolução do quadro, alterações de respiração, circulação ou consciência, histórico relevante e medidas já tomadas (Q2, conforme informações levantadas na Entrega 1).]** A atendente registra parte do relato enquanto também precisa responder a outras pessoas e verificar com a equipe se existe possibilidade de receber o animal.

Quando a informação chega a Marina, alguns dados estão distribuídos entre anotações, uma conversa por telefone e uma mensagem encaminhada. **[NOVO: Durante o plantão, chamadas, mensagens, atendimento presencial e comunicação interna competem pela atenção dos profissionais e podem produzir registros duplicados ou incompletos (Q3, hipótese H05).]** Ela tenta identificar quais sinais foram observados diretamente pelo tutor, quando começaram, como evoluíram e quais dados ainda não foram informados. Como o relato foi recontado, não consegue distinguir com segurança o conteúdo original, o resumo e a interpretação de quem recebeu a ligação. **[NOVO: Marina compara os registros disponíveis, verifica horário e identificação do animal e solicita confirmação dos pontos ausentes ou contraditórios antes de considerar o relato suficientemente organizado (Q4, hipótese H03).]**

Antes de orientar a atendente sobre a continuidade do contato, Marina interrompe outra atividade, pede que algumas perguntas sejam repetidas ao tutor e verifica com a equipe a capacidade de atendimento. **[NOVO: Se a unidade não puder receber o animal, a equipe precisa comunicar essa limitação sem criar garantia sobre outra clínica; se houver relato de agravamento, a prioridade da comunicação e da decisão pode mudar (Q5, lacuna ainda a investigar).]** A troca adicional aumenta o tempo necessário para organizar o caso e pode levar o tutor a repetir informações sob estresse. Se um sinal importante não for transmitido ou se a possibilidade de atendimento for presumida sem confirmação, a preparação da equipe e a decisão do tutor poderão ser prejudicadas.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | Marina, médica-veterinária plantonista; atendente; tutor; demais profissionais da unidade. |
| Objetivo(s) | Compreender o relato inicial, identificar lacunas, verificar a possibilidade de receber o caso e preparar a continuidade do atendimento. |
| Contexto | Plantão noturno, atendimento simultâneo de outros animais, interrupções e pressão de tempo. |
| Recursos/informações | Ligações, mensagens, anotações, comunicação interna, dados do animal, sinais relatados, evolução, histórico, horário e situação operacional da unidade. |
| Ações | Ouvir, anotar, encaminhar informações, comparar registros, repetir perguntas, consultar a equipe e responder ao tutor. |
| Problemas/rupturas | Relato desorganizado, perda de contexto na retransmissão, dados distribuídos em canais diferentes, interrupções, duplicidade e ausência de confirmação. |
| Consequências | Retrabalho, repetição de perguntas, atraso na organização do caso, preparação incompleta da equipe ou expectativa indevida de atendimento. |

### 5. Implicações para as próximas entregas

As tarefas de receber o contato, conferir a origem das informações, identificar lacunas, verificar a capacidade da unidade e comunicar a continuidade do caso merecem análise. Ainda precisam ser coletadas informações com profissionais sobre quais dados são indispensáveis, quem recebe o contato, como as informações são registradas e quais rupturas ocorrem no plantão. H03 e H05 devem continuar tratadas como hipóteses, sem consolidar uma interface secundária para a clínica antes de sua investigação.

> Repita para C02, C03... com autoria individual.

## Checklist

- [ ] Há um cenário completo por integrante.
- [ ] Cada cenário tem título, ator, objetivo, contexto e problema.
- [ ] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [ ] O texto descreve a situação atual, sem antecipar a solução.
- [ ] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”.
- [ ] Questões de refinamento acrescentam informação nova.
- [ ] O refinamento mostra claramente o que foi adicionado/alterado.
- [ ] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [ ] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.
