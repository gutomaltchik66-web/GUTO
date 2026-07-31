# -*- coding: utf-8 -*-
"""
Diário do Empreendedor — versão com cabeçalho padrão CIB (Ensino Fundamental 2),
replicando o modelo oficial extraído de CABEÇALHO EDITÁVEL EF2.docx e o
enquadramento de página (borda) extraído de PAUTA PEQUENA.pdf.
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
BORDER_MARGIN = 10 * mm     # page-frame border, like PAUTA PEQUENA
CONTENT_MARGIN = 16 * mm    # text content margin from page edge
BLACK = colors.black
GREY = colors.HexColor("#8C8C8C")
LIGHTGREY = colors.HexColor("#EDEDED")

aulas = [
    (1, "03/08", "Abertura: além do que você já sabe sobre Israel",
     "Em uma frase, o que você já sabe sobre Israel?"),
    (2, "10/08", "Raízes históricas, sob uma nova ótica",
     "O que você faria se não tivesse água, dinheiro ou tempo suficiente para algo que precisa muito?"),
    (3, "17/08", "Chutzpah: da palavra à atitude empreendedora",
     "Você já discordou de um adulto (professor, pai, treinador) porque achava que ele estava errado? O que aconteceu?"),
    (4, "24/08", "Tolerância ao fracasso",
     "O que você sente quando erra alguma coisa na frente dos outros?"),
    (5, "31/08", "O papel do Estado e do Exército",
     "Você acha que o governo deveria ajudar jovens com ideias de negócio? Por quê?"),
    (6, "14/09", "Estudos de caso: empresas que os alunos usam",
     "Qual desses produtos (Waze, Wix, Mobileye...) você já usou? Como seria sua rotina sem ele?"),
    (7, "28/09", "Tikun olam + lançamento do desafio final",
     "Você prefere criar algo que dá lucro, ou algo que ajuda alguém, mesmo sem ganhar dinheiro com isso? Por quê?"),
    (8, "05/10", "Mapa de Empatia: entendendo o problema de verdade",
     "Pense em alguém (colega, família, vizinho) que sofre com o problema que você quer resolver. Quem é essa pessoa?"),
    (9, "19/10", "Canvas do Projeto Pessoal: primeira ideia",
     "Se você pudesse resolver o problema do seu Mapa de Empatia com uma varinha mágica, o que aconteceria?"),
    (10, "26/10", "Protótipo: tirando a ideia do papel",
     "Se você tivesse que mostrar sua ideia sem falar nenhuma palavra, como faria?"),
    (11, "09/11", "Roteiro de Pitch: contando minha ideia em 2 min",
     "Se você tivesse só 2 minutos para convencer alguém a apoiar sua ideia, qual seria a primeira frase que diria?"),
    (12, "16/11", "Ensaio geral + ajustes finais",
     "O que ainda te deixa nervoso(a) sobre apresentar seu pitch? O que pode te ajudar a ficar mais tranquilo(a)?"),
    (13, "23/11", "PITCH DAY — Semana Avaliativa EF2",
     "Em uma palavra, como você está se sentindo antes de apresentar hoje?"),
    (14, "30/11", "Devolutivas + Feira de Ideias",
     "O que você espera ouvir hoje sobre o seu pitch?"),
    (15, "07/12", "E depois do pitch? Da ideia ao negócio de verdade",
     "Você acha que sua ideia poderia continuar existindo depois do fim do semestre? O que precisaria acontecer?"),
    (16, "14/12", "Banca de investidores (convidado ou simulação)",
     "Se um investidor fizesse só uma pergunta sobre sua ideia, qual você tem mais medo que seja?"),
    (17, "21/12", "Encerramento do semestre",
     "Em uma frase, o que você sabia sobre empreendedorismo/Israel no primeiro dia de aula?"),
]

c = canvas.Canvas("Diario do Empreendedor - Caderno do Aluno.pdf", pagesize=A4)


def page_frame():
    """Full-page border rectangle, as in PAUTA PEQUENA."""
    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(BORDER_MARGIN, BORDER_MARGIN, PAGE_W - 2 * BORDER_MARGIN, PAGE_H - 2 * BORDER_MARGIN)


def cib_header(data_aula):
    """Replicates the official 'Cabeçalho Editável EF2' block."""
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = PAGE_H - BORDER_MARGIN - 11 * mm

    # "Ensino Fundamental 2" (left) + logo (right), same row
    c.setFont("Montserrat-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(x, y, "Ensino Fundamental 2")

    logo_h = 11 * mm
    logo_w = logo_h * LOGO_ASPECT
    c.drawImage(logo_img, right - logo_w, y - 3 * mm, width=logo_w, height=logo_h,
                preserveAspectRatio=True, mask="auto")

    # "Aluno(a): ______________________________"
    y -= 9 * mm
    c.setFont("Montserrat", 11)
    label = "Aluno(a): "
    c.drawString(x, y, label)
    label_w = pdfmetrics.stringWidth(label, "Montserrat", 11)
    c.setLineWidth(0.6)
    c.setStrokeColor(BLACK)
    c.line(x + label_w, y - 1, right, y - 1)

    # "Ano Escolar: ___  Turma: ___  Data: ___"
    y -= 8 * mm
    parts = [("Ano Escolar: ", "________"), ("   Turma: ", "________"), ("   Data: ", data_aula)]
    cx = x
    for label, value in parts:
        c.setFont("Montserrat", 11)
        c.drawString(cx, y, label)
        cx += pdfmetrics.stringWidth(label, "Montserrat", 11)
        c.setFont("Montserrat-Bold" if value not in ("________",) else "Montserrat", 11)
        c.drawString(cx, y, value)
        cx += pdfmetrics.stringWidth(value, "Montserrat", 11)

    # thin rule under the standard header block
    y -= 4 * mm
    c.setLineWidth(0.8)
    c.line(x, y, right, y)
    return y  # bottom of the header, next content starts below this


def section_label(x, right, y, text):
    c.setFillColor(LIGHTGREY)
    c.rect(x, y - 6 * mm, right - x, 6 * mm, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Montserrat-Bold", 10)
    c.drawString(x + 2 * mm, y - 4.3 * mm, text)
    return y - 6 * mm


def writing_line(x, right, y):
    c.setStrokeColor(GREY)
    c.setLineWidth(0.6)
    c.line(x, y, right, y)
    return y


def draw_aula_page(n, data, tema, p2):
    page_frame()
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = cib_header(data)

    y -= 8 * mm
    c.setFont("Montserrat-Bold", 12)
    c.setFillColor(BLACK)
    c.drawString(x, y, f"Aula Nº {n}")
    aula_label_w = pdfmetrics.stringWidth(f"Aula Nº {n}   ", "Montserrat-Bold", 12)
    c.setFont("Montserrat-Italic", 12)
    c.drawString(x + aula_label_w, y, tema)

    y -= 9 * mm
    y = section_label(x, right, y, "ENTRADA  —  preencher sozinho, em silêncio, assim que sentar")
    y -= 6 * mm
    c.setFont("Montserrat", 10.5)
    q1 = "Em uma frase, quem é você e o que espera dessa eletiva?" if n == 1 else "Em uma frase, o que ficou da aula passada?"
    c.drawString(x, y, f"1. {q1}")
    y -= 6 * mm
    y = writing_line(x, right, y); y -= 8 * mm
    y = writing_line(x, right, y); y -= 8 * mm

    c.setFont("Montserrat", 10.5)
    text_obj = c.beginText(x, y)
    text_obj.setFont("Montserrat", 10.5)
    text_obj.textLine("2. Pergunta do dia:")
    c.drawText(text_obj)
    y -= 5.5 * mm
    c.setFont("Montserrat-Italic", 10.5)
    # simple wrap
    words = p2.split()
    line = ""
    max_w = right - x
    lines = []
    for w in words:
        test = (line + " " + w).strip()
        if pdfmetrics.stringWidth(test, "Montserrat-Italic", 10.5) > max_w:
            lines.append(line)
            line = w
        else:
            line = test
    if line:
        lines.append(line)
    for ln in lines:
        c.drawString(x, y, ln)
        y -= 5.2 * mm
    y -= 1 * mm
    y = writing_line(x, right, y); y -= 8 * mm
    y = writing_line(x, right, y); y -= 8 * mm

    y = section_label(x, right, y, "MINHA IDEIA HOJE  —  uma frase, mesmo que ainda não tenha certeza")
    y -= 8 * mm
    y = writing_line(x, right, y); y -= 8 * mm
    y = writing_line(x, right, y); y -= 8 * mm

    y = section_label(x, right, y, "SAÍDA  —  preencher antes de guardar o material, ao final da aula")
    y -= 6 * mm
    c.setFont("Montserrat", 10.5)
    c.drawString(x, y, "O que eu produzi/fiz hoje:")
    y -= 6 * mm
    y = writing_line(x, right, y); y -= 8 * mm
    y = writing_line(x, right, y); y -= 8 * mm

    c.setFont("Montserrat", 10.5)
    c.drawString(x, y, "Uma dúvida que ficou:")
    y -= 6 * mm
    y = writing_line(x, right, y); y -= 8 * mm
    y = writing_line(x, right, y)

    c.showPage()


def draw_cover():
    page_frame()
    c.setFont("Montserrat-Bold", 11)
    c.setFillColor(BLACK)
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = PAGE_H - BORDER_MARGIN - 11 * mm
    c.drawString(x, y, "Ensino Fundamental 2")
    logo_h = 11 * mm
    logo_w = logo_h * LOGO_ASPECT
    c.drawImage(logo_img, right - logo_w, y - 3 * mm, width=logo_w, height=logo_h,
                preserveAspectRatio=True, mask="auto")
    y -= 9 * mm
    c.setFont("Montserrat", 11)
    c.drawString(x, y, "Aluno(a): ")
    lw = pdfmetrics.stringWidth("Aluno(a): ", "Montserrat", 11)
    c.line(x + lw, y - 1, right, y - 1)
    y -= 8 * mm
    c.drawString(x, y, "Ano Escolar: ________   Turma: ________   Data: ________")
    y -= 4 * mm
    c.line(x, y, right, y)

    c.setFont("Montserrat-Bold", 30)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 15 * mm, "Diário do Empreendedor")
    c.setFont("Montserrat-Italic", 13)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 6 * mm, "Eletiva Start Up Nation — Colégio Israelita Brasileiro")

    notes = [
        "Este caderno acompanha você nas 17 aulas do semestre.",
        "Toda aula começa com a ENTRADA e termina com a SAÍDA — sempre sozinho e em silêncio.",
        "A linha “Minha ideia hoje” se repete em toda página — releia-a inteira na Aula 17",
        "e veja o quanto sua ideia evoluiu.",
    ]
    ny = PAGE_H / 2 - 15 * mm
    c.setFont("Montserrat", 10.5)
    for line in notes:
        c.drawCentredString(PAGE_W / 2, ny, line)
        ny -= 6 * mm

    c.showPage()


draw_cover()
for n, data, tema, p2 in aulas:
    draw_aula_page(n, data, tema, p2)

c.save()
print("PDF v2 gerado com sucesso")
