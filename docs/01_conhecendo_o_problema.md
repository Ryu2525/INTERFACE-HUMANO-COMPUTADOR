# Entrega 1 — Conhecendo o projeto, o usuário e o problema

**Data:** 23/08/2026  
**Status:** 🟩 concluída  
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
| Tutor de cão ou gato | Usuário direto prioritário | Descrever sinais, responder perguntas complementares, interpretar a orientação e decidir o próximo passo | **F** TCC, Resumo e seções IV.C e IV.K |
| Atendente de clínica veterinária | Usuário direto secundário possível | Receber o caso, consultar o resumo inicial e apoiar a organização da chegada do animal | **H** H05; o envio estruturado está previsto, mas o fluxo operacional da clínica ainda precisa ser investigado |
| Médico-veterinário | Especialista e decisor clínico | Interpretar as informações recebidas, realizar a triagem profissional e decidir sobre avaliação e tratamento | **F** a literatura de triagem estabelece que a avaliação profissional permanece necessária; TCC, seções II.B e VII |
| Especialista responsável pela curadoria | Configura a base de conhecimento | Selecionar, revisar e atualizar documentos veterinários e critérios de urgência | **F** TCC, seções II.C, II.E e IV.B |
| Administrador técnico | Opera e mantém a solução | Gerenciar infraestrutura, disponibilidade, integrações e controle de acesso | **H** papel necessário para operação futura, mas ainda não detalhado no escopo de interação |
| Pesquisador/engenheiro de IA | Avalia a contribuição técnica | Executar experimentos, comparar variantes e analisar métricas | **F** TCC, seções IV.H e IV.I |

## 2.3 Existem pessoas afetadas que não usariam a interface diretamente?

| Stakeholder | Como é afetado | Usa interface? | Status/evidência |
|---|---|---|---|
| Animal atendido | Pode ser encaminhado com maior ou menor rapidez conforme a interpretação da urgência | não | **F** o tempo e a priorização são relevantes em emergências |
| Familiares ou outros responsáveis pelo animal | Podem participar da decisão, transporte e continuidade do cuidado | não necessariamente | **H** relação plausível, ainda não investigada |
| Clínica ou hospital veterinário | Pode receber informações prévias e ter seu fluxo de atendimento afetado pelo encaminhamento | não como entidade, seus profissionais podem usar | **H**  H03 e H05 |
| Equipe responsável pela plataforma | Assume responsabilidade por manutenção, segurança, disponibilidade e correção de falhas | sim, por interfaces técnicas futuras | **H** papel operacional ainda não detalhado |
| Órgãos e responsáveis por proteção de dados | São interessados na conformidade do tratamento de dados pessoais | não no fluxo principal | **F** o TCC prevê consideração à LGPD |

## 2.4 Que características desses perfis podem influenciar a interação?

Considere conhecimento do domínio, experiência tecnológica, frequência de uso, necessidades de acessibilidade, responsabilidade profissional, familiaridade com métricas, linguagem técnica, urgência etc.

**[F]** O tutor tende a descrever os sinais em linguagem cotidiana, enquanto a base documental utiliza terminologia técnico-científica; essa diferença linguística influencia a compreensão, as perguntas e a recuperação de informações.  

**[F]** O contexto pode envolver urgência, pressão emocional e necessidade de resposta rápida, o que aumenta a importância de comunicação clara e baixa carga de interação.  

**[H] H06** Tutores possuem diferentes níveis de alfabetização digital, conhecimento sobre saúde animal, capacidade de observar sinais e necessidades de acessibilidade; por isso, a interface poderá precisar oferecer linguagem simples, entradas alternativas e ajuda contextual.

**[?]** Ainda não sabemos quais necessidades de acessibilidade são mais frequentes no público pretendido, nem como variam conforme idade, experiência com animais e familiaridade com aplicativos.

**[F]** Profissionais veterinários possuem responsabilidade clínica e utilizam terminologia técnica, de modo que a informação direcionada à clínica poderá exigir maior precisão e estrutura do que a explicação destinada ao tutor.  

---

# 3. Entendendo objetivos e atividades

## 3.1 O que o usuário está tentando conseguir no mundo real?

Não responda “usar o algoritmo”, “clicar no sistema” ou “ver o dashboard”.

**[F]** O tutor está tentando compreender a possível gravidade dos sinais apresentados pelo animal e decidir se precisa buscar atendimento veterinário emergencial, outro tipo de atendimento ou acompanhamento, sem confundir essa orientação inicial com diagnóstico profissional.

## 3.2 Quais são as atividades mais importantes?

| ID | Atividade/objetivo | Quem realiza | Frequência/criticidade inicial | Status/evidência |
|---|---|---|---|---|
| A01 | Observar e descrever os sinais físicos e comportamentais do animal | Tutor | Ocorre no início de toda pré-triagem; criticidade alta | **F** TCC, seções IV.C e IV.K |
| A02 | Informar dados contextuais do animal e responder perguntas complementares | Tutor | Frequente durante a pré-triagem; criticidade alta | **F** coleta híbrida está prevista; quais perguntas são indispensáveis ainda deve ser investigado |
| A03 | Compreender o possível nível de urgência, a justificativa e as limitações da orientação | Tutor | Ocorre ao final da análise; criticidade muito alta | **F** TCC, seções IV.A, IV.K e VII |
| A04 | Decidir e executar o próximo passo de cuidado | Tutor | Condicional ao resultado; criticidade muito alta | **F** TCC, Resumo e seção IV.J |
| A05 | Localizar uma clínica adequada quando houver possível emergência | Tutor | Condicional; criticidade alta | **F** TCC, seções IV.J e IV.K |
| A06 | Receber e interpretar um resumo inicial do caso encaminhado | Atendente ou médico-veterinário | Condicional a emergência e compartilhamento; criticidade alta | **H** H05; estrutura MIST é prevista, mas o fluxo da clínica não foi validado |

## 3.3 Qual atividade parece mais frequente? Por quê?

**[H]** A01, descrever os sinais observados, parece ser a atividade mais frequente porque constitui a entrada obrigatória de todas as pré-triagens, enquanto localização de clínica e encaminhamento só ocorrem em determinados resultados. Essa conclusão deriva do fluxo projetado, e a frequência real de uso ainda não foi medida.

## 3.4 Qual parece mais crítica? Que consequência existe se for mal executada?

**[F]** A03 e A04 são as atividades mais críticas: o tutor precisa compreender a orientação e decidir o próximo passo. Se a urgência for subestimada ou a mensagem gerar falsa segurança, pode haver atraso na procura por atendimento; se for superestimada, pode ocorrer encaminhamento desnecessário e maior pressão sobre serviços emergenciais. A prioridade de reduzir falsas não emergências está refletida no protocolo de avaliação do TCC. 

---

# 4. Entendendo o problema ou processo atual

## 4.1 Como essas atividades são realizadas hoje, antes da interface imaginada na disciplina?

Pode existir software concorrente, linha de comando, planilha, notebook, script, painel técnico, processo manual, consulta a logs, análise visual, troca de mensagens, decisão por especialista etc.

**[F]** A alternativa clinicamente adequada é o contato e a avaliação por um serviço veterinário, que realiza triagem e define a prioridade com base em sinais e critérios clínicos.  

**[F]** Serviços de telemedicina veterinária já são utilizados como forma de orientação remota em situações percebidas pelos tutores como emergências.  

**[H] H07** Quando não conseguem contato imediato com um profissional, tutores podem recorrer a buscas na internet, redes sociais, mensagens, ligações para clínicas ou avaliação própria antes de decidir pelo deslocamento. A importância relativa de cada alternativa no público-alvo ainda deve ser investigada.

## 4.2 O que é difícil, demorado, confuso, repetitivo, arriscado ou pouco transparente?

**[F]** É difícil traduzir sinais descritos em linguagem cotidiana para conceitos clínicos e distinguir uma emergência de uma situação menos urgente sem avaliação especializada. 

**[F]** Respostas produzidas por LLMs podem parecer convincentes mesmo quando estão incorretas ou omitem informações clinicamente relevantes, o que torna arriscado o uso de soluções generalistas sem mecanismos adicionais de recuperação e controle. 

**[H]** Para o tutor, comparar fontes divergentes, avaliar a credibilidade de uma orientação e repetir o relato para diferentes contatos pode tornar o processo mais demorado e confuso. Essa percepção ainda deverá ser investigada com usuários.

## 4.3 Que informações o profissional precisa interpretar para tomar decisão?

**[F]** O profissional precisa interpretar espécie, idade e contexto do animal; sinais relatados; início e evolução do quadro; alterações de respiração, circulação e consciência; presença de hemorragia, trauma, dor ou outros sinais de risco; histórico relevante; e necessidade de estabilização e transporte. 

**[H]** Para receber um caso encaminhado, a clínica também poderá precisar saber localização, tempo estimado de chegada e quais informações ou medidas já foram comunicadas ao tutor. A utilidade e a forma desses dados ainda precisam ser confirmadas com profissionais.

## 4.4 O que acontece quando a atividade falha ou quando o resultado é interpretado incorretamente?

**[F]** Uma falsa não emergência pode atrasar o atendimento de um animal em condição crítica. Uma falsa emergência pode gerar deslocamento e uso desnecessário de um serviço emergencial. Uma orientação ambígua ou sem fundamento pode causar falsa segurança, ansiedade ou execução de uma ação inadequada. Por essa razão, o TCC prioriza métricas sensíveis aos falsos negativos, fidelidade às evidências e revisão das respostas.

## 4.5 Conte uma situação concreta.

Escreva uma pequena narrativa com pessoa, objetivo, atividade, contexto, dificuldade e consequência. **Não descreva ainda a futura solução.**

**[H]** Durante a noite, uma tutora percebe que seu cão está ofegante, mais quieto do que o normal e apresenta mudança na coloração da língua. Ela não conhece os termos clínicos associados a esses sinais e não sabe se deve aguardar, procurar uma clínica no dia seguinte ou se deslocar imediatamente até um hospital veterinário 24 horas. Ao buscar orientação, encontra explicações com diferentes níveis de detalhe e credibilidade, enquanto precisa observar o animal, organizar o transporte e tomar uma decisão sob pressão. Caso subestime a gravidade, o atendimento pode ser atrasado; caso não consiga explicar claramente o quadro, a comunicação inicial com a clínica também pode ficar incompleta. A situação é plausível e baseada nos sinais de exemplo e no contexto de urgência discutidos no TCC, mas deverá ser refinada com dados de usuários.

## 4.6 Que evidência existe hoje?

| Evidência/fonte | O que sustenta | Limitação |
|---|---|---|
| Fortin-Choquette et al. [10], citado na Introdução do TCC | Tutores valorizam orientação remota inicial em situações percebidas como emergenciais | Estudo específico de telemedicina; não valida diretamente a interface proposta |
| Pasteur et al. [33], citado na Introdução do TCC | Existem barreiras de acesso ao cuidado veterinário | Não descreve sozinho o comportamento do público brasileiro da plataforma |
| Ruys et al. [36] e Thomovsky et al. [37], seção II.B do TCC | A triagem deve reconhecer gravidade e priorizar atendimento | Literatura clínica; não descreve a experiência do tutor com uma interface digital |
| Hanel et al. [17], seção II.B do TCC | Sinais críticos e prioridades do cuidado pré-hospitalar veterinário | Recomendações clínicas não substituem pesquisa de IHC com usuários |
| Huang e Chueh [19], seção II.C do TCC | Precisão, completude e utilidade influenciam a aceitação de chatbots veterinários | Avalia intenção de uso; não comprova a usabilidade do protótipo da equipe |
| Artigo do próprio TCC, seções IV.C, IV.J e IV.K | Define os usuários e recursos inicialmente previstos | Documento de proposta; várias decisões ainda são hipóteses a validar |

---

# 5. Entendendo o contexto de uso

## 5.1 Onde e em quais situações a interação poderia ocorrer?

**[H] H08** A interação poderá ocorrer em casa, na rua, durante uma viagem ou no trajeto para uma clínica, geralmente quando o tutor percebe uma alteração e ainda não possui orientação profissional imediata.

**[F]** O contexto considerado pelo TCC é o intervalo entre a percepção dos sinais e o encaminhamento ao atendimento profissional, inclusive em situações percebidas como urgentes. 

## 5.2 Em quais dispositivos/equipamentos?

**[F]** O TCC concebe a entrada do usuário como uma aplicação com experiência próxima à de dispositivos móveis e prevê entrada por texto e áudio. 

**[H]** O smartphone será o dispositivo prioritário, por permitir uso próximo ao animal, gravação de voz e geolocalização. A predominância desse dispositivo entre os usuários-alvo ainda deve ser confirmada.

## 5.3 Existem condições físicas relevantes?

Considere iluminação, ruído, mobilidade, conexão, privacidade, uso compartilhado, interrupções, pressão de tempo etc.

**[H]** Podem existir pouca iluminação, ruído, mãos ocupadas ao conter ou transportar o animal, movimento, interrupções, conexão instável, pressão de tempo e dificuldade para digitar. Essas condições justificam investigar entrada por voz, alvos de toque adequados, recuperação de sessão e mensagens curtas, mas ainda precisam ser verificadas com usuários.

**[F]** Áudio pode facilitar a captura do relato em situações de estresse, embora a qualidade da transcrição dependa de sotaque, ruído e condições acústicas.

## 5.4 Existem fatores sociais ou organizacionais?

Considere papéis, chefias, equipes, permissões, aprovação, responsabilidade profissional, auditoria, turnos e colaboração.

**[F]** O tutor fornece observações, mas a avaliação clínica e a responsabilidade pelo atendimento permanecem com o médico-veterinário; o sistema não deve se apresentar como substituto profissional.

**[H]** Clínicas podem possuir fluxos, equipes, especialidades, horários e capacidades diferentes. Portanto, proximidade geográfica poderá não ser o único critério de encaminhamento.

**[?]** Ainda não sabemos quem dentro da clínica, receberia o caso, validaria a disponibilidade ou responderia ao tutor, nem como o sistema se integraria ao fluxo organizacional existente.

## 5.5 Existe necessidade de histórico, rastreabilidade ou auditoria?

**[F]** Sim. A proposta depende de evidências recuperadas, versão da base e explicações fundamentadas, tornando necessário registrar quais informações apoiaram a orientação. O TCC também prevê possível armazenamento de histórico clínico e vacinação. 

**[H]** Para uso real, também poderá ser necessário registrar data e hora, relato original e transcrição, respostas fornecidas, classificação, versão do modelo, documentos utilizados, encaminhamento e compartilhamento com a clínica.

**[?]** Ainda devem ser definidos prazos de retenção, acesso, correção, exclusão e nível de detalhamento visível para tutor, clínica, administrador e pesquisador.

## 5.6 Um erro pode produzir consequência relevante? Qual?

**[F]** Sim. A subestimação de um caso grave pode atrasar atendimento; a superestimação pode produzir encaminhamento e ansiedade desnecessários; uma transcrição incorreta pode alterar o sentido do relato; uma justificativa sem evidência pode induzir confiança indevida; e um encaminhamento para uma clínica indisponível pode aumentar o tempo até o atendimento.

---

# 6. Entendendo mercado e alternativas existentes

> Nesta entrega faça apenas um **levantamento inicial**. A análise aprofundada ocorre na Entrega 2.

## 6.1 Como pessoas resolvem problemas semelhantes hoje?

| Alternativa atual | Quem usa | Para quê | Status/evidência |
|---|---|---|---|
| Contato direto com clínica ou hospital veterinário | Tutores | Relatar o caso e solicitar orientação ou atendimento | **F** atendimento profissional é o fluxo de referência |
| Consulta veterinária presencial ou emergencial | Tutores e profissionais | Realizar triagem, exame e definição clínica | **F** TCC seção II.B |
| Telemedicina veterinária | Tutores e veterinários | Obter orientação remota inicial | **F** Fortin-Choquette et al. [10], citado no TCC |
| Chatbots ou consultas digitais veterinárias | Tutores | Obter informação ou orientação conversacional | **F** existência do contexto de consulta veterinária por chatbot |
| Mecanismos de busca, redes sociais e conteúdos gerais | Tutores | Procurar explicações sobre sinais observados | **H** H07, frequência e confiabilidade percebida ainda devem ser investigadas |
| Avaliação própria e apoio de familiares | Tutores | Decidir se aguardam ou buscam atendimento | **H** prática plausível ainda sem evidência direta no público do projeto |

## 6.2 Existem produtos que atuam na mesma área, mesmo sem serem equivalentes ao TCC?

**[F]** Existem serviços de telemedicina, agentes conversacionais em saúde, chatbots de consulta veterinária, aplicações de saúde animal e plataformas de localização ou agendamento de clínicas. 

**[?]** Os produtos específicos que mais se aproximam do recorte brasileiro, suas funcionalidades, preços, limitações e padrões de interface ainda serão levantados sistematicamente na Entrega 2.

## 6.3 Quais interfaces profissionais esse público já conhece?

Exemplos possíveis: ferramentas de banco, IDEs, consoles de nuvem, dashboards, plataformas de dados, ferramentas de monitoramento, painéis de IA, sistemas administrativos.

**[H]** Para o tutor, interfaces possivelmente familiares incluem aplicativos de mensagens, mapas, busca, agendamento, atendimento por chat e aplicativos de saúde. Para profissionais, podem ser familiares sistemas de gestão de clínicas, prontuários, agendas e ferramentas de comunicação com clientes.

**[?]** Ainda não sabemos quais produtos e padrões são usados com maior frequência pelos tutores e clínicas que poderão participar da pesquisa.

## 6.4 O que essas soluções parecem fazer bem?

**[F]** A literatura indica que interfaces conversacionais e serviços remotos podem ampliar o acesso, permitir linguagem natural e apoiar o acolhimento inicial. 

**[H]** Aplicativos de mapas podem tornar localização, distância, rota e contato imediatamente reconhecíveis; aplicativos de mensagens podem oferecer um modelo familiar de conversa e envio de áudio. A adequação desses padrões à pré-triagem ainda será avaliada.

## 6.5 O que parecem fazer mal, dificultar ou não atender?

**[F]** Agentes conversacionais de saúde podem apresentar limitações de compreensão, repetitividade e adequação em situações sensíveis. LLMs generalistas também podem produzir respostas factualmente incorretas sem indicar claramente a falha. 

**[H]** Alternativas fragmentadas podem exigir que o tutor procure sintomas, verifique clínicas, explique novamente o caso e compare informações em canais diferentes. Essa dificuldade deverá ser investigada na Entrega 2 e com usuários.

## 6.6 Que padrões de interface ou vocabulário parecem familiares a esse público?

**[H]** Conversa em formato de chat, botão de microfone, reprodução e confirmação de áudio, cartões de resultado, marcadores de status, mapas, rotas, botão de ligação e compartilhamento são padrões possivelmente familiares ao tutor.

**[H]** Termos como “emergência”, “urgente”, “atendimento imediato”, “clínica 24 horas”, “ligar”, “rota” e “compartilhar caso” podem ser mais compreensíveis do que terminologia clínica isolada.

**[?]** Ainda precisamos verificar como os usuários interpretam categorias de urgência, cores, percentuais de confiança, justificativas e avisos de limitação.

---

# 7. Derivando o escopo de IHC da disciplina

## 7.1 Escolha o caminho do projeto

### Caminho A — TCC já possui interface

Explique qual parte da interface será usada como recorte da disciplina e por que esse fluxo é relevante.

O projeto seguirá o Caminho A, pois o TCC já prevê uma interface para o tutor. O recorte principal será a jornada que começa quando o tutor inicia uma pré-triagem, identifica ou cadastra o animal, relata os sinais por texto ou voz e fornece informações complementares. O fluxo termina quando o tutor compreende a classificação de urgência, sua justificativa, as limitações da orientação e o próximo passo; nos casos de possível emergência, inclui a localização de uma clínica adequada e a preparação ou compartilhamento do resumo do caso.

Esse fluxo foi escolhido porque concentra o objetivo humano central, ocorre em contexto potencialmente estressante, envolve tradução entre linguagem leiga e informação técnica e possui consequências relevantes quando a informação é omitida ou interpretada incorretamente. O recorte permite estudar comunicação, acessibilidade, prevenção de erros, confiança, feedback, recuperação e tomada de decisão sem confundir avaliação de IHC com avaliação da precisão clínica do modelo.

### Caminho B — TCC não possui interface prevista

Faça o exercício de transferência de uso:

> **Imagine que o TCC foi concluído com sucesso e uma empresa, laboratório ou organização quer transformar a contribuição em algo utilizável. Quem precisaria interagir com ela e para quê?**

Responda:

1. quem poderia contratar/adotar a solução? **clínicas, hospitais, serviços de telemedicina, organizações de cuidado animal ou responsáveis por uma plataforma de saúde veterinária.**
2. quem seria o usuário direto? **Tutor de cão ou gato; secundariamente, profissionais da clínica que recebem casos encaminhados.**
3. quem administraria/configuraria? **Equipe técnica e responsáveis pela curadoria veterinária.**
4. quem interpretaria resultados? **Tutor, atendente e médico-veterinário, com níveis de detalhe e responsabilidades diferentes.**
5. quem tomaria decisões? **O tutor decide procurar atendimento; a decisão clínica permanece com o médico-veterinário.**
6. quais dados/entradas seriam necessários? **Dados do animal, relato por texto ou voz, respostas complementares, contexto e localização quando autorizada.**
7. quais resultados deveriam ser compreendidos? **Possível nível de urgência, justificativa, limitações, próximos passos e informações da clínica indicada.**
8. que erros/rupturas seriam possíveis? **Áudio não compreendido, relato incompleto, dado inválido, conexão interrompida, evidência insuficiente, resultado incerto, clínica indisponível e interpretação equivocada da orientação.**

## 7.2 Qual perfil será priorizado no projeto de IHC?

Tutor adulto responsável por um cão ou gato que percebe sinais preocupantes e precisa decidir o próximo passo antes de obter avaliação veterinária presencial.

**Por que esse perfil foi escolhido?** É o usuário diretamente mencionado no objetivo e na interface prevista pelo TCC, inicia o fluxo de pré-triagem, fornece as informações das quais o sistema depende e precisa interpretar a saída em uma situação potencialmente crítica. As decisões de linguagem, entrada, feedback, explicabilidade, acessibilidade e encaminhamento afetam diretamente sua capacidade de completar a tarefa.

## 7.3 Qual objetivo desse usuário será priorizado?

Compreender a possível gravidade dos sinais apresentados pelo animal e decidir, com clareza e sem falsa segurança, qual próximo passo deve tomar para buscar o cuidado adequado.

## 7.4 Que interface será explorada na disciplina?

Complete:

> **Para fins da disciplina de IHC, será projetada uma interface que permita a `{{perfil}}` utilizar `{{capacidade/resultado do TCC}}` para `{{objetivo}}`, no contexto de `{{situação}}`.**

Para fins da disciplina de IHC, será projetada uma interface que permita ao **tutor de um cão ou gato** utilizar a **capacidade de interpretação de relatos e apoio à classificação inicial de urgência produzida pelo TCC** para **compreender a possível gravidade do caso e decidir o próximo passo**, no contexto de **dúvida sobre sinais observados, possível pressão emocional e necessidade de orientação rápida antes do atendimento veterinário**.

## 7.5 Qual é a relação dessa interface com o TCC?

- [x] Já fazia parte do TCC.
- [ ] É um aprofundamento de algo parcialmente previsto.
- [ ] É uma extensão conceitual criada para a disciplina.
- [ ] É um protótipo demonstrativo de aplicação potencial.
- [ ] Outra: não se aplica.

> **Declaração:** a interface desenvolvida nesta disciplina é um artefato de aprendizagem de IHC baseado no tema do TCC. Sua inclusão ou implementação no TCC somente ocorrerá se isso for posteriormente decidido pela equipe e pelo orientador.

Embora uma interface para o tutor já esteja prevista no escopo formal, os fluxos, modelos, protótipos e decisões de design produzidos na disciplina não serão automaticamente incorporados à implementação final. Essa incorporação dependerá da viabilidade técnica, das evidências obtidas e da decisão da equipe com o orientador.

---

# 8. Levantando possibilidades de interação — sem desenhar ainda

A equipe pode registrar possibilidades para investigação. **Não significa que todas serão implementadas.**

Marque apenas as que parecem plausíveis e explique o objetivo correspondente.

| Possibilidade | Pode fazer sentido? | Objetivo/tarefa que justificaria | Evidência atual |
|---|---|---|---|
| Dashboard/visão geral | não no fluxo prioritário | Não existe, neste momento, uma tarefa frequente do tutor que exija acompanhar vários indicadores simultaneamente | **H** manter fora do recorte até surgir evidência |
| Configuração/parametrização | não para o tutor | Parâmetros técnicos pertencem à operação e não devem aumentar a carga cognitiva da pré-triagem | **H** complexidade técnica existe, mas o papel administrativo não foi priorizado |
| Entrada/upload/seleção de dados | sim | Informar dados do animal, relatar sinais e, futuramente, anexar informações pertinentes | **F** entrada textual, por voz e dados contextuais prevista no TCC |
| Acompanhamento de processamento | sim | Saber que áudio, relato e análise estão sendo processados e o que fazer em caso de falha | **F** há processamento multimodal e latência; impacto de IHC ainda será modelado |
| Relatório/resultados | sim | Compreender urgência, justificativa, limitações e próximos passos | **F** previsto nas seções IV.A, IV.J e IV.K do TCC |
| Histórico com busca/filtros | talvez | Consultar triagens anteriores e informações recorrentes do animal | **H** histórico é previsto, mas volume, frequência e utilidade ainda não foram investigados |
| Comparação de resultados | não no fluxo do tutor | Comparação de experimentos pertence ao perfil de pesquisador, fora do recorte prioritário | **F** comparação integra a avaliação técnica do TCC |
| Explicabilidade/detalhamento | sim | Entender por que o caso recebeu determinada orientação e quais evidências a sustentam | **H** justificativas são previstas; formato compreensível ainda será investigado |
| Administração/configurações globais | não no recorte prioritário | Seria necessária à operação futura, não ao objetivo principal do tutor | **H** papel administrativo possível, mas fora do recorte |
| Usuários/perfis/permissões | talvez | Proteger dados e diferenciar tutor, profissional e administrador | **H** múltiplos papéis são plausíveis; necessidade ainda não detalhada |
| CRUD de entidade do domínio | talvez | Cadastrar e atualizar animal, responsável, histórico e vacinação | **H** cadastro e histórico são previstos; operações e riscos ainda não foram investigados |
| Auditoria/logs | talvez | Rastrear relato, transcrição, evidências, versão e orientação em situação crítica | **H** necessidade forte para segurança, mas interface e público não definidos |
| Alertas/ocorrências | sim | Comunicar sinais de possível emergência, incerteza, falha ou indisponibilidade | **H** criticidade prevista; semântica e intensidade dos alertas ainda serão avaliadas |
| Ajuda/documentação | sim | Explicar termos, como relatar sinais, limites da plataforma e ações disponíveis | **H** H06; conteúdo e momento adequados ainda serão investigados |

> **Atenção:** “login + dashboard + CRUD” não é uma solução universal. Cada padrão deve surgir de uma tarefa real.

---

# 9. Benefícios e ações iniciais

## 9.1 Qual benefício concreto o projeto de IHC pretende oferecer?

| Benefício esperado | Problema/necessidade | Usuário | Status/evidência |
|---|---|---|---|
| Facilitar a descrição do que está acontecendo com o animal | Tutor pode não conhecer a terminologia clínica ou ter dificuldade para digitar sob pressão | Tutor | **H** diferença linguística e entrada multimodal previstas; usabilidade ainda não avaliada |
| Tornar a orientação inicial compreensível e acionável | Classificação isolada pode não deixar claro o que fazer | Tutor | **H** H02; será investigado em cenários e testes |
| Comunicar incerteza e limites sem produzir falsa segurança | Sistemas de IA podem apresentar respostas plausíveis, porém incorretas | Tutor | **F** risco documentado no TCC; solução de comunicação ainda será projetada |
| Apoiar encaminhamento para atendimento adequado | Tutor precisa localizar e contatar uma clínica compatível com a situação | Tutor | **H** geolocalização prevista; critérios além da proximidade ainda são hipótese |
| Organizar informações relevantes antes da chegada | Relato pode estar disperso ou precisar ser repetido | Tutor e clínica | **H** H03 e H05 |

## 9.2 Que ações o usuário deverá conseguir realizar?

| ID | O usuário precisa conseguir... | Para alcançar... | Prioridade inicial |
|---|---|---|---|
| F01 | identificar ou cadastrar o animal relacionado ao caso | contextualizar a pré-triagem | média |
| F02 | relatar os sinais por texto ou voz | comunicar a situação com o menor atrito possível | alta |
| F03 | revisar a transcrição e corrigir informações | evitar que erro de áudio altere o caso | alta |
| F04 | responder perguntas complementares e informar sinais críticos | completar informações necessárias à análise | alta |
| F05 | acompanhar o estado da análise e recuperar-se de falhas | saber se o sistema está processando e não perder o relato | alta |
| F06 | compreender o possível nível de urgência, a justificativa e as limitações | tomar uma decisão informada | alta |
| F07 | visualizar um próximo passo claro | agir de acordo com a orientação inicial | alta |
| F08 | localizar, avaliar e contatar uma clínica adequada | buscar atendimento quando indicado | alta |
| F09 | revisar e compartilhar um resumo do caso | facilitar a comunicação com a clínica | média |
| F10 | consultar informações anteriores pertinentes | reutilizar contexto sem repetir dados desnecessariamente | baixa, até validação |

## 9.3 Tecnologias/restrições já definidas no TCC

A tecnologia aparece **agora**, depois do entendimento do uso.
| Tecnologia/restrição | Por que existe | Possível impacto na interação |
|---|---|---|
| Entrada por texto e voz com transcrição | Ampliar acessibilidade e facilitar o relato | Exige feedback de gravação, revisão da transcrição e recuperação de erro |
| LLM associado a RAG sobre base veterinária curada | Fundamentar respostas e reduzir dependência do conhecimento paramétrico | A interface deve comunicar evidências, limitações e possíveis incertezas sem expor complexidade desnecessária |
| Query Rewriting, HyDE, LightRAG, re-ranking e Self-Refine | Melhorar recuperação e consistência | Podem aumentar latência; exigem comunicação clara do estado do processamento |
| Classificação inicial de urgência, não diagnóstico | Delimitação clínica e ética do sistema | Mensagens devem evitar linguagem de certeza diagnóstica e reforçar o papel do veterinário |
| Geolocalização de clínicas | Apoiar encaminhamento | Requer consentimento para localização, alternativa manual e informações além da distância quando disponíveis |
| Resumo estruturado do caso | Melhorar comunicação inicial com a clínica | Deve permitir revisão pelo tutor e indicar o caráter preliminar das informações |
| Execução remota em VPS | Aumentar disponibilidade operacional | Depende de conexão e requer tratamento de indisponibilidade e retomada |
| Proteção de dados e LGPD | O fluxo pode tratar dados pessoais e histórico associado ao tutor | Exige minimização, consentimento, controle de acesso, transparência e regras de retenção |
| Prova de conceito em Streamlit | Viabilizar prototipação e avaliação inicial | Pode limitar comportamentos nativos de dispositivos móveis e deve ser tratado como protótipo, não produto final |

---

# 10. Hipóteses e dúvidas prioritárias

| ID | Hipótese/dúvida | Por que importa | Como poderá ser investigada |
|---|---|---|---|
| H01 | A ausência de orientação inicial acessível pode contribuir para atraso em casos graves ou procura inadequada de emergência | Fundamenta o problema humano e a utilidade do recorte | Entregas 2, 3 e 7; literatura, entrevistas e questionário |
| H02 | Tutores conseguem compreender as categorias de urgência e transformar o resultado em uma ação correta | Afeta a principal decisão da jornada | Entregas 3, 6, 7, 11 e 14 |
| H03 | Um resumo estruturado enviado previamente é útil para a clínica se preparar para receber o animal | Justifica a integração tutor–clínica | Entregas 2, 3 e 7; entrevista com profissionais |
| H04 | A plataforma pode reduzir o intervalo entre a percepção do sinal e a decisão de buscar atendimento | Representa um benefício esperado, mas não comprovado | Entregas 7 e 14; estudo com cenários e observação |
| H05 | Atendentes ou veterinários precisam consultar o caso, confirmar capacidade e continuar a comunicação com o tutor | Define se existirá uma interface secundária para clínica | Entregas 2, 3 e 7; análise de sistemas e entrevistas |
| H06 | Linguagem simples, ajuda contextual e entradas alternativas são necessárias para atender diferentes níveis de conhecimento e acessibilidade | Afeta conteúdo, navegação e formas de entrada | Entregas 3, 7, 8 e 14 |
| H07 | Tutores recorrem a busca, redes sociais, mensagens e ligações quando não conseguem contato profissional imediato | Orienta análise de concorrência e jornada atual | Entregas 2 e 7 |
| H08 | O uso ocorre principalmente pelo smartphone e pode acontecer em ambientes móveis, ruidosos ou com iluminação e conexão limitadas | Afeta plataforma, acessibilidade, feedback e recuperação | Entregas 3 e 7; questionário e observação contextual |
| H09 | Tutores consideram útil relatar sinais por voz em situações de estresse, desde que possam revisar a transcrição | Justifica entrada multimodal e fluxo de correção | Entregas 6, 7 e 14 |
| H10 | Proximidade não é o único critério relevante para escolher a clínica; disponibilidade, funcionamento 24 horas e capacidade de atendimento também importam | Afeta encaminhamento e informações exibidas | Entregas 2 e 7 |
| H11 | Justificativas em linguagem acessível aumentam a compreensão sem gerar confiança excessiva | Afeta explicabilidade e segurança | Entregas 6, 7, 8, 13 e 14 |
| H12 | Existe um limite de perguntas complementares aceitável antes que o tutor abandone ou perca tempo em situação urgente | Afeta duração, priorização e adaptação do diálogo | Entregas 5, 6, 7 e 14 |

Registre em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

---

# 11. Síntese da equipe

| Pergunta | Síntese atual |
|---|---|
| Qual é a contribuição central do TCC? | Interpretar relatos leigos, recuperar conhecimento veterinário especializado e apoiar a classificação inicial da urgência e o encaminhamento. |
| O TCC já previa interface? | Sim. Prevê interface com entrada por texto e voz, interação híbrida, resultado fundamentado e geolocalização. |
| Quem é o usuário prioritário de IHC? | Tutor adulto responsável por um cão ou gato com sinais percebidos como preocupantes. |
| O que ele precisa alcançar? | Compreender a possível gravidade do caso e decidir qual próximo passo deve tomar. |
| Qual problema/atividade será estudado? | Relatar sinais, complementar informações, interpretar urgência e agir corretamente sob possível pressão emocional. |
| Como isso acontece hoje? | Por avaliação veterinária presencial ou remota e, possivelmente, por busca, contato com clínicas e avaliação própria quando o acesso imediato não ocorre. |
| Qual é o contexto de uso? | Intervalo entre percepção dos sinais e atendimento, prioritariamente em dispositivo móvel, com possível estresse, urgência, ruído, movimento e conexão limitada. |
| Que interface/recorte será explorado? | Fluxo do tutor desde o início da pré-triagem até compreensão do resultado e, se necessário, encaminhamento e compartilhamento do caso. |
| Como a interface se relaciona ao TCC? | A interface do tutor já integra o escopo do TCC; a disciplina aprofundará sua concepção e avaliação sem tornar automaticamente obrigatórios todos os artefatos produzidos. |
| Quais pontos ainda são hipóteses? | H01–H12, especialmente compreensão das categorias, utilidade da voz, quantidade de perguntas, critérios de clínica e fluxo com profissionais. |

### Delimitação

**Dentro do escopo de IHC:** interação do tutor para identificar o animal, relatar sinais por texto ou voz, revisar transcrição, responder perguntas, acompanhar processamento, compreender urgência, justificativa, incerteza e próximos passos, localizar clínica e revisar/compartilhar o resumo inicial do caso.  
**Fora do escopo de IHC:** funcionamento interno dos algoritmos, treinamento de modelos, implementação integral da infraestrutura, avaliação da precisão clínica pela disciplina de IHC, painel experimental para pesquisadores, administração completa da base e sistema de gestão integral da clínica.  
**Dentro do escopo formal do TCC:** base veterinária curada, pipeline de RAG e LLM, entrada multimodal, classificação de urgência, avaliação experimental, interface de prova de conceito, geolocalização e resumo estruturado para encaminhamento.  
**Interface da disciplina será implementada no TCC?** não definido — o fluxo geral já integra o TCC, mas a incorporação dos modelos, telas e refinamentos produzidos em IHC dependerá da viabilidade e de decisão posterior da equipe e do orientador.

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

1. **Problema/atividade humana:** Tutores podem ter dificuldade para interpretar a gravidade dos sinais apresentados por seus animais e decidir quando buscar atendimento veterinário emergencial.
2. **Contribuição técnica do TCC:** O TCC investiga uma arquitetura de inteligência artificial capaz de interpretar relatos leigos, recuperar conhecimento veterinário especializado e apoiar a classificação inicial de urgência com maior rastreabilidade.
3. **Como uma pessoa poderia utilizar essa contribuição:** Por meio da interface, o tutor poderá relatar a situação por texto ou voz, compreender a orientação inicial e, quando necessário, localizar uma clínica e compartilhar um resumo do caso, sem substituir a avaliação veterinária profissional.

Essa síntese ajuda a apresentar o projeto para público não especializado sem reduzir seu mérito técnico.

---

# Checklist de qualidade

- [x] Está clara a diferença entre tema do TCC, escopo formal do TCC e escopo de IHC.
- [x] A equipe declarou se o TCC já previa interface.
- [x] Se não previa, foi derivado um usuário plausível e um objetivo de uso.
- [x] A interface de IHC não foi apresentada como obrigação automática do TCC.
- [x] A contribuição do TCC foi descrita sem começar por tecnologias de implementação.
- [x] Usuários diretos e stakeholders foram diferenciados.
- [x] Foram considerados profissionais que configuram, administram, interpretam ou decidem, quando pertinente.
- [x] Objetivo do usuário não foi confundido com objetivo do projeto.
- [x] Processo/problema atual foi descrito antes da solução.
- [x] Existe situação concreta de uso/problema.
- [x] Contexto físico, social/organizacional, dispositivos e consequências de erro foram considerados.
- [x] Mercado/alternativas existentes foram levantados inicialmente.
- [x] Possibilidades como dashboard, relatório, histórico, filtros e CRUD foram tratadas como hipóteses de solução, não como requisitos automáticos.
- [x] Cada possibilidade de interface tem um objetivo/tarefa que poderia justificá-la.
- [x] Afirmações relevantes estão marcadas `[F]`, `[H]` ou `[?]`.
- [x] Hipóteses prioritárias receberam IDs e foram para a rastreabilidade.
- [x] O recorte de IHC é viável para modelar, prototipar e avaliar no semestre.
- [x] A equipe consegue explicar problema humano → contribuição computacional → forma de uso.
