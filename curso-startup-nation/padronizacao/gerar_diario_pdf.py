# -*- coding: utf-8 -*-
"""
Diário do Empreendedor — cabeçalho padrão CIB (Ensino Fundamental 2),
replicando o modelo oficial extraído de CABEÇALHO EDITÁVEL EF2.docx e o
enquadramento de página (borda) extraído de PAUTA PEQUENA.pdf.

Cada página traz um trecho de fonte judaica diferente (Torá, Neviim,
Ketuvim, Mishná/Pirkei Avot ou Talmud) e duas "Questões do Dia" — uma
ligada ao trecho, outra ao tema da aula — além da linha contínua
"Minha ideia hoje".
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

# Cada entrada: (n, data, tema, fonte, trecho, q1_ligada_ao_trecho, q2_tema_do_dia)
aulas = [
    (1, "03/08", "Abertura: além do que você já sabe sobre Israel",
     "Pirkei Avot 2:21 (Rabi Tarfon)",
     "“Não te cabe completar a tarefa, mas também não estás livre para dela te eximir.”",
     "O Rabino Tarfon diz que não precisamos terminar uma tarefa grande sozinhos, mas também não podemos deixar de começar. Que “tarefa grande” você imagina que vai construir neste semestre?",
     "Antes de começar: em uma frase, o que você já sabia sobre Israel?"),

    (2, "10/08", "Raízes históricas, sob uma nova ótica",
     "Isaías 35:1",
     "“O deserto e o lugar solitário se alegrarão; e o ermo exultará e florescerá como a rosa.”",
     "Isaías imaginou o deserto florescendo — e Israel tornou essa imagem realidade com tecnologia de irrigação. Que “deserto” (falta de algo) você já viu alguém transformar em oportunidade?",
     "O que você faria se não tivesse água, dinheiro ou tempo suficiente para algo que precisa muito?"),

    (3, "17/08", "Chutzpah: da palavra à atitude empreendedora",
     "Gênesis 18:23-25",
     "“Não farás isso... Não fará justiça o Juiz de toda a terra?” — Abraão, questionando D'us sobre a destruição de Sodoma.",
     "Abraão teve coragem de questionar até D'us, pedindo justiça. Você acha que questionar uma autoridade pode ser um ato de respeito, e não de desrespeito? Por quê?",
     "Você já teve uma ideia que achava “ousada demais” e não contou pra ninguém? Qual?"),

    (4, "24/08", "Tolerância ao fracasso",
     "Provérbios 24:16",
     "“Porque sete vezes cai o justo, e se levanta.”",
     "Provérbios diz que o justo cai sete vezes e se levanta. Qual foi a última vez que você “caiu” e conseguiu se levantar?",
     "O que você sente quando erra alguma coisa na frente dos outros?"),

    (5, "31/08", "O papel do Estado e do Exército",
     "Pirkei Avot 3:2 (Rabi Chanina)",
     "“Reza pelo bem-estar do governo, pois sem o temor a ele, um homem engoliria vivo o seu próximo.”",
     "Rabi Chanina ensinava que devemos torcer pelo bem-estar do governo, porque as instituições nos protegem do caos. Você concorda que instituições (governo, escola, exército) são necessárias para a sociedade funcionar bem? Por quê?",
     "Você acha que o governo deveria ajudar jovens com ideias de negócio? Por quê?"),

    (6, "14/09", "Estudos de caso: empresas que os alunos usam",
     "Pirkei Avot 4:1 (Ben Zoma)",
     "“Quem é sábio? Aquele que aprende com todo homem.”",
     "Ben Zoma dizia que sábio é quem aprende com qualquer pessoa. O que você pode aprender observando uma empresa, mesmo sem ser dono dela?",
     "Qual desses produtos (Waze, Wix, Mobileye...) você já usou? Como seria sua rotina sem ele?"),

    (7, "28/09", "Tikun olam + lançamento do desafio final",
     "Pirkei Avot 1:14 (Hillel)",
     "“Se eu não for por mim, quem será por mim? E quando eu for só por mim, o que sou eu? E se não agora, quando?”",
     "Hillel pergunta “se não agora, quando?”. Por que agora é um bom momento para você começar seu próprio projeto?",
     "Você prefere criar algo que dá lucro, ou algo que ajuda alguém, mesmo sem ganhar dinheiro com isso? Por quê?"),

    (8, "05/10", "Mapa de Empatia: entendendo o problema de verdade",
     "Talmud, Shabat 31a (Hillel)",
     "“O que é odioso para ti, não faças ao teu próximo — essa é toda a Torá; o resto é comentário.”",
     "Hillel resumiu toda a Torá nessa frase. Como ela se conecta com se colocar no lugar de outra pessoa (empatia)?",
     "Pense em alguém (colega, família, vizinho) que sofre com o problema que você quer resolver. Quem é essa pessoa?"),

    (9, "19/10", "Canvas do Projeto Pessoal: primeira ideia",
     "Mishná, Sanhedrin 4:5",
     "“Um homem cunha muitas moedas com o mesmo selo, e todas são iguais entre si; mas o Rei dos reis cunhou todo ser humano com o selo de Adão, e nenhum se parece com outro.”",
     "Cada pessoa é única, mesmo “cunhada com o mesmo selo”. Por que sua ideia, mesmo parecida com outras, pode ser única?",
     "Se você pudesse resolver o problema do seu Mapa de Empatia com uma varinha mágica, o que aconteceria?"),

    (10, "26/10", "Protótipo: tirando a ideia do papel",
     "Pirkei Avot 1:17 (Shimon ben Gamliel)",
     "“Não o estudo é o principal, mas a ação.”",
     "Se não é o estudo, mas a ação, o que é principal — por que só pensar numa ideia não é suficiente, é preciso construir algo?",
     "Se você tivesse que mostrar sua ideia sem falar nenhuma palavra, como faria?"),

    (11, "09/11", "Roteiro de Pitch: contando minha ideia em 2 min",
     "Provérbios 18:21",
     "“A morte e a vida estão no poder da língua.”",
     "Provérbios diz que a língua tem poder sobre a vida e a morte. Como as palavras certas (ou erradas) podem definir o sucesso do seu pitch?",
     "Se você tivesse só 2 minutos para convencer alguém a apoiar sua ideia, qual seria a primeira frase que diria?"),

    (12, "16/11", "Ensaio geral + ajustes finais",
     "Talmud, Chagigá 9b",
     "“Aquele que repete seu estudo cem vezes não se compara ao que o repete cento e uma vezes.”",
     "O Talmud valoriza quem ensaia mais uma vez. Por que ensaiar de novo pode fazer toda diferença no seu pitch?",
     "O que ainda te deixa nervoso(a) sobre apresentar seu pitch? O que pode te ajudar a ficar mais tranquilo(a)?"),

    (13, "23/11", "PITCH DAY — Semana Avaliativa EF2",
     "Números 13:30 (Calebe)",
     "“Subamos, subamos, e a possuiremos, pois totalmente poderemos com ela.”",
     "Calebe disse isso mesmo com outros espiões com medo. De onde você tira coragem para apresentar hoje?",
     "Em uma palavra, como você está se sentindo antes de apresentar hoje?"),

    (14, "30/11", "Devolutivas + Feira de Ideias",
     "Pirkei Avot 1:6 (Yehoshua ben Perachyah)",
     "“Julga toda pessoa favoravelmente.”",
     "Como julgar favoravelmente pode te ajudar a dar — e a receber — feedback hoje na Feira de Ideias?",
     "O que você espera ouvir hoje sobre o seu pitch?"),

    (15, "07/12", "E depois do pitch? Da ideia ao negócio de verdade",
     "Talmud, Taanit 23a (Choni e a alfarrobeira)",
     "Um homem plantava uma alfarrobeira sabendo que não veria seus frutos: “Assim como meus antepassados plantaram para mim, eu planto para meus filhos.”",
     "Que “árvore” você estaria plantando com essa ideia, mesmo sem ver todo o resultado agora?",
     "Você acha que sua ideia poderia continuar existindo depois do fim do semestre? O que precisaria acontecer?"),

    (16, "14/12", "Banca de investidores (convidado ou simulação)",
     "Provérbios 15:22",
     "“Onde não há conselho, os projetos se frustram; mas com muitos conselheiros se confirmam.”",
     "Por que ouvir perguntas difíceis de uma banca pode fortalecer sua ideia, em vez de enfraquecê-la?",
     "Se um investidor fizesse só uma pergunta sobre sua ideia, qual você tem mais medo que seja?"),

    (17, "21/12", "Encerramento do semestre",
     "Salmos 90:12",
     "“Ensina-nos a contar os nossos dias, de tal maneira que alcancemos coração sábio.”",
     "Olhando para trás nas páginas deste diário, o que você aprendeu sobre você mesmo?",
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


def draw_wrapped(x, right, y, text, font, size, leading_mm):
    for ln in wrap_text(text, font, size, right - x):
        c.setFont(font, size)
        c.drawString(x, y, ln)
        y -= leading_mm * mm
    return y


def draw_aula_page(n, data, tema, fonte, trecho, q1, q2):
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

    # --- Trecho da Tradição Judaica ---
    y -= 9 * mm
    y = section_label(x, right, y, "TRECHO DA TRADIÇÃO JUDAICA")
    y -= 6 * mm
    y = draw_wrapped(x, right, y, trecho, "Montserrat-Italic", 11, 5.6)
    y -= 1 * mm
    c.setFont("Montserrat-Bold", 9.5)
    c.setFillColor(GREY)
    c.drawString(x, y, f"— {fonte}")
    c.setFillColor(BLACK)
    y -= 7 * mm

    # --- Questões do Dia ---
    y = section_label(x, right, y, "QUESTÕES DO DIA")
    y -= 6 * mm
    c.setFont("Montserrat", 10.5)
    c.drawString(x, y, "1. Ligada ao trecho acima:")
    y -= 5.4 * mm
    y = draw_wrapped(x, right, y, q1, "Montserrat-Italic", 10.5, 5.2)
    y -= 1 * mm
    y = writing_line(x, right, y); y -= 7 * mm
    y = writing_line(x, right, y); y -= 8 * mm

    c.setFont("Montserrat", 10.5)
    c.drawString(x, y, "2. Sobre o tema de hoje:")
    y -= 5.4 * mm
    y = draw_wrapped(x, right, y, q2, "Montserrat-Italic", 10.5, 5.2)
    y -= 1 * mm
    y = writing_line(x, right, y); y -= 7 * mm
    y = writing_line(x, right, y); y -= 8 * mm

    # --- Minha Ideia Hoje ---
    y = section_label(x, right, y, "MINHA IDEIA HOJE  —  uma frase, mesmo que ainda não tenha certeza")
    y -= 8 * mm
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
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 20 * mm, "Diário do Empreendedor")
    c.setFont("Montserrat-Italic", 13)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 11 * mm, "Eletiva Start Up Nation — Colégio Israelita Brasileiro")

    notes = [
        "Este caderno acompanha você nas 17 aulas do semestre.",
        "Toda aula começa com um trecho da tradição judaica e duas Questões do Dia.",
        "A linha “Minha ideia hoje” se repete em toda página — releia-a inteira na Aula 17",
        "e veja o quanto sua ideia evoluiu.",
    ]
    ny = PAGE_H / 2 - 4 * mm
    c.setFont("Montserrat", 10.5)
    for line in notes:
        c.drawCentredString(PAGE_W / 2, ny, line)
        ny -= 6 * mm

    c.showPage()


draw_cover()
for n, data, tema, fonte, trecho, q1, q2 in aulas:
    draw_aula_page(n, data, tema, fonte, trecho, q1, q2)

c.save()
print("PDF gerado com sucesso")
