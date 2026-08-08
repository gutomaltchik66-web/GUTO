# -*- coding: utf-8 -*-
"""
Enigma e Problemas Sociais (Aula 2) — cabeçalho padrão CIB, mesma
padronização visual dos demais materiais da eletiva. Fonte dos textos:
ferramentas/enigma-e-problemas-aula2.md (mantidos em sincronia manual).

Gera 7 páginas: (1) instruções para o professor, (2) os 4 cartões do
enigma para recortar (imprimir 4 vias, uma por grupo), (3) gabarito do
enigma, (4-6) as 3 fichas-problema (uma por página, com espaço para a
resposta do grupo), (7) gabarito de qual inovação resolve qual problema.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

pdfmetrics.registerFont(TTFont("Montserrat", os.path.join(ASSETS, "MontserratMedium-regular.ttf")))
pdfmetrics.registerFont(TTFont("Montserrat-Bold", os.path.join(ASSETS, "MontserratMedium-bold.ttf")))
pdfmetrics.registerFont(TTFont("Montserrat-Italic", os.path.join(ASSETS, "MontserratMedium-italic.ttf")))

LOGO_PATH = os.path.join(ASSETS, "cib-logo-header.png")
logo_img = ImageReader(LOGO_PATH)
LOGO_W_PX, LOGO_H_PX = logo_img.getSize()
LOGO_ASPECT = LOGO_W_PX / LOGO_H_PX

PAGE_W, PAGE_H = A4
BORDER_MARGIN = 10 * mm
CONTENT_MARGIN = 16 * mm
BLACK = colors.black
GREY = colors.HexColor("#8C8C8C")
LIGHTGREY = colors.HexColor("#EDEDED")

CARTOES_ENIGMA = [
    ("A", "O quintal",
     "Um engenheiro caminhava por um quintal em Israel, nos anos 1950, quando notou uma árvore "
     "crescendo mais forte do que as outras, bem ao lado de um cano velho. Foi ver o motivo: havia "
     "só um único e pequenino furo vazando água, gota a gota, direto na raiz.",
     "Multiplique esse número de furos (1) por ele mesmo, depois some 0. Escreva o resultado (um algarismo):"),
    ("B", "Gota a gota",
     "Intrigado, o engenheiro passou a contar as gotas: caíam 3 gotas a cada 20 segundos.",
     "Quantas gotas caem em 1 minuto inteiro (60 segundos)? Se o resultado tiver mais de um algarismo, some os algarismos entre si até sobrar só um. Escreva o resultado:"),
    ("C", "A forma da colmeia",
     "Anos depois, a ideia de deixar a água vazar devagarinho, gota a gota, virou uma rede inteira "
     "de canos organizados, parecida com a estrutura de uma colmeia de abelhas.",
     "Quantos lados tem um hexágono, a forma da colmeia? Escreva o resultado:"),
    ("D", "Mãos à obra",
     "Para transformar a ideia em invenção de verdade, o engenheiro chamou o próprio filho para "
     "ajudar: os dois trabalharam juntos, lado a lado, testando canos e torneiras.",
     "Quantos dedos tem uma única mão humana? Escreva o resultado:"),
]

FICHAS_PROBLEMA = [
    ("Água que não sobra",
     "Em muitas regiões do mundo, inclusive partes do Brasil, o solo é seco e a água para a "
     "agricultura é escassa. Regar uma plantação do jeito tradicional desperdiça muita água, que "
     "evapora ou escorre para longe da raiz.",
     "Como cultivar plantas gastando o mínimo possível de água, sem desperdiçar nem uma gota?"),
    ("Perdido no caminho",
     "Em cidades grandes, o transporte público costuma ser confuso: as pessoas não sabem qual "
     "ônibus ou trem pegar, nem quando ele vai chegar, e acabam perdendo tempo ou desistindo de "
     "usar transporte público.",
     "Como ajudar milhões de pessoas a se locomoverem pela cidade de forma mais simples e confiável?"),
    ("Um exame difícil",
     "Alguns exames médicos para investigar o sistema digestivo são invasivos, desconfortáveis e "
     "caros: exigem inserir uma câmera ou tubo dentro do corpo do paciente.",
     "Como tornar esse tipo de exame mais simples e menos invasivo para quem precisa fazer?"),
]

GABARITO_PROBLEMAS = [
    ("Água que não sobra", "Irrigação por gotejamento (Netafim)"),
    ("Perdido no caminho", "Moovit"),
    ("Um exame difícil", "PillCam (Given Imaging)"),
]

c = canvas.Canvas(os.path.join(HERE, "Enigma e Problemas - Aula 2.pdf"), pagesize=A4)


def page_frame():
    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(BORDER_MARGIN, BORDER_MARGIN, PAGE_W - 2 * BORDER_MARGIN, PAGE_H - 2 * BORDER_MARGIN)


def cib_header(titulo):
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = PAGE_H - BORDER_MARGIN - 11 * mm

    c.setFont("Montserrat-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(x, y, "Ensino Fundamental 2")

    logo_h = 11 * mm
    logo_w = logo_h * LOGO_ASPECT
    c.drawImage(logo_img, right - logo_w, y - 3 * mm, width=logo_w, height=logo_h,
                preserveAspectRatio=True, mask="auto")

    y -= 11 * mm
    c.setLineWidth(0.8)
    c.line(x, y, right, y)

    y -= 9 * mm
    c.setFont("Montserrat-Bold", 15)
    c.drawString(x, y, titulo)
    return y


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


def draw_numbered(x, right, y, number, text, size=11, leading=5.4 * mm):
    label = f"{number}) "
    label_w = pdfmetrics.stringWidth(label, "Montserrat-Bold", size)
    max_w = right - x
    lines = wrap_text(text, "Montserrat", size, max_w - label_w)
    c.setFont("Montserrat-Bold", size)
    c.setFillColor(BLACK)
    c.drawString(x, y, label)
    c.setFont("Montserrat", size)
    if lines:
        c.drawString(x + label_w, y, lines[0])
    y -= leading
    for ln in lines[1:]:
        c.setFont("Montserrat", size)
        c.drawString(x, y, ln)
        y -= leading
    return y


def writing_line(x, right, y):
    c.setStrokeColor(GREY)
    c.setLineWidth(0.6)
    c.line(x, y, right, y)
    return y


# ---------------------------------------------------------------- Página 1
def draw_instrucoes():
    page_frame()
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = cib_header("Enigma e Problemas Sociais — Aula 2")

    y -= 10 * mm
    c.setFont("Montserrat-Italic", 12)
    c.setFillColor(GREY)
    c.drawString(x, y, "Guia rápido para o professor — não entregar esta página aos alunos.")
    y -= 10 * mm

    paragrafos = [
        "Parte 1 — Enigma (15 min): dividir a turma em 4 grupos. Imprimir a página “Cartões do "
        "enigma” em 4 vias (uma por grupo) e recortar os 4 cartões (A, B, C, D) de cada via.",
        "Cada cartão resolvido dá um algarismo. Juntando os 4 algarismos na ordem A-B-C-D, o grupo "
        "forma um código de 4 dígitos — o mesmo para todos os grupos. Sem celular, só papel e caneta.",
        "O primeiro grupo a decifrar levanta a mão; conferir com o gabarito (página seguinte) e não "
        "revelar o que o código significa — isso só acontece na Parte 3, na apresentação de slides.",
        "Parte 2 — 3 problemas sociais (25 min): sortear as 3 fichas-problema entre os 4 grupos (um "
        "problema pode repetir com 2 grupos). Cada grupo tem 15 min para preencher a ficha de "
        "solução e 2 min para apresentar à turma.",
        "Parte 3 — 3 inovações reais (20 min): apresentar os slides de "
        "padronizacao/gerar_apresentacao_aula2_pptx.js, revelando a inovação real por trás de cada "
        "problema (gabarito na última página deste PDF).",
    ]

    for i, p in enumerate(paragrafos, start=1):
        y = draw_numbered(x, right, y, i, p)
        y -= 2 * mm

    y -= 4 * mm
    c.setStrokeColor(GREY)
    c.setLineWidth(0.6)
    c.line(x, y, right, y)
    y -= 6 * mm
    c.setFont("Montserrat-Italic", 9.5)
    c.setFillColor(GREY)
    draw_wrapped(x, y, "Os fatos usados no enigma são reais (história da Netafim) e checados nas mesmas "
                       "fontes públicas usadas nos slides da Parte 3.", "Montserrat-Italic", 9.5,
                 right - x, 4.6 * mm, color=GREY)
    c.setFillColor(BLACK)
    c.showPage()


# ---------------------------------------------------------------- Página 2
def draw_cartoes_enigma():
    """4 cartões do enigma (2x2), com linhas tracejadas para recortar."""
    cols, rows = 2, 2
    gap = 4 * mm
    grid_x = BORDER_MARGIN + 4 * mm
    grid_y = BORDER_MARGIN + 4 * mm
    grid_w = PAGE_W - 2 * grid_x
    grid_h = PAGE_H - 2 * grid_y
    card_w = (grid_w - (cols - 1) * gap) / cols
    card_h = (grid_h - (rows - 1) * gap) / rows

    for i, (letra, titulo, historia, pergunta) in enumerate(CARTOES_ENIGMA):
        col = i % cols
        row = i // cols
        card_x = grid_x + col * (card_w + gap)
        card_y = PAGE_H - grid_y - (row + 1) * card_h - row * gap

        c.setDash(2, 2)
        c.setStrokeColor(GREY)
        c.setLineWidth(0.7)
        c.rect(card_x, card_y, card_w, card_h)
        c.setDash()

        pad = 6 * mm
        tx = card_x + pad
        tright = card_x + card_w - pad
        ty = card_y + card_h - pad - 4 * mm

        ty = draw_wrapped(tx, ty, f"Cartão {letra} — {titulo}", "Montserrat-Bold", 15, tright - tx, 6.2 * mm)
        ty -= 2 * mm

        ty = draw_wrapped(tx, ty, historia, "Montserrat-Italic", 10.5, tright - tx, 4.6 * mm)
        ty -= 3 * mm
        ty = draw_wrapped(tx, ty, pergunta, "Montserrat-Bold", 10.5, tright - tx, 4.6 * mm)
        ty -= 3 * mm
        c.setStrokeColor(BLACK)
        c.setLineWidth(0.8)
        c.rect(tx, ty - 9 * mm, 22 * mm, 9 * mm)

    c.setFillColor(BLACK)
    c.showPage()


# ---------------------------------------------------------------- Página 3
def draw_gabarito_enigma():
    page_frame()
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = cib_header("Gabarito do enigma")

    y -= 10 * mm
    c.setFont("Montserrat-Italic", 11)
    c.setFillColor(GREY)
    y = draw_wrapped(x, y, "Não entregar aos alunos.", "Montserrat-Italic", 11, right - x, 5 * mm, color=GREY)
    y -= 8 * mm

    respostas = ["1", "9", "6", "5"]
    c.setFont("Montserrat-Bold", 13)
    c.setFillColor(BLACK)
    for i, (letra, titulo, _h, _p) in enumerate(CARTOES_ENIGMA):
        c.drawString(x, y, f"Cartão {letra} ({titulo}): {respostas[i]}")
        y -= 8 * mm

    y -= 4 * mm
    c.setFont("Montserrat-Bold", 16)
    c.drawString(x, y, "Código final: 1 - 9 - 6 - 5  →  1965")
    y -= 12 * mm

    c.setFont("Montserrat", 11)
    c.setFillColor(BLACK)
    y = draw_wrapped(x, y,
                      "Não revelar o que o código significa ainda — isso acontece na Parte 3, quando a "
                      "primeira inovação apresentada (irrigação por gotejamento, Netafim) tiver "
                      "justamente 1965 como o ano de fundação da empresa. É o “gancho” que fecha a aula.",
                      "Montserrat", 11, right - x, 5.4 * mm)
    c.showPage()


# ---------------------------------------------------------- Páginas 4 a 6
def draw_ficha_problema(numero, titulo, contexto, desafio):
    page_frame()
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = cib_header(f"Ficha-problema {numero} — {titulo}")

    y -= 10 * mm
    inner_pad_x = 6 * mm
    inner_pad_y = 5 * mm
    text_w = (right - x) - 2 * inner_pad_x
    ctx_lines = wrap_text(contexto, "Montserrat-Italic", 11.5, text_w)
    des_lines = wrap_text(desafio, "Montserrat-Bold", 11.5, text_w)
    line_h = 5.8 * mm
    box_h = inner_pad_y * 2 + (len(ctx_lines) + len(des_lines)) * line_h + 3 * mm

    box_top = y
    box_bottom = y - box_h
    c.setStrokeColor(BLACK)
    c.setLineWidth(0.8)
    c.rect(x, box_bottom, right - x, box_h, stroke=1, fill=0)

    ty = box_top - inner_pad_y - 3 * mm
    tx = x + inner_pad_x
    tright = x + (right - x) - inner_pad_x
    c.setFillColor(BLACK)
    for ln in ctx_lines:
        c.setFont("Montserrat-Italic", 11.5)
        c.drawString(tx, ty, ln)
        ty -= line_h
    ty -= 3 * mm
    for ln in des_lines:
        c.setFont("Montserrat-Bold", 11.5)
        c.drawString(tx, ty, ln)
        ty -= line_h

    y = box_bottom - 10 * mm
    c.setFont("Montserrat-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(x, y, "Ficha de solução do grupo")
    y -= 9 * mm

    c.setFont("Montserrat", 11)
    c.drawString(x, y, "Grupo: _____________________________________")
    y -= 10 * mm

    c.setFont("Montserrat-Bold", 11)
    c.drawString(x, y, "Nossa ideia:")
    y -= 8 * mm
    for _ in range(4):
        y = writing_line(x, right, y); y -= 8 * mm

    y -= 2 * mm
    c.setFont("Montserrat-Bold", 11)
    c.drawString(x, y, "Por que ela funcionaria:")
    y -= 8 * mm
    for _ in range(3):
        y = writing_line(x, right, y); y -= 8 * mm

    y -= 2 * mm
    c.setFont("Montserrat-Bold", 11)
    c.drawString(x, y, "Desenho (espaço livre):")
    y -= 6 * mm
    c.setStrokeColor(BLACK)
    c.setLineWidth(0.8)
    c.rect(x, BORDER_MARGIN + 8 * mm, right - x, y - (BORDER_MARGIN + 8 * mm))

    c.showPage()


# ---------------------------------------------------------------- Página 7
def draw_gabarito_problemas():
    page_frame()
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = cib_header("Gabarito — problema → inovação real")

    y -= 10 * mm
    c.setFont("Montserrat-Italic", 11)
    c.setFillColor(GREY)
    y = draw_wrapped(x, y, "Não entregar aos alunos — revelar na Parte 3, junto com os slides.",
                      "Montserrat-Italic", 11, right - x, 5 * mm, color=GREY)
    y -= 8 * mm

    for problema, solucao in GABARITO_PROBLEMAS:
        c.setFont("Montserrat-Bold", 13)
        c.setFillColor(BLACK)
        c.drawString(x, y, problema)
        y -= 7 * mm
        c.setFont("Montserrat-Italic", 12)
        c.setFillColor(GREY)
        c.drawString(x, y, f"→ {solucao}")
        y -= 11 * mm

    y -= 4 * mm
    c.setFont("Montserrat", 11)
    c.setFillColor(BLACK)
    y = draw_wrapped(x, y,
                      "O objetivo não é os alunos “acertarem” a mesma solução que os israelenses "
                      "criaram — é perceberem, na apresentação da Parte 3, que o raciocínio deles "
                      "(identificar o problema, pensar em algo simples e direto) é o mesmo processo "
                      "por trás de inovações reais. Vale destacar qualquer semelhança entre a ideia "
                      "de um grupo e a solução real.",
                      "Montserrat", 11, right - x, 5.4 * mm)
    c.showPage()


draw_instrucoes()
draw_cartoes_enigma()
draw_gabarito_enigma()
for i, (titulo, contexto, desafio) in enumerate(FICHAS_PROBLEMA, start=1):
    draw_ficha_problema(i, titulo, contexto, desafio)
draw_gabarito_problemas()

c.save()
print("PDF gerado com sucesso")
