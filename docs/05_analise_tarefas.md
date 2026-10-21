# Entrega 5 — Análise de tarefas: HTA, GOMS e CTT

**Data:** 03/10/2026  
**Status:** 🟩 concluída  
**Responsabilidade:** cada integrante modela pelo menos 1 HTA, 1 GOMS e 1 CTT. As três técnicas podem abordar a mesma funcionalidade ou funcionalidades distintas, conforme a orientação da disciplina.

## Objetivo da atividade

Modelar tarefas importantes sob perspectivas complementares: decomposição hierárquica (HTA), estrutura de metas/métodos/operações (GOMS) e relações temporais entre tarefas (CTT). O diagrama deve ser acompanhado de interpretação textual.

## Para projetos cujo TCC não previa interface

Modele **tarefas humanas relacionadas ao uso da contribuição técnica**, e não a implementação interna do algoritmo. Exemplos de boas tarefas para análise:

- investigar uma consulta de baixo desempenho;
- configurar uma análise e selecionar parâmetros;
- submeter um dataset e verificar sua validade;
- acompanhar uma execução demorada;
- comparar dois resultados/modelos;
- interpretar uma recomendação e decidir se a aceita;
- localizar uma execução anterior usando busca/filtros;
- gerar e compartilhar um relatório;
- administrar papéis/permissões quando isso for parte do trabalho real;
- revisar um alerta e registrar uma decisão.

Um CRUD pode gerar tarefas relevantes, mas “cadastrar usuário” só merece modelagem se tiver significado no domínio (papéis, validações, riscos, permissões, dependências).

## Seleção das tarefas

| ID | Tarefa | Persona/cenário de origem | Frequência/criticidade | Autor responsável |
|---|---|---|---|---|
| T01 | Relatar sinais e fornecer informações úteis à pré-triagem | P01/C01; R01 e R02; H06, H08, H09 e H12 | A cada pré-triagem; alta criticidade pela fidelidade do relato. | Julian Ryu Takeda — 22.224.030-1 |
| T02 | Localizar e contatar uma clínica e preparar a comunicação do caso | P01/C01 e continuidade de C02/P03; R04 e R05; H03, H05 e H10 | Quando há busca de atendimento; alta criticidade pelo risco de encaminhamento sem confirmação. | Vinícius de Castro Duarte — 22.224.020-2 |
| T03 | Compreender a orientação e resolver informações insuficientes | P02/C03; R01 e R03; H02, H06, H11 e H12 | A cada orientação ou complemento; alta criticidade pela interpretação da incerteza. | João Pedro Gardenghi Peterutto — 22.125.066-5 |

> Priorize tarefas necessárias para que o usuário alcance objetivos centrais. Não desperdice a modelagem em ações triviais isoladas, como “clicar em login”, se o objetivo relevante é maior. Da mesma forma, não modele o funcionamento interno do algoritmo como se fosse uma tarefa humana.

As três técnicas de cada integrante modelam a mesma T01, T02 ou T03. Os modelos são propostas de interação derivadas das Entregas 1 a 4, ainda sujeitas à validação das hipóteses. A interface já integra o TCC; a seção pedagógica sobre TCC sem interface foi preservada como enunciado.

---

## HTA — T01 Relatar sinais e fornecer informações úteis à pré-triagem

**Autor(a):** Julian Ryu Takeda — 22.224.030-1

### Descrição da tarefa

Camila percebe sinais preocupantes em Bob e precisa comunicar o que observou sem conhecer termos veterinários. A tarefa começa quando inicia o relato e termina com o relato revisado e as informações disponíveis enviadas, ou com a decisão de procurar contato profissional sem concluir a coleta. O contexto é noturno, com estresse e possível dificuldade para digitar. Voz e apoio estruturado são propostas a validar, não preferências já comprovadas.

### Diagrama

![HTA T01](../assets/05_tarefas/hta_t01.svg)

Figura HTA T01: elaboração para esta entrega. [Fonte editável](../assets/05_tarefas/hta_t01.json).

### Decomposição e planos

| ID | Objetivo/operação | Plano/ordem | Problema ou decisão de design observada |
|---|---|---|---|
| 0 | Relatar sinais e fornecer informações úteis à pré-triagem | 1 > 2 > 3; se não puder continuar ou decidir buscar ajuda, encerrar a coleta e contatar profissional. | **Input:** percepção de sinais preocupantes em Bob e decisão de descrevê-los. **Feedback:** confirmação de que o relato revisado foi recebido e está disponível para análise; em falha, indicação de não recebimento e retomada sem perda. Saída voluntária para contato profissional deve ficar explícita. Não exigir cadastro completo; preservar dados. |
| 1 | Organizar o contexto do animal | 1.1 > 1.2. | Solicitar apenas dados relevantes. |
| 1.1 | Identificar espécie e animal | Operação. | Evitar confundir animais. |
| 1.2 | Lembrar início e evolução dos sinais | Operação; informar desconhecimento se não lembrar. | Não induzir respostas inventadas. |
| 2 | Registrar e conferir o relato | Escolher 2.1 ou 2.2; depois 2.3; repetir correção em 2.3 até refletir o observado. | Texto e voz devem permitir chegar ao mesmo relato revisado. |
| 2.1 | Digitar os sinais observados | Alternativa textual. | Usar linguagem cotidiana. |
| 2.2 | Gravar e conferir a transcrição | Alternativa por voz, se disponível; se falhar, usar 2.1. | Mostrar estado de gravação e permitir cancelamento. |
| 2.3 | Corrigir e confirmar o relato | Operação; voltar a 2.1 ou 2.2 se necessário. | Não enviar transcrição sem revisão. |
| 3 | Complementar e enviar informações | 3.1 > 3.2; repetir 3.1 somente para lacunas úteis; se houver diálogo sem avanço, oferecer pergunta estruturada. | Progresso deve refletir informação nova, não número de mensagens. |
| 3.1 | Responder sobre informações ausentes | Informar o observado ou não sei. | Permitir resposta desconhecida sem inventar sintomas. |
| 3.2 | Enviar e conferir recebimento | Operação; em falha, tentar novamente sem redigitar. | Distinguir envio, recebimento e análise. |

O diagrama representa a hierarquia de objetivos; a tabela determina a execução. `>` indica sequência; as condições escritas indicam escolhas e retornos. Os nós inferiores representam ações humanas em nível útil para projetar a interação, sem decompor o algoritmo ou cada gesto motor. **Convenção visual:** todos os nós-folha têm fundo verde-claro, borda dupla e rótulo “operação final”; os nós decompostos têm fundo branco e borda simples. A convenção é idêntica nos três HTAs. **Input e feedback da tarefa zero** estão explicitados na última célula da linha 0; as linhas filhas não recebem esses campos.

**Verificação do HTA:**

- O objetivo 0 representa uma meta do usuário?
- As subtarefas são necessárias e suficientes?
- Os **planos** indicam ordem, alternativa, repetição ou condição?
- A decomposição parou em nível útil para projeto de interação?

Verificação: o objetivo 0 é uma meta do usuário; as operações cobrem o início e a conclusão delimitados; os planos explicitam ordem, alternativas e condições; a decomposição termina em ações observáveis. As exceções de falha e decisão de buscar contato não ficam escondidas na sequência principal.

---

## HTA — T02 Localizar e contatar uma clínica e preparar a comunicação do caso

**Autor(a):** Vinícius de Castro Duarte — 22.224.020-2

### Descrição da tarefa

Após decidir buscar atendimento, a tutora precisa encontrar uma clínica, conferir informações e iniciar contato. A tarefa começa com a necessidade de atendimento e termina quando a tutora verifica o retorno da unidade e define a continuidade, com o resumo revisado compartilhado se autorizado, ou procura uma alternativa diante de recusa ou ausência de resposta. Iniciar ligação, entregar mensagem e obter confirmação de atendimento são estados diferentes. C01 fundamenta a busca; C02 fundamenta a prevenção de perda de contexto no contato. P03 é destinatária secundária, não usuária de um dashboard incluído nesta entrega. Não há indicação de especialidade nem garantia automática de vaga.

### Diagrama

![HTA T02](../assets/05_tarefas/hta_t02.svg)

Figura HTA T02: elaboração para esta entrega. [Fonte editável](../assets/05_tarefas/hta_t02.json).

### Decomposição e planos

| ID | Objetivo/operação | Plano/ordem | Problema ou decisão de design observada |
|---|---|---|---|
| 0 | Localizar e contatar uma clínica e preparar a comunicação do caso | 1 > 2 > 3; se a clínica não puder receber, voltar a 2 com outra opção. | **Input:** decisão de buscar atendimento para o animal. **Feedback:** o tutor confere o retorno da unidade (pode receber, não pode receber ou não respondeu); envio do resumo e abertura da rota têm estados separados. Sem retorno, não há confirmação e a busca por alternativa continua. Compartilhar resumo não significa obter vaga. |
| 1 | Definir a região de busca | Escolher 1.1 ou 1.2. | Não bloquear a busca por recusa de localização. |
| 1.1 | Autorizar e conferir localização atual | Alternativa automática. | Pedir permissão no momento da busca. |
| 1.2 | Informar endereço ou região | Alternativa manual; usar se a localização falhar. | Confirmar região interpretada. |
| 2 | Escolher opção e iniciar contato | 2.1 > 2.2; repetir com outra clínica se não houver resposta ou capacidade. | Distância isolada não comprova adequação. |
| 2.1 | Conferir horário, endereço e telefone | Operação; dados ausentes ficam explícitos. | Exibir origem/atualidade disponível, sem presumir funcionamento. |
| 2.2 | Contatar a clínica e perguntar sobre atendimento | Operação; decisão humana baseada no retorno. | Confirmação depende da unidade, não do sistema. |
| 3 | Preparar a comunicação e o deslocamento | 3.1 > 3.2; compartilhar somente se autorizado; abrir rota quando decidir deslocar-se. | Separar consentimento, entrega da mensagem e confirmação clínica. |
| 3.1 | Revisar resumo e destinatário | Operação; corrigir antes de enviar. | Distinguir relato e interpretação automática. |
| 3.2 | Autorizar compartilhamento e consultar rota | Operações condicionais; pode recusar envio e prosseguir com contato. | Não obrigar compartilhamento para localizar atendimento. |

O diagrama representa a hierarquia de objetivos; a tabela determina a execução. `>` indica sequência; as condições escritas indicam escolhas e retornos. Os nós inferiores representam ações humanas em nível útil para projetar a interação, sem decompor o algoritmo ou cada gesto motor. **Convenção visual:** todos os nós-folha têm fundo verde-claro, borda dupla e rótulo “operação final”; os nós decompostos têm fundo branco e borda simples. A convenção é idêntica nos três HTAs. **Input e feedback da tarefa zero** estão explicitados na última célula da linha 0; as linhas filhas não recebem esses campos.

**Verificação do HTA:**

- O objetivo 0 representa uma meta do usuário?
- As subtarefas são necessárias e suficientes?
- Os **planos** indicam ordem, alternativa, repetição ou condição?
- A decomposição parou em nível útil para projeto de interação?

Verificação: o objetivo 0 é uma meta do usuário; as operações cobrem o início e a conclusão delimitados; os planos explicitam ordem, alternativas e condições; a decomposição termina em ações observáveis. As exceções de falha e decisão de buscar contato não ficam escondidas na sequência principal.

---

## HTA — T03 Compreender a orientação e resolver informações insuficientes

**Autor(a):** João Pedro Gardenghi Peterutto — 22.125.066-5

### Descrição da tarefa

Roberto precisa compreender a orientação sobre Nina e saber o que fazer. A tarefa começa com a apresentação de um resultado ou de uma solicitação de complemento e termina quando ele identifica a classificação, os limites e o próximo passo, ou busca contato profissional quando a informação permanece insuficiente. O contexto envolve sinais graduais, dados dispersos e pouca familiaridade com aplicações de saúde, sem presumir dificuldades pela idade.

### Diagrama

![HTA T03](../assets/05_tarefas/hta_t03.svg)

Figura HTA T03: elaboração para esta entrega. [Fonte editável](../assets/05_tarefas/hta_t03.json).

### Decomposição e planos

| ID | Objetivo/operação | Plano/ordem | Problema ou decisão de design observada |
|---|---|---|---|
| 0 | Compreender a orientação e resolver informações insuficientes | 1 > 2 > 3; se 2 indicar lacunas, 3.1 e voltar a 1 após nova apresentação; sem avanço, 3.2. | **Input:** preocupação com mudanças em Nina, envio de observações e recebimento de uma orientação ou pedido de complemento. **Feedback:** a interface apresenta o caso/horário, o estado atual, a justificativa ou lacuna e o próximo passo; após complemento, mostra recebimento e atualização ou falha. A compreensão será verificada pelo reconto do tutor em avaliação, não presumida por exibir a mensagem. Persistindo dúvida, contato profissional é alternativa. INCERTO não equivale a NÃO EMERGÊNCIA. |
| 1 | Ler a orientação do caso correto | 1.1 > 1.2. | Evitar interpretar resultado de outro animal. |
| 1.1 | Conferir animal e horário do resultado | Operação. | Identificar contexto e atualidade. |
| 1.2 | Identificar EMERGÊNCIA, NÃO EMERGÊNCIA ou INCERTO | Operação. | Usar texto e hierarquia, além da cor. |
| 2 | Interpretar justificativa e limites | 2.1 > 2.2. | Não apresentar diagnóstico nem garantia de ausência de risco. |
| 2.1 | Relacionar a justificativa ao que relatou | Operação; pedir explicação se houver dúvida. | Distinguir dado do tutor e inferência. |
| 2.2 | Identificar o que falta e o próximo passo | Operação. | Uma ação principal por estado. |
| 3 | Agir conforme a informação disponível | Escolher 3.1 se INCERTO e houver condição de continuar; escolher 3.2 se houver orientação acionável ou necessidade de contato. | Contato profissional deve permanecer acessível durante a coleta. |
| 3.1 | Complementar por conversa ou pergunta estruturada | Repetir apenas com avanço útil; poder responder não sei; revisar e aguardar atualização. | Formulário direto quando o diálogo não produz informação útil. |
| 3.2 | Executar próximo passo ou contatar profissional | Operação; localizar atendimento quando necessário. | Se NÃO EMERGÊNCIA: identificar o que observar, quando reavaliar e o que muda a orientação; acompanhar conforme orientação e buscar contato diante de mudança ou dúvida (H13). Não concluir que o animal está saudável. |

O diagrama representa a hierarquia de objetivos; a tabela determina a execução. `>` indica sequência; as condições escritas indicam escolhas e retornos. Os nós inferiores representam ações humanas em nível útil para projetar a interação, sem decompor o algoritmo ou cada gesto motor. **Convenção visual:** todos os nós-folha têm fundo verde-claro, borda dupla e rótulo “operação final”; os nós decompostos têm fundo branco e borda simples. A convenção é idêntica nos três HTAs. **Input e feedback da tarefa zero** estão explicitados na última célula da linha 0; as linhas filhas não recebem esses campos.

**Verificação do HTA:**

- O objetivo 0 representa uma meta do usuário?
- As subtarefas são necessárias e suficientes?
- Os **planos** indicam ordem, alternativa, repetição ou condição?
- A decomposição parou em nível útil para projeto de interação?

Verificação: o objetivo 0 é uma meta do usuário; as operações cobrem o início e a conclusão delimitados; os planos explicitam ordem, alternativas e condições; a decomposição termina em ações observáveis. As exceções de falha e decisão de buscar contato não ficam escondidas na sequência principal.

---

## GOMS — T02 Localizar e contatar uma clínica e preparar a comunicação do caso

**Autor(a):** Vinícius de Castro Duarte — 22.224.020-2

### Goal

`G0: Localizar uma clínica e iniciar contato com informações conferidas`

### Métodos, operadores e regras de seleção

```text
Method M1: Busca pela localização atual: solicitar localização; autorizar; conferir a região; examinar opções; selecionar clínica; conferir horário/endereço/telefone; iniciar contato; comunicar o caso; verificar o retorno da unidade e a situação do atendimento.
    Operators: Ler solicitação; decidir sobre permissão; tocar autorizar; conferir região; ler opções; comparar dados; tocar clínica; ler informações; tocar contato; relatar o caso; ouvir ou ler a resposta; perceber se houve confirmação, recusa ou ausência de retorno.
Method M2: Busca por região manual: informar endereço ou região; revisar; solicitar busca; examinar opções; selecionar clínica; conferir horário/endereço/telefone; iniciar contato; comunicar o caso; verificar o retorno da unidade e a situação do atendimento.
    Operators: Tocar campo; digitar região; ler e corrigir; tocar buscar; ler opções; comparar dados; tocar clínica; ler informações; tocar contato; relatar o caso; ouvir ou ler a resposta; perceber se houve confirmação, recusa ou ausência de retorno.
Selection Rule SR1: usar M1 quando autorizar localização e ela representar o ponto de partida desejado; usar M2 quando não autorizar, a localização falhar ou quiser buscar outra região. Os métodos alcançam a mesma meta; a confirmação de atendimento depende da resposta explícita da unidade. Sem resposta ou diante de recusa, a verificação detecta que a meta não foi concluída e o HTA orienta nova opção.
```

> Não chame qualquer passo de “método”. Em GOMS, métodos são sequências alternativas capazes de atingir uma meta; regras de seleção explicam quando escolher entre eles.

Interpretação: M1 e M2 são sequências completas alternativas para G0. Ler/perceber são operadores perceptivos; recordar/decidir são cognitivos; tocar/digitar/falar são ações motoras ou de comunicação. Resposta do sistema é uma condição de continuidade, não uma decisão atribuída ao tutor. Foi adotado GOMS qualitativo, sem estimativas KLM de tempo. O modelo descreve execução conhecida da tarefa; recuperação de falhas e estados de incerteza são detalhados no HTA e no CTT.

**Delimitação do GOMS de T02:** G0 cobre a submeta de localizar, contatar e verificar o retorno da unidade, comum aos dois métodos. Revisão/autorização do resumo e rota são continuações opcionais modeladas no HTA/CTT de T02. Não são métodos alternativos para localizar a mesma clínica. A aula GOMS-CTT, pp. 3–14, diferencia meta, método, operadores e regra de seleção; o feedback da equipe já considerou essa estrutura correta. Não foram atribuídos tempos KLM de teclado/mouse ao uso hipotético por smartphone.

---

## GOMS — T01 Relatar sinais e fornecer informações úteis à pré-triagem

**Autor(a):** Julian Ryu Takeda — 22.224.030-1

### Goal

`G0: Enviar um relato revisado dos sinais observados no animal`

### Métodos, operadores e regras de seleção

```text
Method M1: Relato por texto: identificar o animal; recordar início e evolução; digitar os sinais; revisar; corrigir; enviar; verificar recebimento.
    Operators: Ler identificação e instrução; recordar observações; tocar campo; digitar; ler o relato; decidir sobre correções; editar; tocar enviar; perceber confirmação.
Method M2: Relato por voz: identificar o animal; recordar início e evolução; iniciar gravação; narrar os sinais; encerrar; aguardar transcrição; revisar; corrigir; enviar; verificar recebimento.
    Operators: Ler identificação; recordar observações; tocar gravar; falar; tocar encerrar; perceber estado da transcrição; ler; decidir sobre correções; editar; tocar enviar; perceber confirmação.
Selection Rule SR1: usar M1 quando puder digitar ou a voz estiver indisponível/inadequada; usar M2 quando a entrada por voz estiver disponível, o ambiente permitir e o tutor preferir narrar. Ambos terminam no mesmo relato revisado e enviado. A utilidade da voz permanece H09.
```

> Não chame qualquer passo de “método”. Em GOMS, métodos são sequências alternativas capazes de atingir uma meta; regras de seleção explicam quando escolher entre eles.

Interpretação: M1 e M2 são sequências completas alternativas para G0. Ler/perceber são operadores perceptivos; recordar/decidir são cognitivos; tocar/digitar/falar são ações motoras ou de comunicação. Resposta do sistema é uma condição de continuidade, não uma decisão atribuída ao tutor. Foi adotado GOMS qualitativo, sem estimativas KLM de tempo. O modelo descreve execução conhecida da tarefa; recuperação de falhas e estados de incerteza são detalhados no HTA e no CTT.

---

## GOMS — T03 Compreender a orientação e resolver informações insuficientes

**Autor(a):** João Pedro Gardenghi Peterutto — 22.125.066-5

### Goal

`G0: Fornecer um complemento revisado para esclarecer uma orientação INCERTA`

### Métodos, operadores e regras de seleção

```text
Method M1: Complemento pela conversa: ler a pergunta específica; relacioná-la ao que observou; formular resposta; informar desconhecimento se necessário; revisar; enviar; conferir recebimento.
    Operators: Ler; recordar; decidir o que sabe; tocar campo; digitar; ler e corrigir; tocar enviar; perceber confirmação.
Method M2: Complemento pela pergunta estruturada: ler a pergunta direta e suas opções; relacioná-las ao que observou; escolher a resposta ou não sei; revisar; confirmar; conferir recebimento.
    Operators: Ler pergunta; ler opções; recordar; decidir; tocar opção; conferir seleção; tocar confirmar; perceber confirmação.
Selection Rule SR1: usar M1 enquanto a conversa permitir informar a lacuna de modo útil; usar M2 quando o sistema apresentar a pergunta estruturada por falta de avanço útil e a lacuna puder ser respondida pelas opções. Ambos fornecem informação sobre a mesma lacuna; responder não sei é válido e não garante uma classificação conclusiva.
```

> Não chame qualquer passo de “método”. Em GOMS, métodos são sequências alternativas capazes de atingir uma meta; regras de seleção explicam quando escolher entre eles.

Interpretação: M1 e M2 são sequências completas alternativas para G0. Ler/perceber são operadores perceptivos; recordar/decidir são cognitivos; tocar/digitar/falar são ações motoras ou de comunicação. Resposta do sistema é uma condição de continuidade, não uma decisão atribuída ao tutor. Foi adotado GOMS qualitativo, sem estimativas KLM de tempo. O modelo descreve execução conhecida da tarefa; recuperação de falhas e estados de incerteza são detalhados no HTA e no CTT.

G0 é a submeta de complementação de T03. A leitura do resultado e a ação posterior continuam representadas no HTA e no CTT; não foram tratadas como métodos alternativos de fornecer a mesma informação.

---

## CTT — T03 Compreender a orientação e resolver informações insuficientes

**Autor(a):** João Pedro Gardenghi Peterutto — 22.125.066-5

### Descrição

Antes do uso, Roberto percebe mudanças graduais em Nina e decide buscar orientação (U: ação externa, E4:C03). Após obter uma orientação, o sistema apresenta o estado do caso e os dados para interpretação pelo tutor. A classificação, justificativa e limites precedem a escolha entre complementar informações e executar o próximo passo. Encerrar a coleta e iniciar contato pode interromper o fluxo. A opção de complemento só fica habilitada quando há uma lacuna; a ação correspondente ao resultado deve ser apresentada quando houver orientação acionável.

### Diagrama

![CTT T03](../assets/05_tarefas/ctt_t03.svg)

Figura CTT T03: elaboração para esta entrega. [Fonte editável](../assets/05_tarefas/ctt_t03.json).

### Legenda e relações temporais usadas

| Operador/relação | Significado no diagrama | Exemplo no modelo |
|---|---|---|
| `A` | Tarefa abstrata; decompõe-se em subtarefas. | Raiz e agrupamentos internos. |
| `U` | Ação do usuário fora da interação; pode motivar o uso. | Perceber sinais ou decidir buscar atendimento. |
| `I` | Interação usuário–sistema. | Informar, revisar, enviar ou verificar feedback. |
| `S` | Processamento/apresentação pelo sistema. | Registrar relato (T01), apresentar clínicas (T02) ou estado do caso (T03). |
| `>>` | Ativação sequencial. | Gatilho externo antes de iniciar a interação. |
| `[]>>` | Ativação com passagem de informação. | Dados enviados habilitam processamento ou interpretação. |
| `[]` | Escolha exclusiva naquele ciclo. | Texto/voz (T01), localização/manual (T02) ou complemento/ação (T03). |
| `[>` | Desativação: a tarefa à direita interrompe a da esquerda. | Encerrar coleta e iniciar contato; sem retomada automática. |

Os operadores escritos no nó abstrato relacionam seus filhos da esquerda para a direita. A árvore representa decomposição temporal, não navegação entre telas. Tipos de tarefa estão identificados pelas letras, além das cores. `[]>>`, `>>`, `[]` e `[>` seguem as relações apresentadas nos slides de GOMS-CTT, páginas 19 a 23.

Identifique, quando aplicável, tarefas de usuário, sistema, interação e tarefas abstratas. Verifique se concorrência, escolha, habilitação, desabilitação e repetição estão representadas corretamente segundo a notação adotada em aula.

Se o complemento for enviado, um novo ciclo começa com a apresentação atualizada do estado do caso. Esse retorno condicional é descrito no HTA; o CTT mostra um ciclo. Não há repetição obrigatória ou indefinida. A consulta de uma ajuda que preserve o ponto de leitura seria suspensão/retomada (`|>`), mas esse recurso não foi incluído no diagrama.

---

## CTT — T01 Relatar sinais e fornecer informações úteis à pré-triagem

**Autor(a):** Julian Ryu Takeda — 22.224.030-1

### Descrição

Antes do uso, Camila percebe sinais preocupantes em Bob (U: ação externa). Em seguida, o tutor informa contexto antes de preparar e enviar o relato. Texto e voz são alternativas de entrada, não ações obrigatórias cumulativas. O relato produzido é passado à revisão e ao envio; o sistema valida e registra as informações recebidas (S), apresenta o estado de recebimento (S) e o tutor verifica a confirmação (I). A análise clínica do caso fica além da conclusão deste ciclo de relato. A ação de encerrar a coleta e iniciar contato pode interromper o caminho em curso.

### Diagrama

![CTT T01](../assets/05_tarefas/ctt_t01.svg)

Figura CTT T01: elaboração para esta entrega. [Fonte editável](../assets/05_tarefas/ctt_t01.json).

### Legenda e relações temporais usadas

| Operador/relação | Significado no diagrama | Exemplo no modelo |
|---|---|---|
| `A` | Tarefa abstrata; decompõe-se em subtarefas. | Raiz e agrupamentos internos. |
| `U` | Ação do usuário fora da interação; pode motivar o uso. | Perceber sinais ou decidir buscar atendimento. |
| `I` | Interação usuário–sistema. | Informar, revisar, enviar ou verificar feedback. |
| `S` | Processamento/apresentação pelo sistema. | Registrar relato (T01), apresentar clínicas (T02) ou estado do caso (T03). |
| `>>` | Ativação sequencial. | Gatilho externo antes de iniciar a interação. |
| `[]>>` | Ativação com passagem de informação. | Dados enviados habilitam processamento ou interpretação. |
| `[]` | Escolha exclusiva naquele ciclo. | Texto/voz (T01), localização/manual (T02) ou complemento/ação (T03). |
| `[>` | Desativação: a tarefa à direita interrompe a da esquerda. | Encerrar coleta e iniciar contato; sem retomada automática. |

Os operadores escritos no nó abstrato relacionam seus filhos da esquerda para a direita. A árvore representa decomposição temporal, não navegação entre telas. Tipos de tarefa estão identificados pelas letras, além das cores. `[]>>`, `>>`, `[]` e `[>` seguem as relações apresentadas nos slides de GOMS-CTT, páginas 19 a 23.

Identifique, quando aplicável, tarefas de usuário, sistema, interação e tarefas abstratas. Verifique se concorrência, escolha, habilitação, desabilitação e repetição estão representadas corretamente segundo a notação adotada em aula.

Revisões adicionais e perguntas complementares são retornos condicionais descritos no HTA. O CTT cobre um ciclo de envio e a interrupção; não pressupõe concorrência entre falar e digitar nem adiciona operadores sem necessidade.

---

## CTT — T02 Localizar e contatar uma clínica e preparar a comunicação do caso

**Autor(a):** Vinícius de Castro Duarte — 22.224.020-2

### Descrição

Antes do uso, Camila decide buscar atendimento após observar Bob (U: ação externa, E4:C01). A região é definida por localização atual ou entrada manual. O sistema usa essa informação para apresentar clínicas. O tutor examina os dados e seleciona uma opção antes de preparar o contato. Pode comunicar o caso sem compartilhar um resumo ou revisar, autorizar e compartilhar. A escolha não transforma envio em confirmação de atendimento.

### Diagrama

![CTT T02](../assets/05_tarefas/ctt_t02.svg)

Figura CTT T02: elaboração para esta entrega. [Fonte editável](../assets/05_tarefas/ctt_t02.json).

### Legenda e relações temporais usadas

| Operador/relação | Significado no diagrama | Exemplo no modelo |
|---|---|---|
| `A` | Tarefa abstrata; decompõe-se em subtarefas. | Raiz e agrupamentos internos. |
| `U` | Ação do usuário fora da interação; pode motivar o uso. | Perceber sinais ou decidir buscar atendimento. |
| `I` | Interação usuário–sistema. | Informar, revisar, enviar ou verificar feedback. |
| `S` | Processamento/apresentação pelo sistema. | Registrar relato (T01), apresentar clínicas (T02) ou estado do caso (T03). |
| `>>` | Ativação sequencial. | Gatilho externo antes de iniciar a interação. |
| `[]>>` | Ativação com passagem de informação. | Dados enviados habilitam processamento ou interpretação. |
| `[]` | Escolha exclusiva naquele ciclo. | Texto/voz (T01), localização/manual (T02) ou complemento/ação (T03). |

Os operadores escritos no nó abstrato relacionam seus filhos da esquerda para a direita. A árvore representa decomposição temporal, não navegação entre telas. Tipos de tarefa estão identificados pelas letras, além das cores. `[]>>`, `>>`, `[]` e `[>` seguem as relações apresentadas nos slides de GOMS-CTT, páginas 19 a 23.

Identifique, quando aplicável, tarefas de usuário, sistema, interação e tarefas abstratas. Verifique se concorrência, escolha, habilitação, desabilitação e repetição estão representadas corretamente segundo a notação adotada em aula.

Um contato sem resposta ou uma clínica indisponível exige um novo ciclo de escolha de opção, conforme o HTA. Não foi modelado atendimento simultâneo, pois selecionar e verificar a clínica antecedem a comunicação neste recorte.

---

## Síntese da equipe

Quais problemas de interação, oportunidades e requisitos apareceram a partir das modelagens? Quais tarefas irão para o protótipo e para o teste de usabilidade?

T01 evidencia o risco de perder ou distorcer o relato, especialmente por transcrição não revisada, repetição de perguntas e falha no envio. T02 evidencia a diferença entre encontrar uma clínica, iniciar contato, compartilhar informações e obter confirmação de atendimento. T03 evidencia que ler uma classificação não garante compreender os motivos, os limites ou o próximo passo. Essas interpretações são resultados da modelagem, não resultados de testes já realizados.

O protótipo deve permitir revisão e correção sem perda de contexto, alternativa manual à localização, pergunta estruturada quando a conversa não avançar e identificação explícita do estado do caso. A intenção de coleta discutida no projeto usa os campos de sintomas da base para apoiar a classificação; esta revisão documental não confirma a regra atualmente implementada no código. Com informação insuficiente, INCERTO conduz à complementação. Uma contagem de mensagens ou de detalhes administrativos não demonstra suficiência clínica. O tutor não deve inventar um sinal para completar a coleta. O limiar de detecção de conversa improdutiva ainda precisa ser definido e avaliado; a modelagem não estabelece uma quantidade arbitrária de tentativas. O contato profissional continua disponível durante a coleta.

A interface comunica as categorias EMERGÊNCIA e NÃO EMERGÊNCIA e o estado de informação INCERTO. INCERTO significa insuficiência para concluir; NÃO EMERGÊNCIA não representa diagnóstico nem garantia de saúde. O encaminhamento usa endereço, horário e telefone disponíveis, sem indicação de especialidade. A comunicação do resumo depende de revisão e autorização; recebimento da mensagem e capacidade de atendimento são estados distintos. H03, H05 e H09 permanecem abertas; não se afirma validação da interface clínica, da utilidade do resumo ou da preferência por voz.

| Tarefa | Cobertura no protótipo | Situação no teste de usabilidade | Evidência a observar |
|---|---|---|---|
| T01 | Relato por texto; alternativa de voz e revisão quando disponível; complementação; envio e falha | Informar um caso fornecido pelo avaliador e corrigir uma transcrição com erro | Fidelidade do relato, correção percebida, conclusão, tempo, erros e perda de dados |
| T02 | Busca automática/manual; dados da clínica; contato; resumo revisável e consentimento | Buscar atendimento com localização recusada e escolher outra clínica após indisponibilidade | Se encontra a alternativa, confere informações e distingue contato/envio de confirmação |
| T03 | Resultado, justificativa, limites, INCERTO e pergunta estruturada | Explicar o resultado com suas palavras e responder a uma lacuna sem inventar informação | Compreensão da classificação e do próximo passo; uso de não sei; perguntas repetidas e abandono |

Os testes são simulações com casos fictícios e avaliam a interação, não a precisão clínica. A alternativa de voz e o compartilhamento podem ser prototipados para investigar as hipóteses sem transformar sua implementação em fato. O núcleo prioritário é o fluxo do tutor; não foram adicionados login, dashboard, CRUD administrativo ou filtros sem objetivo de domínio.

| Necessidade na matriz | Persona/cenário | Tarefa e artefatos desta entrega |
|---|---|---|
| R01 | P01/C01 e P02/C03 | T01 e T03; respectivos HTA, GOMS e CTT |
| R02 | P01/C01 | T01; HTA-T01, GOMS-T01 e CTT-T01 |
| R03 | P02/C03 | T03; HTA-T03, GOMS-T03 e CTT-T03 |
| R04 | P01/C01 | T02; HTA-T02, GOMS-T02 e CTT-T02 |
| R05 | Continuidade de C02; P01 como emissora e P03 como destinatária | T02; HTA-T02, GOMS-T02 e CTT-T02; hipótese secundária H03/H05 |

A tabela liga os modelos às necessidades existentes. A versão corrigida de `RASTREABILIDADE.md`, incluída no pacote, integra os vínculos T01–T03, personas e cenários e substitui a pendência de aplicar um arquivo paralelo de sugestões. O checklist refere-se ao conjunto local entregue; a publicação no repositório remoto não foi realizada nesta revisão. Referências qualificadas: E2:C01–C03 são concorrentes; E4:C01–C03 são cenários.

**Histórico de revisões — 21/10/2026:** destacados todos os nós-folha dos HTAs; acrescentados input e feedback nas três tarefas zero; incluído um gatilho externo U em cada CTT e processamento S em T01; os dois métodos de T02 terminam em verificação. SVGs e fontes JSON foram atualizados conjuntamente. O ramo de NÃO EMERGÊNCIA foi explicitado no plano de T03 e na jornada da Entrega 3, sem declarar validação clínica.

Base utilizada: guias de uso e escopo, README, matriz e Entregas 1 a 4 do repositório Ryu2525/INTERFACE-HUMANO-COMPUTADOR, consultados em 03/10/2026, revisão 281ba8adfb7734dafd92d090f50dbef1d935b35e. Referência conceitual principal: slides CC8122-HTA, páginas 2 a 10, e CC8122-GOMS-CTT, páginas 2 a 23, material da disciplina baseado em Barbosa e Silva (2010). Os slides de personas, cenários, refinamento, qualidade de uso e abordagens teóricas fundamentam a continuidade entre contexto, tarefa e decisões de interação. As hipóteses de esforço e acessibilidade não foram convertidas em resultados empíricos. Conferência com os PDFs agora fornecidos: HTA, pp. 4–8; GOMS-CTT, pp. 3–14 e 19–24. Mantidos destaque das folhas, input/feedback apenas na raiz, ação externa U nos três CTTs, processamento S em T01 e verificação final em ambos os métodos de T02, conforme o feedback.

## Checklist

- [x] Cada integrante produziu ao menos 1 HTA, 1 GOMS e 1 CTT.
- [x] Cada artefato identifica autor e tarefa.
- [x] Diagramas são legíveis e possuem fonte editável quando possível.
- [x] HTA contém planos, não apenas árvore de tópicos.
- [x] GOMS distingue Goals, Operators, Methods e Selection Rules.
- [x] CTT usa operadores temporais e tipos de tarefa coerentes.
- [x] Há texto explicando cada diagrama.
- [x] Tarefas estão ligadas a cenários/personas na rastreabilidade.
- [x] Em TCC técnico, as tarefas descrevem o que a pessoa faz com a contribuição/resultados, não passos internos do código.
- [x] CRUDs, relatórios, filtros e atividades administrativas foram escolhidos por relevância ao objetivo do usuário.

