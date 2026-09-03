# -*- coding: utf-8 -*-
"""
Cronograma da eletiva StartUp Nation (EF2) — PDF para impressão/arquivo,
com o cabeçalho institucional do CIB (logo + "Ensino Fundamental 2") e
moldura de página, no mesmo padrão dos demais materiais em `padronizacao/`.

Fonte dos dados: tabela e notas de `../calendario.md` (mantidos em sincronia
manualmente — atualizar aqui sempre que o calendário mudar).
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer,
)
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
HEADER_TOP_GAP = 22 * mm  # espaço reservado no topo de cada página para o cabeçalho

# (numero, data, bloco, tema) — mantido em sincronia com calendario.md
AULAS = [
    (1, "03/08", "Fundamentos", "Abertura: além do que você já sabe sobre Israel"),
    (2, "10/08", "Fundamentos", "Evoluções tecnológicas de Israel"),
    (3, "31/08", "Fundamentos", "Chutzpah: da palavra à atitude empreendedora"),
    (4, "14/09", "Fundamentos", "O papel do Estado e do Exército (convidado confirmado)"),
    (5, "28/09", "Ecossistema", "Tikun olam + lançamento do desafio final"),
    (6, "05/10", "Meu Projeto", "Mapa de Empatia: entendendo o problema de verdade"),
    (7, "19/10", "Meu Projeto", "Canvas do Projeto Pessoal: primeira ideia"),
    (8, "26/10", "Meu Projeto", "Protótipo: tirando a ideia do papel"),
    (9, "09/11", "Meu Projeto", "Roteiro de Pitch: contando minha ideia em 2 min"),
    (10, "16/11", "Meu Projeto", "Ensaio geral + ajustes finais"),
    (11, "23/11", "Avaliação", "PITCH DAY — Semana Avaliativa EF2"),
    (12, "30/11", "Fechamento", "Devolutivas + Feira de Ideias"),
    (13, "07/12", "Fechamento", "E depois do pitch? Da ideia ao negócio de verdade"),
    (14, "14/12", "Fechamento", "Banca de investidores (convidado ou simulação)"),
    (15, "21/12", "Fechamento", "Encerramento do semestre"),
]

DADAS = {1, 2, 3}  # aulas já dadas até 01/09

HISTORICO = [
    "17/08 e 24/08 — aulas perdidas, sem reposição.",
    "31/08 — deu a aula de Chutzpah (antiga Aula 3), sem a aula de Tolerância ao erro que estava prevista para 24/08.",
    "A aula de Tolerância ao erro (antiga Aula 4) foi cortada do curso, inclusive a página correspondente do Diário do Empreendedor.",
    "A aula de Estudos de caso: empresas que uso todo dia (antiga Aula 6) também foi cortada, o conteúdo já havia sido coberto nas aulas iniciais, e seu lugar em 14/09 foi ocupado pela aula de Estado e Exército (antiga Aula 5), que já tem convidado confirmado.",
    "A partir daí, todas as datas seguintes coincidem com o calendário original: o desafio final continua sendo lançado em 28/09, e o Pitch Day segue em 23/11 sem qualquer aperto, ainda sobram 6 aulas de bloco “Meu Projeto” (05/10 a 16/11) antes dele.",
    "Resultado: 15 aulas no total (3 já dadas, 12 pela frente), todas renumeradas nos planos de aula para não deixar buracos na sequência.",
]

DATAS_FORA = [
    "07/09 — Independência do Brasil",
    "21/09 — Iom Kipur",
    "12/10 — Nossa Senhora Aparecida / Dia das Crianças",
    "02/11 — Finados",
    "28/12 — já dentro do recesso escolar (iniciado em 24/12)",
]


def header_and_frame(c, doc):
    """Desenha a moldura de página e o cabeçalho institucional em toda página."""
    c.saveState()
    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(BORDER_MARGIN, BORDER_MARGIN, PAGE_W - 2 * BORDER_MARGIN, PAGE_H - 2 * BORDER_MARGIN)

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

    y -= 9 * mm
    c.setFont("Montserrat-Italic", 12)
    c.drawString(x, y, "Eletiva StartUp Nation — Cronograma")

    y -= 4 * mm
    c.setLineWidth(0.8)
    c.line(x, y, right, y)
    c.restoreState()


def build():
    styles = {
        "title": ParagraphStyle("title", fontName="Montserrat-Bold", fontSize=18, leading=22,
                                 spaceAfter=2 * mm, textColor=BLACK),
        "meta": ParagraphStyle("meta", fontName="Montserrat", fontSize=9.5, leading=13,
                                textColor=GREY, spaceAfter=1 * mm),
        "h2": ParagraphStyle("h2", fontName="Montserrat-Bold", fontSize=12, leading=15,
                              spaceBefore=5 * mm, spaceAfter=2 * mm, textColor=BLACK),
        "body": ParagraphStyle("body", fontName="Montserrat", fontSize=9.5, leading=13.5,
                                textColor=BLACK, alignment=TA_LEFT),
        "bullet": ParagraphStyle("bullet", fontName="Montserrat", fontSize=9.5, leading=13.5,
                                  textColor=BLACK, leftIndent=4 * mm, bulletIndent=0,
                                  spaceAfter=1.5 * mm),
        "cell": ParagraphStyle("cell", fontName="Montserrat", fontSize=9, leading=11.5, textColor=BLACK),
        "cellBold": ParagraphStyle("cellBold", fontName="Montserrat-Bold", fontSize=9, leading=11.5, textColor=BLACK),
        "cellNum": ParagraphStyle("cellNum", fontName="Montserrat-Bold", fontSize=9.5, leading=11.5,
                                   textColor=BLACK, alignment=1),
        "headCell": ParagraphStyle("headCell", fontName="Montserrat-Bold", fontSize=9.5, leading=12,
                                    textColor=colors.white),
    }

    story = []
    story.append(Paragraph("Cronograma — Eletiva StartUp Nation", styles["title"]))
    story.append(Paragraph(
        "Colégio Israelita Brasileiro (CIB) · 8º/9º ano EF2 · segundas-feiras, 14h às 15h30 (90 min)",
        styles["meta"]))
    story.append(Paragraph(
        "Revisado em 01/09/2026 — 15 aulas letivas no semestre. Pitch Day em 23/11 "
        "(semana avaliativa das eletivas EF2), auditório já reservado.",
        styles["meta"]))
    story.append(Spacer(1, 4 * mm))

    header_row = [
        Paragraph("Nº", styles["headCell"]), Paragraph("Data", styles["headCell"]),
        Paragraph("Bloco", styles["headCell"]), Paragraph("Tema", styles["headCell"]),
        Paragraph("Status", styles["headCell"]),
    ]
    rows = [header_row]
    for n, data, bloco, tema in AULAS:
        status = "Dada" if n in DADAS else ("Pitch Day" if n == 11 else "")
        style_num = styles["cellNum"]
        style_tema = styles["cellBold"] if n == 11 else styles["cell"]
        rows.append([
            Paragraph(str(n), style_num),
            Paragraph(data, styles["cell"]),
            Paragraph(bloco, styles["cell"]),
            Paragraph(tema, style_tema),
            Paragraph(status, styles["cell"]),
        ])

    col_widths = [9 * mm, 15 * mm, 30 * mm, 98 * mm, 20 * mm]
    table = Table(rows, colWidths=col_widths, repeatRows=1)
    table_style = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.black),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, GREY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.4 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4 * mm),
        ("LEFTPADDING", (0, 0), (-1, -1), 2 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
    ]
    for i, (n, *_rest) in enumerate(AULAS, start=1):
        if n in DADAS:
            table_style.append(("BACKGROUND", (0, i), (-1, i), LIGHTGREY))
        if n == 11:
            table_style.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F5E6D8")))
    table.setStyle(TableStyle(table_style))
    story.append(table)

    story.append(Paragraph("Histórico da revisão (01/09)", styles["h2"]))
    story.append(Paragraph(
        "O calendário original previa 17 aulas. Na prática:", styles["body"]))
    story.append(Spacer(1, 1.5 * mm))
    for item in HISTORICO:
        story.append(Paragraph(f"•&nbsp;&nbsp;{item}", styles["bullet"]))

    story.append(Paragraph("Datas que não contam (feriados / aulas suspensas)", styles["h2"]))
    for item in DATAS_FORA:
        story.append(Paragraph(f"•&nbsp;&nbsp;{item}", styles["bullet"]))

    doc = SimpleDocTemplate(
        "Cronograma - Eletiva StartUp Nation.pdf",
        pagesize=A4,
        topMargin=CONTENT_MARGIN + HEADER_TOP_GAP,
        bottomMargin=CONTENT_MARGIN,
        leftMargin=CONTENT_MARGIN,
        rightMargin=CONTENT_MARGIN,
    )
    doc.build(story, onFirstPage=header_and_frame, onLaterPages=header_and_frame)
    print("PDF gerado com sucesso")


if __name__ == "__main__":
    build()
