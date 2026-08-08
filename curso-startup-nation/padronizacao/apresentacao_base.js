// Sistema visual compartilhado das apresentações de slides da eletiva
// StartUp Nation (Cambria/Calibri, navy + terracota, logo do CIB, motivo
// de círculos). Usado por gerar_apresentacao_aula1_pptx.js,
// gerar_apresentacao_aula2_pptx.js e futuros decks — mudar a paleta ou
// os helpers aqui atualiza todas as apresentações de uma vez.

const path = require("path");

const ASSETS = path.join(__dirname, "assets");
const LOGO_DIR = path.join(ASSETS, "logos");
const logoPath = (id) => path.join(LOGO_DIR, `${id}.png`);
const CIB_LOGO_DARK = path.join(ASSETS, "cib-logo-header.png"); // preto, p/ fundo claro
const CIB_LOGO_LIGHT = path.join(ASSETS, "cib-logo-header-white.png"); // branco, p/ fundo navy
const CIB_LOGO_ASPECT = 1080 / 459;

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

// ---- layout -------------------------------------------------------------
const SW = 13.333, SH = 7.5; // LAYOUT_WIDE, polegadas
const MARGIN = 0.9;

function eyebrow(slide, text, opts = {}) {
  slide.addText(text.toUpperCase(), {
    x: MARGIN, y: opts.y ?? 0.55, w: opts.w ?? 9, h: 0.4,
    fontFace: FONT_BODY, fontSize: 12, bold: true,
    color: opts.color ?? TERRACOTTA, charSpacing: 2, margin: 0,
  });
}

function cibLogo(slide, dark) {
  const h = 0.42, w = h * CIB_LOGO_ASPECT;
  slide.addImage({
    path: dark ? CIB_LOGO_LIGHT : CIB_LOGO_DARK,
    x: SW - MARGIN - w, y: 0.42, w, h,
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
    x, y: opts.y ?? 2.7, w, h: opts.valueH ?? 1.0,
    fontFace: FONT_DISPLAY, fontSize: opts.valueSize ?? 48, bold: true,
    color: opts.valueColor ?? TERRACOTTA, align: "left", margin: 0,
    valign: "bottom",
  });
  slide.addText(label, {
    x, y: (opts.y ?? 2.7) + (opts.valueH ?? 1.0) + 0.12, w, h: opts.labelH ?? 1.1,
    fontFace: FONT_BODY, fontSize: opts.labelSize ?? 13.5,
    color: opts.labelColor ?? INK_SOFT, align: "left", margin: 0, valign: "top",
    lineSpacingMultiple: 1.15,
  });
}

function imagePlaceholder(slide, x, y, w, h, opts = {}) {
  const dark = !!opts.dark;
  const fill = dark ? "1E2F52" : "F2F1EC";
  const borderColor = dark ? ICE_MUTED : INK_SOFT;
  const labelColor = dark ? ICE : INK_SOFT;
  const capColor = dark ? ICE_MUTED : INK_SOFT;
  slide.addShape("roundRect", {
    x, y, w, h, rectRadius: 0.06,
    fill: { color: fill },
    line: { color: borderColor, width: 1.25, dashType: "dash" },
  });
  const label = (opts.label || "Espaço para imagem").toUpperCase();
  const caption = opts.caption || "";
  const labelY = caption ? y + h / 2 - 0.5 : y + h / 2 - 0.2;
  slide.addText(label, {
    x: x + 0.25, y: labelY, w: w - 0.5, h: 0.4,
    fontFace: FONT_BODY, fontSize: 11.5, bold: true, color: labelColor,
    align: "center", valign: "middle", charSpacing: 1, margin: 0,
  });
  if (caption) {
    slide.addText(caption, {
      x: x + 0.35, y: labelY + 0.42, w: w - 0.7, h: h - (labelY + 0.42 - y) - 0.2,
      fontFace: FONT_BODY, fontSize: 10, italic: true, color: capColor,
      align: "center", valign: "top", margin: 0, lineSpacingMultiple: 1.2,
    });
  }
}

function footer(slide, text, dark) {
  slide.addText(text, {
    x: MARGIN, y: SH - 0.62, w: SW - 2 * MARGIN, h: 0.35,
    fontFace: FONT_BODY, fontSize: 9, italic: true,
    color: dark ? ICE_MUTED : INK_SOFT, margin: 0,
  });
}

module.exports = {
  logoPath, CIB_LOGO_DARK, CIB_LOGO_LIGHT, CIB_LOGO_ASPECT,
  NAVY, TERRACOTTA, INK, INK_SOFT, ICE, ICE_MUTED, WHITE,
  FONT_DISPLAY, FONT_BODY, SW, SH, MARGIN,
  eyebrow, cibLogo, dotCluster, statColumn, footer, imagePlaceholder,
};
