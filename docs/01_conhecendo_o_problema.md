# Entrega 1 — Conhecendo o projeto, o usuário e o problema

**Data:** 19/08/2026
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 solução consolidada por equipe

## Objetivo da atividade

Reinterpretar o tema do TCC sob a perspectiva de Interação Humano-Computador e construir um **entendimento comum entre os integrantes da equipe**.

A disciplina utiliza preferencialmente o tema do TCC para os exercícios de IHC. Isso vale tanto para TCCs que já preveem uma interface quanto para trabalhos cujo resultado principal é algoritmo, modelo, API, biblioteca, análise de dados, infraestrutura, estudo experimental ou outro artefato técnico.

> **Importante:** a interface projetada na disciplina é um artefato de aprendizagem de IHC. Ela **não se torna automaticamente uma obrigação do TCC**. Sua incorporação ao trabalho de conclusão depende de decisão da equipe e do orientador.

Antes de preencher, leia [`../GUIA_ESCOPO_IHC.md`](../GUIA_ESCOPO_IHC.md).

Nesta primeira semana a equipe **não deve começar desenhando telas**. Primeiro deverá compreender:

- o que o TCC realmente produz;
- quem poderia obter valor dessa contribuição;
- quais pessoas interagem, administram, configuram, interpretam ou são afetadas;
- o que essas pessoas precisam alcançar;
- como atividades relacionadas acontecem hoje;
- problemas, limitações e contexto;
- alternativas existentes;
- qual recorte de interação fará sentido para a disciplina.

Ao final desta entrega, a equipe deve diferenciar:

- **tema do TCC** × **escopo formal do TCC** × **escopo de IHC da disciplina**;
- **objetivo do projeto** × **objetivo do usuário**;
- **problema do usuário** × **solução tecnológica**;
- **fato conhecido** × **hipótese** × **lacuna de conhecimento**;
- **capacidade técnica** × **forma de uso dessa capacidade**;
- **funcionalidade** × **atividade/resultado que o usuário precisa alcançar**;
- **usuário direto** × **stakeholders**.

---

## Como classificar as respostas

Sempre que a resposta fizer uma afirmação sobre usuários, problemas, atividades, necessidades, contexto ou mercado, use:

- **[F] Fato conhecido** — existe evidência/fonte.
- **[H] Hipótese** — afirmação plausível que ainda precisa ser investigada.
- **[?] Não sabemos ainda** — lacuna relevante.

Quando usar `[F]`, informe a origem. Hipóteses prioritárias devem receber IDs (`H01`, `H02`...) e também ser registradas em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

> **Exemplo:** `[H] H01 — DBAs considerariam útil comparar automaticamente o plano atual de execução com uma recomendação produzida pelo algoritmo.`

Uma hipótese explicitada é melhor do que uma suposição escondida.

---

# 0. Identificação do TCC e da equipe

## 0.1 Membros

| Nome completo | Matrícula | GitHub |
|---|---:|---|
| Vinícius de Castro Duarte | 22.224.020-2 | vinizika |
| João Pedro Gardenghi Peterutto | 22.125.066-5 | jpeterutto |
| Julian Ryu Takeda | 22.224.030-1 | ryu2525 |

## 0.2 Título atual do TCC

Plataforma Inteligente de Pré-Triagem e Apoio à Decisão em Emergências Veterinárias utilizando RAG e Modelos de Linguagem de Grande Escala

## 0.3 Orientador(a)

Rafael Gomes Alves

## 0.4 Qual é o resultado principal atualmente previsto no TCC?

Marque e descreva:

- [x] sistema/aplicação interativa;
- [ ] algoritmo;
- [x] modelo de IA/ML/LLM;
- [ ] biblioteca/API/framework;
- [ ] análise de dataset;
- [x] estudo/benchmark/avaliação experimental;
- [x] infraestrutura/backend;
- [ ] componente embarcado/IoT;
- [ ] outro: não se aplica.

**Descrição:** O TCC prevê o desenvolvimento de uma prova de conceito de plataforma inteligente para pré-triagem veterinária. O sistema receberá relatos de tutores por texto ou voz, processará essas informações por uma arquitetura de LLM associada a RAG e a uma base veterinária curada e classificará o caso quanto à possível urgência. A proposta também prevê avaliação experimental das técnicas do pipeline, interface interativa para o tutor, serviços de backend, geolocalização de clínicas e geração de um resumo estruturado para apoiar o encaminhamento inicial em situações emergenciais.

## 0.5 O TCC já previa desenvolvimento de interface com usuário?

- [x] Sim, a interface já faz parte do TCC.
- [ ] Parcialmente; existe alguma interação, mas ainda não está bem definida.
- [ ] Não. O TCC é predominantemente técnico e não previa interface.

**Explique o que está formalmente previsto no TCC:** O TCC prevê uma interface com experiência próxima à de uma aplicação móvel, inicialmente prototipada com Streamlit, para permitir o cadastro do animal, entrada de relatos por texto ou voz, interação híbrida entre conversa e dados estruturados, apresentação do possível nível de urgência, justificativas fundamentadas, orientações iniciais e localização de clínicas próximas. Também está prevista a possibilidade de armazenar informações contextuais, como histórico clínico e vacinação.

> Esta resposta serve para separar o compromisso do TCC do projeto da disciplina. Mesmo quando a opção for **não**, a equipe irá definir uma interface para exercitar IHC.

---

# 1. Entendendo a contribuição do projeto

## 1.1 Explique o TCC em uma frase, sem citar linguagem de programação, framework ou banco de dados.

Desenvolver e avaliar uma plataforma que interprete relatos de tutores, identifique possíveis situações de emergência veterinária e apoie a decisão sobre o encaminhamento inicial do animal com base em conhecimento técnico especializado.

## 1.2 Qual situação, atividade ou problema do mundo real motivou o TCC?

**[F]** Tutores podem enfrentar incerteza, pressão emocional e dificuldades financeiras, geográficas ou logísticas no intervalo entre perceber sinais clínicos no animal e conseguir atendimento veterinário. Evidências discutidas no TCC indicam que tutores valorizam orientação remota inicial quando não conseguem acessar prontamente um serviço especializado e que casos de emergência exigem triagem e priorização rápidas.

**[F]** A triagem veterinária tem como finalidade inicial reconhecer a gravidade e priorizar o atendimento, e não estabelecer um diagnóstico definitivo.

**[H] H01** — Na ausência de uma orientação inicial acessível, parte dos tutores pode demorar para procurar atendimento em casos graves ou procurar serviços emergenciais em situações que poderiam seguir outro fluxo de cuidado. Essa hipótese deriva da motivação do TCC, mas sua frequência e suas causas no público-alvo ainda precisam ser investigadas diretamente.

## 1.3 Qual é a **capacidade/contribuição central** produzida pelo TCC?

Complete, se ajudar:

> “Nosso TCC produz, melhora, analisa ou permite `{{capacidade}}`.”

Exemplos: otimizar consultas; classificar imagens; detectar anomalias; comparar modelos; identificar padrões; prever demanda; analisar desempenho; gerar resumos; recomendar configurações.

Nosso TCC permite interpretar relatos leigos sobre sinais observados em cães e gatos, recuperar evidências em uma base veterinária especializada e apoiar a classificação inicial do caso como possível emergência, não emergência ou situação incerta, apresentando ao tutor uma orientação fundamentada e um possível encaminhamento.

## 1.4 O que se espera que esteja diferente **para pessoas, organizações ou processos** se essa contribuição for bem-sucedida?

**[H] H02** — Para o tutor, espera-se maior clareza sobre a possível gravidade do caso e sobre qual ação deve ser tomada em seguida.

**[H] H03** — Para clínicas e hospitais veterinários, o envio prévio de um resumo estruturado poderá melhorar a preparação para receber animais encaminhados como possíveis emergências.

**[H] H04** — Para o processo de atendimento, espera-se reduzir o intervalo entre a percepção dos sinais e a decisão de procurar o serviço adequado, sem substituir a avaliação do médico-veterinário.

## 1.5 O que é mérito técnico/científico do TCC e o que seria uma possível aplicação prática?

| Mérito/contribuição técnica | Possível aplicação/valor em uso |
|---|---|
| Projetar e avaliar uma arquitetura modular de RAG aplicada à pré-triagem veterinária. | Apoiar o tutor com respostas relacionadas a uma base de conhecimento veterinária especializada. |
| Comparar a arquitetura completa com variantes de ablação e uma linha de base de RAG simples. | Identificar quais combinações oferecem melhor equilíbrio entre qualidade, segurança e tempo de resposta. |
| Investigar reformulação de consulta, HyDE, recuperação vetorial, LightRAG, re-ranking e autocorreção. | Melhorar a interpretação de relatos leigos e a seleção das evidências mais pertinentes ao caso. |
| Avaliar classificação, recuperação, fidelidade e latência com métricas específicas. | Reduzir respostas sem apoio documental e tornar as limitações do sistema mais verificáveis. |
| Integrar entrada multimodal, classificação e geração de resumo estruturado. | Permitir que o tutor relate o caso por texto ou voz e compartilhe informações relevantes com uma clínica. |

---

# 2. Entendendo as pessoas envolvidas

## 2.1 Quem interage diretamente com o produto, se já existe interface prevista?

**[F]** O usuário direto principal previsto é o tutor de cão ou gato que percebe sinais clínicos ou comportamentais e utiliza a plataforma para descrever a situação e receber apoio inicial. 

**[F]** Profissionais de clínicas veterinárias também podem interagir com informações estruturadas encaminhadas pela plataforma quando um caso for classificado como possível emergência. 

**[H] H05** Caso o módulo de comunicação com a clínica seja aprofundado, atendentes ou médicos-veterinários poderão precisar consultar o resumo do caso, confirmar capacidade de atendimento e continuar a comunicação com o tutor.

## 2.2 Quem poderia **usar, configurar, administrar, operar, interpretar ou tomar decisões** a partir da contribuição técnica?

Considere perfis profissionais e stakeholders, não apenas consumidores finais.

| Perfil | Relação com a contribuição | O que faria | Status/evidência |
|---|---|---|---|
| {{DBA / analista / gestor / técnico / pesquisador / usuário final...}} | {{...}} | {{...}} | F / H / ? |

## 2.3 Existem pessoas afetadas que não usariam a interface diretamente?

| Stakeholder | Como é afetado | Usa interface? | Status/evidência |
|---|---|---|---|
| {{...}} | {{...}} | sim/não | {{...}} |

## 2.4 Que características desses perfis podem influenciar a interação?

Considere conhecimento do domínio, experiência tecnológica, frequência de uso, necessidades de acessibilidade, responsabilidade profissional, familiaridade com métricas, linguagem técnica, urgência etc.

{{[F/H/?] ...}}

---

# 3. Entendendo objetivos e atividades

## 3.1 O que o usuário está tentando conseguir no mundo real?

Não responda “usar o algoritmo”, “clicar no sistema” ou “ver o dashboard”.

{{[F/H/?] ...}}

## 3.2 Quais são as atividades mais importantes?

| ID | Atividade/objetivo | Quem realiza | Frequência/criticidade inicial | Status/evidência |
|---|---|---|---|---|
| A01 | {{...}} | {{...}} | {{...}} | {{...}} |
| A02 | {{...}} | {{...}} | {{...}} | {{...}} |
| A03 | {{...}} | {{...}} | {{...}} | {{...}} |

## 3.3 Qual atividade parece mais frequente? Por quê?

{{[F/H/?] ...}}

## 3.4 Qual parece mais crítica? Que consequência existe se for mal executada?

{{[F/H/?] ...}}

---

# 4. Entendendo o problema ou processo atual

## 4.1 Como essas atividades são realizadas hoje, antes da interface imaginada na disciplina?

Pode existir software concorrente, linha de comando, planilha, notebook, script, painel técnico, processo manual, consulta a logs, análise visual, troca de mensagens, decisão por especialista etc.

{{[F/H/?] ...}}

## 4.2 O que é difícil, demorado, confuso, repetitivo, arriscado ou pouco transparente?

{{[F/H/?] ...}}

## 4.3 Que informações o profissional precisa interpretar para tomar decisão?

{{[F/H/?] ...}}

## 4.4 O que acontece quando a atividade falha ou quando o resultado é interpretado incorretamente?

{{[F/H/?] ...}}

## 4.5 Conte uma situação concreta.

Escreva uma pequena narrativa com pessoa, objetivo, atividade, contexto, dificuldade e consequência. **Não descreva ainda a futura solução.**

{{[F/H/?] narrativa...}}

## 4.6 Que evidência existe hoje?

| Evidência/fonte | O que sustenta | Limitação |
|---|---|---|
| {{...}} | {{...}} | {{...}} |

---

# 5. Entendendo o contexto de uso

## 5.1 Onde e em quais situações a interação poderia ocorrer?

{{[F/H/?] ...}}

## 5.2 Em quais dispositivos/equipamentos?

{{[F/H/?] ...}}

## 5.3 Existem condições físicas relevantes?

Considere iluminação, ruído, mobilidade, conexão, privacidade, uso compartilhado, interrupções, pressão de tempo etc.

{{[F/H/?] ...}}

## 5.4 Existem fatores sociais ou organizacionais?

Considere papéis, chefias, equipes, permissões, aprovação, responsabilidade profissional, auditoria, turnos e colaboração.

{{[F/H/?] ...}}

## 5.5 Existe necessidade de histórico, rastreabilidade ou auditoria?

{{[F/H/?] ...}}

## 5.6 Um erro pode produzir consequência relevante? Qual?

{{[F/H/?] ...}}

---

# 6. Entendendo mercado e alternativas existentes

> Nesta entrega faça apenas um **levantamento inicial**. A análise aprofundada ocorre na Entrega 2.

## 6.1 Como pessoas resolvem problemas semelhantes hoje?

| Alternativa atual | Quem usa | Para quê | Status/evidência |
|---|---|---|---|
| {{...}} | {{...}} | {{...}} | {{...}} |

## 6.2 Existem produtos que atuam na mesma área, mesmo sem serem equivalentes ao TCC?

{{[F/H/?] ...}}

## 6.3 Quais interfaces profissionais esse público já conhece?

Exemplos possíveis: ferramentas de banco, IDEs, consoles de nuvem, dashboards, plataformas de dados, ferramentas de monitoramento, painéis de IA, sistemas administrativos.

{{[F/H/?] ...}}

## 6.4 O que essas soluções parecem fazer bem?

{{[F/H/?] ...}}

## 6.5 O que parecem fazer mal, dificultar ou não atender?

{{[F/H/?] ...}}

## 6.6 Que padrões de interface ou vocabulário parecem familiares a esse público?

{{[F/H/?] ...}}

---

# 7. Derivando o escopo de IHC da disciplina

## 7.1 Escolha o caminho do projeto

### Caminho A — TCC já possui interface

Explique qual parte da interface será usada como recorte da disciplina e por que esse fluxo é relevante.

{{...}}

### Caminho B — TCC não possui interface prevista

Faça o exercício de transferência de uso:

> **Imagine que o TCC foi concluído com sucesso e uma empresa, laboratório ou organização quer transformar a contribuição em algo utilizável. Quem precisaria interagir com ela e para quê?**

Responda:

1. quem poderia contratar/adotar a solução? {{...}}
2. quem seria o usuário direto? {{...}}
3. quem administraria/configuraria? {{...}}
4. quem interpretaria resultados? {{...}}
5. quem tomaria decisões? {{...}}
6. quais dados/entradas seriam necessários? {{...}}
7. quais resultados deveriam ser compreendidos? {{...}}
8. que erros/rupturas seriam possíveis? {{...}}

## 7.2 Qual perfil será priorizado no projeto de IHC?

{{...}}

**Por que esse perfil foi escolhido?** {{...}}

## 7.3 Qual objetivo desse usuário será priorizado?

{{...}}

## 7.4 Que interface será explorada na disciplina?

Complete:

> **Para fins da disciplina de IHC, será projetada uma interface que permita a `{{perfil}}` utilizar `{{capacidade/resultado do TCC}}` para `{{objetivo}}`, no contexto de `{{situação}}`.**

{{...}}

## 7.5 Qual é a relação dessa interface com o TCC?

- [ ] Já fazia parte do TCC.
- [ ] É um aprofundamento de algo parcialmente previsto.
- [ ] É uma extensão conceitual criada para a disciplina.
- [ ] É um protótipo demonstrativo de aplicação potencial.
- [ ] Outra: {{...}}.

> **Declaração:** a interface desenvolvida nesta disciplina é um artefato de aprendizagem de IHC baseado no tema do TCC. Sua inclusão ou implementação no TCC somente ocorrerá se isso for posteriormente decidido pela equipe e pelo orientador.

---

# 8. Levantando possibilidades de interação — sem desenhar ainda

A equipe pode registrar possibilidades para investigação. **Não significa que todas serão implementadas.**

Marque apenas as que parecem plausíveis e explique o objetivo correspondente.

| Possibilidade | Pode fazer sentido? | Objetivo/tarefa que justificaria | Evidência atual |
|---|---|---|---|
| Dashboard/visão geral | sim/não/talvez | {{...}} | {{...}} |
| Configuração/parametrização | sim/não/talvez | {{...}} | {{...}} |
| Entrada/upload/seleção de dados | sim/não/talvez | {{...}} | {{...}} |
| Acompanhamento de processamento | sim/não/talvez | {{...}} | {{...}} |
| Relatório/resultados | sim/não/talvez | {{...}} | {{...}} |
| Histórico com busca/filtros | sim/não/talvez | {{...}} | {{...}} |
| Comparação de resultados | sim/não/talvez | {{...}} | {{...}} |
| Explicabilidade/detalhamento | sim/não/talvez | {{...}} | {{...}} |
| Administração/configurações globais | sim/não/talvez | {{...}} | {{...}} |
| Usuários/perfis/permissões | sim/não/talvez | {{...}} | {{...}} |
| CRUD de entidade do domínio | sim/não/talvez | {{...}} | {{...}} |
| Auditoria/logs | sim/não/talvez | {{...}} | {{...}} |
| Alertas/ocorrências | sim/não/talvez | {{...}} | {{...}} |
| Ajuda/documentação | sim/não/talvez | {{...}} | {{...}} |

> **Atenção:** “login + dashboard + CRUD” não é uma solução universal. Cada padrão deve surgir de uma tarefa real.

---

# 9. Benefícios e ações iniciais

## 9.1 Qual benefício concreto o projeto de IHC pretende oferecer?

| Benefício esperado | Problema/necessidade | Usuário | Status/evidência |
|---|---|---|---|
| {{...}} | {{...}} | {{...}} | {{...}} |

## 9.2 Que ações o usuário deverá conseguir realizar?

| ID | O usuário precisa conseguir... | Para alcançar... | Prioridade inicial |
|---|---|---|---|
| F01 | {{ação}} | {{objetivo}} | alta/média/baixa |

## 9.3 Tecnologias/restrições já definidas no TCC

A tecnologia aparece **agora**, depois do entendimento do uso.

| Tecnologia/restrição | Por que existe | Possível impacto na interação |
|---|---|---|
| {{...}} | {{...}} | {{...}} |

---

# 10. Hipóteses e dúvidas prioritárias

| ID | Hipótese/dúvida | Por que importa | Como poderá ser investigada |
|---|---|---|---|
| H01 | {{...}} | {{...}} | Entrega 2/3/7/... |
| H02 | {{...}} | {{...}} | {{...}} |
| H03 | {{...}} | {{...}} | {{...}} |

Registre em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

---

# 11. Síntese da equipe

| Pergunta | Síntese atual |
|---|---|
| Qual é a contribuição central do TCC? | {{...}} |
| O TCC já previa interface? | {{...}} |
| Quem é o usuário prioritário de IHC? | {{...}} |
| O que ele precisa alcançar? | {{...}} |
| Qual problema/atividade será estudado? | {{...}} |
| Como isso acontece hoje? | {{...}} |
| Qual é o contexto de uso? | {{...}} |
| Que interface/recorte será explorado? | {{...}} |
| Como a interface se relaciona ao TCC? | {{...}} |
| Quais pontos ainda são hipóteses? | {{H01...}} |

### Delimitação

**Dentro do escopo de IHC:** {{...}}  
**Fora do escopo de IHC:** {{...}}  
**Dentro do escopo formal do TCC:** {{...}}  
**Interface da disciplina será implementada no TCC?** não definido / sim / não — {{justificativa, se houver}}

---

# 12. Como esta entrega alimenta as próximas

- **Entrega 2:** verifica mercado, concorrentes e interfaces profissionais representativas.
- **Entrega 3:** detalha perfis e contexto.
- **Entrega 4:** aprofunda situações problemáticas.
- **Entrega 5:** modela tarefas centrais.
- **Entrega 6:** experimenta alternativas em baixa fidelidade.
- **Entrega 7:** investiga hipóteses com dados.
- **Entrega 8:** define restrições e metas de usabilidade.
- **Entregas 9–11:** transformam o recorte em modelo de interação e protótipo.
- **Entregas 12–14:** avaliam a interface construída na disciplina.

A Entrega 1 é uma **fotografia inicial do conhecimento**. Ela pode e deve ser revisada quando surgirem evidências.

---

# 13. Relação com INOVA e comunicação do projeto

Prepare uma explicação de até três frases:

1. **Problema/atividade humana:** {{...}}
2. **Contribuição técnica do TCC:** {{...}}
3. **Como uma pessoa poderia utilizar essa contribuição:** {{...}}

Essa síntese ajuda a apresentar o projeto para público não especializado sem reduzir seu mérito técnico.

---

# Checklist de qualidade

- [ ] Está clara a diferença entre tema do TCC, escopo formal do TCC e escopo de IHC.
- [ ] A equipe declarou se o TCC já previa interface.
- [ ] Se não previa, foi derivado um usuário plausível e um objetivo de uso.
- [ ] A interface de IHC não foi apresentada como obrigação automática do TCC.
- [ ] A contribuição do TCC foi descrita sem começar por tecnologias de implementação.
- [ ] Usuários diretos e stakeholders foram diferenciados.
- [ ] Foram considerados profissionais que configuram, administram, interpretam ou decidem, quando pertinente.
- [ ] Objetivo do usuário não foi confundido com objetivo do projeto.
- [ ] Processo/problema atual foi descrito antes da solução.
- [ ] Existe situação concreta de uso/problema.
- [ ] Contexto físico, social/organizacional, dispositivos e consequências de erro foram considerados.
- [ ] Mercado/alternativas existentes foram levantados inicialmente.
- [ ] Possibilidades como dashboard, relatório, histórico, filtros e CRUD foram tratadas como hipóteses de solução, não como requisitos automáticos.
- [ ] Cada possibilidade de interface tem um objetivo/tarefa que poderia justificá-la.
- [ ] Afirmações relevantes estão marcadas `[F]`, `[H]` ou `[?]`.
- [ ] Hipóteses prioritárias receberam IDs e foram para a rastreabilidade.
- [ ] O recorte de IHC é viável para modelar, prototipar e avaliar no semestre.
- [ ] A equipe consegue explicar problema humano → contribuição computacional → forma de uso.
