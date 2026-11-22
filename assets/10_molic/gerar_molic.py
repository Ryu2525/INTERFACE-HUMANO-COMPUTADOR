"""Gera os DOT da MoLIC (E10) e o modelos.json a partir de uma especificação única.
Uso, dentro de assets/10_molic: python3 gerar_molic.py .
Depois: for f in *.dot; do dot -Tsvg "$f" -o "${f%.dot}.svg"; done
"""
import json, sys, textwrap, os

OUT = sys.argv[1]
G3 = "O03 · entender o que fazer agora"
G4 = "O04 · chegar a um atendimento"
G7 = "O07 · decidir se a unidade recebe o animal"

def esc(t):
    return (t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")
             .replace("|", "\\|").replace("<", "\\<").replace(">", "\\>").replace('"', '\\"'))

def wrap(t, w=46, indent="   "):
    lines = textwrap.wrap(t, w, subsequent_indent=indent, break_long_words=False)
    return "\\l".join(esc(x) for x in lines) + "\\l"

def elabel(t, w=30):
    out = []
    for part in t.split("\n"):
        out += textwrap.wrap(part, w, break_long_words=False) or [""]
    return "\\n".join(x.replace('"', '\\"') for x in out)

# cada folha: nodes (id, kind, title, dialog[], signs[]) e edges (src, dst, fala, recuperacao)
S = []

# ---------------- M01 · folha A ----------------
S.append(dict(
 name="molic_m01", title="M01 · folha A — Relatar e revisar sinais", author="Julian Ryu Takeda — 22.224.030-1",
 goal=f"Abre o objetivo final {G3}",
 nodes=[
  ("inicio","opening"),
  ("C01","scene","M01.C01 · Relatar sinais (O01/O08)",
   ["d: Qual animal e o que você observou? Pode associar o animal depois."],
   ["u: animal (S02)","u: relato (S03)","u: início dos sinais (S04)","d: histórico do animal (S26)","u: d: provedor da análise (S31)"]),
  ("C02","scene","M01.C02 · Gravar relato",
   ["d: Gravação em andamento; pode cancelar e digitar."],
   ["u: relato por voz (S03)"]),
  ("P01","process"),
  ("C03","scene","M01.C03 · Conferir o que será enviado (O01)",
   ["d: Ainda não enviei; corrija e envie quando estiver certo."],
   ["u: d: relato (S03)","u: d: transcrição (S05)","u: d: animal (S02)","d: provedor da análise (S31): para onde o relato vai"]),
  ("P02","process"),
  ("C04","scene","M01.C04 · Acompanhar análise",
   ["d: Recebi seu relato e estou analisando; ele está guardado."],
   ["d: estado da análise (S08): em análise","d: relato (S03)"]),
  ("C05","alert","M01.C05 · Recuperar o relato (O09)",
   ["d: Não consegui concluir a análise. Isso não quer dizer que o caso não é grave."],
   ["d: estado da análise (S08): falha","u: d: relato (S03) mantido","d: próximo passo (S12): procurar atendimento"]),
  ("C06","scene","M01.C06 · Esclarecer lacuna (O02)",
   ["d: Falta esta observação; isso não é não emergência."],
   ["d: orientação (S09): informação insuficiente","d: pergunta complementar (S06)","u: resposta complementar (S07), inclusive não sei"]),
  ("C07","scene","M01.C07 · Compreender orientação (O03)",
   ["d: Pesaram estes sinais. Isto não é um diagnóstico."],
   ["d: orientação (S09)","d: sinais considerados (S30)","d: justificativa (S10)","d: limites (S11)","d: próximo passo (S12)","d: origem da informação (S21): automática","d: horário do registro (S24)"]),
  ("U","ubiquitous","Acesso ubíquo: buscar ajuda",
   ["Disponível em C01–C07: link fixo e item de menu.","Não depende de concluir cadastro ou análise."],[]),
  ("B","reference","Ir a M01 · folha B\nAbre o objetivo final O04 · chegar a um atendimento"),
  ("fim","closing"),
 ],
 invis=[("C06","C07")],
 ranks=[["C04","C05","C06"]],
 edges=[
  ("inicio","C01",f"u: iniciar pré-triagem\n[gco: {G3}]",False),
  ("C01","C03","u: digitei; quero revisar",False),
  ("C01","C02","u: prefiro gravar",False),
  ("C02","P01","u: terminar gravação",False),
  ("C02","C01","u: cancelar áudio e digitar",True),
  ("P01","C03","d: transcrição pronta; confira",False),
  ("P01","C01","d: áudio indisponível; use texto",True),
  ("C03","C01","u: corrigir relato ou animal",True),
  ("C03","P02","u: confirmei; enviar para análise",False),
  ("P02","C03","d: informe espécie e relato não vazio",True),
  ("P02","C04","d: dados recebidos; analisando",False),
  ("C04","P02","u: consultar andamento",False),
  ("P02","C05","d: falha na análise",True),
  ("C05","P02","u: tentar novamente",True),
  ("C05","C03","u: editar antes de retentar",True),
  ("P02","C06","d: informações insuficientes",False),
  ("C06","P02","u: enviar o que observei ou não sei",False),
  ("P02","C07","d: orientação disponível",False),
  ("C07","B","u: encontrar atendimento",False),
  ("C07","C03","u: os sinais mudaram; atualizar",True),
  ("C07","fim",f"u: encerrar leitura\n[gcc: {G3}]",False),
  ("U","B","u: buscar contato profissional",False),
 ]))

# ---------------- M01 · folha B ----------------
S.append(dict(
 name="molic_m01_busca", title="M01 · folha B — Localizar e contatar clínica", author="Julian Ryu Takeda — 22.224.030-1",
 goal=f"Abre o objetivo final {G4} (entrada a partir de M01-A, M03-A, M03-B ou do acesso ubíquo)",
 nodes=[
  ("REF","reference","Vem de M01-A (C07, acesso ubíquo),\nM03-A (C06) ou M03-B (C09, C10)"),
  ("inicio","opening"),
  ("C08","scene","M01.C08 · Definir região",
   ["d: Posso usar sua localização ou você diz onde está."],
   ["u: região (S13): endereço ou localização"]),
  ("P03","process"),
  ("P04","process"),
  ("C09","scene","M01.C09 · Comparar opções",
   ["d: Horário publicado não confirma vaga; ligue para confirmar."],
   ["u: d: região (S13)","d: clínica (S14)","d: horário informado (S15): aberta, fechada ou não informado","u: filtro por horário informado (S15)","d: contato (S16)"]),
  ("C10","alert","M01.C10 · Rever busca",
   ["d: Não encontrei unidade aberta perto desse ponto, ou a busca falhou."],
   ["u: d: região (S13)","d: horário informado (S15)"]),
  ("C11","scene","M01.C11 · Contatar a unidade",
   ["d: Nenhuma unidade tem atendimento confirmado até que ela confirme."],
   ["d: clínica (S14)","d: horário informado (S15)","d: contato (S16)"]),
  ("C12","alert","M01.C12 · Prosseguir sem integração",
   ["d: Esta unidade não recebe o resumo pela plataforma; use o contato direto."],
   ["d: clínica (S14): sem integração","d: contato (S16)"]),
  ("C","reference","Continua em M01 · folha C\nMesmo objetivo O04: revisar, autorizar e acompanhar"),
  ("fim","closing"),
 ],
 invis=[("C09","C11"),("C11","C12")],
 edges=[
  ("REF","inicio","",False),
  ("inicio","C08",f"u: encontrar atendimento\n[gco: {G4}]",False),
  ("C08","P03","u: usar minha localização",False),
  ("P03","C08","d: permissão negada ou falha; informe a região",True),
  ("P03","P04","d: região obtida; buscando",False),
  ("C08","P04","u: buscar pela região digitada",False),
  ("P04","C09","d: opções encontradas",False),
  ("P04","C10","d: nenhuma opção ou erro",True),
  ("C10","C08","u: ajustar região e retentar",True),
  ("C09","P04","u: aplicar ou remover filtro",False),
  ("C09","C11","u: contatar esta clínica",False),
  ("C11","C09","u: sem resposta; outra opção",True),
  ("C11","C","u: compartilhar o caso\n[unidade habilitada]",False),
  ("C11","C12","u: preparar contato\n[unidade sem integração]",False),
  ("C12","C09","u: procurar outra unidade",True),
  ("C11","fim",f"u: seguir pelo contato direto\n[gcc: {G4}]",False),
  ("C08","fim",f"u: desistir da busca\n[gcc: {G4}]\n(sem unidade escolhida)",False),
 ]))

# ---------------- M01 · folha C ----------------
S.append(dict(
 name="molic_m01_envio", title="M01 · folha C — Autorizar e acompanhar o caso", author="Julian Ryu Takeda — 22.224.030-1",
 goal=f"Continua o objetivo final {G4} (sem nova abertura)",
 nodes=[
  ("REF","reference","Continua de M01 · folha B (C11)\nMesmo objetivo O04; sem nova abertura"),
  ("C13","scene","M01.C13 · Revisar compartilhamento (O05)",
   ["d: Confira o que será enviado. O envio não confirma vaga."],
   ["u: d: resumo (S17)","d: relato original (S03)","d: orientação automática (S09) e origem (S21)","d: animal (S02)","d: destinatário (S18)","u: autorização do resumo (S19), desmarcada","u: autorização da conversa completa (S19), separada e opcional"]),
  ("P05","process"),
  ("P06","process"),
  ("P07","process"),
  ("C14","scene","M01.C14 · Acompanhar resposta (O10)",
   ["d: Enviado não é aceito; enquanto não houver aceite, o atendimento não está garantido."],
   ["d: caso/encaminhamento (S25)","u: d: estado do encaminhamento (S20)","d: resposta da clínica (S23)","d: origem da informação (S21)","d: horário do registro (S24)"]),
  ("C15","alert","M01.C15 · Recuperar envio (O09)",
   ["d: Envio não confirmado; o conteúdo foi mantido."],
   ["d: estado do encaminhamento (S20): falha","u: d: resumo (S17) mantido"]),
  ("C16","alert","M01.C16 · Confirmar cancelamento",
   ["d: Cancelar não apaga o que a unidade já viu."],
   ["d: caso/encaminhamento (S25)","d: estado do encaminhamento (S20)"]),
  ("C17","scene","M01.C17 · Conversar com a clínica",
   ["d: Mensagem da equipe da unidade, com autoria e horário; a pré-triagem não responde aqui."],
   ["d: canal com a clínica (S27)","d: mensagem profissional (S22)","u: mensagem do tutor (S27)","d: origem da informação (S21)","d: horário do registro (S24)"]),
  ("U","ubiquitous","Acesso ubíquo: ver outras clínicas",
   ["Disponível em C13–C17.","Leva à busca sem cancelar o pedido."],[]),
  ("B","reference","Voltar a M01 · folha B\nOutra unidade ou contato direto"),
  ("fim","closing"),
 ],
 invis=[],
 ranks=[["C17","P06"]],
 edges=[
  ("REF","C13","u: compartilhar com unidade habilitada",False),
  ("C13","P05","u: revisei e autorizo enviar",False),
  ("P05","C13","d: falta autorização ou destino; nada enviado",True),
  ("P05","C15","d: envio não confirmado",True),
  ("C15","P05","u: verificar situação e retentar",True),
  ("P05","C14","d: caso enviado; aguardando resposta",False),
  ("C14","P06","u: consultar atualização\nou avisar que estou a caminho",False),
  ("P06","C14","d: visualizado, aceito, recusado, a caminho ou cancelado, com horário",False),
  ("P06","C14","d: consulta falhou; último estado mantido",True),
  ("C14","C17","u: abrir a conversa com a clínica",False),
  ("C17","P07","u: enviar mensagem",False),
  ("P07","C17","d: falha; texto mantido",True),
  ("P07","C14","d: mensagem registrada",False),
  ("C14","B","u: procurar outra unidade",True),
  ("C13","B","u: não autorizar; contato direto",True),
  ("C14","C16","u: quero cancelar o envio",False),
  ("C16","C14","u: manter pedido",True),
  ("C16","P06","u: confirmar cancelamento",False),
  ("U","B","u: ver outras clínicas",False),
  ("C14","fim",f"u: encerrar consulta\n[gcc: {G4}]",False),
 ]))

# ---------------- M02 · folha A ----------------
S.append(dict(
 name="molic_m02", title="M02 · folha A — Consultar caso autorizado", author="Vinícius de Castro Duarte — 22.224.020-2",
 goal=f"Abre o objetivo final {G7}",
 nodes=[
  ("inicio","opening"),
  ("C01","scene","M02.C01 · Identificar acesso da clínica",
   ["d: Você verá só os casos autorizados à sua unidade."],
   ["u: usuário (S01)","u: senha (S28)","d: papel (S29): profissional da clínica"]),
  ("P01","process"),
  ("P02","process"),
  ("P03","process"),
  ("C02","scene","M02.C02 · Escolher encaminhamento (O06)",
   ["d: Casos compartilhados com sua unidade, do mais recente ao mais antigo."],
   ["d: caso/encaminhamento (S25)","d: animal (S02)","d: estado do encaminhamento (S20)","d: horário do registro (S24)"]),
  ("C03","scene","M02.C03 · Conferir origem do caso (O06)",
   ["d: Este trecho foi informado pelo tutor; esta orientação é automática. Sem dado não significa sinal ausente."],
   ["d: resumo (S17)","d: relato original (S03)","d: início dos sinais (S04)","d: orientação (S09)","d: sinais considerados (S30)","d: justificativa (S10)","d: origem da informação (S21)","d: horário do registro (S24)"]),
  ("C04","alert","M02.C04 · Recuperar consulta",
   ["d: Nenhum caso novo foi compartilhado com sua unidade, ou a consulta falhou."],
   ["d: caso/encaminhamento (S25)","d: destinatário (S18)","d: autorização (S19)"]),
  ("C05","alert","M02.C05 · Rever permissão",
   ["d: Sessão inválida ou acesso não permitido; nenhum conteúdo privado foi exibido."],
   ["u: usuário (S01)","d: papel (S29)"]),
  ("U","ubiquitous","Acesso ubíquo: sair da área da clínica",
   ["Disponível em C02–C04 e na folha B.","Sem atalho para casos privados."],[]),
  ("B","reference","Continua em M02 · folha B\nMesmo objetivo O07: pedir complemento e decidir"),
  ("fim","closing"),
 ],
 invis=[("inicio","C01"),("C01","P01"),("P01","C02"),("C02","P03"),("P03","C03"),("C03","B")],
 edges=[
  ("inicio","C01",f"u: abrir área da clínica\n[gco: {G7}]",False),
  ("C01","P01","u: entrar com vínculo da unidade",False),
  ("P01","C02","d: acesso autorizado",False),
  ("P01","C05","d: acesso inválido ou sem permissão",True),
  ("C05","C01","u: corrigir acesso",True),
  ("C02","P02","u: atualizar encaminhamentos",False),
  ("P02","C02","d: lista atualizada",False),
  ("P02","C04","d: lista vazia ou erro identificado",True),
  ("C04","P02","u: tentar atualizar",True),
  ("C02","P03","u: abrir este caso",False),
  ("P03","C03","d: caso autorizado e versão disponível",False),
  ("P03","C05","d: sessão expirada ou caso não autorizado",True),
  ("C05","C02","u: voltar à lista permitida",True),
  ("C03","P03","u: conferir atualização do relato",False),
  ("P03","C04","d: falha de consulta",True),
  ("C03","B","u: pedir complemento ou decidir",False),
  ("C03","C02","u: voltar aos encaminhamentos",False),
  ("C05","fim",f"u: sair\n[gcc: {G7}]\n(sem acesso)",False),
  ("U","fim",f"u: sair\n[gcc: {G7}]\n(sem decisão)",False),
 ]))

# ---------------- M02 · folha B ----------------
S.append(dict(
 name="molic_m02_resposta", title="M02 · folha B — Pedir complemento e comunicar a decisão", author="Vinícius de Castro Duarte — 22.224.020-2",
 goal=f"Continua o objetivo final {G7} (sem nova abertura)",
 nodes=[
  ("REF","reference","Continua de M02 · folha A (C03)\nMesmo objetivo O07; sem nova abertura"),
  ("C06","scene","M02.C06 · Pedir complemento ao tutor (O11)",
   ["d: A pergunta vai ao tutor; a resposta aparecerá como atualização, sem apagar o relato original."],
   ["u: mensagem profissional (S22)","d: início dos sinais (S04) e outras lacunas","d: origem da informação (S21)","d: canal com a clínica (S27)"]),
  ("C07","scene","M02.C07 · Confirmar capacidade (O07)",
   ["d: Confirma que sua unidade pode receber o animal? O tutor será avisado. Recebimento do caso não é aceite."],
   ["u: resposta da clínica (S23): pode ou não pode receber","u: mensagem profissional (S22), opcional","d: estado do encaminhamento (S20)"]),
  ("P04","process"),
  ("P05","process"),
  ("C08","scene","M02.C08 · Consultar comunicação registrada",
   ["d: Resposta registrada e identificada como da sua unidade; isso não comprova leitura pelo tutor."],
   ["d: resposta da clínica (S23)","d: estado do encaminhamento (S20)","d: canal com a clínica (S27)","d: origem da informação (S21)","d: horário do registro (S24)"]),
  ("C09","alert","M02.C09 · Recuperar mensagem (O09)",
   ["d: Não foi possível enviar sua mensagem agora; o texto foi mantido."],
   ["u: d: mensagem profissional (S22)","d: canal com a clínica (S27)"]),
  ("C10","alert","M02.C10 · Conferir alteração do caso",
   ["d: O caso mudou desde que você abriu; nada foi sobrescrito."],
   ["d: caso/encaminhamento (S25)","d: origem da informação (S21)","d: horário do registro (S24)"]),
  ("U","ubiquitous","Acesso ubíquo: sair da área da clínica",
   ["Disponível em C06–C10."],[]),
  ("A","reference","Voltar a M02 · folha A\nConferir relato e novas informações"),
  ("fim","closing"),
 ],
 invis=[("C06","C07"),("C07","C08")],
 edges=[
  ("REF","C06","u: perguntar ao tutor",False),
  ("REF","C07","u: informar capacidade",False),
  ("C06","P04","u: enviar pergunta",False),
  ("C07","P04","u: confirmar decisão",False),
  ("C07","C06","u: perguntar antes de decidir",True),
  ("P04","C06","d: mensagem vazia; escreva a pergunta",True),
  ("P04","C09","d: envio não confirmado",True),
  ("C09","P04","u: conferir situação e tentar de novo",True),
  ("P04","C10","d: estado ou versão do caso mudou",True),
  ("C10","A","u: consultar atualização e revisar",True),
  ("P04","C08","d: comunicação registrada",False),
  ("C08","P05","u: consultar retorno do tutor",False),
  ("P05","C08","d: sem resposta nova; último horário",False),
  ("P05","A","d: novo complemento disponível",False),
  ("P05","C08","d: consulta falhou; último estado mantido",True),
  ("C08","C07","u: atualizar a decisão explicitamente",False),
  ("C06","A","u: cancelar e voltar ao caso",True),
  ("U","fim",f"u: sair\n[gcc: {G7}]\n(sem decisão)",False),
  ("C08","fim",f"u: concluir\n[gcc: {G7}]",False),
 ]))

# ---------------- M03 · folha A ----------------
S.append(dict(
 name="molic_m03", title="M03 · folha A — Resolver informação insuficiente", author="João Pedro Gardenghi Peterutto — 22.125.066-5",
 goal=f"Abre o objetivo final {G3}",
 nodes=[
  ("inicio","opening"),
  ("C01","scene","M03.C01 · Conferir contexto e lacuna (O01/O02)",
   ["d: Ainda faltam informações para dizer se é uma emergência. Isso não significa que esteja tudo bem."],
   ["d: animal (S02)","d: relato (S03)","d: início dos sinais (S04)","d: histórico do animal (S26)","d: estado da análise (S08)","d: orientação (S09): informação insuficiente","d: pergunta complementar (S06)","u: resposta complementar (S07)"]),
  ("C02","scene","M03.C02 · Esclarecer sem adivinhar (O02)",
   ["d: Expliquei o que falta e por que pergunto. Não sei não conta como não."],
   ["d: pergunta complementar (S06)","u: resposta complementar (S07): observado, não ou não sei"]),
  ("C03","scene","M03.C03 · Responder pergunta objetiva (O02)",
   ["d: Vou sugerir respostas possíveis; escolha a mais próxima ou responda do seu jeito."],
   ["d: pergunta complementar (S06) com respostas sugeridas, incluindo não sei","u: d: resposta complementar (S07)"]),
  ("P01","process"),
  ("C04","scene","M03.C04 · Acompanhar complemento",
   ["d: Recebi sua resposta e estou considerando de novo; o relato e as respostas anteriores estão guardados."],
   ["d: estado da análise (S08): em análise","d: resposta complementar (S07) incorporada"]),
  ("C05","alert","M03.C05 · Recuperar complemento (O09)",
   ["d: Falha; não há nova orientação confirmada."],
   ["d: estado da análise (S08): falha","u: d: resposta complementar (S07) mantida"]),
  ("C06","alert","M03.C06 · Reconhecer limite da conversa",
   ["d: Ainda não é possível concluir. Procure um veterinário, principalmente se piorar; você pode voltar e contar algo novo."],
   ["d: orientação (S09): informação insuficiente","d: limites (S11)","d: próximo passo (S12)"]),
  ("U","ubiquitous","Acesso ubíquo: buscar ajuda",
   ["Disponível em C01–C06 e na folha B.","Interrompe a coleta sem inferir não emergência."],[]),
  ("B","reference","Continua em M03 · folha B\nMesmo objetivo O03: compreender e agir"),
  ("H","reference","Ir a M01 · folha B\nAbre o objetivo final O04 · chegar a um atendimento"),
  ("fim","closing"),
 ],
 invis=[("C04","C06")],
 ranks=[["C05","C04","C03"]],
 edges=[
  ("inicio","C01",f"u: consultar pedido de complemento\n[gco: {G3}]",False),
  ("C01","C02","u: não entendi o que devo observar",False),
  ("C02","C01","u: voltar à pergunta",True),
  ("C01","P01","u: enviar o que observei ou não sei",False),
  ("P01","C04","d: resposta recebida; analisando",False),
  ("C04","P01","u: consultar andamento",False),
  ("P01","C03","d: sem avanço; pergunta objetiva",False),
  ("C03","P01","u: enviar resposta revisada",False),
  ("P01","C01","d: considerei sua resposta; ainda falta isto",False),
  ("P01","C05","d: falha de processamento",True),
  ("C05","P01","u: tentar novamente",True),
  ("P01","C06","d: insuficiência persiste sem avanço",False),
  ("P01","B","d: orientação disponível; veja o que mudou",False),
  ("C06","C01","u: tenho nova observação",False),
  ("C06","H","u: procurar profissional",False),
  ("U","H","u: buscar ajuda agora",False),
  ("C06","fim",f"u: parar a conversa\n[gcc: {G3}]\n(sem conclusão)",False),
 ]))

# ---------------- M03 · folha B ----------------
S.append(dict(
 name="molic_m03_orientacao", title="M03 · folha B — Compreender e agir", author="João Pedro Gardenghi Peterutto — 22.125.066-5",
 goal=f"Continua o objetivo final {G3} (sem nova abertura)",
 nodes=[
  ("REF","reference","Continua de M03 · folha A (P01)\nMesmo objetivo O03; sem nova abertura"),
  ("C07","scene","M03.C07 · Interpretar orientação (O03)",
   ["d: Veja a orientação, os sinais considerados, seus limites e o próximo passo."],
   ["d: orientação (S09)","d: sinais considerados (S30)","d: limites (S11)","d: origem da informação (S21): automática","d: animal (S02)","d: horário do registro (S24)"]),
  ("C08","scene","M03.C08 · Esclarecer motivos e limites",
   ["d: Justificativa em linguagem simples. Conteúdo automático não é diagnóstico."],
   ["d: justificativa (S10)","d: relato (S03)","d: sinais considerados (S30)","d: limites (S11)"]),
  ("P02","process"),
  ("C09","scene","M03.C09 · Planejar observação e reavaliação",
   ["d: Não identifiquei sinal de emergência. Isto não é um diagnóstico: continue acompanhando."],
   ["d: próximo passo (S12): acompanhar e reavaliar","d: limites (S11): sinais que mudam a orientação","d: horário do registro (S24)"]),
  ("C10","alert","M03.C10 · Priorizar atendimento",
   ["d: Possível emergência: procure atendimento agora; não espere cadastro nem perguntas."],
   ["d: orientação (S09): possível emergência","d: próximo passo (S12): procurar atendimento","d: limites (S11)"]),
  ("A","reference","Voltar a M03 · folha A\nNova observação; corrigir animal ou relato"),
  ("H","reference","Ir a M01 · folha B\nAbre o objetivo final O04 · chegar a um atendimento"),
  ("fim","closing"),
 ],
 invis=[("C07","P02")],
 edges=[
  ("REF","C07","d: orientação disponível",False),
  ("C07","C08","u: quero entender os motivos",False),
  ("C08","C07","u: voltar à orientação",False),
  ("C07","P02","u: o que faço agora?",False),
  ("P02","C09","d: não emergência: acompanhe e reavalie",False),
  ("P02","C10","d: possível emergência: procure atendimento agora",False),
  ("C10","H","u: encontrar atendimento agora",False),
  ("C09","H","u: tenho dúvida; contatar profissional",False),
  ("C07","A","u: animal ou relato incorreto",True),
  ("C09","A","u: observei mudança; atualizar relato",True),
  ("C09","fim",f"u: encerrar consulta\n[gcc: {G3}]",False),
  ("C10","fim",f"u: seguir por contato já conhecido\n[gcc: {G3}]",False),
 ]))

def node_dot(n):
    nid, kind = n[0], n[1]
    if kind == "opening":
        return f'{nid} [shape="circle", style="filled", fillcolor="black", width="0.22", height="0.22", fixedsize="true", label=""];'
    if kind == "closing":
        return f'{nid} [shape="doublecircle", style="filled", fillcolor="black", width="0.20", height="0.20", fixedsize="true", label=""];'
    if kind == "process":
        return f'{nid} [shape="square", style="filled", fillcolor="black", width="0.24", height="0.24", fixedsize="true", label="", xlabel="{nid}"];'
    if kind == "reference":
        return f'{nid} [shape="note", style="filled", fillcolor="#f1f5f9", fontsize=13, label="{n[2].replace(chr(10), chr(92)+"n")}"];'
    title, dialog, signs = n[2], n[3], n[4]
    if kind == "ubiquitous":
        body = "".join(wrap(x) for x in dialog)
        return (f'{nid} [shape="box", style="rounded,filled", fillcolor="#d9d9d9", fontsize=13, margin="0.3,0.12", '
                f'label="{esc(title)}\\n{body}"];')
    d = "".join(wrap(x) for x in dialog)
    sg = "".join(wrap(x, 46, "      ") for x in signs)
    style = "dashed" if kind == "alert" else "solid"
    return f'{nid} [shape="Mrecord", style="{style}", label="{{{esc(title)}|{d}|signos:\\l{sg}}}"];'

def edge_dot(e):
    s, t, fala, rec = e
    attrs = []
    if fala:
        attrs.append(f'label="{elabel(fala)}"')
    if rec:
        attrs.append('style="dashed"')
    return f'{s} -> {t} [{", ".join(attrs)}];' if attrs else f"{s} -> {t};"

graphs = []
for sh in S:
    lines = [
        "digraph molic {",
        f'graph [rankdir=TB, bgcolor="white", pad="0.3", nodesep="0.6", ranksep="0.65", splines=true, '
        f'fontname="Arial", fontsize=18, labelloc=t, label="{sh["title"]}\\n{sh["author"]}\\n{sh["goal"]}\\n'
        f'Cenas = tópicos · u: usuário informa · d: sistema apresenta · u: d: informado e exibido · tracejado = alerta ou recuperação"];',
        'node [fontname="Arial", fontsize=13, color="#343434", penwidth=1.4, margin="0.14,0.08"];',
        'edge [fontname="Arial", fontsize=11, color="#454545", arrowsize=0.7];',
    ]
    for n in sh["nodes"]:
        lines.append(node_dot(n))
    for r in sh.get("ranks", []):
        lines.append("{rank=same; " + "; ".join(r) + ";}")
    for a, b in sh.get("invis", []):
        lines.append(f"{a} -> {b} [style=invis, weight=40];")
    for e in sh["edges"]:
        lines.append(edge_dot(e))
    lines.append("}")
    open(os.path.join(OUT, sh["name"] + ".dot"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    nodes = []
    for n in sh["nodes"]:
        kind = n[1]
        item = {"id": n[0], "kind": kind}
        if kind in ("scene", "alert", "ubiquitous"):
            item.update(title=n[2], dialog=n[3], signs=n[4])
        elif kind == "reference":
            item["title"] = n[2]
        nodes.append(item)
    graphs.append({"name": sh["name"], "title": sh["title"], "author": sh["author"], "goal": sh["goal"],
                   "nodes": nodes,
                   "edges": [{"source": s, "target": t, "speech": f.replace("\n", " "), "recovery": r} for s, t, f, r in sh["edges"]]})

json.dump({"schema": "molic-conversas-v2",
           "description": "Dados próprios desta entrega; não é formato de importação de editor externo. DOT é a fonte para renderização. Signos marcados com u: (informado pelo usuário), d: (apresentado pelo sistema) ou u: d: (ambos).",
           "graphs": graphs},
          open(os.path.join(OUT, "modelos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("ok", len(graphs))
