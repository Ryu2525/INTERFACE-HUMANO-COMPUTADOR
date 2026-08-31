# Entrega 2 — Público-alvo e análise de concorrência

**Data:** {{20/08/2026}}  
**Status:** 🟨 em andamento  
**Responsabilidade mínima:** cada integrante analisa pelo menos 1 concorrente/interface representativa; a equipe produz síntese comparativa.

## Objetivo da atividade

Compreender soluções do mesmo domínio **e também interfaces familiares ao público-alvo**. O objetivo não é copiar telas, mas identificar convenções, padrões, affordances percebidas, problemas recorrentes, expectativas e oportunidades de design.

> **Concorrente não precisa ser idêntico ao produto.** Pode atuar na mesma área, resolver objetivo semelhante ou disputar a mesma necessidade. Quando não houver concorrente direto, use produtos análogos e softwares que o público já utiliza.

### Para TCCs que não previam interface

Não procure apenas um “concorrente do algoritmo”. Investigue **interfaces profissionais que materializam atividades semelhantes** às que o usuário escolhido precisaria realizar.

Exemplos:

- TCC de banco de dados → consoles de administração, ferramentas para DBA, monitoramento e análise de consultas;
- TCC de LLM/ML → painéis de experimentos, gestão de modelos/datasets, comparação de métricas, revisão de resultados;
- TCC de análise de dados → dashboards, ferramentas de BI, filtros, relatórios e exploração;
- TCC de infraestrutura/API → portais administrativos, observabilidade, logs, gestão de credenciais e uso;
- TCC de cibersegurança → consoles de alertas, triagem, histórico e auditoria.

A pergunta é: **“que convenções esse perfil já conhece para executar tarefas equivalentes?”**

## Entrada obrigatória da Entrega 1

Retome o mapa inicial de alternativas e produtos citado na Entrega 1. Aqui a equipe deixa de trabalhar apenas com impressão inicial e passa a **investigar sistematicamente** cada solução.

| Item citado na Entrega 1 | Tipo | Por que foi citado | Status inicial | Decisão nesta entrega |
|---|---|---|---|---|
| Contato direto com clínica ou hospital veterinário | processo manual | É a alternativa de referência usada hoje por tutores para relatar casos e pedir orientação inicial. | F | analisar (para mapear atritos de tempo, comunicação e disponibilização de informações na triagem) |
|Consulta veterinária presencial ou emergencial | processo manual | É o fluxo oficial para triagem, exame e definição clínica do animal. | F | analisar (para entender o limiar onde o tutor decide se deslocar)|
|Telemedicina veterinária | concorrente | Utilizada como forma de orientação remota inicial quando o tutor percebe uma urgência. | F | analisar (como padrão de atendimento remoto e acolhimento) |
|Chatbots ou consultas digitais veterinárias | concorrente | Plataformas conversacionais que oferecem orientação sobre saúde animal por texto. | F | analisar (para identificar falhas comuns de LLMs/chatbots em contexto clínico) |
| Mecanismos de busca, redes sociais e conteúdos gerais | análogo | Canais não especializados aos quais os tutores recorrem na ausência de contato profissional imediato. | H (H07) | analisar (para entender a busca desestruturada de informação e os riscos de desinformação) |
| Avaliação própria e apoio de familiares | processo manual | Prática empírica dos tutores para tentar julgar se aguardam ou buscam atendimento. | H | analisar (para mapear a tomada de decisão sob ansiedade/pressão) |
| Aplicativos de mapas, rotas e localização (ex: Google Maps) | ferramenta cotidiana | Padrão conhecido pelos tutores para buscar serviços locais, distâncias e telefones em emergências. | H | analisar (para reaproveitar padrões de interface de localização e rotas de clínicas) |
| Aplicativos de mensagens (ex: WhatsApp) | ferramenta cotidiana | Padrão de interface familiar para conversa, gravação e envio de áudios. | H | analisar (como referência UX para entrada de áudio, transcrição e diálogo) |
| Sistemas de gestão de clínicas / prontuários | ferramenta cotidiana | Interfaces profissionais utilizadas por atendentes e veterinários no dia a dia da clínica. | H | descartar com justificativa (o perfil prioritário mantido na Entrega 2 é o tutor; a interface da clínica ficou fora do recorte principal de IHC nesta etapa) |

Se uma hipótese da Entrega 1 for confirmada ou refutada durante esta análise, atualize `H01`, `H02`... em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

## 1. Público-alvo desta análise

O público-alvo aqui é o tutor de cão ou gato que percebe algo errado com o animal e precisa saber rápido se é uma emergência e o que fazer. 

- Usuário principal: Escolhemos o tutor porque é ele quem passa pelo susto, descreve os sintomas e precisa decidir na hora se vai correndo pro veterinário ou não.
- O que ele busca: Ele quer entender a gravidade da situação e ter um norte sobre o próximo passo, sabendo que a plataforma dá uma orientação inicial e não um diagnóstico.
- Como e onde ele usa: É uma pessoa leiga em termos médicos, falando do jeito dela, no meio de uma situação estressante e usando o celular na correria.
- O que vamos validar: Queremos testar na prática as hipóteses que levantamos antes — como a tendência de buscar no Google na dúvida, a necessidade de uma linguagem bem simples, o uso pelo celular e o risco de demorar pra agir em casos graves.

## 2. Concorrentes diretos/indiretos

### Análise C01 — Vetster (Módulo de Teletriage)

**Autor(a):** Julian Ryu Takeda RA:22.224.030-1  
**Tipo:** direto / análogo  
**Link oficial:** https://vetster.com 
**Data de acesso:** 26/08/2026

#### Contexto e proposta

A Vetster é uma plataforma global de telemedicina e teletriage veterinária que conecta tutores de pets a médicos-veterinários licenciados. O foco do serviço de teletriage é responder à dúvida imediata do tutor: "Meu pet precisa ir ao veterinário agora ou posso aguardar?" Ela busca orientar o tutor sobre o nível de urgência, diminuindo ida desnecessária à clínica e reduzindo o tempo de tomada de decisão em casos graves.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print | Observação de IHC |
|---|---|---|---|
| Cadastro prévio e histórico do pet | Formulário no início da triagem para registrar perfil, peso, histórico e adicionar informações dos animais. | <img width="1905" height="876" alt="image" src="https://github.com/user-attachments/assets/0668c048-ccac-4ed2-a7ad-3a0bfb74c8e2" /> | Reduz atrito na consulta, mas formulários extensos sob emergência podem gerar fadiga e ansiedade no tutor. |
| Navegação inicial por áreas categorizadas | Categorização clara na tela inicial por tipo de sintoma, espécie e urgência. | <img width="1906" height="863" alt="image" src="https://github.com/user-attachments/assets/9b548585-c97f-4cee-91b2-f2adcd878643" /> | Design intuitivo que reduz a carga cognitiva do usuário em momento de dúvida ou crise. |
| Chamada para ação (CTA) para atendimento veterinário | Botão destacado e explícito para agendar ou conectar imediatamente com um médico-veterinário. | <img width="1733" height="120" alt="image" src="https://github.com/user-attachments/assets/1d6dd94e-0cdd-4f3c-b970-2ea0d57793fa" /> | Evita que o tutor perca tempo procurando o próximo passo (ótima prática de afordância). |
| Vitrine de profissionais com preço, datas e avaliações | Lista de veterinários com notas de outros tutores, horários disponíveis e valores da consulta. | <img width="1917" height="872" alt="image" src="https://github.com/user-attachments/assets/f9ca8c90-9ec6-48bb-98bc-a248de953b35" /> | Traz transparência e confiança ao tutor, permitindo escolha baseada em reputação e custo. |

#### Experiência do usuário e opiniões

Avaliações de tutores nas lojas de aplicativos e plataformas de review destacam que a plataforma traz muita tranquilidade ao tirar dúvidas de emergência sem precisar sair de casa à noite. Por outro lado, tutores em situações de extrema urgência relatam frustração quando há demora no agendamento ou na conexão com o profissional, reforçando a necessidade de uma resposta automatizada e instantânea no primeiro contato.

#### Preço/modelo de negócio

Modelo pago por consulta/atendimento virtual (pay-per-visit) ou planos de assinatura corporativa/planos de saúde pet.

#### Padrões e tendências percebidos

Uso de interface estilo chat/videocall simples, acompanhada de cartões com status de urgência destacados por cores e compartilhamento de arquivos de resumo clínico (PDF/DAP)

#### Pontos positivos, limitações e lições

| Ponto | Evidência | Implicação para nosso projeto |
|---|---|---|
| Ponto Positivo: Navegação intuitiva e categorização clara das áreas no início da triagem. | Telas iniciais organizadas por sintomas e áreas clínicas, facilitando o fluxo antes do atendimento. | Reforça a importância de organizar os sintomas de forma legível e sem termos técnicos complexos para o tutor. |
| Ponto Positivo: Botão de ação para consulta/atendimento em destaque explícito. | Elemento visual chamativo e de fácil acesso para acionar o profissional sem distrações na tela. | Devemos manter um botão principal bem evidente para o próximo passo (ex: Encaminhar, Localizar Clínica ou Ver Orientação). |
| Ponto Positivo: Transparência com avaliações, horários e valores visíveis. | O tutor visualiza notas de outros usuários, preços e dias disponíveis antes de decidir. | Traz confiança ao tutor. Para nosso projeto de geolocalização de clínicas, devemos exibir dados úteis como status 24h e proximidade. |
| Limitação: Foco exclusivo no agendamento pago com humano, sem resposta automatizada em tempo real. | O tutor precisa escolher um profissional e agendar um horário para ter a triagem inicial. | Deixa uma lacuna em emergências imediatas. Nosso sistema com IA/RAG supre essa limitação ao dar um retorno instantâneo no momento do susto. |
| Lição de IHC: Cadastro do pet e do tutor antes da consulta antecipa o contexto. | A plataforma coleta dados prévios do animal para alimentar o atendimento. | Devemos permitir o cadastro do pet (F01), mas garantindo que isso seja opcional ou muito rápido para não travar o tutor em uma emergência grave. |

> Repita a subseção para C02, C03... até atender à quantidade da equipe.

## 3. Softwares que o público-alvo usa no cotidiano

Analise interfaces que moldam a expectativa do público, mesmo que não sejam concorrentes.

| Software | Por que o público usa | Padrões relevantes | Prints | O que aprender |
|---|---|---|---|---|
| {{...}} | {{...}} | {{...}} | {{link local}} | {{...}} |

## 3.1 Padrões de interface relevantes ao escopo de IHC

Registre somente padrões encontrados nas soluções analisadas e que possam ter relação com objetivos reais da equipe.

| Padrão observado | Produto(s) | Para qual tarefa serve | Vantagem percebida | Risco/limitação | Aplicável ao nosso escopo? |
|---|---|---|---|---|---|
| dashboard | {{...}} | {{...}} | {{...}} | {{...}} | sim/não/talvez |
| relatório | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| histórico + filtros | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| administração/CRUD | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| comparação de resultados | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

> O objetivo não é concluir “todo concorrente tem dashboard, então teremos um”. O padrão só será adotado se apoiar uma tarefa rastreável.

## 4. Síntese comparativa da equipe

| Critério | C01 | C02 | C03 | Oportunidade para o projeto |
|---|---|---|---|---|
| Navegação | Estrutura clara por categorias de sintomas e áreas clínicas na tela inicial, mas exige fluxo longo de cadastro e agendamento antes da orientação. |  |  |  |
| Feedback/estado | Atualizações por e-mail/notificação sobre agendamento e status da consulta com o profissional. |  |  |  |
| Prevenção/recuperação de erro |  Validação de campos de formulário e revisão de dados do pet antes de confirmar o agendamento. |  |  |  |
| Terminologia | Uso de termos amigáveis para tutores na seleção de sintomas, mantendo dados clínicos estruturados no resumo final. |  |  |  |
| Acessibilidade | Interface limpa em mobile/web com boa visibilidade de botões principais de ação. |  |  |  |
| Eficiência | Depende do tempo de espera por um veterinário disponível para realizar a triagem humana. |  |  |  |

## 5. Recomendações derivadas

Liste recomendações com origem explícita.

- **RC01:** {{recomendação}} — derivada de {{C01/C02/evidência}}.
- **RC02:** {{...}}

## Referências

{{fontes dos produtos, avaliações e literatura}}

## Checklist

- [ ] O mapa inicial de alternativas da Entrega 1 foi revisitado e aprofundado.
- [ ] Hipóteses relevantes sobre mercado/padrões foram atualizadas na rastreabilidade quando surgiram evidências.
- [ ] Há pelo menos uma análise completa por integrante.
- [ ] Cada análise contém prints legíveis da interface.
- [ ] Prints mostram telas/estados relevantes, não apenas logos/homepage.
- [ ] Foram analisados concorrentes e/ou interfaces representativas ao público.
- [ ] Em TCC sem interface original, foram investigadas ferramentas profissionais análogas às atividades do usuário escolhido.
- [ ] Padrões como dashboard, relatório, filtros e CRUD foram analisados como soluções para tarefas, não como requisitos automáticos.
- [ ] Opiniões de UX têm fonte.
- [ ] A síntese compara critérios comuns e produz recomendações.
- [ ] Não há “copiar porque o concorrente faz”; há justificativa de adequação ao público/contexto.
