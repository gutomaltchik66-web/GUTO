# -*- coding: utf-8 -*-
"""
Diário do Empreendedor — cabeçalho padrão CIB (Ensino Fundamental 2),
replicando o modelo oficial extraído de CABEÇALHO EDITÁVEL EF2.docx e o
enquadramento de página (borda) extraído de PAUTA PEQUENA.pdf.

Cada página traz uma citação livre da Torá (Tanach, foco nos 5 livros
de Moisés), centralizada e enquadrada, seguida de duas perguntas: a
Pergunta 1 é sempre ligada ao trecho (diferente em cada aula) e a
Pergunta 2 é fixa em todas as 17 páginas: "O que eu aprendi na aula de
hoje?". A capa traz o título, o escudo do colégio e uma caixa grande
em branco para o aluno desenhar.
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

PERGUNTA_2_FIXA = "O que eu aprendi na aula de hoje?"

# Cada entrada: (n, data, tema, fonte, trecho, pergunta1_ligada_ao_trecho)
# Todas as citações são da Torá (Tanach, com foco nos 5 livros de Moisés).
aulas = [
    (1, "03/08", "Abertura: além do que você já sabe sobre Israel",
     "Gênesis 12:1",
     "“Sai-te da tua terra, e da tua parentela, e da casa de teu pai, para a terra que eu te mostrarei.”",
     "Abrão teve que partir para uma terra desconhecida, sem saber exatamente onde chegaria. O que você sente ao começar algo novo, sem saber onde vai dar?"),

    (2, "10/08", "Raízes históricas, sob uma nova ótica",
     "Êxodo 17:6",
     "“Eis que eu estarei ali diante de ti sobre a rocha em Horebe; e ferirás a rocha, e dela sairá água, para que o povo beba.”",
     "Moisés encontrou água onde parecia impossível, batendo numa pedra. Que “pedra” (obstáculo) você já viu virar solução, com a abordagem certa?"),

    (3, "17/08", "Chutzpah: da palavra à atitude empreendedora",
     "Gênesis 18:23-25",
     "“Destruirás também o justo com o ímpio? [...] Não fará justiça o Juiz de toda a terra?” — Abraão, questionando D'us sobre a destruição de Sodoma.",
     "Abraão teve coragem de questionar até D'us, pedindo justiça. Você acha que questionar uma autoridade pode ser um ato de respeito, e não de desrespeito? Por quê?"),

    (4, "24/08", "Tolerância ao fracasso",
     "Gênesis 32:25-29",
     "“E Jacó ficou só; e lutava com ele um homem, até que a alva subia. [...] Não te chamarás mais Jacó, mas Israel; pois lutaste com D'us e com os homens, e prevaleceste.”",
     "Jacó saiu machucado da luta, mas não desistiu até ser abençoado — e ganhou o nome Israel. Por que insistir mesmo “machucado” pode transformar quem você é?"),

    (5, "31/08", "O papel do Estado e do Exército",
     "Êxodo 18:21",
     "“Procura dentre o povo homens capazes [...] e põe estes sobre eles por chefes de mil, chefes de cem, chefes de cinquenta e chefes de dez.”",
     "Jetro ajudou Moisés a organizar o povo em grupos, com líderes definidos. Por que até o maior líder precisa de uma boa estrutura/instituição ao seu redor?"),

    (6, "14/09", "Estudos de caso: empresas que os alunos usam",
     "Números 13:17-18",
     "“Subi por aqui para a banda do sul, e subi à montanha; e vede a terra, que tal é.”",
     "Antes de agir, Moisés mandou espiar e estudar de perto a terra prometida. Por que observar de perto um exemplo real (como uma empresa) ajuda antes de criar algo novo?"),

    (7, "28/09", "Tikun olam + lançamento do desafio final",
     "Êxodo 3:9-10",
     "“E agora, eis que o clamor dos filhos de Israel chegou a mim [...] Vem, pois, agora, e enviar-te-ei a Faraó, para que tires do Egito o meu povo.”",
     "D'us chamou Moisés para agir agora, sem esperar mais. Por que agora é um bom momento para você começar seu próprio projeto?"),

    (8, "05/10", "Mapa de Empatia: entendendo o problema de verdade",
     "Levítico 19:18",
     "“Não te vingarás, nem guardarás ira [...]; mas amarás o teu próximo como a ti mesmo.”",
     "Amar o próximo como a si mesmo pede que você se coloque de verdade no lugar do outro. Como isso se conecta com a empatia que você praticou hoje?"),

    (9, "19/10", "Canvas do Projeto Pessoal: primeira ideia",
     "Gênesis 1:27",
     "“E criou D'us o homem à sua imagem; à imagem de D'us o criou; homem e mulher os criou.”",
     "Se cada pessoa é única, criada à imagem de D'us, por que sua ideia — mesmo parecida com outras — também pode ser única?"),

    (10, "26/10", "Protótipo: tirando a ideia do papel",
     "Êxodo 24:7",
     "“Tudo o que o Senhor tem dito faremos, e obedeceremos.”",
     "O povo disse “faremos” antes mesmo de entender tudo direito. Por que agir e testar pode ensinar mais do que só planejar?"),

    (11, "09/11", "Roteiro de Pitch: contando minha ideia em 2 min",
     "Êxodo 4:11-12",
     "“Quem fez a boca do homem? [...] Vai, pois, agora, e eu serei com a tua boca, e te ensinarei o que hás de falar.”",
     "Moisés tinha medo de não saber falar direito, e D'us prometeu as palavras certas. Como preparar bem o que vai dizer pode te dar mais confiança no pitch?"),

    (12, "16/11", "Ensaio geral + ajustes finais",
     "Deuteronômio 6:6-7",
     "“E estas palavras [...] as intimarás a teus filhos, e delas falarás assentado em tua casa, e andando pelo caminho, e deitando-te, e levantando-te.”",
     "A Torá manda repetir e ensinar as palavras o tempo todo, em qualquer lugar. Por que repetir o pitch várias vezes muda como você o apresenta?"),

    (13, "23/11", "PITCH DAY — Semana Avaliativa EF2",
     "Números 13:30",
     "“Subamos, subamos, e a possuiremos, pois totalmente poderemos com ela.” — Calebe",
     "Calebe disse isso mesmo com outros espiões com medo. De onde você tira coragem para apresentar hoje?"),

    (14, "30/11", "Devolutivas + Feira de Ideias",
     "Levítico 19:15",
     "“Não farás injustiça no juízo [...] com justiça julgarás o teu próximo.”",
     "A Torá pede para julgar com justiça, sem favorecer ninguém. Como isso ajuda a dar — e a receber — feedback de verdade hoje?"),

    (15, "07/12", "E depois do pitch? Da ideia ao negócio de verdade",
     "Gênesis 2:15",
     "“E tomou o Senhor D'us o homem, e pô-lo no jardim do Éden para o lavrar e o guardar.”",
     "O primeiro trabalho do ser humano foi cuidar de um jardim que continuaria crescendo. Que “jardim” você estaria cultivando com essa ideia, mesmo sem ver todo o resultado agora?"),

    (16, "14/12", "Banca de investidores (convidado ou simulação)",
     "Êxodo 18:19",
     "“Ouve agora a minha voz, e aconselhar-te-ei, e D'us seja contigo.”",
     "Jetro ofereceu um conselho de fora, e Moisés ouviu. Por que ouvir perguntas difíceis de uma banca pode fortalecer sua ideia, em vez de enfraquecê-la?"),

    (17, "21/12", "Encerramento do semestre",
     "Deuteronômio 8:2",
     "“E te lembrarás de todo o caminho pelo qual o Senhor teu D'us te guiou [...] para saber o que estava no teu coração.”",
     "A Torá pede para lembrar todo o caminho percorrido, não só o destino final. Olhando para trás nas páginas deste diário, o que você aprendeu sobre você mesmo?"),
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


def draw_wrapped(x, right, y, text, font, size, leading_mm):
    for ln in wrap_text(text, font, size, right - x):
        c.setFont(font, size)
        c.drawString(x, y, ln)
        y -= leading_mm * mm
    return y


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


def draw_aula_page(n, data, tema, fonte, trecho, pergunta1):
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

    # --- Pergunta 1 (ligada ao trecho) ---
    y -= 9 * mm
    c.setFont("Montserrat-Bold", 11)
    c.setFillColor(BLACK)
    c.drawString(x, y, "1)")
    y -= 6 * mm
    y = draw_wrapped(x, right, y, pergunta1, "Montserrat-Italic", 10.5, 5.2)
    y -= 1 * mm
    y = writing_line(x, right, y); y -= 8 * mm
    y = writing_line(x, right, y); y -= 8 * mm

    # --- Pergunta 2 (fixa) ---
    y -= 2 * mm
    c.setFont("Montserrat-Bold", 11)
    c.setFillColor(BLACK)
    c.drawString(x, y, f"2) {PERGUNTA_2_FIXA}")
    y -= 8 * mm
    for _ in range(4):
        y = writing_line(x, right, y); y -= 8 * mm

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

    # Caixa grande em branco (sem legenda)
    y -= 12 * mm
    box_top = y
    box_bottom = BORDER_MARGIN + 8 * mm
    c.setStrokeColor(BLACK)
    c.setLineWidth(0.8)
    c.rect(x, box_bottom, right - x, box_top - box_bottom, stroke=1, fill=0)

    c.showPage()


draw_cover()
for n, data, tema, fonte, trecho, pergunta1 in aulas:
    draw_aula_page(n, data, tema, fonte, trecho, pergunta1)

c.save()
print("PDF gerado com sucesso")
