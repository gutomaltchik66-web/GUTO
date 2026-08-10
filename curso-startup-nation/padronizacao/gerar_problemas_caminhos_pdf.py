# -*- coding: utf-8 -*-
"""
Problemas e Caminhos (Aula 2) — material simples, sem o cabeçalho
institucional do CIB (sem logo, sem campos Aluno/Turma/Data): só a
problemática e o espaço de resposta do grupo, como pedido. Fonte dos
textos: ferramentas/problemas-caminhos-aula2.md (mantidos em sincronia
manual).

Três problemas fictícios (sem relação com casos reais usados em outras
aulas), cada um com "Como eu resolvo?" (resposta livre do grupo, antes de
ver os caminhos) e 3 caminhos possíveis com sua consequência, terminando
numa pergunta de reflexão.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

pdfmetrics.registerFont(TTFont("Montserrat", os.path.join(ASSETS, "MontserratMedium-regular.ttf")))
pdfmetrics.registerFont(TTFont("Montserrat-Bold", os.path.join(ASSETS, "MontserratMedium-bold.ttf")))
pdfmetrics.registerFont(TTFont("Montserrat-Italic", os.path.join(ASSETS, "MontserratMedium-italic.ttf")))

PAGE_W, PAGE_H = A4
MARGIN = 20 * mm
BLACK = colors.black
GREY = colors.HexColor("#6B6B63")
TERRACOTTA = colors.HexColor("#B5651D")
LIGHTBG = colors.HexColor("#F5F4EF")

CAMINHO_LABELS = ["Caminho 1 (mais fácil)", "Caminho 2 (esforço médio)", "Caminho 3 (mais trabalhoso)"]

PROBLEMAS = [
    ("O parque sujo",
     "O parque perto da sua escola está cada vez mais sujo. Tem lixo espalhado pelo chão, os bancos "
     "estão pichados, e cada vez menos gente frequenta o lugar.",
     [
         ("Colocar mais uma lixeira no parque.",
          "Ajuda um pouco por algumas semanas, mas as pessoas voltam a jogar lixo no chão, porque o "
          "hábito de cuidar do espaço não mudou."),
         ("Fazer cartazes pedindo para não sujar o parque.",
          "Chama atenção por alguns dias, mas sem lembrete constante o efeito passa rápido e tudo "
          "volta ao normal."),
         ("Organizar um mutirão de limpeza com moradores da região, formar um grupo fixo de "
          "voluntários que cuida do parque toda semana, e conversar com a prefeitura sobre coleta "
          "regular de lixo.",
          "Dá muito mais trabalho para começar e manter, mas o parque fica limpo de forma duradoura, "
          "porque virou hábito da comunidade e não depende de uma ação isolada."),
     ],
     "Se você já soubesse essas 3 consequências antes de escolher, a decisão seria fácil. Na vida "
     "real, ninguém sabe o futuro de antemão. Por que o caminho mais trabalhoso costuma ser o que "
     "realmente resolve o problema?"),
    ("A biblioteca vazia",
     "A biblioteca da sua escola está cada vez mais vazia. Os alunos preferem passar o intervalo no "
     "celular, e quase ninguém pega livros emprestados.",
     [
         ("Colocar um cartaz “Venha ler mais!” na porta da biblioteca.",
          "Quase ninguém muda de comportamento; o cartaz vira só mais um enfeite na parede."),
         ("Comprar alguns livros novos e mais populares.",
          "Ajuda um pouco, mas se ninguém souber que chegaram livros novos, poucos alunos aparecem."),
         ("Criar um clube do livro com os próprios alunos escolhendo os títulos, organizando "
          "encontros semanais, e indicando livros uns para os outros.",
          "Dá muito mais trabalho organizar e manter funcionando, mas em poucos meses a biblioteca "
          "vira um lugar que os alunos escolhem frequentar, porque agora é deles."),
     ],
     "De novo, o caminho mais óbvio (o cartaz) foi o que menos funcionou. O que o clube do livro tem "
     "que os outros dois caminhos não têm?"),
    ("O aluno novo sozinho",
     "Um aluno novo chegou na sua turma este ano. Ele sempre fica sozinho no intervalo e quase não "
     "conversa com ninguém.",
     [
         ("O professor pede para alguém sentar com o aluno novo, só naquele dia.",
          "Ajuda naquele dia específico, mas no dia seguinte o aluno novo volta a ficar sozinho."),
         ("Apresentar o aluno novo para toda a turma no primeiro dia de aula.",
          "Todo mundo passa a saber o nome dele, mas isso sozinho não cria amizades de verdade."),
         ("Um pequeno grupo decide, de verdade, incluir o aluno novo nas próximas semanas: chamar "
          "para o grupo do intervalo, apresentar para outros amigos, perguntar como ele está se "
          "sentindo.",
          "Exige esforço contínuo e interesse genuíno por várias semanas, mas o aluno novo passa a "
          "se sentir parte de verdade da turma, não só “bem recebido” uma vez."),
     ],
     "Dos 3 problemas desta ficha, qual caminho 3 pareceu mais difícil de colocar em prática de "
     "verdade? Por quê?"),
]

c = canvas.Canvas(os.path.join(HERE, "Problemas e Caminhos - Aula 2.pdf"), pagesize=A4)


def _break_long_token(token, font, size, max_w):
    pieces = []
    cur = ""
    for ch in token:
        test = cur + ch
        if cur and pdfmetrics.stringWidth(test, font, size) > max_w:
            pieces.append(cur)
            cur = ch
        else:
            cur = test
    if cur:
        pieces.append(cur)
    return pieces


def wrap_text(text, font, size, max_w):
    words = text.split()
    lines = []
    line = ""
    for w in words:
        test = (line + " " + w).strip()
        if pdfmetrics.stringWidth(test, font, size) > max_w:
            if line:
                lines.append(line)
                line = ""
            if pdfmetrics.stringWidth(w, font, size) > max_w:
                pieces = _break_long_token(w, font, size, max_w)
                lines.extend(pieces[:-1])
                line = pieces[-1] if pieces else ""
            else:
                line = w
        else:
            line = test
    if line:
        lines.append(line)
    return lines


def draw_wrapped(x, y, text, font, size, max_w, leading, color=BLACK):
    c.setFillColor(color)
    for ln in wrap_text(text, font, size, max_w):
        c.setFont(font, size)
        c.drawString(x, y, ln)
        y -= leading
    return y


def writing_line(x, right, y):
    c.setStrokeColor(GREY)
    c.setLineWidth(0.6)
    c.line(x, y, right, y)
    return y


# --------------------------------------------------------------- página 1
def draw_instrucoes():
    x = MARGIN
    right = PAGE_W - MARGIN
    y = PAGE_H - MARGIN

    c.setFont("Montserrat-Bold", 20)
    c.setFillColor(BLACK)
    c.drawString(x, y, "Problemas e Caminhos")
    y -= 8 * mm
    c.setFont("Montserrat-Italic", 12)
    c.setFillColor(GREY)
    c.drawString(x, y, "Aula 2, guia rápido para o professor")
    y -= 12 * mm

    paragrafos = [
        "3 problemas fictícios (sem relação com casos reais usados em outras aulas). Dividir a turma "
        "em grupos, um problema por grupo, repetindo se houver mais grupos que problemas.",
        "Cada grupo primeiro escreve a própria ideia em “Como eu resolvo?”, sem ver os 3 caminhos "
        "possíveis. Só depois de escrever é que o grupo lê os 3 caminhos e as consequências.",
        "Fechar com uma roda rápida: cada grupo conta se a ideia que teve no início se pareceu mais "
        "com o caminho 1, 2 ou 3.",
        "A ideia pedagógica: ver as 3 consequências de uma vez deixa a escolha óbvia, o caminho mais "
        "trabalhoso é sempre o melhor. Na vida real ninguém vê o futuro antes de decidir; por isso a "
        "pergunta de reflexão em cada problema pergunta por quê, mesmo sem saber o resultado, vale a "
        "pena escolher o caminho mais difícil quando se quer resolver um problema de verdade.",
    ]
    for p in paragrafos:
        y = draw_wrapped(x, y, p, "Montserrat", 11.5, right - x, 5.6 * mm)
        y -= 5 * mm

    c.showPage()


# ------------------------------------------------------- páginas 2, 3, 4
def draw_problema(numero, titulo, contexto, caminhos, reflexao):
    x = MARGIN
    right = PAGE_W - MARGIN
    y = PAGE_H - MARGIN

    c.setFont("Montserrat-Bold", 20)
    c.setFillColor(BLACK)
    c.drawString(x, y, f"Problema {numero}")
    y -= 8.5 * mm
    c.setFont("Montserrat-Italic", 15)
    c.setFillColor(TERRACOTTA)
    c.drawString(x, y, titulo)
    y -= 11 * mm

    y = draw_wrapped(x, y, contexto, "Montserrat", 12.5, right - x, 6.2 * mm)
    y -= 8 * mm

    c.setFont("Montserrat-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(x, y, "Como eu resolvo?")
    y -= 9 * mm
    for _ in range(3):
        y = writing_line(x, right, y); y -= 8 * mm

    y -= 3 * mm
    c.setStrokeColor(GREY)
    c.setLineWidth(0.5)
    c.line(x, y, right, y)
    y -= 9 * mm

    for label, (acao, consequencia) in zip(CAMINHO_LABELS, caminhos):
        inner_pad = 4.5 * mm
        text_w = (right - x) - 2 * inner_pad
        acao_lines = wrap_text(acao, "Montserrat-Bold", 10.8, text_w)
        cons_lines = wrap_text(f"Consequência: {consequencia}", "Montserrat-Italic", 10.5, text_w)
        line_h = 5.1 * mm
        box_h = inner_pad * 2 + 5.5 * mm + len(acao_lines) * line_h + 2 * mm + len(cons_lines) * line_h

        box_top = y
        box_bottom = y - box_h
        c.setFillColor(LIGHTBG)
        c.rect(x, box_bottom, right - x, box_h, stroke=0, fill=1)

        ty = box_top - inner_pad - 3.5 * mm
        c.setFont("Montserrat-Bold", 9.5)
        c.setFillColor(TERRACOTTA)
        c.drawString(x + inner_pad, ty, label.upper())
        ty -= 5.5 * mm
        for ln in acao_lines:
            c.setFont("Montserrat-Bold", 10.8)
            c.setFillColor(BLACK)
            c.drawString(x + inner_pad, ty, ln)
            ty -= line_h
        ty -= 2 * mm
        for ln in cons_lines:
            c.setFont("Montserrat-Italic", 10.5)
            c.setFillColor(GREY)
            c.drawString(x + inner_pad, ty, ln)
            ty -= line_h

        y = box_bottom - 5 * mm

    y -= 2 * mm
    c.setFont("Montserrat-Bold", 12)
    c.setFillColor(BLACK)
    y = draw_wrapped(x, y, f"Reflexão: {reflexao}", "Montserrat-Bold", 12, right - x, 6 * mm)
    y -= 5 * mm
    for _ in range(3):
        y = writing_line(x, right, y); y -= 8 * mm

    c.showPage()


draw_instrucoes()
for i, (titulo, contexto, caminhos, reflexao) in enumerate(PROBLEMAS, start=1):
    draw_problema(i, titulo, contexto, caminhos, reflexao)

c.save()
print("PDF gerado com sucesso")
