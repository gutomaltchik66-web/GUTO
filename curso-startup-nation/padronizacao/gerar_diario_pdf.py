# -*- coding: utf-8 -*-
"""
Diário do Empreendedor — cabeçalho padrão CIB (Ensino Fundamental 2),
replicando o modelo oficial extraído de CABEÇALHO EDITÁVEL EF2.docx e o
enquadramento de página (borda) extraído de PAUTA PEQUENA.pdf.

Cada página traz uma citação livre da Torá (Tanach, foco nos 5 livros
de Moshé), centralizada e enquadrada, seguida de duas perguntas: a
Pergunta 1 é sempre ligada ao trecho (diferente em cada aula) e a
Pergunta 2 é fixa em todas as 15 páginas: "O que eu aprendi na aula de
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
from bidi.algorithm import get_display

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

pdfmetrics.registerFont(TTFont("Montserrat", os.path.join(ASSETS, "MontserratMedium-regular.ttf")))
pdfmetrics.registerFont(TTFont("Montserrat-Bold", os.path.join(ASSETS, "MontserratMedium-bold.ttf")))
pdfmetrics.registerFont(TTFont("Montserrat-Italic", os.path.join(ASSETS, "MontserratMedium-italic.ttf")))
pdfmetrics.registerFont(TTFont("Hebrew", os.path.join(ASSETS, "NotoSansHebrew-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Hebrew-Bold", os.path.join(ASSETS, "NotoSansHebrew-Bold.ttf")))

# Nome hebraico de cada um dos 5 livros da Torá, para exibir ao lado da referência.
LIVRO_HEBRAICO = {
    "Gênesis": "בְּרֵאשִׁית",
    "Êxodo": "שְׁמוֹת",
    "Levítico": "וַיִּקְרָא",
    "Números": "בְּמִדְבַּר",
    "Deuteronômio": "דְּבָרִים",
}

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

# Cada entrada: (n, tema, fonte, trecho, pergunta1_ligada_ao_trecho)
# Todas as citações são da Torá (Tanach, com foco nos 5 livros de Moshé).
aulas = [
    (1, "Abertura: além do que você já sabe sobre Israel",
     "Gênesis 12:1",
     "“Sai-te da tua terra, e da tua parentela, e da casa de teu pai, para a terra que eu te mostrarei.”",
     "Avraham teve que partir para uma terra desconhecida, sem saber exatamente onde chegaria. O que você sente ao começar algo novo, sem saber onde vai dar?"),

    (2, "Raízes históricas, sob uma nova ótica",
     "Êxodo 17:6",
     "“Eis que eu estarei ali diante de ti sobre a rocha em Horebe; e ferirás a rocha, e dela sairá água, para que o povo beba.”",
     "Moshé encontrou água onde parecia impossível, batendo numa pedra. Que “pedra” (obstáculo) você já viu virar solução, com a abordagem certa?"),

    (3, "Chutzpah: da palavra à atitude empreendedora",
     "Gênesis 18:23-25",
     "“Destruirás também o justo com o ímpio? [...] Não fará justiça o Juiz de toda a terra?” — Avraham, questionando D'us sobre a destruição de Sodoma.",
     "Avraham teve coragem de questionar até D'us, pedindo justiça. Você acha que questionar uma autoridade pode ser um ato de respeito, e não de desrespeito? Por quê?"),

    (4, "O papel do Estado e do Exército",
     "Êxodo 18:21",
     "“Procura dentre o povo homens capazes [...] e põe estes sobre eles por chefes de mil, chefes de cem, chefes de cinquenta e chefes de dez.”",
     "Jetro ajudou Moshé a organizar o povo em grupos, com líderes definidos. Por que até o maior líder precisa de uma boa estrutura/instituição ao seu redor?"),

    (5, "Tikun olam + lançamento do desafio final",
     "Êxodo 3:9-10",
     "“E agora, eis que o clamor dos filhos de Israel chegou a mim [...] Vem, pois, agora, e enviar-te-ei a Faraó, para que tires do Egito o meu povo.”",
     "D'us chamou Moshé para agir agora, sem esperar mais. Por que agora é um bom momento para você começar seu próprio projeto?"),

    (6, "Mapa de Empatia: entendendo o problema de verdade",
     "Levítico 19:18",
     "“Não te vingarás, nem guardarás ira [...]; mas amarás o teu próximo como a ti mesmo.”",
     "Amar o próximo como a si mesmo pede que você se coloque de verdade no lugar do outro. Como isso se conecta com a empatia que você praticou hoje?"),

    (7, "Canvas do Projeto Pessoal: primeira ideia",
     "Gênesis 1:27",
     "“E criou D'us o homem à sua imagem; à imagem de D'us o criou; homem e mulher os criou.”",
     "Se cada pessoa é única, criada à imagem de D'us, por que sua ideia — mesmo parecida com outras — também pode ser única?"),

    (8, "Protótipo: tirando a ideia do papel",
     "Êxodo 24:7",
     "“Tudo o que o Senhor tem dito faremos, e obedeceremos.”",
     "O povo disse “faremos” antes mesmo de entender tudo direito. Por que agir e testar pode ensinar mais do que só planejar?"),

    (9, "Roteiro de Pitch: contando minha ideia em 2 min",
     "Êxodo 4:11-12",
     "“Quem fez a boca do homem? [...] Vai, pois, agora, e eu serei com a tua boca, e te ensinarei o que hás de falar.”",
     "Moshé tinha medo de não saber falar direito, e D'us prometeu as palavras certas. Como preparar bem o que vai dizer pode te dar mais confiança no pitch?"),

    (10, "Ensaio geral + ajustes finais",
     "Deuteronômio 6:6-7",
     "“E estas palavras [...] as intimarás a teus filhos, e delas falarás assentado em tua casa, e andando pelo caminho, e deitando-te, e levantando-te.”",
     "A Torá manda repetir e ensinar as palavras o tempo todo, em qualquer lugar. Por que repetir o pitch várias vezes muda como você o apresenta?"),

    (11, "PITCH DAY — Semana Avaliativa EF2",
     "Números 13:30",
     "“Subamos, subamos, e a possuiremos, pois totalmente poderemos com ela.” — Calebe",
     "Calebe disse isso mesmo com outros espiões com medo. De onde você tira coragem para apresentar hoje?"),

    (12, "Devolutivas + Feira de Ideias",
     "Levítico 19:15",
     "“Não farás injustiça no juízo [...] com justiça julgarás o teu próximo.”",
     "A Torá pede para julgar com justiça, sem favorecer ninguém. Como isso ajuda a dar — e a receber — feedback de verdade hoje?"),

    (13, "E depois do pitch? Da ideia ao negócio de verdade",
     "Gênesis 2:15",
     "“E tomou o Senhor D'us o homem, e pô-lo no jardim do Éden para o lavrar e o guardar.”",
     "O primeiro trabalho do ser humano foi cuidar de um jardim que continuaria crescendo. Que “jardim” você estaria cultivando com essa ideia, mesmo sem ver todo o resultado agora?"),

    (14, "Banca de investidores (convidado ou simulação)",
     "Êxodo 18:19",
     "“Ouve agora a minha voz, e aconselhar-te-ei, e D'us seja contigo.”",
     "Jetro ofereceu um conselho de fora, e Moshé ouviu. Por que ouvir perguntas difíceis de uma banca pode fortalecer sua ideia, em vez de enfraquecê-la?"),

    (15, "Encerramento do semestre",
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


def cib_header():
    """Replicates the official 'Cabeçalho Editável EF2' block. O campo "Data"
    fica em branco (não pré-preenchido), já que as datas das aulas podem
    mudar ao longo do semestre."""
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
    parts = [("Ano Escolar: ", "________"), ("   Turma: ", "________"), ("   Data: ", "________")]
    cx = x
    for label, value in parts:
        c.setFont("Montserrat", 11)
        c.drawString(cx, y, label)
        cx += pdfmetrics.stringWidth(label, "Montserrat", 11)
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


def wrap_with_first_line_offset(text, font, size, full_width, first_line_width):
    """Quebra de linha em que a 1ª linha tem menos espaço (por causa do rótulo
    inline, ex: "1) ") e as linhas seguintes usam a largura cheia."""
    words = text.split()
    lines = []
    line = ""
    max_w = first_line_width
    for w in words:
        test = (line + " " + w).strip()
        if pdfmetrics.stringWidth(test, font, size) > max_w:
            if line:
                lines.append(line)
            line = w
            max_w = full_width
        else:
            line = test
    if line:
        lines.append(line)
    return lines


def draw_numbered_question(x, right, y, number, text, leading_mm=5.2):
    """Desenha "N) texto..." com o número na mesma linha do início da pergunta."""
    label = f"{number}) "
    label_w = pdfmetrics.stringWidth(label, "Montserrat-Bold", 11)
    full_w = right - x
    first_w = full_w - label_w
    lines = wrap_with_first_line_offset(text, "Montserrat-Italic", 10.5, full_w, first_w)

    c.setFont("Montserrat-Bold", 11)
    c.setFillColor(BLACK)
    c.drawString(x, y, label)
    c.setFont("Montserrat-Italic", 10.5)
    if lines:
        c.drawString(x + label_w, y, lines[0])
    y -= leading_mm * mm
    for ln in lines[1:]:
        c.setFont("Montserrat-Italic", 10.5)
        c.drawString(x, y, ln)
        y -= leading_mm * mm
    return y


def draw_centered_segments(center_x, y, segments):
    """segments: lista de (texto, fonte, tamanho, cor). Centraliza o conjunto
    todo, tratando texto hebraico (fonte começando com "Hebrew") com bidi."""
    total_w = sum(pdfmetrics.stringWidth(t, f, s) for (t, f, s, _col) in segments)
    cx = center_x - total_w / 2
    for t, f, s, col in segments:
        c.setFont(f, s)
        c.setFillColor(col)
        draw_t = get_display(t) if f.startswith("Hebrew") else t
        c.drawString(cx, y, draw_t)
        cx += pdfmetrics.stringWidth(t, f, s)
    c.setFillColor(BLACK)


def draw_citation_box(x, right, y, trecho, fonte):
    """Citação livre, centralizada, dentro de uma caixa enquadrada — sem rótulo.
    A referência (fonte) traz o nome do livro em português e, ao lado, em
    hebraico (ex: "Gênesis בְּרֵאשִׁית 12:1")."""
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
    livro, _, resto = fonte.partition(" ")
    hebraico = LIVRO_HEBRAICO.get(livro, "")
    segments = [("— ", "Montserrat-Bold", 9.5, GREY), (livro, "Montserrat-Bold", 9.5, GREY)]
    if hebraico:
        # Espaços ficam em segmentos próprios (fonte latina), nunca dentro da
        # string hebraica — presos ali, o bidi os reordena para o lado errado
        # e "cola" o texto seguinte no trecho em hebraico.
        segments.append(("  ", "Montserrat-Bold", 9.5, GREY))
        segments.append((hebraico, "Hebrew-Bold", 10.5, GREY))
        segments.append(("  ", "Montserrat-Bold", 9.5, GREY))
    else:
        segments.append((" ", "Montserrat-Bold", 9.5, GREY))
    segments.append((resto, "Montserrat-Bold", 9.5, GREY))
    draw_centered_segments(center_x, ty, segments)
    c.setFillColor(BLACK)

    return box_bottom


def draw_aula_page(n, tema, fonte, trecho, pergunta1):
    page_frame()
    x = CONTENT_MARGIN
    right = PAGE_W - CONTENT_MARGIN
    y = cib_header()

    y -= 8 * mm
    c.setFont("Montserrat-Bold", 12)
    c.setFillColor(BLACK)
    c.drawString(x, y, f"Aula Nº {n}")
    aula_label_w = pdfmetrics.stringWidth(f"Aula Nº {n}   ", "Montserrat-Bold", 12)
    c.setFont("Montserrat-Italic", 12)
    c.drawString(x + aula_label_w, y, f"{tema}.")

    # --- Citação livre, centralizada e enquadrada (sem rótulo) ---
    y -= 10 * mm
    y = draw_citation_box(x, right, y, trecho, fonte)

    # --- Pergunta 1 (ligada ao trecho) — número na mesma linha do texto ---
    y -= 9 * mm
    y = draw_numbered_question(x, right, y, 1, pergunta1)
    y -= 1 * mm
    for _ in range(5):
        y = writing_line(x, right, y); y -= 8 * mm

    # --- Pergunta 2 (fixa) ---
    y -= 2 * mm
    c.setFont("Montserrat-Bold", 11)
    c.setFillColor(BLACK)
    c.drawString(x, y, f"2) {PERGUNTA_2_FIXA}")
    y -= 8 * mm
    for _ in range(5):
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
    c.drawCentredString(PAGE_W / 2, y, "Eletiva StartUp Nation")
    y -= 6.5 * mm
    c.drawCentredString(PAGE_W / 2, y, "Colégio Israelita Brasileiro")

    # Caixa grande em branco (sem legenda)
    y -= 12 * mm
    box_top = y
    box_bottom = BORDER_MARGIN + 8 * mm
    c.setStrokeColor(BLACK)
    c.setLineWidth(0.8)
    c.rect(x, box_bottom, right - x, box_top - box_bottom, stroke=1, fill=0)

    c.showPage()


draw_cover()
for n, tema, fonte, trecho, pergunta1 in aulas:
    draw_aula_page(n, tema, fonte, trecho, pergunta1)

c.save()
print("PDF gerado com sucesso")
