# Matriz de rastreabilidade de IHC

A matriz deve ser atualizada ao longo do semestre. Ela ajuda a demonstrar que a interface não surgiu arbitrariamente e registra **como o conhecimento da equipe evoluiu**.

Para projetos cujo TCC não previa interface, esta matriz é especialmente importante: deve ficar visível a passagem da **contribuição técnica do TCC** para um **cenário de uso plausível**, e desse cenário para as decisões de interação.

## 1. Derivação do escopo de IHC a partir do TCC

| Elemento | Registro da equipe | Evidência/justificativa | Estado |
|---|---|---|---|
| Tema do TCC | Plataforma inteligente de pré-triagem e apoio à decisão em emergências veterinárias utilizando RAG e modelos de linguagem de grande escala | TCC, título, Resumo e Introdução | definido |
| Resultado técnico esperado | Prova de conceito de um sistema interativo composto por interface para o tutor, arquitetura de LLM associada a RAG, base veterinária curada, serviços de backend e avaliação experimental das técnicas utilizadas | TCC, Resumo e seções IV.A, IV.H, IV.I, IV.J e IV.K | definido |
| O TCC previa interface? | Sim | O TCC prevê uma interface com experiência próxima à de uma aplicação móvel, com entrada por texto e voz, interação híbrida, apresentação da possível urgência e encaminhamento. Fonte: TCC, seções IV.C, IV.D, IV.J e IV.K | definido |
| Capacidade/contribuição central | Interpretar relatos leigos sobre sinais observados em cães e gatos, recuperar conhecimento veterinário especializado e apoiar a classificação inicial da urgência e o encaminhamento | TCC, Resumo, Introdução e seções IV.A, IV.E, IV.F e IV.G | definido |
| Possíveis beneficiários/stakeholders | Tutor como beneficiário direto; animal, clínicas, atendentes, médicos-veterinários, responsáveis pela curadoria, administradores técnicos e pesquisadores como possíveis beneficiários ou stakeholders | Tutor: **F**, conforme TCC, Resumo e seção IV.C. Demais perfis: **F**, **H** ou **?**, conforme detalhamento da Entrega 1, seções 2.2 e 2.3 | F / H / ? |
| Usuário escolhido para IHC | Tutor adulto responsável por um cão ou gato que percebe sinais preocupantes e precisa decidir o próximo passo antes de obter avaliação veterinária presencial | O tutor é o usuário diretamente mencionado no objetivo e na interface prevista pelo TCC. Fonte: TCC, Resumo e seções IV.C e IV.K | F |
| Objetivo principal do usuário | Compreender a possível gravidade dos sinais apresentados pelo animal e decidir, com clareza e sem falsa segurança, qual próximo passo tomar para buscar o cuidado adequado | Objetivo derivado da proposta do TCC e consolidado na Entrega 1, seções 3.1 e 7.3 | F |
| Contexto de uso adotado | Intervalo entre a percepção dos sinais e o atendimento profissional, prioritariamente por dispositivo móvel e em situação que pode envolver dúvida, pressão emocional, ruído, movimento ou conexão limitada | O intervalo entre percepção e atendimento é **F**, conforme TCC, Resumo e Introdução. As condições específicas de uso são **H**, registradas em H08 | F / H |
| Interface/recorte de IHC | Fluxo do tutor desde a identificação do animal e o relato por texto ou voz até a compreensão da classificação, da justificativa e do próximo passo; em possível emergência, inclui localização de clínica e preparação ou compartilhamento do resumo do caso | O recorte utiliza a interface já prevista no TCC e prioriza as atividades A01–A05 da Entrega 1 | proposta |
| Relação com o TCC | Parte já prevista no TCC, aprofundada na disciplina sob a perspectiva de usuários, tarefas, contexto, comunicação, acessibilidade e usabilidade | TCC, seção IV.K, e Entrega 1, seções 0.5 e 7.5 | definido |

> Se o escopo de IHC mudar ao longo do semestre, preserve a decisão anterior no histórico e registre **qual evidência motivou a mudança**.

## 2. Registro de hipóteses e lacunas da Entrega 1

Use esta tabela para itens importantes marcados como `[H]` ou `[?]`. Preserve o histórico: não apague uma hipótese refutada.

| ID | Afirmação / dúvida inicial | Tipo | Por que importa | Como/onde investigar | Evidência obtida | Estado atual | Impacto no projeto |
|---|---|---|---|---|---|---|---|
| H01 | A ausência de orientação inicial acessível pode contribuir para atraso em casos graves ou procura inadequada por atendimento emergencial | H | Fundamenta o problema humano e a utilidade do recorte de IHC | Entregas 2 e 7; revisão de literatura, questionário e entrevistas com tutores | PENDENTE | aberta | Se refutada, será necessário revisar a formulação do problema e os benefícios atribuídos à interface |
| H02 | Tutores conseguem compreender as categorias de urgência e transformar o resultado apresentado em uma ação adequada | H | Afeta a principal decisão do usuário e a segurança da interação | Entregas 3, 6, 7, 11 e 14; protótipos, questionário e testes de usabilidade | PENDENTE | aberta | Pode alterar nomes, cores, explicações, alertas e próximos passos apresentados |
| H03 | Um resumo estruturado enviado previamente é útil para a clínica se preparar para receber o animal | H | Justifica a integração entre tutor e clínica e o compartilhamento do caso | Entregas 2, 3 e 7; análise de concorrentes e entrevistas com profissionais | PENDENTE | aberta | Pode justificar, modificar ou retirar o fluxo de envio do resumo à clínica |
| H04 | A plataforma pode reduzir o intervalo entre a percepção dos sinais e a decisão de buscar atendimento | H | Representa um dos principais benefícios esperados da proposta | Entregas 7 e 14; investigação da percepção dos usuários e observação em cenários simulados | PENDENTE | aberta | Se não houver evidência, o benefício deverá ser reformulado sem afirmar redução de tempo |
| H05 | Atendentes ou médicos-veterinários precisam consultar o caso, confirmar capacidade de atendimento e continuar a comunicação com o tutor | H | Define se será necessária uma interface secundária para profissionais da clínica | Entregas 2, 3 e 7; análise de sistemas veterinários e entrevistas com profissionais | PENDENTE | aberta | Pode incluir, reduzir ou retirar a interface da clínica do escopo de IHC |
| H06 | Linguagem simples, ajuda contextual e entradas alternativas são necessárias para atender diferentes níveis de conhecimento e acessibilidade | H | Afeta conteúdo, vocabulário, navegação, ajuda e formas de entrada | Entregas 3, 7, 8 e 14; personas, questionário e testes com usuários | PENDENTE | aberta | Pode gerar requisitos de linguagem, acessibilidade e ajuda contextual |
| H07 | Tutores recorrem a mecanismos de busca, redes sociais, mensagens e ligações quando não conseguem contato profissional imediato | H | Orienta a descrição do processo atual, a jornada e a análise de alternativas | Entregas 2 e 7; análise de alternativas, questionário e entrevistas | PENDENTE | aberta | Pode alterar a jornada atual e os concorrentes ou produtos análogos analisados |
| H08 | O uso ocorrerá principalmente por smartphone e poderá acontecer em ambientes móveis, ruidosos ou com iluminação e conexão limitadas | H | Afeta plataforma, acessibilidade, tamanho dos controles, feedback e recuperação de sessão | Entregas 3 e 7; questionário e investigação do contexto de uso | PENDENTE | aberta | Pode alterar a plataforma prioritária e os requisitos de interação |
| H09 | Tutores consideram útil relatar sinais por voz em situações de estresse, desde que possam revisar e corrigir a transcrição | H | Justifica a entrada multimodal e a necessidade de um fluxo de correção | Entregas 6, 7 e 14; protótipo em papel, questionário e teste de usabilidade | PENDENTE | aberta | Pode manter, modificar ou retirar a entrada por voz do fluxo prioritário |
| H10 | Proximidade não é o único critério relevante para escolher uma clínica; disponibilidade, funcionamento 24 horas e capacidade de atendimento também importam | H | Afeta as informações apresentadas e a lógica de encaminhamento | Entregas 2 e 7; análise de plataformas, questionário e entrevistas | PENDENTE | aberta | Pode alterar filtros, ordenação e informações apresentadas sobre as clínicas |
| H11 | Justificativas em linguagem acessível aumentam a compreensão da orientação sem gerar confiança excessiva | H | Afeta explicabilidade, segurança, confiança e interpretação do resultado | Entregas 6, 7, 8, 13 e 14; protótipos, coleta de dados, avaliação heurística e testes | PENDENTE | aberta | Pode alterar o formato, nível de detalhe e posicionamento das justificativas |
| H12 | Existe um limite de perguntas complementares aceitável antes que o tutor abandone a interação ou perca tempo em uma situação urgente | H | Afeta duração, priorização das perguntas e adaptação do diálogo | Entregas 5, 6, 7 e 14; análise de tarefas, protótipos, questionário e testes | PENDENTE | aberta | Pode reduzir, reorganizar ou tornar adaptativas as perguntas da pré-triagem |

## 3. Rastreabilidade entre contribuição técnica, necessidades e artefatos

| ID | Capacidade do TCC utilizada | Necessidade/problema | Persona | Cenário problema | Objetivo/tarefa | HTA/GOMS/CTT | Cenário de interação / signos | MoLIC | Tela(s) Figma | Heurística / problema | Tarefa no teste | Decisão/melhoria |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | Interpretação de relatos leigos e classificação inicial de urgência | Tutor precisa descrever os sinais e compreender a possível gravidade do caso — H01 e H02 | PENDENTE | PENDENTE | A01, A03 e A04 da Entrega 1; tarefas T ainda PENDENTES | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE |
| R02 | Entrada por voz e conversão de fala em texto | Tutor pode precisar relatar sinais em situação de estresse, ruído ou dificuldade para digitar — H08 e H09 | PENDENTE | PENDENTE | A01 e A02 da Entrega 1; tarefa T PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE |
| R03 | Recuperação de evidências e geração de justificativas | Tutor precisa compreender a orientação sem receber falsa segurança — H02 e H11 | PENDENTE | PENDENTE | A03 da Entrega 1; tarefa T PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE |
| R04 | Geolocalização e identificação de clínicas | Tutor precisa localizar uma clínica adequada quando houver possível emergência — H10 | PENDENTE | PENDENTE | A05 da Entrega 1; tarefa T PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE |
| R05 | Geração e compartilhamento de resumo estruturado | Tutor e clínica podem precisar organizar as informações do caso antes da chegada — H03 e H05 | PENDENTE | PENDENTE | A06 da Entrega 1; tarefa T PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE |

## 4. Rastreabilidade de padrões de interface

Use esta tabela quando o projeto incorporar padrões como dashboard, relatório, histórico, filtros ou administração. O objetivo é **justificar o padrão**, não apenas listar telas.
| ID da tela/fluxo | Padrão de interface | Objetivo/tarefa que justifica | Informação/ação principal | Evidência de necessidade | Artefatos relacionados |
|---|---|---|---|---|---|
| PENDENTE | Padrões de interface ainda não definidos | Serão definidos após o aprofundamento de usuários, concorrentes, cenários e tarefas | As possibilidades iniciais estão registradas na seção 8 da Entrega 1 | H02, H03, H05, H08, H09, H10, H11 e H12 ainda estão abertas | Entrega 1; próximas definições nas Entregas 2, 5, 6, 9, 10 e 11 |

## 5. Registro de mudanças de escopo

| Data | O que mudou | Evidência/feedback que motivou | Artefatos afetados | Responsável |
|---|---|---|---|---|
| 23/08/2026 | Definição inicial do escopo de IHC: priorização do tutor e do fluxo de pré-triagem até a orientação e o possível encaminhamento | TCC e consolidação realizada na Entrega 1 | Entrega 1 e Matriz de Rastreabilidade | Equipe |

## Como usar

- Use identificadores estáveis (`H01`, `P01`, `C01`, `T01`, `M01`, `F01`, `UT01`).
- Quando uma necessidade/problema tiver origem em hipótese da Entrega 1, cite o ID correspondente.
- Em TCC sem interface original, pelo menos uma linha deve mostrar claramente **como uma capacidade técnica chega até uma tarefa de usuário e uma tela/fluxo**.
- Uma linha pode se desdobrar quando um objetivo possui múltiplos caminhos.
- Não force relação inexistente: se algo ainda não foi modelado, marque `PENDENTE`.
- Ao remover uma funcionalidade, registre a decisão em vez de apagar silenciosamente o histórico.
- Dashboard, CRUD, filtros e relatórios só devem aparecer quando houver objetivo/tarefa que os justifique.
