# -*- coding: utf-8 -*-
"""
Jogo dos 10 Cartões (Aula 1) — cabeçalho padrão CIB (Ensino Fundamental 2),
mesma padronização visual do Diário do Empreendedor (Montserrat, moldura de
página, cores preto/branco/cinza).

Gera 3 páginas: (1) instruções para o professor, (2) os 10 cartões para
recortar (sem o país de origem — é isso que os alunos precisam descobrir),
(3) gabarito do professor, com os dados de fundação/aquisição checados em
fontes públicas (não deve ser entregue aos alunos).
"""
import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
sys.path.insert(0, HERE)
from dados_jogo_10_cartoes import CARTOES as _CARTOES_DADOS, GABARITO as _GABARITO_DADOS

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

# CARTOES e GABARITO vêm de dados_jogo_10_cartoes.py (fonte única, compartilhada
# com o gerador do jogo em HTML) — 8 empresas reais + 2 pegadinha.
CARTOES = [(nome, problema, solucao) for (_id, nome, problema, solucao) in _CARTOES_DADOS]

GABARITO = []
for _id, nome, _problema, _solucao in _CARTOES_DADOS:
    is_israel, pais, fato = _GABARITO_DADOS[_id]
    pais_label = pais if is_israel else f"{pais} — PEGADINHA"
    GABARITO.append((nome, pais_label, fato))

c = canvas.Canvas(os.path.join(HERE, "Jogo dos 10 Cartoes - Aula 1.pdf"), pagesize=A4)


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
    """Quebra um único token (sem espaços) que sozinho ultrapassa max_w,
    ex: 'Suécia/Dinamarca' — evita que ele vaze para a coluna seguinte."""
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


def draw_paragraphs(x, right, y, paragraphs, size=11, leading=5.2 * mm, gap=3 * mm):
    max_w = right - x
    for p in paragraphs:
        y = draw_wrapped(x, y, p, "Montserrat", size, max_w, leading)
        y -= gap
    return y


# ---------------------------------------------------------------- Página 1
def draw_instrucoes():
    page_frame()
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = cib_header("Jogo dos 10 Cartões — Aula 1")

    y -= 10 * mm
    c.setFont("Montserrat-Italic", 12)
    c.setFillColor(GREY)
    c.drawString(x, y, "Guia rápido para o professor — não entregar esta página aos alunos.")
    y -= 10 * mm

    paragrafos = [
        "Turma de aproximadamente 20 alunos: dividir em 5 grupos de 4. Cada grupo recebe seu "
        "próprio conjunto de 10 cartões, embaralhado.",
        "Imprima a página “Cartões para recortar” em 5 vias (uma por grupo) e recorte pelas "
        "linhas tracejadas — são 10 cartões por via, 50 no total.",
        "Cada cartão traz apenas o nome do produto/empresa, o problema que ele resolve e a "
        "solução criada — sem o país de origem.",
        "Desafio do grupo (25 min): ler os 10 cartões e decidir, por argumentação (sem celular, "
        "sem pesquisar), quais 2 dos 10 NÃO são israelenses — são a pegadinha.",
        "Correção coletiva (15 min): revisar cartão a cartão com a turma toda, revelando o país "
        "de cada um a partir do gabarito (página seguinte).",
        "Objetivo pedagógico: não é “decorar que Israel é inovador” — é treinar o raciocínio de "
        "identificar problema → solução em qualquer produto, e só depois perceber a escala do "
        "fenômeno (8 em cada 10 produtos do dia a dia dos alunos, neste jogo, vieram de Israel).",
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
    y = draw_wrapped(x, y, "Dados de fundação, fundadores e valores de aquisição do gabarito foram checados em "
                           "registros públicos (Wikipedia, Forbes, arquivos da SEC e histórico das próprias "
                           "empresas) em julho de 2026.", "Montserrat-Italic", 9.5, right - x, 4.6 * mm, color=GREY)
    c.setFillColor(BLACK)
    c.showPage()


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


# ---------------------------------------------------------------- Página 2
def draw_cartoes():
    """10 cartões (2 colunas x 5 linhas) com linhas tracejadas para recortar.
    Sem cabeçalho/logo — a página inteira vira cartões, sem espaço perdido."""
    cols, rows = 2, 5
    gap = 3 * mm
    grid_x = BORDER_MARGIN + 2 * mm
    grid_y = BORDER_MARGIN + 2 * mm
    grid_w = PAGE_W - 2 * grid_x
    grid_h = PAGE_H - 2 * grid_y
    card_w = (grid_w - (cols - 1) * gap) / cols
    card_h = (grid_h - (rows - 1) * gap) / rows

    for i, (nome, problema, solucao) in enumerate(CARTOES):
        col = i % cols
        row = i // cols
        card_x = grid_x + col * (card_w + gap)
        card_y = PAGE_H - grid_y - (row + 1) * card_h - row * gap

        c.setDash(2, 2)
        c.setStrokeColor(GREY)
        c.setLineWidth(0.7)
        c.rect(card_x, card_y, card_w, card_h)
        c.setDash()

        pad = 4 * mm
        tx = card_x + pad
        tright = card_x + card_w - pad
        ty = card_y + card_h - pad - 3 * mm

        nome_lines = wrap_text(nome, "Montserrat-Bold", 12, tright - tx)
        c.setFillColor(BLACK)
        for ln in nome_lines:
            c.setFont("Montserrat-Bold", 12)
            c.drawString(tx, ty, ln)
            ty -= 5 * mm
        ty -= 1.5 * mm

        c.setFont("Montserrat-Bold", 8.5)
        c.setFillColor(GREY)
        c.drawString(tx, ty, "PROBLEMA")
        ty -= 4 * mm
        ty = draw_wrapped(tx, ty, problema, "Montserrat", 8.7, tright - tx, 3.7 * mm)

        ty -= 1.5 * mm
        c.setFont("Montserrat-Bold", 8.5)
        c.setFillColor(GREY)
        c.drawString(tx, ty, "SOLUÇÃO")
        ty -= 4 * mm
        draw_wrapped(tx, ty, solucao, "Montserrat", 8.7, tright - tx, 3.7 * mm)

    c.setFillColor(BLACK)
    c.showPage()


# ---------------------------------------------------------------- Página 3
def draw_gabarito():
    page_frame()
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = cib_header("Gabarito do professor")

    y -= 10 * mm
    c.setFont("Montserrat-Italic", 11)
    c.setFillColor(GREY)
    y = draw_wrapped(x, y, "Não entregar aos alunos — revelar só depois da rodada de adivinhação.",
                      "Montserrat-Italic", 11, right - x, 5 * mm, color=GREY)
    y -= 6 * mm

    col1_w = 46 * mm
    col2_w = 40 * mm
    col3_x = x + col1_w + col2_w
    row_gap = 2.5 * mm

    c.setFont("Montserrat-Bold", 9.5)
    c.setFillColor(BLACK)
    c.drawString(x, y, "PRODUTO")
    c.drawString(x + col1_w, y, "PAÍS")
    c.drawString(col3_x, y, "FATO VALIDADO")
    y -= 3 * mm
    c.setStrokeColor(BLACK)
    c.setLineWidth(0.6)
    c.line(x, y, right, y)
    y -= 5 * mm

    for nome, pais, fato in GABARITO:
        nome_lines = wrap_text(nome, "Montserrat-Bold", 9, col1_w - 2 * mm)
        pais_lines = wrap_text(pais, "Montserrat", 8.7, col2_w - 2 * mm)
        fato_lines = wrap_text(fato, "Montserrat", 8.7, right - col3_x)
        n_lines = max(len(nome_lines), len(pais_lines), len(fato_lines))

        ly = y
        c.setFont("Montserrat-Bold", 9)
        c.setFillColor(BLACK)
        for ln in nome_lines:
            c.drawString(x, ly, ln)
            ly -= 3.8 * mm

        ly = y
        c.setFont("Montserrat", 8.7)
        c.setFillColor(BLACK)
        for ln in pais_lines:
            c.drawString(x + col1_w, ly, ln)
            ly -= 3.8 * mm

        ly = y
        c.setFont("Montserrat", 8.7)
        c.setFillColor(BLACK)
        for ln in fato_lines:
            c.drawString(col3_x, ly, ln)
            ly -= 3.8 * mm

        y -= n_lines * 3.8 * mm + row_gap
        c.setStrokeColor(LIGHTGREY)
        c.setLineWidth(0.4)
        c.line(x, y + row_gap / 2, right, y + row_gap / 2)

    y -= 4 * mm
    c.setFont("Montserrat-Italic", 9)
    c.setFillColor(GREY)
    draw_wrapped(x, y, "Fontes: Wikipedia, Forbes, arquivos da SEC e histórico das próprias empresas "
                       "(checado em julho de 2026). Valores de aquisição variam entre fontes — os números "
                       "acima são os mais citados em registros públicos.",
                 "Montserrat-Italic", 9, right - x, 4.3 * mm, color=GREY)
    c.setFillColor(BLACK)
    c.showPage()


draw_instrucoes()
draw_cartoes()
draw_gabarito()

c.save()
print("PDF gerado com sucesso")
