# Entrega 2 — Público-alvo e análise de concorrência

**Data:** 31/08/2026  
**Status:** 🟩 concluída  
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

### Análise C02 — Joii Pet Care

**Autor(a):** João Pedro Gardenghi Peterutto — RA: 22.125.066-5  
**Tipo:** direto / análogo  
**Link oficial:** https://www.joiipetcare.com  
**Data de acesso:** 31/08/2026

#### Contexto e proposta

A Joii Pet Care combina um verificador digital de sintomas com consultas veterinárias por chat ou vídeo. O tutor seleciona ou pesquisa o problema, responde perguntas guiadas, recebe uma orientação de urgência e pode avançar para contato com um profissional. A solução é relevante por integrar coleta estruturada, resultado inicial, escalonamento humano e registro do animal em um fluxo móvel.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print | Observação de IHC |
|---|---|---|---|
| Busca e seleção do sintoma | O tutor procura um sintoma ou navega por opções antes de iniciar as perguntas. | <img width="320" alt="Seleção de sintomas na Joii" src="https://www.joiipetcare.com/cdn/shop/files/mobilestep1.webp?v=1762507129" /> | A combinação entre busca e categorias atende quem sabe nomear o sinal e quem precisa reconhecê-lo em uma lista. |
| Questionário guiado | O verificador apresenta perguntas sucessivas sobre o animal e os sinais observados. | <img width="405" alt="Verificador de sintomas e videochamada da Joii" src="https://www.purelypetsinsurance.co.uk/media/hogbq2lc/video-call-and-symptom-checker.png?height=405&rmode=max&width=405" /> | A condução passo a passo reduz a necessidade de formular um relato completo, mas pode ficar longa em casos urgentes. |
| Consulta com profissional | O aplicativo oferece chat e videochamada com profissionais veterinários. | [Página do aplicativo no Google Play](https://play.google.com/store/apps/details?id=com.vetai.joii) | O escalonamento humano é claro e preserva um caminho quando a automação não basta. |
| Perfil e histórico do pet | Informações do animal e registros das interações ficam associados à conta. | [Site oficial da Joii](https://www.joiipetcare.com) | Evita repetição e ajuda na continuidade, desde que o tutor possa iniciar um caso urgente sem completar dados não essenciais. |

#### Experiência do usuário e opiniões

Na página consultada do Trustpilot, a Joii apresentava avaliação próxima de 4,7/5, com cerca de 9 mil opiniões. Avaliações positivas mencionam rapidez, acolhimento e conveniência. Entre as críticas encontradas estão dificuldades com múltiplos vínculos de seguradoras ou contas, login e encerramento do chat após período curto de inatividade. Esses relatos mostram a importância de preservar o estado da interação, avisar antes de encerrar e oferecer recuperação simples.

#### Preço/modelo de negócio

O verificador de sintomas é apresentado como gratuito. A consulta por vídeo é anunciada por £28 para pagamento avulso e pode ser incluída sem custo adicional para clientes de seguradoras parceiras, conforme as condições de cada plano.

#### Padrões e tendências percebidos

Interface mobile com navegação inferior, seleção de sintomas, questionário em etapas, perfil do animal, resultado inicial e possibilidade de encaminhar para chat ou vídeo com profissional.

#### Pontos positivos, limitações e lições

| Ponto | Evidência | Implicação para nosso projeto |
|---|---|---|
| Ponto positivo: busca combinada com categorias | O tutor pode localizar o problema por mais de um caminho | Oferecer relato livre e apoio por categorias, sem obrigar o tutor a conhecer terminologia clínica. |
| Ponto positivo: perguntas guiadas | O verificador coleta dados de forma progressiva | Fazer perguntas complementares adaptativas e priorizar sinais de risco antes de detalhes secundários. |
| Ponto positivo: escalonamento humano | O resultado pode levar a chat ou vídeo | Disponibilizar encaminhamento claro quando houver risco, incerteza ou limitação do sistema. |
| Ponto positivo: continuidade | Perfil e histórico reúnem dados do pet | Permitir revisão e reaproveitamento de dados, sem transformar o cadastro em barreira inicial. |
| Limitação: perda ou expiração de sessão | Usuários relatam encerramento do chat após inatividade | Salvar respostas, avisar sobre expiração e permitir retomar o fluxo. |
| Limitação: atrito de conta e seguradora | Há relatos de dificuldade com vínculos e autenticação | Manter a pré-triagem independente de integrações comerciais ou cadastros complexos. |
| Limitação: possíveis distrações comerciais | Serviços e benefícios fazem parte da navegação | Em situação crítica, priorizar orientação e ação, reduzindo conteúdo promocional. |

### Análise C03 — Petriage

**Autor(a):** Vinícius de Castro Duarte — RA: 22.224.020-2  
**Tipo:** direto  
**Link oficial:** https://petriage.com  
**Data de acesso:** 27/08/2026

#### Contexto e proposta

A Petriage oferece teletriagem veterinária baseada em um questionário sobre sintomas. Ao final, apresenta um nível de urgência e pode conectar o tutor à clínica veterinária. É o concorrente mais próximo da atividade central do projeto, embora utilize coleta predominantemente estruturada e não apresente, nos materiais públicos consultados, o mesmo recorte de relato livre com RAG e justificativa documental.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print | Observação de IHC |
|---|---|---|---|
| Questionário estruturado | O tutor responde perguntas sucessivas sobre o sinal e o estado do animal. | <img width="260" alt="Questionário de teletriagem da Petriage" src="https://maccormickvet.com/files/2021/07/Petriage-iPhone_Teletriage-2-520x1024-1.png" /> | Padroniza a coleta, mas pode limitar relatos não previstos e aumentar o número de etapas. |
| Quatro níveis de urgência | O resultado utiliza as categorias Non-threatening, Worrisome, Urgent e Emergency. | <img width="96" alt="Ícone de não ameaçador" src="https://petriage.com/wp-content/uploads/2021/04/non-threatening-lg.svg" /> <img width="96" alt="Ícone de preocupante" src="https://petriage.com/wp-content/uploads/2021/04/worrisome-lg.svg" /> <img width="96" alt="Ícone de urgente" src="https://petriage.com/wp-content/uploads/2021/04/urgent-icon-lg.svg" /> <img width="96" alt="Ícone de emergência" src="https://petriage.com/wp-content/uploads/2021/04/emergency-icon-lg.svg" /> | Texto, ícone e cor criam redundância visual; ainda é necessário validar a interpretação das categorias pelo público-alvo. |
| Orientação associada ao resultado | Após a classificação, o tutor recebe indicação sobre o próximo passo. | [FAQ oficial da Petriage](https://petriage.com/faq/) | Aproxima resultado e ação, reduzindo o risco de o tutor receber apenas uma categoria sem saber como agir. |
| Conexão com clínica | A plataforma pode integrar a triagem ao relacionamento com uma clínica participante. | [Site oficial da Petriage](https://petriage.com) | Favorece continuidade, mas cria dependência da adesão e da disponibilidade da clínica. |

#### Experiência do usuário e opiniões

Os materiais públicos da Petriage destacam rapidez, disponibilidade contínua e orientação de urgência. Não foi encontrada, durante esta análise, uma base ampla e recente de avaliações independentes comparável às páginas de Vetster e Joii. Por isso, as conclusões de UX sobre facilidade e satisfação ficam limitadas ao fluxo documentado e não devem ser tratadas como validação com usuários.

#### Preço/modelo de negócio

O verificador de sintomas é apresentado como gratuito para tutores. Clínicas podem cobrar por serviços profissionais adicionais. Para organizações, a Petriage oferece modelo B2B; a página consultada anunciava o plano Premium por US$ 199,99 mensais.

#### Padrões e tendências percebidos

Questionário em etapas, classificação por níveis de urgência, uso redundante de texto, ícone e cor, orientação vinculada ao resultado e integração opcional com uma clínica.

#### Pontos positivos, limitações e lições

| Ponto | Evidência | Implicação para nosso projeto |
|---|---|---|
| Ponto positivo: níveis de urgência explícitos | Quatro categorias nomeadas e diferenciadas visualmente | Comunicar gravidade com texto e ícone, sem depender apenas da cor; validar se a quantidade e os nomes são compreensíveis. |
| Ponto positivo: resultado ligado ao próximo passo | A classificação é acompanhada de orientação | Toda saída deve responder “o que fazer agora”, inclusive nos casos incertos. |
| Ponto positivo: coleta padronizada | Perguntas estruturadas orientam o tutor | Usar perguntas complementares para preencher lacunas relevantes, preservando a possibilidade de relato livre. |
| Limitação: formato predominantemente fechado | O fluxo público observado depende de seleção e perguntas | Permitir que o tutor descreva sinais não previstos e revise como o sistema interpretou o relato. |
| Limitação: explicabilidade pública pouco detalhada | Os materiais consultados enfatizam o nível e a ação | Explicar os principais sinais considerados, a incerteza e os limites, sem apresentar diagnóstico. |
| Limitação: risco de dependência da cor | As categorias possuem codificação cromática forte | Adotar redundância com texto, ícone, hierarquia e instrução explícita, considerando daltonismo e baixa visão. |

> Repita a subseção para C02, C03... até atender à quantidade da equipe.

## 3. Softwares que o público-alvo usa no cotidiano

Analise interfaces que moldam a expectativa do público, mesmo que não sejam concorrentes.

| Software | Por que o público usa | Padrões relevantes | Prints | O que aprender |
|---|---|---|---|---|
| Google Search | Buscar rapidamente explicações para termos, sintomas e serviços | Campo de texto livre em destaque, sugestões, correção de termos e resultados ordenados | <img width="720" alt="Campo de busca do Google" src="https://i.insider.com/57682dd8dd08957a0e8b4a49?format=jpeg&width=1200" /> | A entrada inicial deve aceitar linguagem natural. Como resultados gerais podem ser ambíguos ou contraditórios, o projeto deve explicitar fonte, limite e ação recomendada. |
| Google Maps | Encontrar clínicas, verificar distância, horário, telefone e iniciar uma rota | Mapa combinado com lista, cartões de locais, filtros, ação de ligar e navegação passo a passo | <img width="720" alt="Busca de serviços próximos no Google Maps" src="https://support.similarweb.com/hc/article_attachments/15395427761181" /> | Reaproveitar convenções de mapa e lista; apresentar distância, funcionamento, telefone e rota. Disponibilidade e capacidade de atendimento ainda precisam ser confirmadas diretamente. |
| WhatsApp | Conversar, enviar texto, fotos e áudio em uma interface familiar no celular | Campo de mensagem persistente, botão de microfone, estado de gravação, envio, reprodução e transcrição de voz | <img width="720" alt="Transcrição de mensagem de voz no WhatsApp" src="https://www.bug.hr/img/whatsapp-ce-uskoro-moci-transkribirati-glasovne-poruke_LzHLOi.jpg" /> | A entrada por voz deve mostrar claramente quando está gravando, permitir cancelar, ouvir e revisar a transcrição antes de enviar. Sua utilidade no contexto do projeto permanece condicionada à validação de H09. |

## 3.1 Padrões de interface relevantes ao escopo de IHC

Registre somente padrões encontrados nas soluções analisadas e que possam ter relação com objetivos reais da equipe.

| Padrão observado | Produto(s) | Para qual tarefa serve | Vantagem percebida | Risco/limitação | Aplicável ao nosso escopo? |
|---|---|---|---|---|---|
| Entrada livre combinada com categorias de sintomas | Joii e Google Search | Iniciar o relato e localizar o sinal observado | Atende tanto quem sabe descrever quanto quem precisa reconhecer opções | Categorias podem induzir escolha inadequada ou omitir sinais não previstos | sim |
| Questionário guiado e progressivo | Petriage e Joii | Coletar dados complementares do caso | Reduz esquecimento e organiza a coleta | Pode alongar o fluxo e atrasar ação urgente | sim, se adaptativo |
| Classificação de urgência com texto, ícone e cor | Petriage | Compreender a gravidade inicial | Cria hierarquia e redundância visual | Cores e rótulos podem ser mal interpretados ou gerar falsa segurança | sim, com validação |
| CTA principal vinculado ao próximo passo | Vetster, Petriage e Google Maps | Agendar, ligar, localizar ou iniciar rota | Reduz hesitação após o resultado | Uma ação genérica pode não atender todos os níveis de urgência | sim |
| Perfil e histórico do animal | Vetster e Joii | Reutilizar contexto em atendimentos futuros | Evita repetição e apoia continuidade | Cadastro obrigatório pode atrasar a pré-triagem | talvez; opcional no início |
| Escalonamento para atendimento humano | Vetster, Joii e Petriage | Obter avaliação profissional quando necessário | Preserva um caminho seguro diante de risco ou incerteza | Depende de disponibilidade, custo e integração | sim |
| Resumo persistente e revisável | Joii e fluxos de telemedicina | Conferir dados e continuar o cuidado | Facilita correção, continuidade e compartilhamento | Um resumo incorreto pode propagar erro se não puder ser editado | sim |
| Mapa combinado com lista de serviços | Google Maps | Localizar clínica e iniciar deslocamento | Combina visão espacial com informações comparáveis | Proximidade não garante funcionamento ou capacidade de atendimento | sim |
| Gravação de voz com transcrição revisável | WhatsApp | Relatar sinais sem digitar | É familiar e pode facilitar entrada em certas situações | Ruído, falha de transcrição, privacidade e baixa discrição | talvez; depende de H09 |
| Cartões de profissionais ou serviços | Vetster e Google Maps | Comparar opções de atendimento | Torna dados relevantes escaneáveis | Pode sobrecarregar a decisão em uma emergência | talvez; mostrar apenas dados essenciais |

> O objetivo não é concluir “todo concorrente tem dashboard, então teremos um”. O padrão só será adotado se apoiar uma tarefa rastreável.

## 4. Síntese comparativa da equipe

| Critério | C01 | C02 | C03 | Oportunidade para o projeto |
|---|---|---|---|---|
| Navegação | Estrutura clara por categorias de sintomas e áreas clínicas na tela inicial, mas exige fluxo longo de cadastro e agendamento antes da orientação. | Fluxo móvel guiado, com seleção de sintomas, questionário em etapas e acesso a chat ou videochamada com profissional. | Questionário estruturado e linear, seguido da apresentação do nível de urgência e da orientação correspondente. | Combinar relato livre com categorias e perguntas complementares adaptativas, permitindo iniciar a pré-triagem sem cadastro obrigatório. |
| Feedback/estado | Atualizações por e-mail/notificação sobre agendamento e status da consulta com o profissional. | Apresenta o avanço do questionário e os estados do atendimento por chat ou vídeo, mas há relatos de encerramento da sessão por inatividade. | Apresenta o resultado em quatro níveis de urgência diferenciados por texto, ícones e cores. | Exibir claramente o progresso, o processamento das informações, a gravação de áudio e o resultado, além de avisar antes de encerrar uma sessão. |
| Prevenção/recuperação de erro | Validação de campos de formulário e revisão de dados do pet antes de confirmar o agendamento. | A coleta guiada reduz omissões, mas dificuldades de login, vínculo com seguradoras e expiração da sessão podem prejudicar a recuperação. | As perguntas estruturadas reduzem respostas incompletas, mas o formato fechado pode impedir que o tutor descreva sinais não previstos. | Salvar as respostas automaticamente, permitir voltar e corrigir informações, revisar transcrições e retomar uma pré-triagem interrompida. |
| Terminologia | Uso de termos amigáveis para tutores na seleção de sintomas, mantendo dados clínicos estruturados no resumo final. | Combina linguagem cotidiana com categorias de sintomas e perguntas mais específicas durante a avaliação. | Utiliza categorias explícitas de urgência, mas seus nomes podem não ser interpretados da mesma maneira por todos os tutores. | Utilizar linguagem simples, explicar termos clínicos e associar cada nível de urgência a uma ação concreta, sem apresentar diagnóstico. |
| Acessibilidade | Interface limpa em mobile/web com boa visibilidade de botões principais de ação. | Interface voltada a dispositivos móveis e com diferentes canais de atendimento, embora os materiais analisados não demonstrem cobertura completa de acessibilidade. | Utiliza texto, ícones e cores para diferenciar os níveis de urgência, mas a forte dependência visual das cores pode dificultar a compreensão de alguns usuários. | Não depender apenas de cores ou áudio; utilizar contraste adequado, ícones acompanhados de texto, controles amplos e alternativas de entrada. |
| Eficiência | Depende do tempo de espera por um veterinário disponível para realizar a triagem humana. | O verificador oferece orientação inicial antes do atendimento humano, mas o questionário pode ser longo e o acesso profissional depende de disponibilidade. | Produz uma classificação rapidamente por meio de perguntas estruturadas, mas pode exigir etapas desnecessárias quando já existem sinais críticos. | Priorizar sinais de risco, adaptar a quantidade de perguntas e apresentar encaminhamento imediato quando houver indícios de emergência. |

## 5. Recomendações derivadas

Liste recomendações com origem explícita.

- **RC01:** permitir iniciar a pré-triagem sem cadastro obrigatório e solicitar apenas os dados essenciais; o perfil completo do animal pode ser criado ou complementado depois, derivada de C01, C02 e da criticidade temporal do contexto.
- **RC02:** combinar relato livre com categorias reconhecíveis e perguntas complementares adaptativas, derivada de C02, C03 e Google Search.
- **RC03:** comunicar urgência por texto, ícone, hierarquia visual e cor, sem depender somente da codificação cromática, derivada de C03 e da análise de acessibilidade.
- **RC04:** apresentar um próximo passo principal, específico ao resultado, como procurar atendimento agora, ligar para a clínica, iniciar rota ou acompanhar sinais, derivada de C01, C03 e Google Maps.
- **RC05:** preservar respostas e rascunhos, avisar antes de expirar a sessão e permitir retomada, derivada dos relatos de uso de C02.
- **RC06:** mostrar um resumo revisável do que foi entendido sobre o animal e os sinais antes de produzir ou compartilhar a orientação, derivada da coleta estruturada de C01, C02 e C03.
- **RC07:** se H09 for sustentada, adotar convenções familiares de gravação: estado visível, duração, cancelar, reproduzir e revisar a transcrição antes do envio, derivada do WhatsApp.
- **RC08:** distinguir visualmente mensagens do tutor, perguntas do sistema, evidências recuperadas e eventual intervenção humana, derivada dos fluxos conversacionais de C01 e C02 e da necessidade de não confundir automação com avaliação profissional.
- **RC09:** apresentar clínicas em mapa e lista com distância, horário, telefone, rota e indicação verificável de atendimento; não ordenar apenas por proximidade, derivada de Google Maps, C01 e H10.
- **RC10:** interromper o fluxo comum e antecipar o encaminhamento quando respostas indicarem sinal crítico, evitando perguntas secundárias, derivada do questionário de C03 e da limitação de eficiência observada.
- **RC11:** explicar incerteza, limites da pré-triagem e principais fatores que sustentam a orientação, sem apresentar diagnóstico, derivada das limitações de C01 e C03 e da proposta técnica do TCC.
- **RC12:** reduzir anúncios, planos, benefícios comerciais e escolhas não essenciais no fluxo urgente, derivada de C01 e C02.

## Referências

- [Vetster — site oficial](https://vetster.com). Acesso em: 26 ago. 2026.
- [Vetster — Veterinary Telehealth & Telemedicine Glossary](https://vetster.com/en-us/telemedicine-glossary). Acesso em: 26 ago. 2026.
- [Vetster — What to do in a pet emergency](https://vetster.com/en/wellness/what-to-do-in-a-pet-emergency). Acesso em: 26 ago. 2026.
- [Vetster — Membership](https://vetster.com/en-us/membership). Acesso em: 26 ago. 2026.
- [Vetster — App Store](https://apps.apple.com/us/app/vetster-vet-appointments/id1551130660). Acesso em: 26 ago. 2026.
- [Vetster — avaliações no Trustpilot](https://www.trustpilot.com/review/vetster.com). Acesso em: 26 ago. 2026.
- [Joii Pet Care — site oficial](https://www.joiipetcare.com). Acesso em: 27 ago. 2026.
- [Joii Pet Care — App Store](https://apps.apple.com/gb/app/joii-pet-care/id1459361529). Acesso em: 27 ago. 2026.
- [Joii Pet Care — Google Play](https://play.google.com/store/apps/details?id=com.vetai.joii). Acesso em: 27 ago. 2026.
- [Joii Pet Care — avaliações no Trustpilot](https://www.trustpilot.com/review/joiipetcare.com). Acesso em: 27 ago. 2026.
- [Petriage — site oficial](https://petriage.com). Acesso em: 31 ago. 2026.
- [Petriage — FAQ](https://petriage.com/faq/). Acesso em: 31 ago. 2026.
- [Petriage — Pricing](https://petriage.com/pricing/). Acesso em: 31 ago. 2026.
- [Dr. Phillips Animal Hospital — Petriage app](https://drphillipsanimalhospital.com/petriage-app/). Acesso em: 31 ago. 2026.
- [Google Maps Help — Search for nearby places and explore the area](https://support.google.com/maps/answer/4610185). Acesso em: 31 ago. 2026.
- [Google Maps Help — Use navigation](https://support.google.com/maps/answer/3273406). Acesso em: 31 ago. 2026.
- [WhatsApp Help Center — How to send voice messages](https://faq.whatsapp.com/1206940699982241). Acesso em: 31 ago. 2026.
- STANS, S. E. A. et al. [Evaluation of animal symptom checkers](https://pmc.ncbi.nlm.nih.gov/articles/PMC10084260/). Acesso em: 31 ago. 2026.

## Checklist

- [x] O mapa inicial de alternativas da Entrega 1 foi revisitado e aprofundado.
- [x] Hipóteses relevantes sobre mercado/padrões foram atualizadas na rastreabilidade quando surgiram evidências.
- [x] Há pelo menos uma análise completa por integrante.
- [x] Cada análise contém prints legíveis da interface.
- [x] Prints mostram telas/estados relevantes, não apenas logos/homepage.
- [x] Foram analisados concorrentes e/ou interfaces representativas ao público.
- [x] Em TCC sem interface original, foram investigadas ferramentas profissionais análogas às atividades do usuário escolhido.
- [x] Padrões como dashboard, relatório, filtros e CRUD foram analisados como soluções para tarefas, não como requisitos automáticos.
- [x] Opiniões de UX têm fonte.
- [x] A síntese compara critérios comuns e produz recomendações.
- [x] Não há “copiar porque o concorrente faz”; há justificativa de adequação ao público/contexto.
