# Entrega 8 — Ciclo de vida e engenharia de usabilidade

**Data:** 21/10/2026  
**Status:** 🟩 concluída  
**Responsabilidade:** 1 solução por equipe

## Objetivo da atividade

Transformar o conhecimento acumulado sobre usuários, tarefas, plataforma e contexto em princípios e **metas de usabilidade verificáveis**, mantendo o caráter iterativo do projeto.

## Delimitação do sistema interativo

Antes das características da plataforma, separe:

| Camada | O que pertence ao projeto | O que será avaliado em IHC |
|---|---|---|
| contribuição técnica do TCC | Pré-triagem com LLM/RAG, base veterinária, API e classificação de relatos. | desempenho técnico não é substituído pelo teste de IHC |
| camada de interação da disciplina | Cadastro do tutor/pet, chat, orientação, mapa e continuidade com a clínica. | compreensão, eficácia, eficiência, satisfação, erros, acessibilidade etc. |
| integrações/dados simulados | Na E6, telas em papel e casos, respostas e clínicas fictícios; na aplicação, serviços de IA/mapas e unidades acadêmicas identificadas. | A simulação avalia a interação; envio simulado não confirma atendimento real nem valida a classificação clínica. |

Em um protótipo de disciplina, é aceitável simular processamento ou resultados quando a implementação técnica não estiver integrada, desde que isso seja declarado e a simulação seja suficiente para avaliar a interação.

## 1. Características da plataforma

| Característica | Descrição | Consequência para IHC |
|---|---|---|
| Software | Aplicação web React integrada ao backend do TCC. | Manter navegação e linguagem consistentes entre cadastro, chat e atendimento. |
| Hardware/dispositivos | Navegador em celular ou computador; microfone opcional para voz. | Adaptar o conteúdo à tela e permitir relato por texto sem microfone. |
| Capacidades | Cadastro de pets, chat por texto/voz, histórico, mapa, encaminhamento e painel da clínica, conforme documentação do TCC. | Permitir revisar informações e distinguir mensagem automática de resposta profissional. |
| Restrições | Pré-triagem acadêmica; dados de horário e proximidade não comprovam capacidade de atendimento. | Explicar limites, tratar informação insuficiente e orientar confirmação com a clínica. |
| Conectividade/latência | IA e mapas dependem de serviços e conexão; podem ocorrer falhas ou indisponibilidade. | Mostrar espera e erro, preservar o relato e oferecer retentativa ou busca manual de região. |
| Segurança/privacidade | Contas de tutor/clínica, compartilhamento autorizado e contas acadêmicas compartilhadas. | Explicitar destino e conteúdo do envio; usar dados fictícios nas contas acadêmicas. |
| Volume de dados/histórico | Pets, conversas e encaminhamentos; volume de uso ainda não medido. | Identificar animal, data e estado; avaliar busca/filtros somente se a consulta ao histórico exigir. |
| Tempo de processamento | A análise pode demorar conforme provedor e infraestrutura; sem tempo fixo garantido. | Informar processamento e falha, evitando envio repetido por falta de feedback. |
| Papéis/permissões | Tutor gerencia seus casos; clínica acessa encaminhamentos autorizados para sua unidade; administração controla o vínculo institucional. | Diferenciar acessos e impedir ações ou exposição de casos de outra unidade. |

## 2. Princípios gerais do projeto

Inclua apenas normas, leis, padrões e princípios realmente relevantes, explicando **como** afetam o projeto. Não transforme esta seção em lista de links.

| Princípio/norma | Aplicabilidade ao contexto | Decisão/requisito decorrente | Fonte |
|---|---|---|---|
| Contexto de uso | Tutores adultos de cães/gatos, com diferentes familiaridades digitais; uso sob pressão é hipótese das personas. | Priorizar relato e próximo passo, com linguagem simples e cadastro sem bloquear a orientação inicial. | Entregas 1/3 |
| LGPD, se aplicável | Cadastro, contato e localização podem identificar o tutor. | Solicitar apenas dados necessários, explicar uso/compartilhamento e restringir acesso; nas avaliações, usar casos fictícios. | [Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) |
| Acessibilidade | Leitura, navegação e interpretação em diferentes dispositivos. | Usar texto além de cor, contraste legível, rótulos nos campos e foco visível na navegação por teclado. | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), critérios 1.4.1, 1.4.3, 2.1.1, 2.4.7 e 3.3.2 |
| Feedback e recuperação de erros | Relato, processamento e encaminhamento possuem estados diferentes. | Informar espera/falha, permitir correção e distinguir envio de confirmação de atendimento. | Entregas 2/5/6 |

## 3. Metas de usabilidade

Usabilidade deve ser discutida **no contexto de uso**. Metas quantitativas devem dizer o que será medido, em qual tarefa, com qual população e qual limite será considerado aceitável.

### 3.1 Metas qualitativas

| Meta | Para quem/tarefa | Evidência desejada | Justificativa |
|---|---|---|---|
| Compreender orientação e limites. | P01/P02; T03. | Recontar o resultado e o próximo passo, distinguindo não emergência de ausência de cuidado e INCERTO de não emergência. | Evitar falsa segurança; H02/H13. |
| Relatar e corrigir informações com controle. | P01/P02; T01. | Informar um caso fictício e corrigir o que foi entendido. | Preservar fidelidade e reduzir retrabalho. |
| Distinguir clínica localizada de atendimento confirmado. | P01; T02. | Explicar o estado do contato e o que falta confirmar. | Listagem, envio e aceitação não são equivalentes. |

### 3.2 Metas quantitativas

As metas abaixo são critérios iniciais de projeto, ainda não resultados medidos. Serão verificadas com tutores adultos de cães/gatos, em tarefas fictícias T01–T03, com instruções e dispositivo registrados. A amostra e a versão avaliadas serão definidas no planejamento da Entrega 12. Os limites de 80%, 3 minutos e 4/5 são referências iniciais de autonomia, esforço e satisfação, sem linha de base medida; poderão ser revistos com justificativa após as primeiras avaliações. A compreensão recebe critério mais rigoroso pelo risco de falsa segurança.

| ID | Dimensão | Métrica | Tarefa/escopo | Meta | Como medir | Justificativa |
|---|---|---|---|---|---|---|
| MU01 | eficácia | taxa de conclusão sem ajuda | T01 | ≥ 80% | Observar se registra, confere e envia o relato fictício; dividir conclusões sem ajuda pelo total de participantes da tarefa. | O fluxo central deve ser executável com autonomia. |
| MU02 | eficiência | tempo mediano | T02 | ≤ 3 minutos de interação | Cronometrar da abertura da busca até selecionar uma clínica e localizar o contato, sem ajuda; pausar durante espera de serviço ou troca de telas pelo mediador. Calcular a mediana das conclusões e informar também as falhas. | Limitar esforço para encontrar o próximo passo; não medir deslocamento nem tempo de resposta da clínica. |
| MU03 | satisfação | escala pós-tarefa | T01–T03 | mediana ≥ 4 em escala de 1 a 5 | Após cada tarefa: “Quão satisfeito ficou com a facilidade para realizar esta tarefa?”, de 1 (muito insatisfeito) a 5 (muito satisfeito); calcular a mediana por tarefa. | Registrar a percepção de facilidade junto do desempenho observado. |
| MU04 | compreensão | proporção de interpretações compatíveis | T03 e estado final de T02 | 100% dos participantes em cada situação apresentada | Pedir reconto de mensagens fictícias de não emergência, INCERTO e envio sem confirmação. Contar quem distingue necessidade de acompanhamento, falta de informação e ausência de aceite da clínica; registrar cada situação separadamente. | Interpretações de falsa segurança ou atendimento garantido exigem revisão. |

### 3.3 Priorização das metas (se exigida na disciplina)

Se o professor solicitar porcentagens que somem 100%, trate-as como **peso de prioridade**, não como métrica de usabilidade.

| Meta | Peso de prioridade | Justificativa |
|---|---:|---|
| MU01 | 30% | Autonomia no relato. |
| MU02 | 20% | Esforço para encontrar contato. |
| MU03 | 10% | Satisfação percebida. |
| MU04 | 40% | Compreensão da orientação e dos limites. |
| **Total** | **100%** | |

## 4. Como o ciclo será iterado

Explique que artefatos serão revisitados após protótipos e avaliações.

A coleta da E7 poderá refinar personas, contexto e requisitos. A simulação em papel da E6 orientará ajustes nos fluxos e mensagens. Nas Entregas 12–14, as metas serão verificadas e os problemas encontrados orientarão revisão do protótipo e dos modelos afetados. As decisões e seus vínculos serão registrados em `RASTREABILIDADE.md`; as tarefas afetadas serão reavaliadas quando necessário.

A necessidade do painel da clínica permanece vinculada a H03/H05 e à investigação com profissionais. Este documento conclui a definição da plataforma, dos princípios e das metas; a verificação ocorrerá nas avaliações posteriores.

Base: [documentação funcional do TCC](https://github.com/vinizika/tcc/blob/main/docs/poc-utilizavel.md) e Entregas 1, 3, 5, 6 e 7.

## Checklist

- [x] Capacidades e restrições têm impacto de IHC explicitado.
- [x] Está claro o limite entre contribuição técnica do TCC e camada interativa da disciplina.
- [x] Resultados/processamento simulados no protótipo foram explicitados.
- [x] Metas de usabilidade avaliam a interação, não substituem métricas técnicas do TCC.
- [x] Normas/princípios estão contextualizados, não apenas copiados.
- [x] Metas quantitativas são mensuráveis e associadas a tarefas/público.
- [x] Eficácia, eficiência e satisfação são consideradas quando pertinentes.
- [x] Metas poderão ser verificadas nas Entregas 12–14.

