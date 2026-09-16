# Entrega 4 — Cenários de análise/problema

**Data:** 13/09/2026 <br>
**Status:** 🟨 em andamento <br>
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

## Cenário C01 — Triagem e busca de orientações em situação de emergência veterinária noturna

**Autor(a):** Julian Ryu Takeda RA:22.224.030-1 <br>
**Persona(s) relacionada(s):** Tutora em situação de urgência noturna (Camila Rocha) <br>
**Necessidade relacionada:** Necessidade de obter uma avaliação preliminar confiável e rápida sobre a gravidade dos sintomas de um animal para decidir o próximo passo logístico e de cuidado. <br>
**Situação concreta da Entrega 1 relacionada:** Relatos de dificuldade de acesso rápido a suporte em horários críticos e falta de clareza sobre o que constitui uma verdadeira emergência veterinária. <br>
**Hipóteses ainda presentes:** —

### 1. Cenário inicial

Em uma noite de semana, por volta das 23h, Camila percebe que seu cão de estimação, Bob, começa a apresentar apatia severa, vômitos repetidos e rigidez abdominal incomum. Tomada por forte apreensão por estar sozinha em casa e sem conhecimento clínico para diferenciar se o quadro é uma urgência crítica ou um mal-estar passageiro, Camila tenta buscar orientações rápidas na internet. Ela digita termos vagos em buscadores gerais, encontrando fóruns genéricos, artigos conflitantes e fóruns de opinião com informações contraditórias. Diante do excesso de dados desencontrados e sem saber se deve correr imediatamente para um pronto-socorro veterinário ou aguardar a manhã seguinte, Camila perde preciosos minutos tentando correlacionar os sintomas descritos na web com o estado real do animal. Com medo de errar e sem conseguir estimar a gravidade exata da situação, ela permanece angustiada, sem uma linha de raciocínio estruturada para orientar sua decisão de transporte ou os primeiros cuidados pré-hospitalares.

### 2. Questões de refinamento

Use os tipos de questões/taxonomia definidos na aula. As perguntas devem revelar informações **ainda ausentes** do cenário, não repetir o que já foi respondido.

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q1 | Quais termos de busca informais Camila costuma utilizar ao relatar sintomas gastrointestinais agudos em cães? | Para entender a distância semântica (lexical gap) entre a linguagem leiga utilizada pela persona e a terminologia clínica veterinária presente na base especializada do TCC. | Literatura sobre triagem digital e entrevistas exploratórias com tutores. |
| Q2 | Quanto tempo em média Camila gasta navegando por fontes genéricas antes de decidir procurar ajuda profissional? | Para dimensionar o impacto da falta de suporte inicial na violação da "Golden Hour" do atendimento de emergência veterinária. |  Estudos sobre premissas de atendimento pré-hospitalar veterinário (Hanel et al., 2016). |
| Q3 | De que forma Camila tenta registrar ou memorizar os sintomas observados para repassar posteriormente ao veterinário de plantão? | Para identificar quais informações clínicas a usuária consegue reter e transmitir sob alto estresse emocional. | Observação comportamental e mapeamento de jornada da persona. |

### 3. Cenário refinado

Em uma noite de semana, por volta das 23h, Camila percebe que seu cão de estimação, Bob, começa a apresentar apatia severa, vômitos repetidos e rigidez abdominal incomum. Tomada por forte apreensão por estar sozinha em casa e sem conhecimento clínico para diferenciar se o quadro é uma urgência crítica ou um mal-estar passageiro, Camila tenta buscar orientações rápidas na internet. [NOVO: Q1: Utilizando termos coloquiais e vagos em mecanismos de busca comuns, ela encontra uma disparidade enorme entre a sua forma de descrever o problema e os termos técnicos restritos encontrados nos sites médicos.] Ela digita termos vagos em buscadores gerais, encontrando fóruns genéricos, artigos conflitantes e fóruns de opinião com informações contraditórias. Diante do excesso de dados desencontrados e sem saber se deve correr imediatamente para um pronto-socorro veterinário ou aguardar a manhã seguinte, Camila perde preciosos minutos tentando correlacionar os sintomas descritos na web com o estado real do animal. [NOVO: Q2: Esse processo de varredura manual e incerta consome mais de quarenta minutos críticos, retardando a tomada de decisão em um cenário onde o tempo de resposta é vital para a sobrevida do animal.] Com medo de errar e sem conseguir estimar a gravidade exata da situação, ela permanece angustiada, sem uma linha de raciocínio estruturada para orientar sua decisão de transporte ou os primeiros cuidados pré-hospitalares. [NOVO: Q3: Na ausência de um resumo ou guia estruturado, Camila anota os sintomas de forma dispersa em um bloco de notas no celular para tentar explicar o ocorrido ao chegar à clínica.]

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | Camila Rocha (tutora de animal de estimação, leiga em medicina veterinária, sob forte estresse emocional noturno). |
| Objetivo(s) | Compreender a gravidade dos sintomas apresentados por Bob e decidir se deve buscar atendimento emergencial imediato. |
| Contexto | Período noturno (fora do horário comercial), ambiente doméstico sob forte pressão emocional, isolamento informacional e ausência de suporte especializado acessível. |
| Recursos/informações | Motores de busca gerais, artigos da internet, fóruns genéricos de opinião e bloco de notas improvisado no celular. |
| Ações | Digitar termos informais na web, ler múltiplos sites divergentes, alternar entre páginas de conteúdo incerto, tentar correlacionar visualmente os sintomas e anotar observações de forma dispersa. |
| Problemas/rupturas | Lexical gap (dificuldade de traduzir a linguagem leiga em critérios clínicos), sobrecarga de informações desencontradas na web, ausência de validação técnica confiável, perda de tempo crítico (Golden Hour) e elevado estresse na tomada de decisão. |
| Consequências | Risco de atrasar o socorro a um paciente grave, subvalorização ou pânico diante de falsas emergências, e esgotamento emocional da tutora. |

### 5. Implicações para as próximas entregas

Quais tarefas merecem análise? Quais informações precisam ser coletadas? **Não desenhe a solução ainda.**

- O que merece análise detalhada: O processo de transição cognitiva que Camila realiza entre perceber um sintoma informal em casa e convertê-lo em uma avaliação de risco.
- O que precisa ser coletado: Quais são os principais gatilhos sintomáticos que geram maior confusão em tutores (distinção entre urgências reais e casos leves) e quais protocolos de pré-triagem de Manchester adaptados para animais melhor estruturam essa hierarquia de gravidade.

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
