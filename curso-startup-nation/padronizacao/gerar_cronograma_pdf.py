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
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, KeepTogether,
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

# (numero, data, bloco, tema, status) — mantido em sincronia com calendario.md.
# A Aula 4 aparece em duas linhas (dois encontros).
AULAS = [
    (1, "03/08", "Fundamentos", "Abertura: além do que você já sabe sobre Israel", "Dada"),
    (2, "10/08", "Fundamentos", "Evoluções tecnológicas de Israel", "Dada"),
    (3, "31/08", "Fundamentos", "Chutzpah: da palavra à atitude empreendedora", "Dada"),
    (4, "14/09", "Fundamentos", "O papel do Estado e do Exército (1º encontro: David cards + Google Classroom)", "Dada"),
    (4, "28/09", "Fundamentos", "O papel do Estado e do Exército (2º encontro: Aliot, Tnuot Noar e conferência com João Gus, IDF)", "Dada"),
    (5, "05/10", "Ecossistema", "Tikun olam: inovação com propósito (última aula com o Diário)", ""),
    (6, "19/10", "Meu Projeto", "Oficina de projeto 1: problema, público e evidência", ""),
    (7, "26/10", "Meu Projeto", "Oficina de projeto 2: protótipo e modelo de negócio", ""),
    (8, "09/11", "Meu Projeto", "Oficina de projeto 3: valores judaicos e roteiro do pitch", ""),
    (9, "16/11", "Meu Projeto", "Ensaio geral + ajustes finais", ""),
    (10, "23/11", "Avaliação", "PITCH DAY — Semana Avaliativa EF2 (auditório)", "Pitch Day"),
    (11, "30/11", "Fechamento", "Devolutivas + Feira de Ideias", ""),
    (12, "07/12", "Fechamento", "E depois do pitch? Da ideia ao negócio de verdade", ""),
    (13, "14/12", "Fechamento", "Banca de investidores (convidado ou simulação)", ""),
    (14, "21/12", "Fechamento", "Encerramento do semestre", ""),
]

# (titulo, itens) — uma entrada por revisão do calendário.
HISTORICO = [
    ("Revisão de 01/09", [
        "17/08 e 24/08: aulas perdidas, sem reposição.",
        "Cortadas do plano original de 17 aulas: Tolerância ao erro e Estudos de caso (o conteúdo das empresas já tinha sido coberto nas aulas iniciais).",
    ]),
    ("Revisão de 01/10", [
        "A Aula 4 aconteceu em dois encontros: 14/09 (David cards + atividade no Google Classroom) e 28/09 (conferência com o João Gus, das IDF). Em 21/09 não houve aula (Iom Kipur).",
        "Tikun olam passou para 05/10 e é a última aula com o Diário do Empreendedor, que fica com 5 páginas.",
        "Os alunos já têm projetos do primeiro semestre: 19/10, 26/10 e 09/11 viram oficinas para terminar os trabalhos, e 16/11 é o ensaio geral. O Pitch Day segue em 23/11, no auditório.",
        "Resultado: 14 aulas (15 encontros, contando os dois da Aula 4).",
    ]),
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
        "Revisado em 01/10/2026: 14 aulas (15 encontros). Pitch Day em 23/11 "
        "(semana avaliativa das eletivas EF2), no auditório já reservado.",
        styles["meta"]))
    story.append(Spacer(1, 4 * mm))

    header_row = [
        Paragraph("Nº", styles["headCell"]), Paragraph("Data", styles["headCell"]),
        Paragraph("Bloco", styles["headCell"]), Paragraph("Tema", styles["headCell"]),
        Paragraph("Status", styles["headCell"]),
    ]
    rows = [header_row]
    for n, data, bloco, tema, status in AULAS:
        style_num = styles["cellNum"]
        style_tema = styles["cellBold"] if status == "Pitch Day" else styles["cell"]
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
    for i, (*_rest, status) in enumerate(AULAS, start=1):
        if status == "Dada":
            table_style.append(("BACKGROUND", (0, i), (-1, i), LIGHTGREY))
        if status == "Pitch Day":
            table_style.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F5E6D8")))
    table.setStyle(TableStyle(table_style))
    story.append(table)

    story.append(Paragraph("Histórico das revisões", styles["h2"]))
    story.append(Paragraph("O calendário original previa 17 aulas.", styles["body"]))
    for titulo, itens in HISTORICO:
        bloco = [Spacer(1, 2 * mm), Paragraph(titulo, styles["cellBold"]), Spacer(1, 1 * mm)]
        bloco += [Paragraph(f"•&nbsp;&nbsp;{item}", styles["bullet"]) for item in itens]
        story.append(KeepTogether(bloco))

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
