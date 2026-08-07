// Apresentação de slides — Aula 2 (StartUp Nation, CIB)
// Usada na Parte 3 do roteiro ("3 inovações reais", 20 min): revela, uma a
// uma, a inovação israelense real por trás de cada problema social da
// Parte 2 (ver ferramentas/enigma-e-problemas-aula2.md) e fecha o enigma
// da Parte 1 (código 1965 = ano de fundação da Netafim).
//
// Fatos checados em fontes públicas (julho de 2026): Wikipedia, Times of
// Israel, TechCrunch, Wikipedia (Gavriel Iddan / capsule endoscopy).

const pptxgen = require("pptxgenjs");
const {
  logoPath, NAVY, TERRACOTTA, INK, INK_SOFT, ICE, ICE_MUTED, WHITE,
  FONT_DISPLAY, FONT_BODY, SW, SH, MARGIN,
  eyebrow, cibLogo, dotCluster, footer,
} = require("./apresentacao_base");

const HERE = __dirname;

const INOVACOES = [
  {
    id: "netafim",
    nome: "Irrigação por gotejamento",
    categoria: "Agricultura em terra seca (Netafim)",
    problema: "O desafio da Parte 2: cultivar alimentos gastando o mínimo possível de água.",
    resumo: "Nos anos 1950, o engenheiro Simcha Blass notou uma árvore crescendo mais forte do que as outras ao lado de um cano com um pequeno vazamento — a água pingava devagar, direto na raiz, sem desperdício. A partir dessa observação, ele e o filho Yeshayahu desenvolveram um sistema experimental de irrigação por gotejamento em 1959. Em 1965, fundaram a Netafim junto com o Kibutz Hatzerim — hoje a tecnologia é usada em mais de 110 países.",
    statValue: "110+",
    statLabel: "países usam irrigação por gotejamento hoje",
    callback: "O código do enigma era 1965 — o ano em que a Netafim foi fundada.",
  },
  {
    id: "moovit",
    nome: "Moovit",
    categoria: "Mobilidade urbana",
    problema: "O desafio da Parte 2: ajudar milhões de pessoas a se locomoverem pela cidade de forma simples e confiável.",
    resumo: "Fundado em 2012, em Ness Ziona, por Nir Erez, Roy Bick e Yaron Evron — originalmente com o nome Tranzmate —, o Moovit organiza em um único aplicativo as informações de ônibus, trem e metrô de milhares de cidades, ajudando cada pessoa a encontrar o trajeto mais confiável até o destino.",
    statValue: "US$ 900 mi",
    statLabel: "valor pago pela Intel para comprar o Moovit, em 2020",
    callback: "O Moovit hoje faz parte da Mobileye — a mesma empresa israelense de carros autônomos do Jogo dos 10 Cartões (Aula 1).",
  },
  {
    id: "pillcam",
    nome: "PillCam",
    categoria: "Diagnóstico médico não invasivo (Given Imaging)",
    problema: "O desafio da Parte 2: tornar um exame invasivo e desconfortável em algo simples para o paciente.",
    resumo: "O engenheiro israelense Gavriel Iddan, que trabalhava no laboratório de defesa Rafael, teve a ideia em 1981: uma câmera pequena o bastante para ser engolida como um comprimido, capaz de fotografar o interior do sistema digestivo enquanto passa por ele. Depois de quase 20 anos de desenvolvimento, registrou a patente em 1997 e fundou a Given Imaging em 1998, com Gavriel Meron. O PillCam foi aprovado pela agência de saúde dos EUA (FDA) em 2001.",
    statValue: "20 anos",
    statLabel: "entre a primeira ideia (1981) e a aprovação do PillCam pela FDA (2001)",
    callback: null,
  },
];

// ---- setup --------------------------------------------------------------
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";

// ---- Slide 1: título -------------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  dotCluster(slide, 11.6, 6.1);
  cibLogo(slide, true);
  eyebrow(slide, "Ensino Fundamental 2 · Eletiva StartUp Nation · Aula 2");
  slide.addText("De um problema a uma solução real", {
    x: MARGIN, y: 2.5, w: 10.8, h: 1.9,
    fontFace: FONT_DISPLAY, fontSize: 40, bold: true, color: WHITE, margin: 0,
  });
  slide.addText("Três inovações israelenses que começaram exatamente como os desafios de hoje", {
    x: MARGIN, y: 4.15, w: 10.3, h: 0.9,
    fontFace: FONT_BODY, fontSize: 19, color: ICE, margin: 0, lineSpacingMultiple: 1.25,
  });
  slide.addText("Colégio Israelita Brasileiro", {
    x: MARGIN, y: SH - 0.62, w: 6, h: 0.35,
    fontFace: FONT_BODY, fontSize: 11, color: ICE_MUTED, margin: 0,
  });
}

// ---- Slides 2-4: as 3 inovações --------------------------------------------
INOVACOES.forEach((inv, idx) => {
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  cibLogo(slide, false);
  eyebrow(slide, `Inovação ${idx + 1} de ${INOVACOES.length}`);
  slide.addText(inv.problema, {
    x: MARGIN, y: 1.02, w: 11, h: 0.5,
    fontFace: FONT_BODY, fontSize: 14, italic: true, color: INK_SOFT, margin: 0,
  });

  slide.addImage({ path: logoPath(inv.id), x: MARGIN, y: 1.68, w: 1.3, h: 1.3 });
  slide.addText(inv.nome, {
    x: MARGIN + 1.65, y: 1.68, w: 9.5, h: 1.3,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: INK, margin: 0, valign: "middle",
  });
  slide.addText(inv.categoria.toUpperCase(), {
    x: MARGIN, y: 3.18, w: 11, h: 0.35,
    fontFace: FONT_BODY, fontSize: 12, bold: true, color: TERRACOTTA, charSpacing: 1, margin: 0,
  });
  slide.addText(inv.resumo, {
    x: MARGIN, y: 3.66, w: 10.9, h: 2.05,
    fontFace: FONT_BODY, fontSize: 14.5, color: INK, margin: 0,
    valign: "top", lineSpacingMultiple: 1.3,
  });

  // linha de estatística
  slide.addText(inv.statValue, {
    x: MARGIN, y: 5.85, w: 3.4, h: 0.6,
    fontFace: FONT_DISPLAY, fontSize: 30, bold: true, color: TERRACOTTA, margin: 0, valign: "middle",
  });
  slide.addText(inv.statLabel, {
    x: MARGIN + 3.5, y: 5.85, w: 7.3, h: 0.6,
    fontFace: FONT_BODY, fontSize: 12.5, color: INK_SOFT, margin: 0, valign: "middle", lineSpacingMultiple: 1.15,
  });

  if (inv.callback) {
    slide.addShape("roundRect", {
      x: MARGIN, y: 6.55, w: 11, h: 0.55, rectRadius: 0.08,
      fill: { color: "FBEEE0" }, line: { type: "none" },
    });
    slide.addText(inv.callback, {
      x: MARGIN + 0.2, y: 6.55, w: 10.6, h: 0.55,
      fontFace: FONT_BODY, fontSize: 12.5, bold: true, color: "8A4E17", margin: 0, valign: "middle",
    });
  }
});

// ---- Slide 5: fechamento ----------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  dotCluster(slide, 11.6, 6.4, { dots: [[0, 0, 0.9, 20], [0.9, 0.3, 0.4, 28], [-0.6, 0.6, 0.3, 26]] });
  cibLogo(slide, true);
  eyebrow(slide, "Recapitulando");
  slide.addText("Três problemas, três soluções reais", {
    x: MARGIN, y: 0.95, w: 11, h: 0.85,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: WHITE, margin: 0,
  });

  const colW = (SW - 2 * MARGIN - 1.0) / 3;
  const xs = [MARGIN, MARGIN + colW + 0.5, MARGIN + 2 * (colW + 0.5)];
  const recap = [
    ["Água que não sobra", "Irrigação por gotejamento — Netafim"],
    ["Perdido no caminho", "Moovit"],
    ["Um exame difícil", "PillCam — Given Imaging"],
  ];
  recap.forEach(([problema, solucao], i) => {
    const x = xs[i];
    slide.addImage({ path: logoPath(INOVACOES[i].id), x, y: 2.35, w: 0.85, h: 0.85 });
    slide.addText(problema, {
      x, y: 3.35, w: colW, h: 0.6,
      fontFace: FONT_DISPLAY, fontSize: 16, bold: true, color: WHITE, margin: 0, lineSpacingMultiple: 1.15,
    });
    slide.addText(solucao, {
      x, y: 3.95, w: colW, h: 0.6,
      fontFace: FONT_BODY, fontSize: 12.5, color: TERRACOTTA, bold: true, margin: 0, lineSpacingMultiple: 1.15,
    });
  });

  slide.addText(
    "O caminho é sempre parecido: um problema real, observado de perto, vira o começo de uma inovação.",
    {
      x: MARGIN, y: 5.6, w: 10.8, h: 0.9,
      fontFace: FONT_DISPLAY, fontSize: 18, italic: true, color: ICE, margin: 0, lineSpacingMultiple: 1.25,
    }
  );
}

const OUT = require("path").join(HERE, "Aula 2 - Apresentacao.pptx");
pres.writeFile({ fileName: OUT }).then(() => {
  console.log("PPTX gerado com sucesso:", OUT);
});
