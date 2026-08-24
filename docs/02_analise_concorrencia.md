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

{{descrever e ligar à Entrega 1}}

## 2. Concorrentes diretos/indiretos

### Análise C01 — {{produto}}

**Autor(a):** {{nome — matrícula}}  
**Tipo:** direto / indireto / análogo  
**Link oficial:** {{URL}}  
**Data de acesso:** {{dd/mm/aaaa}}

#### Contexto e proposta

{{...}}

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print | Observação de IHC |
|---|---|---|---|
| {{...}} | {{...}} | `../assets/02_concorrencia/...` | {{...}} |

#### Experiência do usuário e opiniões

Use avaliações públicas, relatos, estudos, testes próprios ou outra fonte identificável. Não trate opinião isolada como verdade universal.

#### Preço/modelo de negócio

{{...}}

#### Padrões e tendências percebidos

{{...}}

#### Pontos positivos, limitações e lições

| Ponto | Evidência | Implicação para nosso projeto |
|---|---|---|
| {{...}} | {{...}} | {{...}} |

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
| Navegação |  |  |  |  |
| Feedback/estado |  |  |  |  |
| Prevenção/recuperação de erro |  |  |  |  |
| Terminologia |  |  |  |  |
| Acessibilidade |  |  |  |  |
| Eficiência |  |  |  |  |

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
