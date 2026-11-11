# Entrega 10 — MoLIC

**Data:** 04/11/2026

**Status:** 🟨 em andamento — etapa 2/3

**Responsabilidade:** 1 solução completa por integrante e consolidação da equipe.

**Versão cumulativa 2/3:** Vinícius + Julian. O que já foi incluído permanece completo; faltam as contribuições seguintes. Os IDs são estáveis: M02 = Vinícius; M01 = Julian; M03 = João. A ordem de commit não altera esses vínculos com CI02/CI01/CI03.

## Objetivo da atividade

Modelar a interação como uma conversa entre usuário e preposto do designer, explicitando tópicos, signos, alternativas, processamentos e recuperação de rupturas. As cenas representam assuntos da conversa, não apenas páginas nem etapas internas do RAG.

## Entradas e delimitação

Base: `main`, revisão `ef16972f7582b482494a0827304caa1c57244e82`, consultada em 04/11/2026. Considerados README, guias, bibliografia, checklist, matriz, entregas, instrumentos e fontes dos assets do repositório. Referências diretas: [E4](04_cenarios_problema.md), [E5](05_analise_tarefas.md), [E6](06_prototipacao_papel.md), [E8](08_engenharia_usabilidade.md) e [E9](09_modelo_conceitual.md), além dos três PDFs de MoLIC fornecidos.

Os modelos descrevem a interação proposta para a POC acadêmica. Modelagem não comprova implementação, compreensão, precisão clínica ou benefício do resumo. Casos e unidades da prototipação são fictícios. H03/H05 e as demais hipóteses continuam abertas; a clínica permanece exploratória e secundária. Não há encaminhamento automático por especialidade.

**Recorte da E6 atual:** esta iteração cobre o caminho de possível emergência de P01: relato no chat, compreensão da orientação, mapa e envio autorizado do caso (PF02/PF03; T01/T03/T02). A E6 relata uma simulação com o orientador e distingue clínicas públicas para contato das unidades acadêmicas habilitadas para envio. Cadastro completo, informação insuficiente e painel da clínica ficam fora dessa iteração. M01 articula o caminho do tutor; M02 e M03 mantêm origem conceitual em CI02/CI03 da E9 e não são apresentados como avaliados pela simulação atual. H03/H05 continuam abertas. A E10 preserva os três cenários da E9.

**Continuidade da E9:** a revisão-base contém CI01, CI02 e CI03, os três mapas individuais, o mapa consolidado e o esquema único de signos. M01 deriva de CI01 (Julian), M02 de CI02 (Vinícius) e M03 de CI03 (João). O01–O10 e S01–S24 mantêm seus nomes e significados; os documentos já concluídos são preservados.

### Notação e organização dos diagramas

| Elemento | Representação e significado |
|---|---|
| Abertura | Círculo preto e fala de entrada; `gco` indica abertura da conversa sobre a meta. |
| Cena | Retângulo arredondado com tópico separado dos diálogos/signos. `M01.C01` identifica cena, sem reutilizar E4:C01. |
| Diálogo | `u:` = usuário; `d:` = preposto do designer; `u+d:` = diálogo sobre os signos indicados. Em M02, o usuário é o profissional; nos demais, o tutor. |
| Transição | Seta com fala do usuário ou preposto; condições entre colchetes. |
| Processo | Quadrado preto: o sistema determina a continuação após a solicitação; saídas são falas `d:`. `P01` etc. são IDs locais à folha, não personas. |
| Alerta e recuperação | Cena de contorno tracejado para alerta/erro; setas tracejadas destacam recuperação/volta. Não significam ação automática. |
| Acesso ubíquo | Cena cinza informa em quais cenas pode ser acionada. Busca de ajuda não depende de concluir coleta/cadastro. |
| Encerramento | Círculo preto com anel externo; `gcc` fecha a conversa sobre a meta, sem afirmar desfecho clínico. |
| Referência entre folhas | Nota com destino: recurso editorial, não novo símbolo de cena ou nova tela. As aberturas das folhas seguintes continuam a mesma conversa. |

Notação baseada nos slides CC8122 — MoLIC, Parte A, pp. 3–15, e Parte B, pp. 2–5. Parte C, pp. 14–18, fundamenta a passagem para interface: uma cena pode corresponder a uma ou mais apresentações. Os desenhos foram divididos em folhas para preservar os textos; os SVGs permitem ampliar sem perda. [Índice e fontes editáveis](../assets/10_molic/README.md).

## M02 — Organizar o caso e responder sobre a capacidade da clínica

**Autor(a):** Vinícius de Castro Duarte — 22.224.020-2

**Cenário de interação de origem:** CI02; E4:C02; P03.

**Objetivo(s):** O06 — Consultar o caso e conferir sua origem; O07 — Solicitar complemento e informar capacidade; O09 — Corrigir e recuperar a interação; O10 — Acompanhar a resposta da clínica, pelo lado profissional que a registra.

**Tarefa(s) relacionada(s):** continuidade de T02 e cenário CI02 da E9. Não se cria uma tarefa formal T04 inexistente na E5.

**Signos relevantes:** S01–S04, S09/S10, S17 e S20–S24. R05; RC05/RC08/RC13; H03/H05/H17; L02/L03.

### Diagrama

![MoLIC M02 — folha A: acesso e consulta](../assets/10_molic/molic_m02.svg)

*Figura M02-A — Consultar caso autorizado. [Fonte editável](../assets/10_molic/molic_m02.dot).*

![MoLIC M02 — folha B: comunicação e capacidade](../assets/10_molic/molic_m02_resposta.svg)

*Figura M02-B — Comunicar decisão humana. [Fonte editável](../assets/10_molic/molic_m02_resposta.dot). Fonte: elaboração para esta entrega sob a responsabilidade individual indicada. Fluxo exploratório, H03/H05.*

### Leitura do diagrama

#### Caminho principal

1. Marina acessa a área da unidade em C01; P01 verifica o vínculo e apresenta os encaminhamentos autorizados àquela clínica.
2. Seleciona caso em C02. P03 confere acesso antes de C03 mostrar resumo, relato original, orientação automática, lacunas e horários. Visualização/recebimento não aceita o caso automaticamente.
3. Se faltar informação, prepara pergunta em C06 e envia por P04. A resposta do tutor aparece como atualização identificada, sem reescrever silenciosamente o registro original.
4. Confere a capacidade com a equipe fora do sistema. Em C07, informa se a unidade pode ou não receber, revisa destinatário e confirma a decisão humana.
5. P04 registra a comunicação; C08 mostra origem e horário, sem presumir leitura pelo tutor. O tutor consulta esse mesmo estado no fluxo CI01, preservando a distinção entre envio, leitura e aceite. Nova informação ou alteração de capacidade exige atualização explícita e comunicação.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Recuperação/saída |
|---|---|---|---|
| Credencial inválida, sessão expirada ou caso não autorizado | P01/P03/C05 | Mensagem de acesso sem exibir conteúdo privado. | Corrigir acesso, reautenticar, voltar à lista permitida ou sair. |
| Lista vazia ou falha | P02/C04 | Ausência de pedidos diferenciada de erro. | Atualizar; falha não implica desaparecimento de casos. |
| Dado ausente, antigo ou contraditório | C03/C06 | Relato, origem e horários separados; lacuna identificada. | Solicitar confirmação; não informado não vira negativa clínica. |
| Mensagem vazia ou envio não confirmado | P04/C09 | Validação ou erro, com texto mantido. | Corrigir ou consultar o registro antes de retentar; não duplicar comunicação já registrada. |
| Unidade não pode receber | C07/C08 | Recusa e mensagem explícitas. | Comunicar limitação; tutor procura outra unidade pelo fluxo CI01, sem promessa de vaga externa. |
| Estado/versão mudou antes da decisão | P04/C10 | Atualização sinalizada; nada sobrescrito silenciosamente. | Conferir M02-A e revisar resposta. |
| Tutor ainda não respondeu | P05/C08 | Último estado e horário. | Consultar depois, voltar ao caso ou atualizar comunicação conforme decisão profissional. |
| Desistência da edição | C06 | Volta sem confirmação de envio. | Cancelar edição; sair da consulta não apaga o pedido. |

### Checklist específico de modelagem

- [x] Abertura identifica perfil e protege acesso ao caso.
- [x] Cenas representam consultar origem, complementar e informar capacidade.
- [x] Falas distinguem profissional, preposto e dados do tutor.
- [x] Há encerramentos por saída e conclusão da consulta.
- [x] Processos de acesso, consulta e registro têm feedback.
- [x] Permissão, vazio, falha, conflito e cancelamento têm recuperação.
- [x] Sem atalho ubíquo a casos privados; vínculo autorizado é obrigatório.
- [x] Aceite, recusa e pedido de complemento são alternativas.
- [x] Terminologia da E9 e H03/H05 abertas foram preservadas.
- [x] Folhas vetoriais com fontes, legenda e explicação textual.
- [x] Capacidade é decisão humana; algoritmo não é modelado internamente.
- [x] Lista, histórico e comunicação incluem os estados pertinentes.

## M01 — Relatar os sinais de Bob e buscar atendimento

**Autor(a):** Julian Ryu Takeda — 22.224.030-1

**Cenário de interação de origem:** CI01; E4:C01; P01.

**Objetivo(s):** O01–O05 e O08–O10, conforme o dicionário da E9.

**Tarefa(s) relacionada(s):** T01 e T02; T03 na interpretação da orientação.

**Signos relevantes:** S02–S24 conforme a etapa; credenciais não bloqueiam a orientação inicial. R01–R05; RC01–RC11/RC13/RC14; H09/H12/H14/H16–H18.

### Diagrama

![MoLIC M01 — folha A: relato e análise](../assets/10_molic/molic_m01.svg)

*Figura M01-A — Relatar e revisar sinais. [Fonte editável](../assets/10_molic/molic_m01.dot).*

![MoLIC M01 — folha B: busca e contato](../assets/10_molic/molic_m01_busca.svg)

*Figura M01-B — Localizar e contatar clínica. [Fonte editável](../assets/10_molic/molic_m01_busca.dot).*

![MoLIC M01 — folha C: compartilhamento e acompanhamento](../assets/10_molic/molic_m01_envio.svg)

*Figura M01-C — Autorizar e acompanhar o caso. [Fonte editável](../assets/10_molic/molic_m01_envio.dot). Fonte das três figuras: elaboração para esta entrega sob a responsabilidade individual indicada.*

### Leitura do diagrama

#### Caminho principal

1. A abertura leva a M01.C01: Camila informa espécie, animal e sinais observados. Pode completar o cadastro depois; nova conversa não herda silenciosamente o animal anterior.
2. Por texto, segue à revisão em C03. Por voz, passa por C02/P01, confere a transcrição e corrige antes de enviar. Confirmar o relato não autoriza compartilhamento com a clínica.
3. P02 valida o mínimo e comunica recebimento/análise em C04. Se faltar informação útil, C06 recebe o complemento; a pergunta e seu efeito ficam explícitos. Sem avanço, a interação oferece pergunta objetiva, aceita “não sei” e mantém o contato disponível, conforme CI03/O02/O09.
4. C07 comunica orientação, motivos, limites e próximo passo. No caso fictício de Bob, segue à busca de atendimento; o contato fica acessível sem concluir perguntas secundárias. Na não emergência, C07 comunica observação e reavaliação; na insuficiência, C06 mantém a conversa inconclusiva.
5. Na folha B, define a região em C08, compara opções em C09 e confere contato/funcionamento em C11. Localização automática é opcional. Horário publicado não confirma capacidade; abrir uma ligação/rota não comprova atendimento.
6. Se a unidade for habilitada e quiser compartilhar, passa à folha C: em C13 revisa resumo, relato original, destinatário e autorização inicialmente desmarcada. Pode corrigir os dados dentro dessa cena; selecionar uma clínica não autoriza envio.
7. Após registro, acompanha C14. Estado, autor e horário distinguem enviado/aguardando, visualizado, aceito e recusado. A clínica registra a decisão humana em M02. Encerrar a consulta não cancela o pedido nem significa atendimento concluído.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Recuperação/saída |
|---|---|---|---|
| Áudio cancelado, microfone negado ou transcrição indisponível | C02/P01 | Gravação e indisponibilidade explícitas. | Texto em C01; preservar texto já digitado e revisar transcrição quando existir. |
| Animal incorreto ou relato vazio | C03/P02 | Animal visível e solicitação de dados mínimos. | Corrigir C01/C03, sem cadastro completo obrigatório. |
| Demora/falha de análise | C04/C05 | Analisando ou falha; erro não vira não emergência. | Consultar andamento, retentar com relato mantido ou buscar ajuda pelo acesso ubíquo. |
| Informação insuficiente/repetição | C06 | Lacuna explícita e “não sei” permitido. | Complementar; pergunta objetiva prevista em CI03; sem avanço, contato profissional. |
| Localização negada, região inválida, falha ou lista vazia | C08/P03/P04/C10 | Permissão, falha e ausência de opções diferenciadas. | Corrigir região, remover filtro/ampliar busca e retentar. |
| Unidade sem resposta/capacidade ou sem integração | C11/C12 | Não há confirmação; unidade sem integração não recebe resumo pela plataforma. | Outra unidade ou contato direto, sem envio obrigatório. |
| Falta autorização/destinatário ou envio não confirmado | C13/P05/C15 | Falta indicada, rascunho preservado, sem falso sucesso. | Corrigir; conferir o estado do mesmo pedido antes de retentar, evitando duplicação. |
| Pendência, recusa ou pergunta profissional | C14/C17 | Mensagem da unidade identificada, estado e horário. | Outra unidade; resposta observada ou “não sei”; falha mantém texto. |
| Cancelamento acidental | C16/P06 | Confirmação explica que conteúdo já compartilhado não será apagado. | Manter pedido ou confirmar cancelamento; só apresentar cancelado após registro. |

### Checklist específico de modelagem

- [x] Abertura coerente e cadastro completo não bloqueante.
- [x] Cenas representam tópicos, com diálogos/signos.
- [x] Transições distinguem falas do tutor e do preposto.
- [x] Encerramentos distinguem consulta, abandono e continuidade entre folhas.
- [x] Processos possuem saídas comunicadas pelo preposto.
- [x] Rupturas têm feedback e recuperação, sem erro convertido em resultado.
- [x] Contato ubíquo é justificado pela possível urgência.
- [x] Texto/voz, busca manual, contato direto e compartilhamento opcional são alternativas.
- [x] Nomes de objetivos/signos são coerentes com E9.
- [x] Folhas vetoriais legíveis, com fontes e leitura textual.
- [x] Conversa usuário–sistema, sem detalhamento do algoritmo.
- [x] Busca/filtros, processamento e histórico do pedido incluem retornos pertinentes.

## Consolidação da equipe

### Cobertura dos objetivos

| Objetivo da E9 | Modelagem presente | O que falta na E10 |
|---|---|---|
| O01 — Relatar e revisar sinais | M01 | M03 |
| O02 — Complementar informações insuficientes | M01 | M03 |
| O03 — Compreender orientação e próximo passo | M01 | M03 |
| O04 — Localizar e contatar uma clínica | M01 | M03 |
| O05 — Revisar e autorizar compartilhamento | M01 | Coberto nesta etapa |
| O06 — Consultar o caso e conferir sua origem | M02 | Coberto nesta etapa |
| O07 — Solicitar complemento e informar capacidade | M02 | Coberto nesta etapa |
| O08 — Identificar o animal do relato | M01 | M03 |
| O09 — Corrigir e recuperar a interação | M01, M02 | M03 |
| O10 — Acompanhar a resposta da clínica | M01, M02 | Coberto nesta etapa |

### Preparação para o Figma

Estados derivados apenas dos modelos presentes; E11 continua não iniciada.

| Conversas presentes | Estados e recuperações necessários |
|---|---|
| M02.C01–C05 | Acesso da unidade, permissão negada/sessão expirada, lista vazia/falha, caso com relato original, síntese, origem e horário. |
| M02.C06–C10 | Pedido de complemento, confirmação de capacidade/recusa, texto vazio, comunicação registrada, falha com rascunho, conflito e retorno ao caso. |
| M01.C01–C07 | Animal/relato, gravação/cancelamento/transcrição revisável, dados mínimos, análise/falha, complemento e orientação. |
| M01.C08–C12 | Região manual/localização, permissão recusada, mapa/lista/filtro, vazio/falha, contato e unidade sem integração. |
| M01.C13–C17 | Revisão/autorização, envio não confirmado, aguardando, aceite/recusa, complemento profissional e cancelamento com confirmação. |

### Decisões de integração

M01 e M02 compartilham o mesmo pedido: envio/visualização não representam aceite. Origem e horário acompanham as mensagens. A pergunta objetiva e a interpretação detalhada de CI03 serão incorporadas em M03, sem mudar objetivos ou signos da E9.

Retentativas consultam o registro da mesma operação antes de reenviar; não duplicam comunicações registradas. Modelagem não confirma implementação nem sustenta/refuta H03/H05. As colunas futuras da matriz permanecem pendentes.

### Checklist da consolidação

- [x] Contribuições presentes completas e identificadas por nome/matrícula.
- [x] E9 concluída e seus vínculos CI01–CI03 foram preservados.
- [x] Fontes editáveis, diagramas e rastreabilidade dos modelos presentes incluídos.
- [x] Estados para a E11 derivados somente das conversas disponíveis.
- [ ] Três soluções individuais reunidas.
- [ ] Cobertura O01–O10 e preparação para o Figma consolidadas com M01–M03.
- [ ] Entrega 10 concluída no README.

## Referências e histórico

- **CC8122 — MoLIC, Partes A, B e C**, material fornecido, baseado em Barbosa e Silva (2010). Notação: A, pp. 3–15; abertura/fechamento de metas: B, pp. 3–5; passagem para interface: C, pp. 14–18.
- BARBOSA, Simone D. J.; SILVA, Bruno S. **Interação Humano-Computador**. Elsevier/Campus, 2010. Referência indicada nos slides e na [bibliografia do projeto](../BIBLIOGRAFIA.md).
- E1–E9 e [matriz](../RASTREABILIDADE.md), na revisão indicada. Templates E11–E14/instrumentos orientam a continuidade, sem avaliações fictícias preenchidas.

**Histórico cumulativo — 04/11/2026:**

- Etapa 1: Vinícius adiciona M02-A/B, leitura, rupturas, fontes e vínculos de R05.
- Etapa 2: Julian acrescenta M01-A/B/C e vínculos R01–R05, preservando M02.

Base: `ef16972f7582b482494a0827304caa1c57244e82`. Referências à E6 ajustadas ao percurso de emergência, mapa e envio; INCERTO e painel continuam como modelagem de E5/E9. E7/E9 já concluídas foram preservadas; não há alteração nos seus arquivos. Este conjunto prepara commits; não representa envio remoto nem validação com o professor.
