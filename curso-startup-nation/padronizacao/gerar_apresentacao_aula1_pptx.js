// Apresentação de slides — Aula 1 (StartUp Nation, CIB)
// Usada na etapa "Dados de impacto e estrutura do semestre" (15 min).
// Números de Israel checados em fontes públicas (OCDE, StartupBlink, Nasdaq/
// US Dept of State) — ver rodapé do slide 3. Dados das 8 empresas cruzados
// com dados_jogo_10_cartoes.py (mesma fonte usada no Jogo dos 10 Cartões).

const path = require("path");
const pptxgen = require("pptxgenjs");

const HERE = __dirname;
const LOGO_DIR = path.join(HERE, "assets", "logos");
const logoPath = (id) => path.join(LOGO_DIR, `${id}.png`);

// ---- paleta -----------------------------------------------------------
const NAVY = "12213D";
const TERRACOTTA = "E08A3E";
const INK = "1B1B18";
const INK_SOFT = "6B6B63";
const ICE = "CADCFC";
const ICE_MUTED = "8FA6CE";
const WHITE = "FFFFFF";

const FONT_DISPLAY = "Cambria";
const FONT_BODY = "Calibri";

// ---- dados das 8 empresas (cf. dados_jogo_10_cartoes.py) ---------------
const EMPRESAS = [
  { id: "waze", nome: "Waze", categoria: "GPS colaborativo em tempo real",
    fundacao: "Fundada em 2006, por Ehud Shabtai, Uri Levine e Amir Shinar",
    fato: "Comprada pelo Google em 2013 por cerca de US$ 970 milhões" },
  { id: "icq", nome: "ICQ", categoria: "1º mensageiro instantâneo popular do mundo",
    fundacao: "Criado em 1996, pela Mirabilis (Yair Goldfinger e equipe)",
    fato: "Base do que hoje são o WhatsApp e o Telegram" },
  { id: "mobileye", nome: "Mobileye", categoria: "Visão computacional para carros autônomos",
    fundacao: "Fundada em 1999, por Amnon Shashua e Ziv Aviram",
    fato: "Comprada pela Intel em 2017 por US$ 15,3 bilhões" },
  { id: "wix", nome: "Wix", categoria: "Criação de sites sem programar",
    fundacao: "Fundada em 2006, em Tel Aviv",
    fato: "Uma das maiores plataformas de criação de sites do mundo" },
  { id: "solaredge", nome: "SolarEdge", categoria: "Otimização de energia solar",
    fundacao: "Fundada em 2006, por Guy Sella e equipe",
    fato: "Uma das maiores empresas de tecnologia solar do mundo" },
  { id: "fiverr", nome: "Fiverr", categoria: "Marketplace global de freelancers",
    fundacao: "Fundada em 2010, em Tel Aviv, por Micha Kaufman e Shai Wininger",
    fato: "Conecta milhões de freelancers a clientes no mundo todo" },
  { id: "pendrive", nome: "Pen drive (M-Systems)", categoria: "Memória portátil USB",
    fundacao: "Patente registrada em 1999, por Dov Moran e equipe (M-Systems)",
    fato: "Virou padrão mundial de armazenamento portátil" },
  { id: "sisense", nome: "Sisense", categoria: "Análise de dados (Business Intelligence)",
    fundacao: "Fundada em 2004, em Tel Aviv",
    fato: "Transforma dados complexos em gráficos simples de entender" },
];
const PARES = [[0, 1], [2, 3], [4, 5], [6, 7]];

// ---- setup --------------------------------------------------------------
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
const SW = 13.333, SH = 7.5;
const MARGIN = 0.9;

function eyebrow(slide, text, opts = {}) {
  slide.addText(text.toUpperCase(), {
    x: MARGIN, y: opts.y ?? 0.55, w: opts.w ?? 9, h: 0.4,
    fontFace: FONT_BODY, fontSize: 12, bold: true,
    color: opts.color ?? TERRACOTTA, charSpacing: 2, margin: 0,
  });
}

function dotCluster(slide, cx, cy, opts = {}) {
  const dots = opts.dots ?? [
    [0, 0, 1.5, 14], [1.3, -0.6, 0.7, 22], [-1.0, 0.9, 0.5, 18],
    [1.9, 0.8, 0.35, 28], [-1.6, -0.3, 0.35, 24], [0.5, 1.6, 0.9, 16],
  ];
  dots.forEach(([dx, dy, r, transp]) => {
    slide.addShape("ellipse", {
      x: cx + dx - r, y: cy + dy - r, w: r * 2, h: r * 2,
      fill: { color: TERRACOTTA, transparency: transp },
      line: { type: "none" },
    });
  });
}

function statColumn(slide, x, w, value, label, opts = {}) {
  slide.addText(value, {
    x, y: opts.y ?? 2.7, w, h: opts.valueH ?? 1.1,
    fontFace: FONT_DISPLAY, fontSize: opts.valueSize ?? 54, bold: true,
    color: opts.valueColor ?? TERRACOTTA, align: "left", margin: 0,
    valign: "bottom",
  });
  slide.addText(label, {
    x, y: (opts.y ?? 2.7) + (opts.valueH ?? 1.1) + 0.12, w, h: opts.labelH ?? 1.3,
    fontFace: FONT_BODY, fontSize: opts.labelSize ?? 14,
    color: opts.labelColor ?? INK_SOFT, align: "left", margin: 0, valign: "top",
    lineSpacingMultiple: 1.15,
  });
}

function footer(slide, text, dark) {
  slide.addText(text, {
    x: MARGIN, y: SH - 0.62, w: SW - 2 * MARGIN, h: 0.35,
    fontFace: FONT_BODY, fontSize: 9, italic: true,
    color: dark ? ICE_MUTED : INK_SOFT, margin: 0,
  });
}

// ---- Slide 1: título -----------------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  dotCluster(slide, 11.6, 6.1);
  eyebrow(slide, "Ensino Fundamental 2 · Eletiva StartUp Nation · Aula 1", { color: TERRACOTTA });
  slide.addText("Israel também é isso.", {
    x: MARGIN, y: 2.5, w: 10.8, h: 1.9,
    fontFace: FONT_DISPLAY, fontSize: 52, bold: true, color: WHITE, margin: 0,
  });
  slide.addText("A potência de tecnologia por trás da StartUp Nation", {
    x: MARGIN, y: 4.35, w: 9.5, h: 0.6,
    fontFace: FONT_BODY, fontSize: 20, color: ICE, margin: 0,
  });
  slide.addText("Colégio Israelita Brasileiro", {
    x: MARGIN, y: SH - 0.62, w: 6, h: 0.35,
    fontFace: FONT_BODY, fontSize: 11, color: ICE_MUTED, margin: 0,
  });
}

// ---- Slide 2: 3 números básicos -------------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  eyebrow(slide, "Antes de começar", { color: TERRACOTTA });
  slide.addText("O que vocês já sabem, rapidinho", {
    x: MARGIN, y: 0.95, w: 10.5, h: 0.8,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: INK, margin: 0,
  });

  const colW = (SW - 2 * MARGIN - 1.0) / 3;
  const xs = [MARGIN, MARGIN + colW + 0.5, MARGIN + 2 * (colW + 0.5)];
  const basics = [
    ["1948", "Ano de fundação do Estado de Israel"],
    ["10,2M", "Habitantes em 2025"],
    ["א", "Hebraico é o idioma oficial"],
  ];
  basics.forEach(([value, label], i) => {
    statColumn(slide, xs[i], colW, value, label, {
      valueSize: value === "א" ? 66 : 54,
      valueColor: NAVY,
    });
  });
  footer(slide, "Fonte: Central Bureau of Statistics de Israel (população, jan/2026).", false);
}

// ---- Slide 3: a potência que poucos conhecem ------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  eyebrow(slide, "O lado que quase ninguém conta", { color: TERRACOTTA });
  slide.addText("Só isso já bastaria para impressionar.", {
    x: MARGIN, y: 0.95, w: 11, h: 0.8,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: WHITE, margin: 0,
  });

  const colW = (SW - 2 * MARGIN - 1.0) / 3;
  const xs = [MARGIN, MARGIN + colW + 0.5, MARGIN + 2 * (colW + 0.5)];
  const stats = [
    ["7.000+", "startups ativas — a maior densidade de startups por habitante do mundo"],
    ["6,3%", "do PIB em Pesquisa & Desenvolvimento — o maior índice do mundo"],
    ["130+", "empresas israelenses negociadas na NASDAQ — só EUA, Canadá e China têm mais"],
  ];
  stats.forEach(([value, label], i) => {
    statColumn(slide, xs[i], colW, value, label, {
      valueColor: TERRACOTTA, labelColor: ICE, valueSize: 54,
    });
  });
  footer(slide, "Fontes: StartupBlink (2025) · OCDE / Israel Innovation Authority (2023) · US Dept. of State, lista Nasdaq (2023).", true);
}

// ---- Slide 4: ponte para as empresas --------------------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: WHITE };
  eyebrow(slide, "E tem mais", { color: TERRACOTTA });
  slide.addText("Vocês já usam produtos criados lá — sem saber.", {
    x: MARGIN, y: 1.0, w: 11, h: 1.1,
    fontFace: FONT_DISPLAY, fontSize: 32, bold: true, color: INK, margin: 0,
  });
  slide.addText("A seguir: 8 empresas israelenses que viraram parte do seu dia a dia.", {
    x: MARGIN, y: 2.15, w: 10, h: 0.5,
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
  eyebrow(slide, "Empresas israelenses que você conhece", { color: TERRACOTTA, w: 8 });
  slide.addText(`${idx + 1} de ${PARES.length}`, {
    x: SW - MARGIN - 2, y: 0.55, w: 2, h: 0.4,
    fontFace: FONT_BODY, fontSize: 12, color: INK_SOFT, align: "right", margin: 0,
  });

  const colW = (SW - 2 * MARGIN - 0.8) / 2;
  const xs = [MARGIN, MARGIN + colW + 0.8];

  pair.forEach((empresaIdx, col) => {
    const e = EMPRESAS[empresaIdx];
    const x = xs[col];
    slide.addImage({ path: logoPath(e.id), x, y: 1.75, w: 1.15, h: 1.15 });
    slide.addText(e.nome, {
      x, y: 3.1, w: colW, h: 0.55,
      fontFace: FONT_DISPLAY, fontSize: 24, bold: true, color: INK, margin: 0,
    });
    slide.addText(e.categoria.toUpperCase(), {
      x, y: 3.65, w: colW, h: 0.4,
      fontFace: FONT_BODY, fontSize: 12, bold: true, color: TERRACOTTA,
      charSpacing: 1, margin: 0,
    });
    slide.addText(e.fundacao, {
      x, y: 4.15, w: colW, h: 0.85,
      fontFace: FONT_BODY, fontSize: 13, color: INK_SOFT, margin: 0,
      valign: "top", lineSpacingMultiple: 1.2,
    });
    slide.addText(e.fato, {
      x, y: 5.05, w: colW, h: 0.9,
      fontFace: FONT_BODY, fontSize: 13, italic: true, color: INK,
      margin: 0, valign: "top", lineSpacingMultiple: 1.2,
    });
  });
});

// ---- Slide 9: fechamento / jornada do semestre ----------------------------
{
  const slide = pres.addSlide();
  slide.background = { color: NAVY };
  dotCluster(slide, 11.8, 1.1, { dots: [[0,0,0.9,20],[0.9,0.3,0.4,28],[-0.6,0.6,0.3,26]] });
  eyebrow(slide, "Sua jornada nesta eletiva", { color: TERRACOTTA });
  slide.addText("Da tradição ao seu próprio pitch.", {
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

  slide.addText("Vamos começar.", {
    x: MARGIN, y: 6.35, w: 8, h: 0.5,
    fontFace: FONT_DISPLAY, fontSize: 18, italic: true, color: WHITE, margin: 0,
  });
}

const OUT = path.join(HERE, "Aula 1 - Apresentacao.pptx");
pres.writeFile({ fileName: OUT }).then(() => {
  console.log("PPTX gerado com sucesso:", OUT);
});
