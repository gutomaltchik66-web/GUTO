// Apresentação de slides — Aula 1 (StartUp Nation, CIB)
// Usada na etapa "Dados de impacto e estrutura do semestre" (15 min).
// Números de Israel checados em fontes públicas (OCDE, StartupBlink, Nasdaq/
// US Dept of State, CBS Israel) — ver rodapé dos slides 2 e 3. Dados das 8
// empresas cruzados com dados_jogo_10_cartoes.py (mesma fonte usada no
// Jogo dos 10 Cartões).

const path = require("path");
const pptxgen = require("pptxgenjs");
const {
  logoPath, NAVY, TERRACOTTA, INK, INK_SOFT, ICE, ICE_MUTED, WHITE,
  FONT_DISPLAY, FONT_BODY, SW, SH, MARGIN,
  eyebrow, cibLogo, dotCluster, statColumn, footer,
} = require("./apresentacao_base");

const HERE = __dirname;

// ---- dados das 8 empresas (cf. dados_jogo_10_cartoes.py) ---------------
// "resumo": 2-3 frases (o que a empresa faz + fundação + fato de impacto).
const EMPRESAS = [
  { id: "waze", nome: "Waze", categoria: "GPS colaborativo em tempo real",
    resumo: "Aplicativo de GPS em que os próprios motoristas informam trânsito, radares e buracos em tempo real, ajudando a encontrar o caminho mais rápido. Fundada em 2006 por Ehud Shabtai, Uri Levine e Amir Shinar, foi comprada pelo Google em 2013 por cerca de US$ 970 milhões." },
  { id: "icq", nome: "ICQ", categoria: "1º mensageiro instantâneo popular do mundo",
    resumo: "Criado em 1996 pela Mirabilis (Yair Goldfinger e equipe), permitia conversar com outras pessoas em tempo real pela internet, algo inédito até então. Foi comprado pela AOL em 1998 por US$ 287 milhões e é considerado a base do que hoje são o WhatsApp e o Telegram." },
  { id: "mobileye", nome: "Mobileye", categoria: "Visão computacional para carros autônomos",
    resumo: "Fundada em 1999 por Amnon Shashua e Ziv Aviram, desenvolve câmeras e inteligência artificial que ajudam o carro a identificar o que está à frente e evitar colisões, tecnologia essencial para veículos autônomos. Foi comprada pela Intel em 2017 por US$ 15,3 bilhões." },
  { id: "wix", nome: "Wix", categoria: "Criação de sites sem programar",
    resumo: "Fundada em 2006, em Tel Aviv, permite que qualquer pessoa monte um site profissional arrastando e soltando elementos, sem escrever código. É hoje uma das maiores plataformas de criação de sites do mundo." },
  { id: "solaredge", nome: "SolarEdge", categoria: "Otimização de energia solar",
    resumo: "Fundada em 2006 por Guy Sella e equipe, desenvolve tecnologia que otimiza cada painel solar individualmente, mesmo quando parte do sistema está na sombra ou suja. É hoje uma das maiores empresas de tecnologia de energia solar do mundo." },
  { id: "fiverr", nome: "Fiverr", categoria: "Marketplace global de freelancers",
    resumo: "Fundada em 2010, em Tel Aviv, por Micha Kaufman e Shai Wininger, conecta freelancers (design, tradução, programação e outros serviços) a clientes no mundo inteiro. Facilita contratar ou oferecer trabalho remoto em qualquer lugar." },
  { id: "pendrive", nome: "Pen drive (M-Systems)", categoria: "Memória portátil USB",
    resumo: "Antes dele, levar arquivos de um computador a outro exigia CD ou disquete, lentos e frágeis. A patente foi registrada em 1999 pela M-Systems (Amir Ban, Dov Moran e Oron Ogdan), e o produto DiskOnKey chegou ao mercado em 2000, tornando-se padrão mundial de armazenamento portátil." },
  { id: "sisense", nome: "Sisense", categoria: "Análise de dados (Business Intelligence)",
    resumo: "Fundada em 2004, em Tel Aviv, desenvolve softwares de análise de dados que transformam números complexos em gráficos simples de entender, ajudando empresas a tomar decisões melhores com os dados que já possuem." },
];
const PARES = [[0, 1], [2, 3], [4, 5], [6, 7]];

// ---- setup --------------------------------------------------------------
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in

// ---- Slide 1: título -----------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  dotCluster(slide, 11.6, 6.1);
  cibLogo(slide, true);
  eyebrow(slide, "Ensino Fundamental 2 · Eletiva StartUp Nation · Aula 1", { color: TERRACOTTA });
  slide.addText("Israel: também uma potência tecnológica", {
    x: MARGIN, y: 2.5, w: 10.8, h: 1.9,
    fontFace: FONT_DISPLAY, fontSize: 44, bold: true, color: WHITE, margin: 0,
  });
  slide.addText("A tecnologia e o empreendedorismo por trás da StartUp Nation", {
    x: MARGIN, y: 4.15, w: 10, h: 0.6,
    fontFace: FONT_BODY, fontSize: 20, color: ICE, margin: 0,
  });
  slide.addText("Colégio Israelita Brasileiro", {
    x: MARGIN, y: SH - 0.62, w: 6, h: 0.35,
    fontFace: FONT_BODY, fontSize: 11, color: ICE_MUTED, margin: 0,
  });
}

// ---- Slide 2: panorama do país --------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  cibLogo(slide, false);
  eyebrow(slide, "Sobre Israel", { color: TERRACOTTA });
  slide.addText("Panorama do país", {
    x: MARGIN, y: 0.95, w: 10.5, h: 0.8,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: INK, margin: 0,
  });

  const colW = (SW - 2 * MARGIN - 1.0) / 3;
  const xs = [MARGIN, MARGIN + colW + 0.5, MARGIN + 2 * (colW + 0.5)];
  const rows = [
    [
      ["1948", "Ano de fundação do Estado de Israel"],
      ["10,2M", "Habitantes em 2025"],
      ["Jerusalém", "Capital do país", 30],
    ],
    [
      ["א", "Hebraico é o idioma oficial", 66],
      ["120", "Membros do Knesset, o parlamento israelense"],
      ["₪", "Novo shekel (NIS) é a moeda oficial", 54],
    ],
  ];
  const rowYs = [2.55, 4.55];
  rows.forEach((row, ri) => {
    row.forEach(([value, label, valueSize], i) => {
      statColumn(slide, xs[i], colW, value, label, {
        y: rowYs[ri], valueSize: valueSize ?? 44, valueColor: NAVY,
        valueH: 0.85, labelH: 0.9,
      });
    });
  });
  footer(slide, "Fontes: Central Bureau of Statistics de Israel (população, jan/2026) · Knesset.gov.il.", false);
}

// ---- Slide 3: impacto econômico e tecnológico -----------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  cibLogo(slide, true);
  eyebrow(slide, "Impacto econômico e tecnológico", { color: TERRACOTTA });
  slide.addText("Israel é uma potência global de inovação", {
    x: MARGIN, y: 0.95, w: 11, h: 0.8,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: WHITE, margin: 0,
  });

  const colW = (SW - 2 * MARGIN - 1.0) / 3;
  const xs = [MARGIN, MARGIN + colW + 0.5, MARGIN + 2 * (colW + 0.5)];
  const stats = [
    ["7.000+", "startups ativas, a maior densidade de startups por habitante do mundo"],
    ["6,3%", "do PIB em Pesquisa & Desenvolvimento, o maior índice do mundo"],
    ["130+", "empresas israelenses negociadas na NASDAQ, atrás apenas de EUA, Canadá e China"],
  ];
  stats.forEach(([value, label], i) => {
    statColumn(slide, xs[i], colW, value, label, {
      valueColor: TERRACOTTA, labelColor: ICE, valueSize: 48,
    });
  });
  footer(slide, "Fontes: StartupBlink (2025) · OCDE / Israel Innovation Authority (2023) · US Dept. of State, lista Nasdaq (2023).", true);
}

// ---- Slide 4: ponte para as empresas --------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  cibLogo(slide, false);
  eyebrow(slide, "Empresas israelenses no cotidiano", { color: TERRACOTTA });
  slide.addText("Produtos usados diariamente, criados em Israel", {
    x: MARGIN, y: 1.0, w: 11, h: 1.1,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: INK, margin: 0,
  });
  slide.addText("A seguir, um resumo de 8 empresas israelenses que fazem parte da rotina de milhões de pessoas.", {
    x: MARGIN, y: 2.15, w: 10.5, h: 0.5,
    fontFace: FONT_BODY, fontSize: 16, color: INK_SOFT, margin: 0,
  });

  const n = EMPRESAS.length;
  const cell = 1.15, gap = 0.28;
  const totalW = n * cell + (n - 1) * gap;
  let x = (SW - totalW) / 2;
  const y = 4.35;
  EMPRESAS.forEach((e) => {
    slide.addImage({ path: logoPath(e.id), x, y, w: cell, h: cell });
    x += cell + gap;
  });
}

// ---- Slides 5-8: empresas em pares ----------------------------------------
PARES.forEach((pair, idx) => {
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  cibLogo(slide, false);
  eyebrow(slide, "Empresas israelenses", { color: TERRACOTTA, w: 8 });
  slide.addText(`${idx + 1} de ${PARES.length}`, {
    x: SW - MARGIN - 2.2, y: 0.98, w: 1.3, h: 0.3,
    fontFace: FONT_BODY, fontSize: 11, color: INK_SOFT, align: "right", margin: 0,
  });

  const colW = (SW - 2 * MARGIN - 0.8) / 2;
  const xs = [MARGIN, MARGIN + colW + 0.8];

  pair.forEach((empresaIdx, col) => {
    const e = EMPRESAS[empresaIdx];
    const x = xs[col];
    slide.addImage({ path: logoPath(e.id), x, y: 1.65, w: 1.0, h: 1.0 });
    slide.addText(e.nome, {
      x, y: 2.75, w: colW, h: 0.5,
      fontFace: FONT_DISPLAY, fontSize: 22, bold: true, color: INK, margin: 0,
    });
    slide.addText(e.categoria.toUpperCase(), {
      x, y: 3.24, w: colW, h: 0.35,
      fontFace: FONT_BODY, fontSize: 11.5, bold: true, color: TERRACOTTA,
      charSpacing: 1, margin: 0,
    });
    slide.addText(e.resumo, {
      x, y: 3.72, w: colW, h: 2.4,
      fontFace: FONT_BODY, fontSize: 13.5, color: INK,
      margin: 0, valign: "top", lineSpacingMultiple: 1.28,
    });
  });
});

// ---- Slide 9: estrutura do semestre ---------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  dotCluster(slide, 11.6, 6.4, { dots: [[0,0,0.9,20],[0.9,0.3,0.4,28],[-0.6,0.6,0.3,26]] });
  cibLogo(slide, true);
  eyebrow(slide, "Estrutura do semestre", { color: TERRACOTTA });
  slide.addText("Da tradição judaica ao pitch final", {
    x: MARGIN, y: 0.95, w: 11, h: 0.85,
    fontFace: FONT_DISPLAY, fontSize: 34, bold: true, color: WHITE, margin: 0,
  });

  const fases = [
    ["1", "Conteúdo & Cultura", "Aulas 1–7", "Os valores por trás da StartUp Nation"],
    ["2", "Meu Projeto", "Aulas 8–13", "Da ideia ao protótipo"],
    ["3", "Pitch Day", "23/11", "Apresentação final, valendo nota"],
  ];
  const colW = (SW - 2 * MARGIN - 1.0) / 3;
  const xs = [MARGIN, MARGIN + colW + 0.5, MARGIN + 2 * (colW + 0.5)];
  fases.forEach(([num, titulo, quando, desc], i) => {
    const x = xs[i];
    slide.addShape("ellipse", {
      x, y: 2.3, w: 0.7, h: 0.7,
      fill: { color: TERRACOTTA }, line: { type: "none" },
    });
    slide.addText(num, {
      x, y: 2.3, w: 0.7, h: 0.7, align: "center", valign: "middle",
      fontFace: FONT_DISPLAY, fontSize: 24, bold: true, color: NAVY, margin: 0,
    });
    slide.addText(titulo, {
      x, y: 3.2, w: colW, h: 0.5,
      fontFace: FONT_DISPLAY, fontSize: 19, bold: true, color: WHITE, margin: 0,
    });
    slide.addText(quando, {
      x, y: 3.68, w: colW, h: 0.4,
      fontFace: FONT_BODY, fontSize: 13, bold: true, color: TERRACOTTA, margin: 0,
    });
    slide.addText(desc, {
      x, y: 4.1, w: colW, h: 0.6,
      fontFace: FONT_BODY, fontSize: 13, color: ICE, margin: 0, lineSpacingMultiple: 1.2,
    });
  });
}

const OUT = path.join(HERE, "Aula 1 - Apresentacao.pptx");
pres.writeFile({ fileName: OUT }).then(() => {
  console.log("PPTX gerado com sucesso:", OUT);
});
