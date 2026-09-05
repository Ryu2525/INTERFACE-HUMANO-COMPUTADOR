# Entrega 3 — Personas, mapa de empatia, contexto de uso e jornada

**Data:** 05/09/2026  
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 persona por integrante; 1 mapa de empatia, 1 contexto de uso consolidado e 1 jornada por equipe (salvo orientação diferente do docente).

## Objetivo da atividade

Representar grupos de usuários de forma útil para decisões de design. Persona não é personagem decorativo: suas características devem alterar requisitos, prioridades, linguagem, fluxos ou critérios de avaliação.

## Atenção a projetos técnicos

Em TCCs sem interface original, a persona pode representar um **profissional que se apropria da contribuição técnica**: DBA, analista, cientista de dados, administrador, pesquisador, técnico, operador, gestor ou especialista de domínio.

Não escolha um perfil apenas porque “parece combinar” com a tecnologia. Explique **qual objetivo esse perfil teria e qual parte da contribuição do TCC produziria valor para ele**. Se ainda for hipótese, mantenha como hipótese/proto-persona a validar.

Também considere papéis diferentes quando houver tarefas distintas, por exemplo:

- operador que executa análises;
- administrador que configura e gerencia permissões;
- especialista que interpreta resultados;
- gestor que consulta relatórios e decide;
- auditor que revisa histórico.

## Entradas da Entrega 1

Antes de criar personas, retome os tipos de usuários, características relevantes, objetivos e hipóteses registradas na Entrega 1. A persona **não deve transformar uma hipótese inicial em fato por meio de uma história fictícia**.

| Item da Entrega 1 | Status inicial | Evidência disponível agora | Como será tratado nesta entrega |
|---|---|---|---|
| U01 — Tutor de cão ou gato (Usuário Principal) | F | Resumo, seções 2.1 e 7.2 da Entrega 1; fundamentado no vínculo afetivo | Incorporar como o perfil prioritário na criação das personas de uso do aplicativo. |
|U02 — Profissional de Clínica / Hospital Veterinário 24h | H | Seção 2.1 e 2.2 da Entrega 1; literatura de triagem veterinária | Incorporar no papel de recebedor/avaliador do resumo técnico no padrão MIST. |
| H01 — Atraso em casos graves ou busca inadequada de emergência | H | Seção 1.2 e 10 (H01) da Entrega 1; motivação do problema real em saúde animal. | Manter como hipótese (servirá para balizar as dores e motivações das personas em cenários de incerteza). |
| H02 — Compreensão das categorias de urgência e ação correta pelo tutor | H | Seções 1.4 (H02), 3.4 e 10 (H02) da Entrega 1. | Investigar no mapeamento das jornadas de usuário para avaliar o impacto das decisões de design. |
| H03 / H05 — Utilidade do resumo MIST e envio prévio para a clínica | H | Seções 1.4 (H03), 2.2 (H05) e 10 (H03/H05) da Entrega 1. | Manter como hipótese na jornada do profissional e na transição de encaminhamento do tutor. |
| H06 — Dificuldade com termos técnicos (Lexical Gap) e necessidade de linguagem simples | F | Seções 2.4, 4.2 e 10 (H06) da Entrega 1 | Incorporar como característica essencial de alfabetização do tutor, justificando o uso do Query Rewriting. |
| H08 — Uso prioritário via smartphone em ambientes ruidosos/móveis com estresse | H | Seções 5.1 a 5.3 e 10 (H08) da Entrega 1. | Incorporar diretamente no Mapeamento do Contexto de Uso (físico, emocional e tecnológico). |
|H09 — Preferência pela entrada de relatos por voz (Speech-to-Text via Whisper) | H | Seções 5.3, 9.3 e 10 (H09) da Entrega 1 | Investigar no fluxo de entrada de dados da jornada do tutor. |
| H10 — Critérios de escolha da clínica além da distância (funcionamento 24h, capacidade) | H | Seções 5.4 e 10 (H10) da Entrega 1. | Manter como hipótese nas etapas de encaminhamento e decisão da jornada. |

## 1. Personas

### Persona P01 — Camila Rocha — Tutor em Situação de Urgência Noturna

**Autor(a):** Julian Ryu Takeda 22.224.030-1 
**Tipo:** primária   
**Base de evidências:** literatura / proto-persona a validar <br>
**Hipóteses da Entrega 1 relacionadas:** H01, H02, H06, H08, H09, H10

<!-- ![Persona P01](../assets/03_personas/persona_p01.svg) -->
<img width="757" height="277" alt="image" src="https://github.com/user-attachments/assets/e8830b51-2c8b-4bf9-94c1-13f391a94df0" />

| Campo | Descrição |
|---|---|
| Faixa etária / contexto relevante | 31 anos; tutora de cão braquicefálico (Bob, Pug, 6 anos); uso emergencial noturno em ambiente doméstico. |
| Ocupação/papel | usuária direta principal (tutor). |
| Conhecimento do domínio | Leigo em veterinária; não domina terminologia clínica (descreve sintomas como "língua roxa", "ofegante" em vez de cianose/taquipneia).|
| Experiência tecnológica | Alta familiaridade com smartphones e aplicativos de mensagens/transporte; baixa tolerância a interfaces complexas em momentos de estresse. |
| Objetivos | Compreender a gravidade dos sinais do animal e decidir imediatamente o próximo passo de cuidado. |
| Necessidades | Entrada rápida de relato sem precisar digitar longos textos; resultado de triagem direto, claro e acionável com localização de clínica 24h próxima. |
| Dores/frustrações | Pânico sob pressão emocional; medo de errar a digitação ou perder tempo buscando informações genéricas na internet. |
| Motivadores | Garantir a segurança do animal o mais rápido possível e reduzir a incerteza durante a crise. |
| Restrições/acessibilidade | Mãos ocupadas/móveis enquanto ampara o animal; alta carga cognitiva devido à ansiedade. |
| Ambiente típico de uso | Residência em horário noturno/madrugada ou dentro do veículo a caminho de um hospital. |
| Comportamentos relevantes | Prefere relatar o problema por áudio em vez de texto quando nervosa; busca rotas diretas no mapa em casos críticos. |

**Decisões de design influenciadas por P01:**

- Entrada Multimodal em Destaque: Implementação de botão de gravação de áudio acessível na primeira tela para ativar a transcrição por voz via Whisper.
- Interface de Baixa Carga Cognitiva: Design visual de alto contraste com foco em botões amplos, evitando menus escondidos ou formulários extensos.
- Ação Imediata de Encaminhamento: Exibição direta do nível de urgência acompanhado de botão de ligação e rota de geolocalização para clínicas 24h ativas.  

### Persona P02 — Roberto Nunes — Tutor com menor familiaridade com aplicativos de saúde

**Autor(a):** João Pedro Gardenghi Peterutto — 22.125.066-5  
**Tipo:** primária  
**Base de evidências:** TCC, Entregas 1 e 2 e proto-persona a validar  
**Hipóteses da Entrega 1 relacionadas:** H02, H06, H07, H10, H11 e H12

| Campo | Descrição |
|---|---|
| Faixa etária / contexto relevante | 58 anos; responsável por Nina, uma gata idosa que apresenta redução de apetite e comportamento incomum. Identidade e situação são hipotéticas. |
| Ocupação/papel | Tutor e usuário direto do fluxo de pré-triagem. |
| Conhecimento do domínio | Conhece a rotina e o histórico da gata, mas não domina termos veterinários nem critérios de urgência. |
| Experiência tecnológica | Usa smartphone para mensagens, chamadas e buscas, mas possui pouca experiência com aplicativos de saúde e configurações complexas. |
| Objetivos | Relatar mudanças graduais, entender se pode observar o animal ou se precisa procurar atendimento e conferir os motivos da orientação. |
| Necessidades | Instruções passo a passo, linguagem cotidiana, ajuda próxima às dúvidas, controles claros e possibilidade de revisar respostas antes de concluir. |
| Dores/frustrações | Termos técnicos, perguntas sem explicação, excesso de opções, mensagens alarmistas e receio de apertar algo errado e perder as informações. |
| Motivadores | Cuidar do animal com responsabilidade e tomar uma decisão compreensível, sem depender de interpretar resultados genéricos de busca. |
| Restrições/acessibilidade | Pode precisar de fonte redimensionável, contraste adequado e alvos de toque amplos. Essas necessidades devem ser verificadas com usuários reais, sem atribuí-las automaticamente à idade. |
| Ambiente típico de uso | Residência, sem pressão imediata de deslocamento, mas com preocupação crescente e possível busca paralela por informações. |
| Comportamentos relevantes | Tende, como hipótese, a preferir leitura e seleção de opções a gravação de áudio e pode buscar confirmação adicional antes de agir. |

**Decisões de design influenciadas por P02:**

- Apresentar uma ação principal por etapa e explicar por que uma informação é solicitada.
- Usar termos cotidianos e oferecer explicações breves para conceitos inevitavelmente técnicos.
- Permitir voltar, corrigir e retomar a interação sem perder respostas.
- Não usar somente cor, gesto, áudio ou conhecimento prévio como condição de uso.
- Explicar incerteza, limites e motivos da orientação sem transmitir certeza diagnóstica.

### Persona P03 — Marina Lopes — Médica-veterinária plantonista

**Autor(a):** Vinícius de Castro Duarte — 22.224.020-2  
**Tipo:** secundária  
**Base de evidências:** TCC, Entregas 1 e 2 e proto-persona a validar  
**Hipóteses da Entrega 1 relacionadas:** H03, H05 e H10

| Campo | Descrição |
|---|---|
| Faixa etária / contexto relevante | 37 anos; médica-veterinária em plantão noturno de hospital 24 horas. Identidade e rotina específica são hipotéticas. |
| Ocupação/papel | Profissional que pode receber e avaliar um resumo de pré-triagem antes da chegada do animal. |
| Conhecimento do domínio | Alto conhecimento veterinário e familiaridade com triagem clínica; sabe que o resultado automatizado não substitui exame e decisão profissional. |
| Experiência tecnológica | Utiliza prontuário eletrônico, mensagens e sistemas internos durante o plantão; precisa consultar informações rapidamente e sem alternar entre muitos canais. |
| Objetivos | Identificar os sinais relatados, compreender a origem das informações, avaliar se a unidade possui capacidade de receber o caso e preparar o atendimento inicial. |
| Necessidades | Resumo curto e estruturado, distinção entre relato original, transcrição e interpretação automática, horário, identificação do animal e canal de contato com o tutor. |
| Dores/frustrações | Relatos incompletos ou dispersos, informações automáticas apresentadas como diagnóstico, duplicidade de dados e expectativa de atendimento criada sem confirmação da clínica. |
| Motivadores | Reduzir perda de informação, organizar o atendimento e preservar a responsabilidade da equipe clínica pela triagem e conduta. |
| Restrições/acessibilidade | Interrupções frequentes, pressão de tempo e necessidade de manter atenção simultânea em outros pacientes. |
| Ambiente típico de uso | Recepção ou área clínica durante um plantão, com múltiplos profissionais, ruído e alternância de tarefas. |
| Comportamentos relevantes | Verifica primeiro sinais críticos, tempo de evolução, dados do animal e disponibilidade da unidade; o uso efetivo desse resumo e a continuação da conversa permanecem hipóteses — H03 e H05. |

**Decisões de design influenciadas por P03:**

- Estruturar o resumo sem ocultar o relato original do tutor e indicar quais informações foram produzidas automaticamente.
- Exigir revisão e autorização do tutor antes do compartilhamento.
- Não informar que a clínica receberá o animal sem confirmação explícita da unidade.
- Destacar sinais críticos, horário, espécie, dados de contato e informações ausentes.
- Manter a interface da clínica fora do fluxo prioritário até que H03 e H05 sejam investigadas com profissionais.

> Repita para P02, P03... Cada integrante deve produzir ao menos uma persona.

### Síntese das personas

P01 e P02 representam o mesmo perfil prioritário — o tutor —, mas não são duplicatas. P01 enfatiza uma situação aguda, alta pressão emocional, atenção dividida e necessidade de ação imediata. P02 representa sinais menos evidentes, menor familiaridade com aplicativos de saúde e maior necessidade de orientação passo a passo, recuperação de erros e explicações. P03 possui outro papel, vocabulário e responsabilidade: é uma profissional que poderá consumir o resumo do caso e decidir sobre a preparação ou capacidade de atendimento da clínica.

P01 é a persona prioritária porque concentra as atividades centrais do recorte de IHC e o contexto de maior risco: relatar sinais, compreender a possível urgência e executar o próximo passo. P02 impede que a interface seja projetada apenas para usuários tecnologicamente confiantes. P03 delimita requisitos de continuidade e comunicação, mas permanece secundária enquanto H03 e H05 não forem investigadas.

## 2. Mapa de empatia — equipe

**Persona escolhida:** P01 <BR>
**Justificativa:** P01 representa o tutor no contexto mais crítico do recorte de IHC. Suas limitações situacionais — estresse, atenção dividida e necessidade de decisão rápida — afetam diretamente eficácia, eficiência, segurança no uso, experiência, acessibilidade e comunicabilidade.  
<img width="785" height="568" alt="image" src="https://github.com/user-attachments/assets/13bdc3f1-4334-43cf-abb4-5edd466db8ec" />

<!--  ![Mapa de empatia](../assets/03_personas/mapa_empatia.svg) -->

Documente também em texto: o que vê; ouve; diz/faz; pensa/sente; dores; ganhos. Diferencie **evidência** de **hipótese**.  

Como P01 é uma proto-persona, os conteúdos do mapa abaixo são hipóteses de trabalho, não evidências empíricas sobre tutores:

- **O que vê:** **[H]** percebe alterações físicas no animal, encontra resultados variados em buscas e visualiza opções de clínicas sem saber imediatamente quais estão disponíveis — H07 e H10.
- **O que ouve:** **[H]** pode receber orientações divergentes de familiares, conhecidos ou conteúdos on-line, aumentando a incerteza — H07.
- **O que diz e faz:** **[H]** descreve sinais com palavras cotidianas, tenta manter o animal seguro e pode preferir áudio quando suas mãos ou atenção estão ocupadas — H06, H08 e H09.
- **O que pensa e sente:** **[H]** teme subestimar um caso grave ou se deslocar sem necessidade; sente ansiedade e busca uma resposta que possa converter em ação — H01 e H02.
- **Dores:** **[H]** dificuldade para organizar o relato, interpretar categorias de urgência, corrigir uma transcrição, decidir quantas perguntas responder e verificar uma clínica adequada — H02, H09, H10 e H12.
- **Ganhos esperados:** **[H]** compreender os sinais considerados, receber orientação inicial clara, saber os limites da plataforma e alcançar rapidamente o próximo passo adequado — H02, H04 e H11.

## 3. Contexto de uso — consolidação

| Dimensão | Descrição | Implicação de design |
|---|---|---|
| Usuários | **[F]** O tutor é o usuário prioritário previsto no TCC. **[H]** Tutores podem variar em conhecimento veterinário, alfabetização digital, experiência com animais e necessidades de acessibilidade — H06. Profissionais da clínica são usuários secundários possíveis — H05. | Utilizar linguagem cotidiana, ajuda contextual e alternativas de interação; não pressupor conhecimento clínico ou alta familiaridade tecnológica. |
| Tarefas | **[F]** Identificar o animal, relatar sinais, revisar informações, responder perguntas, compreender possível urgência e próximo passo e, quando necessário, localizar atendimento e compartilhar um resumo. **[H]** A quantidade aceitável de perguntas não foi definida — H12. | Organizar as ações por prioridade, apresentar progresso e permitir correção; interromper perguntas secundárias quando houver sinal crítico. |
| Equipamentos | **[F]** O TCC prevê experiência próxima a uma aplicação móvel e entrada por texto ou voz. **[H]** O uso ocorrerá principalmente por smartphone e poderá depender de conexão móvel instável — H08. | Adotar abordagem mobile-first, conteúdo leve, salvamento de estado e equivalência entre entrada textual e por voz. |
| Ambiente físico | **[H]** A interação pode ocorrer em casa, na rua ou durante um trajeto, com ruído, movimento, pouca iluminação e atenção dividida — H08. | Usar texto legível, contraste adequado, controles amplos, feedback visível e possibilidade de revisar a transcrição; não depender apenas de áudio ou cor. |
| Ambiente social/organizacional | **[F]** A plataforma atua antes da avaliação profissional e não substitui diagnóstico, triagem clínica ou conduta veterinária. **[H]** Familiares podem participar da decisão e a clínica pode receber informações antes da chegada — H03 e H05. | Comunicar claramente o papel e os limites da plataforma, indicar quando procurar atendimento e não prometer recepção pela clínica sem confirmação. |
| Papéis/permissões/governança | **[F]** O tutor fornece e revisa dados e a proposta considera proteção de dados. **[H]** O profissional poderá receber o resumo e continuar a comunicação — H05. | Solicitar consentimento para localização, gravação e compartilhamento; permitir que o tutor revise o resumo e escolha o que será enviado. |
| Volume de dados/histórico | **[F]** A proposta pode lidar com cadastro do animal, relato, áudio, transcrição, perguntas, evidências recuperadas e resumo. **[?]** Volume real, tempo de retenção e necessidade de histórico ainda não foram definidos para IHC. | Salvar o estado da interação para recuperação, minimizar coleta, informar finalidade e retenção e só incluir histórico se houver tarefa e evidência que o justifiquem. |

## 4. Jornada do usuário — equipe

**Persona:** P01  
**Objetivo da jornada:** Avaliar a gravidade dos sintomas do animal durante uma suspeita de crise na madrugada e tomar uma decisão rápida sobre o encaminhamento emergencial sem perder tempo crítico.    
**Início e fim da jornada:** Início: Percepção dos primeiros sinais físicos anormais no pet. Fim: Chegada ao pronto-socorro veterinário indicado ou início da observação segura em casa.

| Etapa | Situação/ação | Objetivo | Pensamento/emoção | Dor | Oportunidade de design | Evidência |
|---|---|---|---|---|---|---|
| 1 — Percepção | Camila percebe que Bob está ofegante e com alteração na coloração da língua. | Entender se existe risco que exija ação imediata. | “Não sei se isso pode esperar.” — medo e incerteza. | Não possuir critérios clínicos para avaliar a gravidade. | Comunicar desde o início que sinais críticos exigem atendimento e que a plataforma oferece pré-triagem, não diagnóstico. | **[H]** Situação da proto-persona; H01 e H08. **[F]** A triagem profissional permanece necessária — Entrega 1. |
| 2 — Busca de orientação | Antes de conseguir contato profissional, decide utilizar a plataforma; poderia também recorrer a busca, mensagens ou ligação. | Encontrar uma orientação inicial confiável sem perder tempo. | “Preciso saber qual é o próximo passo.” — urgência e expectativa. | Alternativas dispersas podem oferecer respostas contraditórias ou não acionáveis. | Oferecer entrada imediata, sem cadastro obrigatório, e saída rápida para atendimento emergencial. | **[H]** H07. **RC01** e **RC10**, Entrega 2. |
| 3 — Relato | Escolhe entre digitar e gravar um áudio com suas próprias palavras; informa os sinais e dados essenciais do animal. | Comunicar o ocorrido com o menor esforço possível. | “Espero conseguir explicar direito.” — tensão e foco. | Atenção dividida e dificuldade para organizar o relato. | Manter texto e voz como alternativas; mostrar estado de gravação e preservar o relato enviado. | **[F]** Entrada por texto e voz prevista no TCC. **[H]** Preferência e contexto de voz — H08 e H09. |
| 4 — Revisão e complementação | Confere o que foi entendido e responde somente às perguntas complementares relevantes ao caso. | Corrigir erros e completar informações indispensáveis. | “Ele entendeu que a língua está roxa?” — preocupação com a interpretação. | Ruído, erro de transcrição, perguntas excessivas ou informação importante omitida. | Exibir resumo revisável, permitir correção rápida, explicar por que a pergunta importa e adaptar a quantidade de questões. | **[H]** H09 e H12. **RC02**, **RC05**, **RC06** e **RC07**, Entrega 2. |
| 5 — Processamento | Aguarda a análise das informações e das evidências recuperadas. | Saber que o pedido foi recebido e que o sistema continua funcionando. | “Está analisando ou travou?” — ansiedade. | Ausência de feedback pode gerar repetição, abandono ou perda de confiança. | Exibir estado e progresso, manter os dados salvos e oferecer recuperação em caso de falha ou conexão instável. | **[H]** H08. **RC05**, Entrega 2; critérios de eficiência, segurança e comunicabilidade das aulas. |
| 6 — Interpretação | Recebe “possível emergência”, os sinais considerados, uma justificativa simples, o grau de incerteza e a orientação de procurar atendimento. | Compreender a gravidade possível e transformar o resultado em ação. | “Preciso procurar atendimento agora.” — direcionamento, ainda com preocupação. | Categoria ambígua, jargão, excesso de confiança ou dependência exclusiva da cor. | Usar texto, ícone e hierarquia visual; explicar motivos, limites e próximo passo sem apresentar diagnóstico. | **[H]** H02 e H11. **RC03**, **RC04** e **RC11**, Entrega 2. |
| 7 — Encaminhamento | Consulta clínicas em mapa e lista, verifica informações disponíveis, liga para confirmar atendimento e autoriza o compartilhamento do resumo. | Escolher uma unidade adequada e preparar o contato com a equipe profissional. | “Esta unidade está aberta e consegue receber o Bob?” — foco e cautela. | Proximidade não garante funcionamento, disponibilidade ou capacidade; compartilhamento incorreto pode propagar erros. | Mostrar distância, horário, telefone e rota; solicitar confirmação da clínica e revisão/consentimento antes do envio. | **[H]** H03, H05 e H10. **RC09**, Entrega 2. |
| 8 — Continuidade | Inicia o deslocamento ou segue a instrução recebida da clínica; o profissional realiza a triagem e a avaliação presencial. | Garantir continuidade segura entre orientação inicial e cuidado profissional. | “Agora sei para onde ir e o que informar.” — alívio parcial e atenção ao animal. | Confundir pré-triagem com confirmação de diagnóstico ou atendimento garantido. | Reforçar limites, manter o resumo acessível e distinguir orientação automatizada de decisão profissional. | **[F]** O TCC não substitui avaliação veterinária. **[H]** Benefício sobre tempo e preparação — H03 e H04. |

> A jornada pode incluir etapas **antes, durante e depois** do uso do produto. Não transforme a jornada em lista de telas.

## Síntese

Quais necessidades e objetivos devem obrigatoriamente aparecer nos cenários e nas tarefas seguintes?  

- **Entrada flexível e eficiente:** o tutor deve conseguir iniciar sem cadastro obrigatório e relatar por texto; voz permanece uma alternativa condicionada à validação de H09.
- **Compreensão e correção:** o tutor deve revisar o que foi entendido, corrigir erros e responder perguntas complementares pertinentes, permitindo investigar H12.
- **Feedback e recuperação:** a interação deve comunicar gravação, envio, processamento, sucesso e falha, preservar o estado e permitir retomada.
- **Urgência compreensível e acionável:** o resultado deve combinar texto, ícone e hierarquia visual, apresentar justificativa simples, incerteza, limites e uma ação concreta — H02 e H11.
- **Acessibilidade situacional e permanente:** a interface não deve depender somente de cor, áudio, gesto ou conhecimento técnico; contraste, legibilidade, alvos de toque e alternativas de entrada devem ser considerados.
- **Encaminhamento verificável:** o tutor deve consultar informações úteis da clínica, confirmar atendimento e iniciar ligação ou rota; os critérios de H10 ainda precisam ser validados.
- **Privacidade e controle:** localização, áudio e resumo só devem ser utilizados ou compartilhados com finalidade clara, consentimento e possibilidade de revisão.
- **Continuidade profissional:** o resumo deve distinguir relato, transcrição e interpretação automática e não pode ser apresentado como diagnóstico ou garantia de atendimento — H03 e H05.

## Checklist

- [x] Existe pelo menos uma persona por integrante.
- [x] As personas não são apenas diferenças demográficas superficiais.
- [x] Está claro o que é dado real e o que é hipótese/proto-persona.
- [x] A persona não “validou por ficção” uma hipótese da Entrega 1; afirmações continuam marcadas como hipótese quando não há evidência.
- [x] Objetivos e dores têm consequência para o design.
- [x] Contexto de uso está coerente com a Entrega 1.
- [x] Em TCC sem interface original, a persona possui relação explícita com a contribuição técnica.
- [x] Papéis administrativos, técnicos e decisórios só foram criados quando possuem objetivos/tarefas diferentes.
- [x] Jornada possui etapas, dores e oportunidades e não é apenas wireflow.
- [ ] IDs das personas foram adicionados à rastreabilidade.
