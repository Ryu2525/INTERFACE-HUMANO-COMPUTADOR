# Entrega 6 — Prototipação em papel

**Data:** 21/10/2026  
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 solução integrada por equipe

## Objetivo da atividade

Externalizar rapidamente ideias de interação em baixa fidelidade para explorar alternativas antes de investir em detalhes visuais. O valor da atividade está no **ciclo construir → simular → observar → revisar**, não na beleza do desenho.

## 1. Escopo do protótipo

**Personas:** P01 — Camila Rocha; P02 — Roberto Nunes; P03 — Marina Lopes.  
**Cenários/tarefas cobertos:** C01/T01 e T02; C03/T03; continuidade de C02 para P03.  
**Objetivos principais:** Explorar em papel o cadastro do tutor e do pet, o relato e a orientação pelo chat, a localização de clínicas no mapa e a consulta do resumo do caso pela clínica. O cadastro não deve impedir o acesso inicial à orientação. O painel da clínica será exploratório, associado às hipóteses H03 e H05.

## 1.1 Possíveis famílias de interface

Escolha apenas o que for coerente com tarefas e cenários. Para TCCs técnicos, o protótipo pode explorar:

- **dashboard** para monitoramento e tomada de decisão;
- **configuração/parametrização** para preparar algoritmo/modelo/processo;
- **entrada/seleção de dados** com validação;
- **acompanhamento de execução** com progresso, fila, cancelamento e recuperação;
- **relatório/resultados** com explicação, gráficos e exportação;
- **histórico** com busca, filtros, ordenação e detalhes;
- **comparação** entre execuções, versões, algoritmos ou períodos;
- **administração** de usuários, papéis, permissões ou entidades do domínio;
- **auditoria/logs** traduzidos para o perfil;
- **alertas/ocorrências** com ação de resposta.

> Não desenhe todas essas telas por obrigação. O objetivo da baixa fidelidade é experimentar a **estrutura da interação** necessária para as tarefas priorizadas.

## 2. Fluxos escolhidos

| Fluxo | Tarefa/objetivo | Por que foi priorizado |
|---|---|---|
| PF01 | Cadastrar tutor e pet: informar dados do tutor, nome, espécie e idade do pet; revisar e corrigir campos. Apoio à T01. | Associar o relato ao animal correto e explorar a validação dos dados, sem bloquear a orientação inicial. |
| PF02 | Usar o chat: selecionar o pet, relatar sinais, responder às perguntas e compreender a orientação e o próximo passo. T01 e T03. | É o fluxo central da pré-triagem; deve contemplar emergência, não emergência e informação insuficiente. |
| PF03 | Achar uma clínica no mapa: usar localização ou informar região, consultar dados da unidade, selecionar e iniciar contato. T02. | Transformar a orientação em busca de atendimento, sem confundir clínica listada com disponibilidade confirmada. |
| PF04 | Consultar o dashboard da clínica: abrir um caso compartilhado com autorização, ler o resumo e informar a possibilidade de atendimento. Continuidade de C02/P03. | Explorar a continuidade tutor–clínica prevista em H03 e H05, ainda sem tarefa própria detalhada na Entrega 5. |

## 3. Telas e estados

- Numere as telas/estados (`P01`, `P02`...).
- Indique controles que mudam o estado.
- Mostre pelo menos caminhos principais e estados de erro/retorno relevantes.


## 4. Simulação / walkthrough

Realize uma simulação com uma pessoa que não participou da elaboração dessas telas. Um colega pode ser usado **para essa iteração formativa**, mas isso não substitui os participantes finais da Entrega 14.

| Observação | Tela/ação | Evidência | Consequência para o design |
|---|---|---|---|
| {{...}} | {{...}} | {{...}} | {{...}} |

## 5. Alterações após a simulação

| Antes | Problema | Depois | Justificativa |
|---|---|---|---|
| {{...}} | {{...}} | {{...}} | {{...}} |

## Checklist

- [ ] O protótipo cobre tarefas relevantes da Entrega 5.
- [ ] Cada tela/estado pode ser justificado por uma tarefa, decisão ou informação necessária.
- [ ] O projeto não criou dashboard/CRUD/login apenas para parecer “completo”.
- [ ] Telas/estados estão numerados e navegáveis na documentação.
- [ ] Há pelo menos uma simulação/walkthrough documentado.
- [ ] Críticas não foram apenas listadas: geraram decisão de revisão.
- [ ] O protótipo continua em baixa fidelidade; detalhes visuais não mascaram problemas de fluxo.

