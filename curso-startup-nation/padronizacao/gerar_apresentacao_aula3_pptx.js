// Apresentação de slides — Aula 3 (StartUp Nation, CIB)
// Dá apoio visual ao roteiro: reenquadrar chutzpah como atitude (não só
// palavra), explicar chevruta e beit midrash, e mostrar a mecânica do
// rodízio em duplas que os alunos vão fazer com as fichas de
// ferramentas/fichas-produtos-israelenses.md.
//
// Não repete o conteúdo das fichas (cada dupla recebe uma delas na hora);
// o deck é só o pano de fundo conceitual da aula.

const pptxgen = require("pptxgenjs");
const {
  NAVY, TERRACOTTA, INK, INK_SOFT, ICE, ICE_MUTED, WHITE,
  FONT_DISPLAY, FONT_BODY, SW, SH, MARGIN,
  eyebrow, cibLogo, dotCluster, statColumn, imagePlaceholder,
} = require("./apresentacao_base");

const HERE = __dirname;

// ---- setup --------------------------------------------------------------
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";

// ---- Slide 1: título -------------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  cibLogo(slide, true);
  eyebrow(slide, "Ensino Fundamental 2 · Eletiva StartUp Nation · Aula 3");
  slide.addText("Chutzpah: da palavra à atitude empreendedora", {
    x: MARGIN, y: 2.3, w: 7.0, h: 1.7,
    fontFace: FONT_DISPLAY, fontSize: 34, bold: true, color: WHITE, margin: 0,
  });
  slide.addText("A audácia de questionar, discordar e propor, aplicada a decisões de negócio reais", {
    x: MARGIN, y: 4.0, w: 6.8, h: 1.1,
    fontFace: FONT_BODY, fontSize: 18, color: ICE, margin: 0, lineSpacingMultiple: 1.25,
  });
  slide.addText("Colégio Israelita Brasileiro", {
    x: MARGIN, y: SH - 0.62, w: 6, h: 0.35,
    fontFace: FONT_BODY, fontSize: 11, color: ICE_MUTED, margin: 0,
  });
  imagePlaceholder(slide, 8.3, 1.3, 4.13, 4.9, {
    dark: true,
    label: "Espaço para imagem",
    caption: "Sugestão: foto representando questionamento ou debate (ex: uma pessoa levantando a mão).",
  });
}

// ---- Slide 2: o que é chutzpah ---------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  cibLogo(slide, false);
  eyebrow(slide, "Reenquadrando o que vocês já sabem", { color: TERRACOTTA });
  slide.addText("Chutzpah não é só uma palavra", {
    x: MARGIN, y: 0.95, w: 10.8, h: 0.8,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: INK, margin: 0,
  });
  slide.addText("חוצפה", {
    x: MARGIN, y: 1.95, w: 6.4, h: 0.9,
    fontFace: FONT_DISPLAY, fontSize: 40, bold: true, color: TERRACOTTA, margin: 0,
  });
  slide.addText(
    "A audácia de questionar quem manda e de romper hierarquias quando algo parece errado, mesmo correndo risco.",
    {
      x: MARGIN, y: 2.95, w: 6.4, h: 1.1,
      fontFace: FONT_BODY, fontSize: 16, color: INK, margin: 0, lineSpacingMultiple: 1.3,
    }
  );
  slide.addShape("roundRect", {
    x: MARGIN, y: 4.25, w: 6.4, h: 1.5, rectRadius: 0.08,
    fill: { color: "FBEEE0" }, line: { type: "none" },
  });
  slide.addText(
    "Exemplo: no exército israelense, um soldado pode questionar a ordem de um general se achar que está errada.",
    {
      x: MARGIN + 0.25, y: 4.25, w: 5.9, h: 1.5,
      fontFace: FONT_BODY, fontSize: 13.5, bold: true, color: "8A4E17", margin: 0,
      valign: "middle", lineSpacingMultiple: 1.25,
    }
  );
  imagePlaceholder(slide, 7.9, 1.95, 4.53, 3.8, {
    label: "Espaço para imagem",
    caption: "Sugestão: foto ou ilustração ligada ao exemplo do exército, ou outro caso de chutzpah conhecido pela turma.",
  });
}

// ---- Slide 3: chevruta e beit midrash ---------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  dotCluster(slide, 11.6, 6.1);
  cibLogo(slide, true);
  eyebrow(slide, "De onde vem essa atitude", { color: TERRACOTTA });
  slide.addText("Uma tradição de perguntar e discordar", {
    x: MARGIN, y: 0.95, w: 11, h: 0.85,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: WHITE, margin: 0,
  });

  const colW = (SW - 2 * MARGIN - 1.0) / 2;
  const xs = [MARGIN, MARGIN + colW + 1.0];
  const conceitos = [
    ["Chevruta", "Estudo em duplas: aprender debatendo e discordando com o colega, não decorando sozinho."],
    ["Beit midrash", "\"Casa de estudo\": o lugar onde essa forma de aprender, perguntando e questionando, acontece."],
  ];
  conceitos.forEach(([titulo, desc], i) => {
    const x = xs[i];
    slide.addText(titulo, {
      x, y: 2.4, w: colW, h: 0.7,
      fontFace: FONT_DISPLAY, fontSize: 26, bold: true, color: TERRACOTTA, margin: 0,
    });
    slide.addText(desc, {
      x, y: 3.15, w: colW, h: 1.6,
      fontFace: FONT_BODY, fontSize: 14.5, color: ICE, margin: 0,
      valign: "top", lineSpacingMultiple: 1.3,
    });
  });

  slide.addText(
    "É exatamente esse método que vamos usar agora: aprender é perguntar, não decorar.",
    {
      x: MARGIN, y: 5.6, w: 10.8, h: 0.9,
      fontFace: FONT_DISPLAY, fontSize: 17, italic: true, color: WHITE, margin: 0, lineSpacingMultiple: 1.25,
    }
  );
}

// ---- Slide 4: mecânica do rodízio -------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  cibLogo(slide, false);
  eyebrow(slide, "Como funciona agora", { color: TERRACOTTA });
  slide.addText("Chevruta em rodízio: 3 fichas, 3 perguntas", {
    x: MARGIN, y: 0.95, w: 11, h: 0.85,
    fontFace: FONT_DISPLAY, fontSize: 30, bold: true, color: INK, margin: 0,
  });
  slide.addText(
    "Em dupla, cada rodada recebe uma ficha diferente de produto israelense (ferramentas/fichas-produtos-israelenses.md). 8 minutos por rodada, para debater e responder às 3 perguntas abaixo.",
    {
      x: MARGIN, y: 1.85, w: 10.8, h: 0.7,
      fontFace: FONT_BODY, fontSize: 14, color: INK_SOFT, margin: 0, lineSpacingMultiple: 1.25,
    }
  );

  const perguntas = [
    ["1", "O que essa ideia tem de chutzpah?"],
    ["2", "Que regra ou hábito ela quebrou?"],
    ["3", "Você teria coragem de propor isso?"],
  ];
  const colW = (SW - 2 * MARGIN - 1.0) / 3;
  const xs = [MARGIN, MARGIN + colW + 0.5, MARGIN + 2 * (colW + 0.5)];
  perguntas.forEach(([num, texto], i) => {
    const x = xs[i];
    slide.addShape("ellipse", {
      x, y: 3.0, w: 0.7, h: 0.7,
      fill: { color: TERRACOTTA }, line: { type: "none" },
    });
    slide.addText(num, {
      x, y: 3.0, w: 0.7, h: 0.7, align: "center", valign: "middle",
      fontFace: FONT_DISPLAY, fontSize: 24, bold: true, color: NAVY, margin: 0,
    });
    slide.addText(texto, {
      x, y: 3.9, w: colW, h: 1.2,
      fontFace: FONT_DISPLAY, fontSize: 17, bold: true, color: INK, margin: 0,
      lineSpacingMultiple: 1.2,
    });
  });

  slide.addText("Ao final: cada aluno passa por 3 fichas diferentes, em 3 duplas diferentes.", {
    x: MARGIN, y: 5.7, w: 10.8, h: 0.5,
    fontFace: FONT_BODY, fontSize: 13, italic: true, color: INK_SOFT, margin: 0,
  });
}

// ---- Slide 5: fechamento -----------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  dotCluster(slide, 11.6, 6.4, { dots: [[0, 0, 0.9, 20], [0.9, 0.3, 0.4, 28], [-0.6, 0.6, 0.3, 26]] });
  cibLogo(slide, true);
  eyebrow(slide, "Guarde essa pergunta", { color: TERRACOTTA });
  slide.addText("Uma ideia que você achou ousada demais", {
    x: MARGIN, y: 0.95, w: 11, h: 0.85,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: WHITE, margin: 0,
  });

  slide.addShape("roundRect", {
    x: MARGIN, y: 2.35, w: SW - 2 * MARGIN, h: 1.7, rectRadius: 0.08,
    fill: { color: "1E2F52" }, line: { type: "none" },
  });
  slide.addText(
    "Você já teve uma ideia que achava \"ousada demais\" e não contou pra ninguém? Qual?",
    {
      x: MARGIN + 0.4, y: 2.35, w: SW - 2 * MARGIN - 0.8, h: 1.7,
      fontFace: FONT_DISPLAY, fontSize: 22, italic: true, bold: true, color: WHITE,
      margin: 0, valign: "middle", lineSpacingMultiple: 1.25,
    }
  );

  slide.addText(
    "Anote num cartão avulso e guarde: essa reflexão volta direto no Canvas do seu projeto pessoal, na Aula 9.",
    {
      x: MARGIN, y: 4.4, w: 10.8, h: 0.7,
      fontFace: FONT_BODY, fontSize: 15, color: ICE, margin: 0, lineSpacingMultiple: 1.3,
    }
  );
}

const OUT = require("path").join(HERE, "Aula 3 - Apresentacao.pptx");
pres.writeFile({ fileName: OUT }).then(() => {
  console.log("PPTX gerado com sucesso:", OUT);
});
