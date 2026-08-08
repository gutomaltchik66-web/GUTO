// Apresentação de slides — Aula 2 (StartUp Nation, CIB)
// Usada na Parte 3 do roteiro ("3 inovações reais", 20 min): revela, uma a
// uma, a inovação israelense real por trás de cada problema social da
// Parte 2 (ver ferramentas/enigma-e-problemas-aula2.md) e fecha o enigma
// da Parte 1 (código 1965 = ano de fundação da Netafim).
//
// Fatos checados em fontes públicas (julho de 2026): Wikipedia, Times of
// Israel, TechCrunch, Wikipedia (Gavriel Iddan / capsule endoscopy).
//
// Cada slide de inovação tem um quadrante para o professor colar uma
// imagem própria (não temos como buscar fotos reais neste ambiente) e um
// vídeo sugerido, quando encontramos um adequado em busca na web — os
// links não foram assistidos por aqui, vale conferir antes de usar em
// sala.

const pptxgen = require("pptxgenjs");
const {
  logoPath, NAVY, TERRACOTTA, INK, INK_SOFT, ICE, ICE_MUTED, WHITE,
  FONT_DISPLAY, FONT_BODY, SW, SH, MARGIN,
  eyebrow, cibLogo, imagePlaceholder,
} = require("./apresentacao_base");

const HERE = __dirname;

const INOVACOES = [
  {
    id: "netafim",
    nome: "Irrigação por gotejamento",
    categoria: "Agricultura em terra seca (Netafim)",
    problema: "O desafio da Parte 2: cultivar alimentos gastando o mínimo possível de água.",
    resumo: "Nos anos 1950, o engenheiro Simcha Blass notou uma árvore crescendo mais forte do que as outras ao lado de um cano com um pequeno vazamento. A água pingava devagar, direto na raiz, sem desperdício. A partir dessa observação, ele e o filho Yeshayahu desenvolveram um sistema experimental de irrigação por gotejamento em 1959. Em 1965, fundaram a Netafim junto com o Kibutz Hatzerim; hoje a tecnologia é usada em mais de 110 países.",
    statValue: "110+",
    statLabel: "países usam irrigação por gotejamento hoje",
    callback: "O código do enigma era 1965: o ano em que a Netafim foi fundada.",
    imageCaption: "Sugestão: foto de um sistema de irrigação por gotejamento em uma plantação.",
    video: {
      title: "Desert Miracle of Israel: The True Story of Drip Irrigation and Kibbutz Hatzerim (Netafim)",
      source: "canal oficial Netafim, YouTube",
      url: "https://www.youtube.com/watch?v=4wspTRnwcgc",
    },
  },
  {
    id: "moovit",
    nome: "Moovit",
    categoria: "Mobilidade urbana",
    problema: "O desafio da Parte 2: ajudar milhões de pessoas a se locomoverem pela cidade de forma simples e confiável.",
    resumo: "Fundado em 2012, em Ness Ziona, por Nir Erez, Roy Bick e Yaron Evron (originalmente com o nome Tranzmate), o Moovit organiza em um único aplicativo as informações de ônibus, trem e metrô de milhares de cidades, ajudando cada pessoa a encontrar o trajeto mais confiável até o destino.",
    statValue: "US$ 900 mi",
    statLabel: "valor pago pela Intel para comprar o Moovit, em 2020",
    callback: "O Moovit hoje faz parte da Mobileye, a mesma empresa israelense de carros autônomos do Jogo dos 10 Cartões (Aula 1).",
    imageCaption: "Sugestão: captura de tela do aplicativo Moovit mostrando uma rota.",
    video: null, // não encontramos um vídeo curto e confiável sobre a história do Moovit
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
    imageCaption: "Sugestão: a cápsula do PillCam ao lado de uma moeda, para mostrar o tamanho.",
    video: {
      title: "Gavriel Iddan: pill-sized camera for wireless capsule endoscopy",
      source: "European Patent Office, European Inventor Award",
      url: "https://www.youtube.com/watch?v=vYNRrj3SrNo",
    },
  },
];

// ---- setup --------------------------------------------------------------
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";

function videoNote(slide, x, y, w, video) {
  if (video) {
    slide.addText(
      [
        { text: "Vídeo sugerido: ", options: { bold: true, color: INK } },
        {
          text: `"${video.title}" (${video.source})`,
          options: { color: "1955C7", hyperlink: { url: video.url } },
        },
      ],
      {
        x, y, w, h: 1.0,
        fontFace: FONT_BODY, fontSize: 10.5, margin: 0, valign: "top", lineSpacingMultiple: 1.25,
      }
    );
    slide.addText("Link encontrado por busca na web; conferir antes de exibir em sala.", {
      x, y: y + 0.62, w, h: 0.4,
      fontFace: FONT_BODY, fontSize: 9, italic: true, color: INK_SOFT, margin: 0,
    });
  } else {
    slide.addText(
      "Não encontramos um vídeo curto e confiável sobre essa história. Sugestão: contar a partir do resumo ao lado.",
      {
        x, y, w, h: 1.0,
        fontFace: FONT_BODY, fontSize: 10.5, italic: true, color: INK_SOFT, margin: 0,
        valign: "top", lineSpacingMultiple: 1.25,
      }
    );
  }
}

// ---- Slide 1: título -------------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  cibLogo(slide, true);
  eyebrow(slide, "Ensino Fundamental 2 · Eletiva StartUp Nation · Aula 2");
  slide.addText("De um problema a uma solução real", {
    x: MARGIN, y: 2.3, w: 7.0, h: 1.7,
    fontFace: FONT_DISPLAY, fontSize: 36, bold: true, color: WHITE, margin: 0,
  });
  slide.addText("Três inovações israelenses que começaram exatamente como os desafios de hoje", {
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
    caption: "Sugestão: foto ou colagem representando inovação israelense.",
  });
}

// ---- Slides 2-4: as 3 inovações --------------------------------------------
const LEFT_W = 6.6;
const RIGHT_X = 8.0;
const RIGHT_W = SW - MARGIN - RIGHT_X;

INOVACOES.forEach((inv, idx) => {
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  cibLogo(slide, false);
  eyebrow(slide, `Inovação ${idx + 1} de ${INOVACOES.length}`);
  slide.addText(inv.problema, {
    x: MARGIN, y: 1.02, w: LEFT_W, h: 0.6,
    fontFace: FONT_BODY, fontSize: 13.5, italic: true, color: INK_SOFT, margin: 0, lineSpacingMultiple: 1.2,
  });

  slide.addImage({ path: logoPath(inv.id), x: MARGIN, y: 1.75, w: 1.05, h: 1.05 });
  slide.addText(inv.nome, {
    x: MARGIN + 1.3, y: 1.75, w: LEFT_W - 1.3, h: 1.05,
    fontFace: FONT_DISPLAY, fontSize: 27, bold: true, color: INK, margin: 0, valign: "middle",
  });
  slide.addText(inv.categoria.toUpperCase(), {
    x: MARGIN, y: 2.95, w: LEFT_W, h: 0.35,
    fontFace: FONT_BODY, fontSize: 11.5, bold: true, color: TERRACOTTA, charSpacing: 1, margin: 0,
  });
  slide.addText(inv.resumo, {
    x: MARGIN, y: 3.4, w: LEFT_W, h: 2.5,
    fontFace: FONT_BODY, fontSize: 13.5, color: INK, margin: 0,
    valign: "top", lineSpacingMultiple: 1.28,
  });

  if (inv.callback) {
    slide.addShape("roundRect", {
      x: MARGIN, y: 6.05, w: LEFT_W, h: 0.8, rectRadius: 0.08,
      fill: { color: "FBEEE0" }, line: { type: "none" },
    });
    slide.addText(inv.callback, {
      x: MARGIN + 0.2, y: 6.05, w: LEFT_W - 0.4, h: 0.8,
      fontFace: FONT_BODY, fontSize: 12, bold: true, color: "8A4E17", margin: 0, valign: "middle",
      lineSpacingMultiple: 1.15,
    });
  } else {
    slide.addText(inv.statValue, {
      x: MARGIN, y: 6.05, w: 2.1, h: 0.6,
      fontFace: FONT_DISPLAY, fontSize: 26, bold: true, color: TERRACOTTA, margin: 0, valign: "middle",
    });
    slide.addText(inv.statLabel, {
      x: MARGIN + 2.2, y: 6.05, w: LEFT_W - 2.2, h: 0.8,
      fontFace: FONT_BODY, fontSize: 11.5, color: INK_SOFT, margin: 0, valign: "middle", lineSpacingMultiple: 1.15,
    });
  }

  imagePlaceholder(slide, RIGHT_X, 1.75, RIGHT_W, 2.85, {
    label: "Espaço para imagem",
    caption: inv.imageCaption,
  });
  videoNote(slide, RIGHT_X, 4.78, RIGHT_W, inv.video);
});

// ---- Slide 5: fechamento ----------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  cibLogo(slide, true);
  eyebrow(slide, "Recapitulando");
  slide.addText("Três problemas, três soluções reais", {
    x: MARGIN, y: 0.95, w: 11, h: 0.85,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: WHITE, margin: 0,
  });

  const colW = (SW - 2 * MARGIN - 1.0) / 3;
  const xs = [MARGIN, MARGIN + colW + 0.5, MARGIN + 2 * (colW + 0.5)];
  const recap = [
    ["Água que não sobra", "Irrigação por gotejamento (Netafim)"],
    ["Perdido no caminho", "Moovit"],
    ["Um exame difícil", "PillCam (Given Imaging)"],
  ];
  recap.forEach(([problema, solucao], i) => {
    const x = xs[i];
    slide.addImage({ path: logoPath(INOVACOES[i].id), x, y: 2.0, w: 0.8, h: 0.8 });
    slide.addText(problema, {
      x, y: 2.95, w: colW, h: 0.6,
      fontFace: FONT_DISPLAY, fontSize: 16, bold: true, color: WHITE, margin: 0, lineSpacingMultiple: 1.15,
    });
    slide.addText(solucao, {
      x, y: 3.55, w: colW, h: 0.6,
      fontFace: FONT_BODY, fontSize: 12.5, color: TERRACOTTA, bold: true, margin: 0, lineSpacingMultiple: 1.15,
    });
  });

  imagePlaceholder(slide, MARGIN, 4.35, SW - 2 * MARGIN, 1.05, {
    dark: true,
    label: "Espaço para imagem",
    caption: "Sugestão: colagem com as 3 inovações lado a lado.",
  });

  slide.addText(
    "O caminho é sempre parecido: um problema real, observado de perto, vira o começo de uma inovação.",
    {
      x: MARGIN, y: 5.75, w: 10.8, h: 0.9,
      fontFace: FONT_DISPLAY, fontSize: 17, italic: true, color: ICE, margin: 0, lineSpacingMultiple: 1.25,
    }
  );
}

const OUT = require("path").join(HERE, "Aula 2 - Apresentacao.pptx");
pres.writeFile({ fileName: OUT }).then(() => {
  console.log("PPTX gerado com sucesso:", OUT);
});
