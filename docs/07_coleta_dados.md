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

### A02 — Julian Ryu Takeda

**Autor(a):** Julian Ryu Takeda — 22.224.030-1

A A01 investiga o tutor. Esta contribuição investiga o outro lado do encaminhamento, a clínica, onde H03, H05 e L02 seguem abertas e o questionário não alcança. A resposta decide se A06 entra no recorte ou se o resumo permanece apenas como algo que o tutor revisa e envia (F09), conforme a Entrega 1, seção 7.1.1.

#### Que dados coletar?

Os dados seguem as cinco categorias da aula (Identificação de Necessidades A, pp. 2–7).

| Dado/informação | Hipótese/lacuna relacionada | Por que é necessário | Qual decisão de design pode afetar |
|---|---|---|---|
| **Usuário:** função na clínica, faixa de tempo de experiência, tipo de unidade (24 horas ou não) e termos usados para falar de urgência. | L02; H17 | Distinguir veterinário, atendente e outros papéis e conhecer o vocabulário profissional (p. 3). | Destinatário do resumo e vocabulário em que ele é escrito. |
| **Relação com tecnologia:** canais e sistemas usados quando o tutor entra em contato antes de chegar (telefone, mensagens, prontuário, agenda), com satisfações e incômodos. | H05; L05 | Saber se um novo canal se somaria aos que a equipe já alterna no plantão (p. 4). | Integração com canal existente ou interface própria da clínica (A06). |
| **Domínio:** informações necessárias para julgar urgência à distância e relatos leigos mais difíceis de interpretar. | H03; H01a/H01b, apenas como percepção | O conhecimento especialista indica o que torna um relato útil (p. 5). | Campos e ordem do resumo; perguntas complementares feitas ao tutor. |
| **Tarefas:** quem recebe o contato prévio, quem decide se a unidade pode receber, como a resposta volta ao tutor, frequência aproximada e erros com suas consequências (informação perdida, expectativa de vaga não confirmada). | L02; H05; H10a/H10c | Descrever o processo atual e a gravidade dos erros (p. 6). | Entrada ou não de A06 no recorte; texto sobre disponibilidade não confirmada no mapa. |
| **Motivações e valores:** atitude diante de uma pré-triagem automatizada, preservação da responsabilidade clínica, receio de o tutor chegar com conclusão pronta, disposição para aprender um sistema novo. | H03; H17; L03 | Atitudes da equipe podem inviabilizar um fluxo que parece útil no papel (p. 7). | Rótulos de origem, avisos de limitação, quem na clínica vê o caso e por quanto tempo. |

#### De quem coletar?

| Perfil/stakeholder | Critério de inclusão | Relação com persona/público |
|---|---|---|
| Médicos-veterinários que atendem urgências de cães/gatos. | 18 anos ou mais; ao menos 6 meses em clínica ou hospital que recebe urgências; participação voluntária. | P03; interpreta o caso e decide a conduta. |
| Atendentes/recepcionistas dessas unidades. | Mesmos critérios; responsável por receber ligações ou mensagens de tutores. | U02 (E3); possivelmente o primeiro a receber o caso (L02). |
| Responsável pela unidade, somente se surgir nas entrevistas. | Indicado pelos entrevistados como quem decide canais e processos de contato. | Quem define os processos que o sistema apoiaria (p. 8). |

Respostas às questões da aula (p. 8) para este recorte:

- **Quem utilizaria?** Tutores, pelo lado principal; na clínica, possivelmente atendente e veterinário, o que é justamente o que está em aberto (H05).
- **Quem seria afetado?** A equipe da clínica, que receberia resumos e expectativas criadas pela plataforma, mesmo sem usar uma tela própria.
- **Quem decide objetivos e funcionalidades?** A equipe do TCC e o orientador; na clínica, o responsável pela unidade decide se um novo canal é adotado.
- **Quem definiu os processos atuais?** Desconhecido; é uma das perguntas da entrevista (L02).

**Amostra:** 3 a 5 entrevistas, com ao menos um veterinário e um atendente, de preferência de unidades diferentes. O recrutamento é por conveniência, em clínicas conhecidas da equipe. A amostra não representa as clínicas em geral: serve para descobrir papéis, necessidades e contradições, não frequências.

#### Aspectos éticos

A aula orienta pelos princípios da Resolução CNS 196/96 (pp. 9–12). Essa resolução foi substituída pela Resolução CNS 466/2012, que mantém os mesmos princípios. Por ser um exercício da disciplina, a coleta não passa por comitê de ética; se os resultados forem usados como pesquisa no TCC, a equipe consultará o orientador sobre essa exigência. Os riscos concretos desta entrevista são:

- **Dados de terceiros.** Ao contar casos, o profissional pode identificar tutores, animais ou datas. Ele será orientado a não citar nomes nem detalhes identificáveis; se citar, o trecho não vai para a ficha nem para a transcrição.
- **Exposição profissional.** Críticas ao processo da clínica ou a colegas podem prejudicar o participante. Os registros usam IDs (`E01`, `E02`…), sem nome da pessoa ou da clínica, e trechos que permitam deduzir a unidade (por exemplo, "o único hospital 24 h do bairro") são descritos de forma genérica.
- **Subordinação (autonomia, p. 11).** O convite é feito diretamente ao profissional, mesmo que o contato tenha vindo de um gestor. O gestor não é informado de quem aceitou nem do que foi dito.
- **Não maleficência (p. 10).** A entrevista não pode competir com o atendimento: é agendada fora do horário de atendimento ou em período calmo, e é interrompida se surgir uma urgência.
- **Gravação.** Apenas áudio, com permissão pedida separadamente do aceite; quem recusar a gravação participa com anotações. O áudio sai do celular do entrevistador no mesmo dia para uma pasta de acesso restrito à equipe e é excluído após a transcrição anonimizada ser conferida, no máximo ao fim da disciplina.
- **Minimização.** Não serão coletados nome na ficha, idade exata, CRMV, salário nem nome da clínica. A ficha online não coleta e-mail nem exige login. O aceite é registrado na ficha apenas com ID e data; se a unidade exigir termo assinado (modelo em [`../instrumentos/termo_consentimento_modelo.md`](../instrumentos/termo_consentimento_modelo.md)), ele é guardado separado das respostas, sem ligação entre nome e ID.
- **Beneficência e justiça (pp. 10–11).** Não há benefício direto ao participante; para reduzir o ônus, a duração é limitada a cerca de 40 minutos e quem quiser recebe a síntese dos resultados.

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

### Instrumento I02 — Entrevista semiestruturada com profissionais de clínica

**Autor(a):** Julian Ryu Takeda — 22.224.030-1  
**Técnica:** entrevista semiestruturada individual (Identificação de Necessidades B, pp. 3–5)  
**Objetivo:** Entender como a clínica recebe hoje o contato de tutores antes da chegada do animal (quem recebe, quem decide, que informação falta) para decidir se o resumo do caso (H03) e uma interface para a clínica (H05, A06) são necessários e em que forma.  
**Público:** Médicos-veterinários e atendentes de clínicas ou hospitais que recebem urgências de cães/gatos, relacionados a P03 e U02.  
**Duração e formato:** 30 a 40 minutos, presencial ou por videochamada, com um entrevistador e, se possível, um anotador.  
**Ferramenta online:** ficha do entrevistador em Google Forms, conforme a atividade da aula (p. 21), com uma seção por bloco do roteiro; o roteiro integral fica neste repositório.

**Por que esta técnica.** A entrevista coleta informações mais detalhadas de cada pessoa do que questionários e grupos de foco (p. 3), o que é necessário para reconstruir um processo de trabalho que nenhum integrante conhece por dentro. O questionário da I01 não alcança esse público, e reunir plantonistas em um grupo de foco é pouco viável. O formato semiestruturado mantém o mesmo roteiro para entrevistadores diferentes, mas permite seguir relatos não previstos.

#### Procedimento padronizado de aplicação

O protocolo de execução é o instrumento mais importante (p. 20), porque garante que entrevistadores diferentes apliquem a coleta do mesmo modo.

**Antes**

1. Criar a ficha no Google Forms com os campos do roteiro (uma seção por bloco, perguntas fechadas como múltipla escolha e um campo de anotação por bloco). Desativar a coleta de e-mail e a exigência de login e testar com um colega.
2. Enviar o convite padrão diretamente ao profissional, sem depender de intermediação do gestor. Agendar fora do horário de atendimento. Atribuir o ID (`E01`, `E02`…) pela ordem das entrevistas.
3. Ter à mão o resumo fictício do Bloco 6 (impresso ou em tela compartilhada).

**Durante**

4. Ler a apresentação e o consentimento como estão escritos. Perguntar sobre gravação separadamente. Se a pessoa não aceitar participar, agradecer e encerrar. Na ficha, registrar apenas ID, data e as duas respostas.
5. Seguir os blocos de 1 a 7 na ordem. Ler as perguntas principais como estão escritas e usar apenas as sondagens listadas ou neutras: "Pode dar um exemplo?", "Como foi?", "E depois?".
6. **Não mencionar a plataforma, o resumo nem o painel antes do Bloco 6**, para não induzir as respostas sobre a rotina atual.
7. Pedir exemplos concretos e recentes ("A última vez que…") e lembrar de não citar nomes de tutores, animais ou da clínica.
8. Não explicar, defender ou corrigir a proposta. Dúvidas sobre o projeto são respondidas apenas no encerramento.
9. Se surgir uma urgência, interromper imediatamente e retomar outro dia ou encerrar.
10. Ao fim de cada bloco, anotar na ficha os fatos relatados e citações curtas sem identificação, marcando com `[I]` o que for interpretação do entrevistador.

**Depois**

11. No mesmo dia, mover o áudio para a pasta restrita, apagá-lo do celular, completar a ficha e registrar a duração e qualquer ocorrência.
12. Transcrever os trechos relevantes com anonimização; excluir o áudio depois que a transcrição for conferida.

**Convite padrão:** "Olá! Somos estudantes de Ciência da Computação da FEI e estamos estudando como clínicas veterinárias recebem contatos de tutores antes de um atendimento urgente. Gostaríamos de conversar com você por cerca de 30 a 40 minutos, em um horário fora do atendimento. A participação é voluntária e não usaremos seu nome nem o da clínica. Podemos combinar um horário?"

#### Instrumento

**Apresentação e consentimento (ler ao participante)**

Obrigado por aceitar conversar. Somos estudantes da disciplina de Interação Humano-Computador da FEI e queremos entender como a clínica recebe contatos de tutores antes da chegada de um animal em situação urgente. Não estamos avaliando você nem a clínica, e não há respostas certas. A conversa leva de 30 a 40 minutos. Você pode não responder qualquer pergunta e parar a qualquer momento, sem justificar. Por favor, ao contar casos, não cite nomes de tutores, animais ou da clínica. Não registraremos seu nome nem o da clínica; os resultados serão apresentados com códigos como E01. Somente a equipe terá acesso às anotações. Você aceita participar?

( ) Sim. ( ) Não — agradecer e encerrar.

**Posso gravar apenas o áudio para não perder detalhes? A gravação fica com acesso restrito à equipe e é apagada depois de transcrita, sem seu nome.**

( ) Sim. ( ) Não — seguir só com anotações.

**Bloco 1 — Perfil e papel (função – experiência – unidade)**

1.1 Qual é a sua função? ( ) Médico(a)-veterinário(a) ( ) Atendente/recepção ( ) Auxiliar ou técnico(a) ( ) Gestão ( ) Outra: ____  
1.2 Há quanto tempo trabalha no atendimento de cães e gatos? ( ) Menos de 1 ano ( ) 1 a 3 anos ( ) 4 a 10 anos ( ) Mais de 10 anos  
1.3 A unidade funciona 24 horas? ( ) Sim ( ) Não ( ) Em parte (plantão em alguns dias ou horários)  
1.4 Quais são suas principais atividades quando chega um caso urgente? Quais são as mais frequentes?

**Bloco 2 — Contato antes da chegada (canal – frequência – quem recebe)**

2.1 Os tutores costumam entrar em contato antes de trazer um animal em situação urgente? Por quais meios? Com que frequência, aproximadamente?  
2.2 Conte a última vez em que isso aconteceu: quem recebeu o contato, o que o tutor disse e o que foi feito em seguida?  
2.3 Quem decide se a unidade pode receber o caso naquele momento? Como a informação chega até essa pessoa e como a resposta volta ao tutor?  
2.4 *Se os tutores não costumam avisar antes:* Por que você acha que isso acontece? O que muda para a equipe quando o animal chega sem aviso?

**Bloco 3 — Informação que chega e informação que falta**

3.1 Quando o tutor descreve o problema à distância, quais informações são essenciais para vocês? Quais costumam faltar?  
3.2 Que descrições de tutores são mais difíceis de interpretar ou costumam enganar? Pode dar um exemplo, sem identificar o caso?  
3.3 Já aconteceu de uma informação passada antes da chegada estar errada ou se perder no caminho? O que isso causou?  
3.4 Na sua experiência, os tutores costumam procurar atendimento no momento adequado, cedo demais ou tarde demais em relação à gravidade? Pode dar exemplos?

**Bloco 4 — Disponibilidade e capacidade de atendimento**

4.1 O que pode fazer a unidade não conseguir receber um caso em determinado momento?  
4.2 Como o tutor fica sabendo disso hoje? Já aconteceu de um tutor chegar acreditando que seria atendido e não ser possível? O que aconteceu?  
4.3 Que informação sobre a unidade seria importante o tutor saber antes de decidir ir até vocês?

**Bloco 5 — Tecnologia usada hoje (tecnologia – frequência – satisfação – desejos)**

5.1 A equipe usa algum sistema ou aplicativo para receber contatos de tutores, registrar o caso ou responder ao tutor?  
- *Se sim:* Quais? Para quê? Com que frequência? O que mais gosta? O que menos gosta? O que faria diferente?  
- *Se não:* Já usou? Por que não usa (mais)? O que precisaria ter para usar?

5.2 Durante um plantão, quantos canais ou telas diferentes você costuma acompanhar? O que acontece quando surge mais um?

**Bloco 6 — Reação a um resumo fictício**

Ler: "Agora vou mostrar um exemplo fictício de resumo que um tutor poderia enviar antes de chegar. Não é um caso real e esse recurso ainda não existe. Não há resposta certa."

> **Resumo enviado pelo tutor — exemplo fictício**  
> **Animal:** cão, 8 anos, cerca de 20 kg. Enviado às 23h40.  
> **Relato do tutor (texto original):** "Ele vomitou três vezes desde as 21h, está muito parado e a barriga parece inchada."  
> **Respostas às perguntas complementares:** comeu normalmente às 19h; não sabe se ingeriu algo; respiração "rápida".  
> **Interpretação automática (não é diagnóstico):** sinais compatíveis com possível emergência, pela combinação de vômitos repetidos, abdômen aparentemente distendido e apatia.  
> **Informações ausentes:** cor das gengivas, temperatura, medicamentos em uso.  
> **Contato do tutor:** (11) 90000-0000 (fictício). **A clínica ainda não confirmou o atendimento.**

6.1 O que você lê primeiro? O que nesse resumo seria útil para você? Por quê?  
6.2 O que falta, o que sobra ou o que está fora de ordem?  
6.3 Fica claro o que foi dito pelo tutor e o que foi gerado automaticamente? Essa distinção importa para você? Por quê?  
6.4 Se um resumo assim chegasse, o que você faria com ele? Por qual meio deveria chegar e quem deveria recebê-lo?  
6.5 Depois de ler, você precisaria fazer algo pelo mesmo meio (por exemplo, confirmar, recusar ou pedir mais informações) ou o canal que vocês já usam resolveria?  
6.6 Por quanto tempo esse resumo deveria ficar disponível para a clínica? Quem na equipe deveria poder vê-lo?  
6.7 Que riscos você vê em a clínica receber, ou em o tutor ver, uma interpretação automática como essa?

**Bloco 7 — Sistema ideal e comentários adicionais**

7.1 Se pudesse mudar uma coisa na forma como os tutores entram em contato ou chegam até vocês, o que seria?  
7.2 Há algo importante sobre a rotina da clínica que eu não perguntei?  
7.3 Gostaria de receber a síntese dos resultados? *Se sim, anotar o contato fora da ficha e apagá-lo após o envio.*

**Encerramento:** Obrigado pela conversa. O resumo mostrado era fictício e não se refere a nenhum caso real. Se quiser retirar o que disse, basta nos avisar até o fim da disciplina.

#### Como os dados serão analisados

As perguntas fechadas do Bloco 1 serão resumidas por contagem (número de entrevistas, funções e tipos de unidade), sem percentuais, porque a amostra é pequena.

As anotações e transcrições anonimizadas serão organizadas em uma tabela por ID e bloco e analisadas por temas. Os temas previstos são canais, papéis e responsabilidades, informação essencial ou ausente, disponibilidade, origem da informação e confiança, retenção e acesso; temas novos serão acrescentados quando aparecerem. Dois integrantes codificarão juntos ao menos uma entrevista para alinhar os códigos. Para cada entrevista será desenhado o fluxo atual (quem recebe → quem decide → como responde), que poderá revisar a jornada da E3 e a persona P03.

A análise separa o que o profissional **relata fazer**, com exemplo (Blocos 2 a 5), do que ele **opina sobre a proposta** (Bloco 6). A reação ao resumo fictício é preferência declarada: não comprova uso nem testa usabilidade, que fica para a E14.

| Hipótese/lacuna | Blocos | Sustentada se… | Refutada ou refinada se… | Decisão de design |
|---|---|---|---|---|
| H05 | 2, 4, 5, 6.4–6.5 | os profissionais precisam confirmar, recusar ou pedir informações sobre o caso e o canal atual não basta. | o canal atual basta e uma tela própria seria mais um canal a acompanhar (refutada); a necessidade varia por função (refinada). | Incluir A06 no recorte; ou retirá-lo e manter o resumo como F09, enviado pelo tutor. |
| H03 | 3, 6.1–6.2 | partes do resumo são apontadas como úteis para preparar o atendimento. | o resumo é visto como redundante ou arriscado. | Campos, ordem e existência do resumo. |
| L02 | 2.2–2.3 | — (lacuna) | — | Descrição de quem recebe, decide e responde; destinatário do resumo. |
| H10a/H10c | 4 | o que define capacidade e disponibilidade fica claro e é algo que o tutor deveria saber. | a capacidade depende de fatores que a clínica não consegue antecipar. | Texto de disponibilidade não confirmada no mapa (T02). |
| H17 | 6.3, 6.7 | a distinção entre relato e conteúdo automático é considerada importante. | — | Rótulos de origem no resumo. |
| L03 | 6.6 | — (lacuna) | — | Requisitos preliminares de retenção e acesso para a E8 e o orientador. |
| H01a/H01b | 3.4 | — | — | Apenas percepção dos profissionais; não mede atraso nem procura inadequada. |

A síntese registrará o número real de entrevistas e as limitações: amostra por conveniência, profissionais de poucas unidades e percepções que não medem frequência. Se as últimas entrevistas ainda trouxerem temas novos, a equipe tentará ampliar a amostra. Após a análise, o histórico em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md) será atualizado.

*Base utilizada: slides CC8122 — Identificação de Necessidades dos Usuários e Requisitos de IHC, partes A (pp. 2–12) e B (pp. 3–5, 20–21), baseados em Barbosa e Silva (2010); Entrega 1 (A06, seção 7.1.1), persona P03 (E3), fluxo PF04 (E6) e matriz de rastreabilidade.*

## Síntese

Explique quais lacunas de conhecimento sobre usuários o conjunto de técnicas pretende reduzir. Indique explicitamente quais hipóteses da Entrega 1 deverão ficar **sustentadas, refutadas ou refinadas** após a análise dos dados. Quando os dados forem coletados/analisados, atualize o histórico em `RASTREABILIDADE.md`.

Esta versão contém as contribuições de Vinícius (A01/I01, questionário com tutores) e de Julian (A02/I02, entrevista semiestruturada com profissionais de clínica). Ambos os instrumentos estão planejados e com cópia textual, sem aplicação ou resultados declarados.

O questionário pretende refinar H07, H08, H06, H09, H10a/H10b/H10c, H12, H14 e H02/H13, além de L05. A entrevista cobre o lado da clínica, que o questionário não alcança: H03, H05 e L02, com contribuições para H10a/H10c, H17 e L03. As duas técnicas se complementam em H10a/H10c, comparando o que o tutor considera ao escolher uma clínica com o que a clínica consegue informar. Após a análise, será indicado quais hipóteses ficaram sustentadas, refutadas ou refinadas no alcance das respostas. Nenhum dos dois instrumentos comprova efeitos sobre tempo ou segurança clínica; a entrevista indica se a interface da clínica é necessária, mas não testa sua usabilidade.

O planejamento considera as personas P01/P02/P03, as tarefas T01–T03 e os fluxos da E6, em conjunto com o [TCC](https://github.com/vinizika/tcc), sua [documentação funcional](https://github.com/vinizika/tcc/blob/main/docs/poc-utilizavel.md) e a [rastreabilidade](../RASTREABILIDADE.md). A entrega permanece em andamento, aguardando a contribuição de João Pedro, com técnica distinta de questionário e entrevista.


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
