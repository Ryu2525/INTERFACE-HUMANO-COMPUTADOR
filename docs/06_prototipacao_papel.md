# Entrega 6 — Prototipação em papel

**Data:** {{06/10/2026}}  
**Status:** 🟨 em andamento       
**Responsabilidade:** 1 solução integrada por equipe

## Objetivo da atividade

Externalizar rapidamente ideias de interação em baixa fidelidade para explorar alternativas antes de investir em detalhes visuais. O valor da atividade está no **ciclo construir → simular → observar → revisar**, não na beleza do desenho.

## 1. Escopo do protótipo

**Personas:** P01 — Camila Rocha (primária, urgência noturna com Bob); P02 — Roberto Nunes (primária, menor familiaridade com aplicativos de saúde, Nina); P03 — Marina Lopes (secundária, apenas como destinatária do resumo; não há tela para ela neste protótipo). 
**Cenários/tarefas cobertos:** C01/T01, C01/T02, C02/T02
**Objetivos principais:** relatar os sinais em linguagem cotidiana, por texto ou voz, e revisar o relato antes do envio (T01; R01, R02; H06, H09);
complementar informações sem inventar sinais, com alternativa estruturada quando a conversa não avança (T01/T03; H12);
compreender a classificação, a justificativa, os limites e o próximo passo, distinguindo INCERTO de NÃO EMERGÊNCIA (T03; R01, R03; H02, H11);
localizar uma clínica com alternativa manual à localização, contatá-la e compartilhar um resumo apenas com revisão e autorização (T02; R04, R05; H03, H05, H10);
manter o contato profissional acessível em qualquer ponto do fluxo (desativação [> dos CTT T01 e T03).

Plataforma prototipada: smartphone, conforme H08 (ainda hipótese). Todos os dados de animais, relatos e clínicas são fictícios.

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
| PF01 | {{...}} | {{...}} |

## 3. Telas e estados

- Numere as telas/estados (`P01`, `P02`...).
- Indique controles que mudam o estado.
- Mostre pelo menos caminhos principais e estados de erro/retorno relevantes.

![Protótipo](../assets/06_prototipos/prototipo_fluxo_01.svg)

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
