# Diagramas MoLIC — Entrega 10

Modelos: M01 (Julian), M02 (Vinícius) e M03 (João). [Leitura, legenda e rastreabilidade](../../docs/10_molic.md).

| Modelo/folha | Objetivo final | Responsável | Diagrama | Fonte editável |
|---|---|---|---|---|
| M01 · folha A — Relatar e revisar sinais | O03 (abre e fecha) | Julian Ryu Takeda — 22.224.030-1 | [SVG](molic_m01.svg) | [DOT](molic_m01.dot) |
| M01 · folha B — Localizar e contatar clínica | O04 (abre e fecha) | Julian Ryu Takeda — 22.224.030-1 | [SVG](molic_m01_busca.svg) | [DOT](molic_m01_busca.dot) |
| M01 · folha C — Autorizar e acompanhar o caso | O04 (continua e fecha) | Julian Ryu Takeda — 22.224.030-1 | [SVG](molic_m01_envio.svg) | [DOT](molic_m01_envio.dot) |
| M02 · folha A — Consultar caso autorizado | O07 (abre e fecha) | Vinícius de Castro Duarte — 22.224.020-2 | [SVG](molic_m02.svg) | [DOT](molic_m02.dot) |
| M02 · folha B — Pedir complemento e comunicar a decisão | O07 (continua e fecha) | Vinícius de Castro Duarte — 22.224.020-2 | [SVG](molic_m02_resposta.svg) | [DOT](molic_m02_resposta.dot) |
| M03 · folha A — Resolver informação insuficiente | O03 (abre e fecha) | João Pedro Gardenghi Peterutto — 22.125.066-5 | [SVG](molic_m03.svg) | [DOT](molic_m03.dot) |
| M03 · folha B — Compreender e agir | O03 (continua e fecha) | João Pedro Gardenghi Peterutto — 22.125.066-5 | [SVG](molic_m03_orientacao.svg) | [DOT](molic_m03_orientacao.dot) |

As notas entre folhas são referências editoriais, não cenas. Os SVGs mantêm textos vetoriais; o DOT é a fonte Graphviz.

**Como regenerar.** Os DOT e o [modelos.json](modelos.json) são gerados por [`gerar_molic.py`](gerar_molic.py), que guarda cenas, signos e transições num só lugar. Para alterar um diagrama, edite a especificação no script e rode, dentro desta pasta:

```bash
python3 gerar_molic.py .
for f in *.dot; do dot -Tsvg "$f" -o "${f%.dot}.svg"; done
```

[modelos.json](modelos.json) usa esquema próprio (`molic-conversas-v2`) para nós, signos e transições; não é formato de importação de editor externo. Arestas invisíveis e `rank=same` no DOT organizam apenas o desenho. Fonte conceitual: slides CC8122 — MoLIC A/B/C, baseados em Barbosa e Silva (2010).
