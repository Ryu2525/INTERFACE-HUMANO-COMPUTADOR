# Diagramas MoLIC — etapa 3/3

Modelos presentes: M02, M01, M03. [Leitura, legenda e rastreabilidade](../../docs/10_molic.md).

| Modelo/folha | Responsável | Diagrama | Fonte editável |
|---|---|---|---|
| M01 · folha A — Relatar e revisar sinais | Julian Ryu Takeda — 22.224.030-1 | [SVG](molic_m01.svg) | [DOT](molic_m01.dot) |
| M01 · folha B — Localizar e contatar clínica | Julian Ryu Takeda — 22.224.030-1 | [SVG](molic_m01_busca.svg) | [DOT](molic_m01_busca.dot) |
| M01 · folha C — Autorizar e acompanhar o caso | Julian Ryu Takeda — 22.224.030-1 | [SVG](molic_m01_envio.svg) | [DOT](molic_m01_envio.dot) |
| M02 · folha A — Consultar caso autorizado | Vinícius de Castro Duarte — 22.224.020-2 | [SVG](molic_m02.svg) | [DOT](molic_m02.dot) |
| M02 · folha B — Comunicar decisão humana | Vinícius de Castro Duarte — 22.224.020-2 | [SVG](molic_m02_resposta.svg) | [DOT](molic_m02_resposta.dot) |
| M03 · folha A — Resolver informação insuficiente | João Pedro Gardenghi Peterutto — 22.125.066-5 | [SVG](molic_m03.svg) | [DOT](molic_m03.dot) |
| M03 · folha B — Compreender e agir | João Pedro Gardenghi Peterutto — 22.125.066-5 | [SVG](molic_m03_orientacao.svg) | [DOT](molic_m03_orientacao.dot) |

As notas entre folhas são referências editoriais, não cenas. SVGs mantêm textos/objetos vetoriais; DOT é a fonte Graphviz. Para regenerar uma folha:

```bash
dot -Tsvg ARQUIVO.dot -o ARQUIVO.svg
```

[modelos.json](modelos.json) usa esquema próprio para nós, diálogos e transições; não é formato de importação de editor externo. Atualize DOT, SVG e JSON juntos. Arestas invisíveis do DOT organizam apenas o desenho. Fonte conceitual: slides CC8122 — MoLIC A/B/C, baseados em Barbosa e Silva (2010).
