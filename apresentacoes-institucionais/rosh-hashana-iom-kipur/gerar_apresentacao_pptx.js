// Apresentação institucional do CIB para o encontro virtual de escolas:
// propostas e vivências do colégio em Rosh Hashaná e Iom Kipur.
//
// Reaproveita a identidade visual do CIB (navy + terracota, logo do
// colégio) já usada nas apresentações da eletiva StartUp Nation, mas o
// conteúdo aqui não é do curso, é institucional.
//
// Conteúdo relatado por Morá Lu (troca de cartões, fábrica de cartões da
// Kitá Alef, música "One Day") e pelo coordenador Felipe (bonecos de
// argila na Reunião Geral de professores).

const pptxgen = require("pptxgenjs");
const {
  NAVY, TERRACOTTA, INK, INK_SOFT, ICE, ICE_MUTED, WHITE,
  FONT_DISPLAY, FONT_BODY, SW, SH, MARGIN,
  eyebrow, cibLogo, dotCluster,
} = require("../../curso-startup-nation/padronizacao/apresentacao_base");

const HERE = __dirname;

// ---- setup --------------------------------------------------------------
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";

// ---- Slide 1: título -------------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  dotCluster(slide, 11.6, 6.1);
  cibLogo(slide, true);
  eyebrow(slide, "Colégio Israelita Brasileiro · Encontro virtual de escolas");
  slide.addText("Rosh Hashaná e Iom Kipur no CIB", {
    x: MARGIN, y: 2.4, w: 10.5, h: 1.5,
    fontFace: FONT_DISPLAY, fontSize: 40, bold: true, color: WHITE, margin: 0,
  });
  slide.addText("Propostas e vivências do nosso colégio, para compartilhar com outras escolas", {
    x: MARGIN, y: 3.85, w: 9.5, h: 0.9,
    fontFace: FONT_BODY, fontSize: 19, color: ICE, margin: 0, lineSpacingMultiple: 1.25,
  });
  slide.addText("Colégio Israelita Brasileiro", {
    x: MARGIN, y: SH - 0.62, w: 6, h: 0.35,
    fontFace: FONT_BODY, fontSize: 11, color: ICE_MUTED, margin: 0,
  });
}

// ---- Slide 2: com os alunos --------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  cibLogo(slide, false);
  eyebrow(slide, "Com os alunos", { color: TERRACOTTA });
  slide.addText("Celebrando em comunidade, entre turmas", {
    x: MARGIN, y: 0.95, w: 11, h: 0.8,
    fontFace: FONT_DISPLAY, fontSize: 30, bold: true, color: INK, margin: 0,
  });

  const itens = [
    ["Troca de cartões", "Todos os anos, os alunos trocam cartões de brachot (bênçãos) entre as turmas do colégio."],
    ["Fábrica de cartões da Kitá Alef", "Os alunos do 1º ano confeccionaram e venderam cartões para famílias e amigos. Com a renda arrecadada, o colégio comprou brinquedos e doou ao Lar Anne Frank."],
    ["\"One Day\", de Matisyahu", "O colégio inteiro se reúne e canta essa música juntos, em comunidade."],
  ];
  const colW = (SW - 2 * MARGIN - 1.0) / 3;
  const xs = [MARGIN, MARGIN + colW + 0.5, MARGIN + 2 * (colW + 0.5)];
  itens.forEach(([titulo, desc], i) => {
    const x = xs[i];
    slide.addShape("ellipse", {
      x, y: 2.15, w: 0.7, h: 0.7,
      fill: { color: TERRACOTTA }, line: { type: "none" },
    });
    slide.addText(String(i + 1), {
      x, y: 2.15, w: 0.7, h: 0.7, align: "center", valign: "middle",
      fontFace: FONT_DISPLAY, fontSize: 24, bold: true, color: NAVY, margin: 0,
    });
    slide.addText(titulo, {
      x, y: 3.05, w: colW, h: 0.75,
      fontFace: FONT_DISPLAY, fontSize: 18, bold: true, color: INK, margin: 0, lineSpacingMultiple: 1.15,
    });
    slide.addText(desc, {
      x, y: 3.8, w: colW, h: 3.2,
      fontFace: FONT_BODY, fontSize: 13.5, color: INK_SOFT, margin: 0,
      valign: "top", lineSpacingMultiple: 1.3,
    });
  });
}

// ---- Slide 3: com os professores ---------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  cibLogo(slide, true);
  eyebrow(slide, "Com os professores", { color: TERRACOTTA });
  const fullW = SW - 2 * MARGIN;
  slide.addText("Um aniversário para refletir: por que nós?", {
    x: MARGIN, y: 0.95, w: fullW, h: 1.1,
    fontFace: FONT_DISPLAY, fontSize: 30, bold: true, color: WHITE, margin: 0, lineSpacingMultiple: 1.1,
  });
  slide.addText(
    "Na Reunião Geral, os professores modelaram bonecos de argila, lembrando a data em que se comemora o aniversário do ser humano na Terra.",
    {
      x: MARGIN, y: 2.25, w: fullW, h: 1.0,
      fontFace: FONT_BODY, fontSize: 16.5, color: ICE, margin: 0, lineSpacingMultiple: 1.35,
    }
  );

  slide.addShape("roundRect", {
    x: MARGIN, y: 3.65, w: fullW, h: 2.1, rectRadius: 0.08,
    fill: { color: "1E2F52" }, line: { type: "none" },
  });
  slide.addText(
    "Por que nós? Entre todos os seres, por que fomos os escolhidos para estar ali?",
    {
      x: MARGIN + 0.5, y: 3.65, w: fullW - 1.0, h: 2.1,
      fontFace: FONT_DISPLAY, fontSize: 24, italic: true, bold: true, color: WHITE,
      margin: 0, valign: "middle", lineSpacingMultiple: 1.3,
    }
  );
}

const OUT = require("path").join(HERE, "Rosh Hashana e Iom Kipur - CIB.pptx");
pres.writeFile({ fileName: OUT }).then(() => {
  console.log("PPTX gerado com sucesso:", OUT);
});
