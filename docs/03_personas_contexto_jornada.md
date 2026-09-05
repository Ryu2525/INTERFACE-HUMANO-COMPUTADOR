# Entrega 3 — Personas, mapa de empatia, contexto de uso e jornada

**Data:** 31/08/2026  
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

> Repita para P02, P03... Cada integrante deve produzir ao menos uma persona.

### Síntese das personas

Explique diferenças entre os perfis e qual persona é prioritária. Evite personas duplicadas que só mudam nome/foto.

## 2. Mapa de empatia — equipe

**Persona escolhida:** P01 <BR>
**Justificativa:** É a persona primária do projeto. Representa o tutor em situação crítica e de alto estresse emocional, onde a usabilidade da interface, a rapidez na captura do relato e a clareza da orientação têm o maior impacto na tomada de decisão e na vida do animal.  
<img width="785" height="568" alt="image" src="https://github.com/user-attachments/assets/13bdc3f1-4334-43cf-abb4-5edd466db8ec" />

<!--  ![Mapa de empatia](../assets/03_personas/mapa_empatia.svg) -->

Documente também em texto: o que vê; ouve; diz/faz; pensa/sente; dores; ganhos. Diferencie **evidência** de **hipótese**.

## 3. Contexto de uso — consolidação

| Dimensão | Descrição | Implicação de design |
|---|---|---|
| Usuários | Tutores de cães e gatos (ex: Camila Rocha), com conhecimento leigo em medicina veterinária, operando sob alto estresse emocional, ansiedade e urgência perceptual durante uma suspeita de crise. | Utilizar linguagem simples e direta sem jargões clínicos; aplicar interface limpa com contraste elevado, botões de toque amplos e baixíssima carga cognitiva. |
| Tarefas | Relatar sinais/sintomas do animal por texto ou áudio, revisar transcrição, interpretar a classificação de urgência (emergência vs. não emergência) com sua justificativa e acionar rota/contato da clínica. | Priorizar a entrada multimodal com botão de gravação de voz em destaque (Whisper); exibir resultados com cores de alerta universais e acesso rápido ao mapa/ligação em 1 clique. |
| Equipamentos | Uso prioritário em smartphones (dispositivos móveis) via conexões móveis de dados (4G/5G). | Layout responsivo focado em mobile-first; telas leves de rápido carregamento e baixo consumo de banda para não travar em redes instáveis. |
| Ambiente físico | Ambientes domésticos (frequentemente de madrugada), ruas ou dentro de veículos a caminho do hospital; presença de iluminação reduzida, ruídos e movimento. | Tipografia com fontes grandes e alto contraste; fluxo de voz otimizado para capturar o áudio e permitir revisão rápida da transcrição mesmo com ruído de fundo. |
| Ambiente social/organizacional | O tutor é o responsável primário pelo animal no momento da crise, interagindo com o sistema como intermediário antes do contato com a equipe médica veterinária. | A interface deve deixar claro que a ferramenta apoia a triagem, mas não realiza diagnóstico definitivo nem substitui a consulta presencial com o médico-veterinário. |
| Papéis/permissões/governança | Papel de Tutor (fornece relato, visualiza orientação e envia caso) e Papel de Clínica/Veterinário (recebe o resumo estruturado MIST); aderência às diretrizes de privacidade e LGPD. | Solicitar consentimento claro para acesso à localização; permitir a revisão e autorização do tutor antes de compartilhar o resumo prévio com a clínica. |
| Volume de dados/histórico | Gravações de áudio curtas, transcrições textuais, cadastro prévio do pet (espécie, raça, histórico) e relatórios MIST gerados por atendimento. | Manter um fluxo contínuo e salvo automaticamente para evitar perda de dados caso a sessão caia; permitir acesso rápido ao histórico de triagens passadas. |

## 4. Jornada do usuário — equipe

**Persona:** P01  
**Objetivo da jornada:** Avaliar a gravidade dos sintomas do animal durante uma suspeita de crise na madrugada e tomar uma decisão rápida sobre o encaminhamento emergencial sem perder tempo crítico.    
**Início e fim da jornada:** Início: Percepção dos primeiros sinais físicos anormais no pet. Fim: Chegada ao pronto-socorro veterinário indicado ou início da observação segura em casa.

| Etapa | Situação/ação | Objetivo | Pensamento/emoção | Dor | Oportunidade de design | Evidência |
|---|---|---|---|---|---|---|
| 1 | Percepção dos sintomas: Acorda de madrugada e nota o cão engasgado, ofegante e com a língua arroxada. | Entender se o animal está em risco iminente de vida. | "Meu Deus, o Bob não consegue respirar! Será que ele vai sufocar?" — Pânico e impotência. | Dificuldade para avaliar a gravidade por falta de conhecimento técnico. | Acolhimento digital rápido e ponto de entrada imediato (Digital Front Door). | [F] TCC, seções I e IV.C; |
| 2 | Abertura e envio do relato: Abre o aplicativo e grava um áudio descrevendo o quadro do pet em linguagem leiga. | Comunicar o que está acontecendo da forma mais rápida possível. | "Não consigo digitar agora, minhas mãos estão trêmulas. Vou mandar um áudio." — Urgência e estresse. | Mãos ocupadas amparando o pet e incapacidade de digitar textos longos. | Entrada por voz em destaque (Whisper) com transcrição automática e tradução do relato leigo por Query Rewriting. | [F] TCC, seções IV.D e IV.E; [H] H09 |
| 3 | Validação das informações: Revisa rapidamente a transcrição gerada antes da análise final. | Garantir que o sistema capturou corretamente os sinais principais. | "Tomara que o aplicativo tenha entendido que a língua dele tá roxa." — Expectativa e tensão. | Medo de falhas na transcrição por ruído de fundo alterarem a triagem. | Exibição clara dos termos identificados e mecanismo de correção rápida sem reescrever tudo. | [F] TCC, seção IV.D; [H] H09 |
| 4 | Leitura da triagem: Recebe o resultado "POSSÍVEL EMERGÊNCIA" e a justificativa fundamentada. | Compreender o nível de gravidade e o porquê da recomendação. | "É grave mesmo! Não dá para esperar amanhecer, preciso ir pro hospital agora!" — Clareza e direcionamento. | Medo de alertas ambíguos ou linguagem médica incompreensível. | Alerta visual de alto contraste, linguagem direta e justificativa ancorada em base veterinária curada sem alucinações. | [F] TCC, seções IV.G e IV.K; [H] H02, H11 |
| 5 | Encaminhamento e ação: Visualiza o mapa com clínicas 24h abertas próximas e envia o resumo MIST para a recepção. | Iniciar o deslocamento imediatamente e preparar a clínica para a recepção. | "O hospital X tá aberto a 10 minutos. Já mandei os dados do Bob pra equipe se preparar!" — Resolução e foco. | Incerteza sobre quais hospitais estão realmente abertos na madrugada e tempo perdido na recepção. | Botão de rota direta em 1 clique, ligação para a clínica e envio de resumo técnico padronizado (MIST). | [F] TCC, seções IV.J e IV.K; [H] H03, H05, H10 |

> A jornada pode incluir etapas **antes, durante e depois** do uso do produto. Não transforme a jornada em lista de telas.

## Síntese

Quais necessidades e objetivos devem obrigatoriamente aparecer nos cenários e nas tarefas seguintes?
- Captura de áudio sem fricção: A permissão de gravação de voz imediata (Whisper) e a tolerância à linguagem leiga precisam estar presentes desde o primeiro contato, pois o tutor sob pânico não digita.
- Feedback de processamento transparente: O usuário precisa visualizar que o áudio foi compreendido e convertido corretamente para evitar insegurança em relação ao resultado.
- Classificação inequívoca de emergência: A resposta de urgência deve usar cores universais e mensagens diretas, acompanhadas de uma justificativa simples e sem jargões indeferidos.
- Ação em 1 clique para a Golden Hour: A transição do resultado da triagem para a rota do mapa, ligação para a clínica 24h e envio do resumo estruturado no padrão MIST deve ocorrer de maneira integrada na mesma tela.  

## Checklist

- [ ] Existe pelo menos uma persona por integrante.
- [ ] As personas não são apenas diferenças demográficas superficiais.
- [ ] Está claro o que é dado real e o que é hipótese/proto-persona.
- [ ] A persona não “validou por ficção” uma hipótese da Entrega 1; afirmações continuam marcadas como hipótese quando não há evidência.
- [ ] Objetivos e dores têm consequência para o design.
- [ ] Contexto de uso está coerente com a Entrega 1.
- [ ] Em TCC sem interface original, a persona possui relação explícita com a contribuição técnica.
- [ ] Papéis administrativos, técnicos e decisórios só foram criados quando possuem objetivos/tarefas diferentes.
- [ ] Jornada possui etapas, dores e oportunidades e não é apenas wireflow.
- [ ] IDs das personas foram adicionados à rastreabilidade.
