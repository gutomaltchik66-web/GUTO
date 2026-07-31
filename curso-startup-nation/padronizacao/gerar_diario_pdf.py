# -*- coding: utf-8 -*-
"""
Diário do Empreendedor — cabeçalho padrão CIB (Ensino Fundamental 2),
replicando o modelo oficial extraído de CABEÇALHO EDITÁVEL EF2.docx e o
enquadramento de página (borda) extraído de PAUTA PEQUENA.pdf.

Cada página traz uma citação livre de fonte judaica diferente (Torá,
Neviim, Ketuvim, Mishná/Pirkei Avot ou Talmud), centralizada e
enquadrada, seguida de uma pergunta padrão ("O que eu aprendi na aula
de hoje?") e da linha contínua "Minha ideia hoje". A capa traz o
título, o escudo do colégio e uma caixa grande para o aluno desenhar.
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

ESCUDO_PATH = os.path.join(ASSETS, "cib-escudo.png")
escudo_img = ImageReader(ESCUDO_PATH)
ESCUDO_W_PX, ESCUDO_H_PX = escudo_img.getSize()
ESCUDO_ASPECT = ESCUDO_W_PX / ESCUDO_H_PX

PAGE_W, PAGE_H = A4
BORDER_MARGIN = 10 * mm     # page-frame border, like PAUTA PEQUENA
CONTENT_MARGIN = 16 * mm    # text content margin from page edge
BLACK = colors.black
GREY = colors.HexColor("#8C8C8C")
LIGHTGREY = colors.HexColor("#EDEDED")

PERGUNTA_PADRAO = "O que eu aprendi na aula de hoje?"

# Cada entrada: (n, data, tema, fonte, trecho)
aulas = [
    (1, "03/08", "Abertura: além do que você já sabe sobre Israel",
     "Pirkei Avot 2:21 (Rabi Tarfon)",
     "“Não te cabe completar a tarefa, mas também não estás livre para dela te eximir.”"),

    (2, "10/08", "Raízes históricas, sob uma nova ótica",
     "Isaías 35:1",
     "“O deserto e o lugar solitário se alegrarão; e o ermo exultará e florescerá como a rosa.”"),

    (3, "17/08", "Chutzpah: da palavra à atitude empreendedora",
     "Gênesis 18:23-25",
     "“Não farás isso... Não fará justiça o Juiz de toda a terra?” — Abraão, questionando D'us sobre a destruição de Sodoma."),

    (4, "24/08", "Tolerância ao fracasso",
     "Provérbios 24:16",
     "“Porque sete vezes cai o justo, e se levanta.”"),

    (5, "31/08", "O papel do Estado e do Exército",
     "Pirkei Avot 3:2 (Rabi Chanina)",
     "“Reza pelo bem-estar do governo, pois sem o temor a ele, um homem engoliria vivo o seu próximo.”"),

    (6, "14/09", "Estudos de caso: empresas que os alunos usam",
     "Pirkei Avot 4:1 (Ben Zoma)",
     "“Quem é sábio? Aquele que aprende com todo homem.”"),

    (7, "28/09", "Tikun olam + lançamento do desafio final",
     "Pirkei Avot 1:14 (Hillel)",
     "“Se eu não for por mim, quem será por mim? E quando eu for só por mim, o que sou eu? E se não agora, quando?”"),

    (8, "05/10", "Mapa de Empatia: entendendo o problema de verdade",
     "Talmud, Shabat 31a (Hillel)",
     "“O que é odioso para ti, não faças ao teu próximo — essa é toda a Torá; o resto é comentário.”"),

    (9, "19/10", "Canvas do Projeto Pessoal: primeira ideia",
     "Mishná, Sanhedrin 4:5",
     "“Um homem cunha muitas moedas com o mesmo selo, e todas são iguais entre si; mas o Rei dos reis cunhou todo ser humano com o selo de Adão, e nenhum se parece com outro.”"),

    (10, "26/10", "Protótipo: tirando a ideia do papel",
     "Pirkei Avot 1:17 (Shimon ben Gamliel)",
     "“Não o estudo é o principal, mas a ação.”"),

    (11, "09/11", "Roteiro de Pitch: contando minha ideia em 2 min",
     "Provérbios 18:21",
     "“A morte e a vida estão no poder da língua.”"),

    (12, "16/11", "Ensaio geral + ajustes finais",
     "Talmud, Chagigá 9b",
     "“Aquele que repete seu estudo cem vezes não se compara ao que o repete cento e uma vezes.”"),

    (13, "23/11", "PITCH DAY — Semana Avaliativa EF2",
     "Números 13:30 (Calebe)",
     "“Subamos, subamos, e a possuiremos, pois totalmente poderemos com ela.”"),

    (14, "30/11", "Devolutivas + Feira de Ideias",
     "Pirkei Avot 1:6 (Yehoshua ben Perachyah)",
     "“Julga toda pessoa favoravelmente.”"),

    (15, "07/12", "E depois do pitch? Da ideia ao negócio de verdade",
     "Talmud, Taanit 23a (Choni e a alfarrobeira)",
     "Um homem plantava uma alfarrobeira sabendo que não veria seus frutos: “Assim como meus antepassados plantaram para mim, eu planto para meus filhos.”"),

    (16, "14/12", "Banca de investidores (convidado ou simulação)",
     "Provérbios 15:22",
     "“Onde não há conselho, os projetos se frustram; mas com muitos conselheiros se confirmam.”"),

    (17, "21/12", "Encerramento do semestre",
     "Salmos 90:12",
     "“Ensina-nos a contar os nossos dias, de tal maneira que alcancemos coração sábio.”"),
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

    c.setFont("Montserrat-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(x, y, "Ensino Fundamental 2")

    logo_h = 11 * mm
    logo_w = logo_h * LOGO_ASPECT
    c.drawImage(logo_img, right - logo_w, y - 3 * mm, width=logo_w, height=logo_h,
                preserveAspectRatio=True, mask="auto")

    y -= 9 * mm
    c.setFont("Montserrat", 11)
    label = "Aluno(a): "
    c.drawString(x, y, label)
    label_w = pdfmetrics.stringWidth(label, "Montserrat", 11)
    c.setLineWidth(0.6)
    c.setStrokeColor(BLACK)
    c.line(x + label_w, y - 1, right, y - 1)

    y -= 8 * mm
    parts = [("Ano Escolar: ", "________"), ("   Turma: ", "________"), ("   Data: ", data_aula)]
    cx = x
    for label, value in parts:
        c.setFont("Montserrat", 11)
        c.drawString(cx, y, label)
        cx += pdfmetrics.stringWidth(label, "Montserrat", 11)
        c.setFont("Montserrat-Bold" if value != "________" else "Montserrat", 11)
        c.drawString(cx, y, value)
        cx += pdfmetrics.stringWidth(value, "Montserrat", 11)

    y -= 4 * mm
    c.setLineWidth(0.8)
    c.line(x, y, right, y)
    return y


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


def wrap_text(text, font, size, max_w):
    words = text.split()
    lines = []
    line = ""
    for w in words:
        test = (line + " " + w).strip()
        if pdfmetrics.stringWidth(test, font, size) > max_w:
            lines.append(line)
            line = w
        else:
            line = test
    if line:
        lines.append(line)
    return lines


def draw_citation_box(x, right, y, trecho, fonte):
    """Citação livre, centralizada, dentro de uma caixa enquadrada — sem rótulo."""
    inner_pad_x = 6 * mm
    inner_pad_y = 5 * mm
    text_w = (right - x) - 2 * inner_pad_x
    lines = wrap_text(trecho, "Montserrat-Italic", 12, text_w)
    line_h = 6 * mm
    box_h = inner_pad_y * 2 + len(lines) * line_h + 6 * mm  # + espaço para a fonte

    box_top = y
    box_bottom = y - box_h
    c.setStrokeColor(BLACK)
    c.setLineWidth(0.8)
    c.rect(x, box_bottom, right - x, box_h, stroke=1, fill=0)

    ty = box_top - inner_pad_y - 4 * mm
    center_x = (x + right) / 2
    c.setFillColor(BLACK)
    for ln in lines:
        c.setFont("Montserrat-Italic", 12)
        c.drawCentredString(center_x, ty, ln)
        ty -= line_h

    ty -= 1 * mm
    c.setFont("Montserrat-Bold", 9.5)
    c.setFillColor(GREY)
    c.drawCentredString(center_x, ty, f"— {fonte}")
    c.setFillColor(BLACK)

    return box_bottom


def draw_aula_page(n, data, tema, fonte, trecho):
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

    # --- Citação livre, centralizada e enquadrada (sem rótulo) ---
    y -= 10 * mm
    y = draw_citation_box(x, right, y, trecho, fonte)

    # --- Pergunta padrão do dia ---
    y -= 10 * mm
    c.setFont("Montserrat-Bold", 11)
    c.setFillColor(BLACK)
    c.drawString(x, y, PERGUNTA_PADRAO)
    y -= 8 * mm
    for _ in range(4):
        y = writing_line(x, right, y); y -= 8 * mm

    # --- Minha Ideia Hoje ---
    y -= 2 * mm
    y = section_label(x, right, y, "MINHA IDEIA HOJE  —  uma frase, mesmo que ainda não tenha certeza")
    y -= 8 * mm
    y = writing_line(x, right, y); y -= 8 * mm
    y = writing_line(x, right, y)

    c.showPage()


def draw_cover():
    page_frame()
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN

    # Cabeçalho oficial (compacto, no topo)
    y = PAGE_H - BORDER_MARGIN - 11 * mm
    c.setFont("Montserrat-Bold", 11)
    c.setFillColor(BLACK)
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

    # Escudo do colégio, grande e centralizado
    y -= 14 * mm
    escudo_h = 38 * mm
    escudo_w = escudo_h * ESCUDO_ASPECT
    c.drawImage(escudo_img, (PAGE_W - escudo_w) / 2, y - escudo_h, width=escudo_w, height=escudo_h,
                preserveAspectRatio=True, mask="auto")
    y -= escudo_h

    # Título
    y -= 14 * mm
    c.setFont("Montserrat-Bold", 28)
    c.setFillColor(BLACK)
    c.drawCentredString(PAGE_W / 2, y, "Diário do Empreendedor")
    y -= 9 * mm
    c.setFont("Montserrat-Italic", 13)
    c.drawCentredString(PAGE_W / 2, y, "Eletiva Start Up Nation — Colégio Israelita Brasileiro")

    # Caixa grande para desenhar
    y -= 12 * mm
    c.setFont("Montserrat-Bold", 11)
    c.drawCentredString(PAGE_W / 2, y, "Desenhe aqui a sua ideia (ou o que você quiser!)")
    y -= 6 * mm
    box_top = y
    box_bottom = BORDER_MARGIN + 8 * mm
    c.setStrokeColor(BLACK)
    c.setLineWidth(0.8)
    c.rect(x, box_bottom, right - x, box_top - box_bottom, stroke=1, fill=0)

    c.showPage()


draw_cover()
for n, data, tema, fonte, trecho in aulas:
    draw_aula_page(n, data, tema, fonte, trecho)

c.save()
print("PDF gerado com sucesso")
