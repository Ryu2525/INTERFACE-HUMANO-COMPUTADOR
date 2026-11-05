# Diagramas MoLIC — etapa 1/3

Modelos presentes: M02. [Leitura, legenda e rastreabilidade](../../docs/10_molic.md).

| Modelo/folha | Responsável | Diagrama | Fonte editável |
|---|---|---|---|
| M02 · folha A — Consultar caso autorizado | Vinícius de Castro Duarte — 22.224.020-2 | [SVG](molic_m02.svg) | [DOT](molic_m02.dot) |
| M02 · folha B — Comunicar decisão humana | Vinícius de Castro Duarte — 22.224.020-2 | [SVG](molic_m02_resposta.svg) | [DOT](molic_m02_resposta.dot) |

As notas entre folhas são referências editoriais, não cenas. SVGs mantêm textos/objetos vetoriais; DOT é a fonte Graphviz. Para regenerar uma folha:

```bash
dot -Tsvg ARQUIVO.dot -o ARQUIVO.svg
```

[modelos.json](modelos.json) usa esquema próprio para nós, diálogos e transições; não é formato de importação de editor externo. Atualize DOT, SVG e JSON juntos. Arestas invisíveis do DOT organizam apenas o desenho. Fonte conceitual: slides CC8122 — MoLIC A/B/C, baseados em Barbosa e Silva (2010).
