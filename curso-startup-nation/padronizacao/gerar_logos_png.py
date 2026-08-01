# -*- coding: utf-8 -*-
"""
Renderiza os logos ilustrativos de logos_svg.py como PNG (512x512, fundo
transparente fora do badge arredondado), para uso em materiais que não
aceitam SVG diretamente — como a apresentação de slides em PPTX.

Requer Playwright com o Chromium já instalado (ambiente de execução do
Claude Code): PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers.
"""
import base64
import os
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT_DIR = os.path.join(ASSETS, "logos")
sys.path.insert(0, HERE)
from logos_svg import LOGOS

os.makedirs(OUT_DIR, exist_ok=True)


def font_b64(filename):
    with open(os.path.join(ASSETS, filename), "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


FONT_BOLD = font_b64("MontserratMedium-bold.ttf")

# Embute a Montserrat (mesma usada no jogo em HTML) para os logos que usam
# texto (wix, fiverr) renderizarem com a fonte certa, não um fallback serifado.
PAGE_TEMPLATE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{
  font-family: "Montserrat";
  font-weight: 700;
  font-style: normal;
  src: url(data:font/ttf;base64,""" + FONT_BOLD + """) format("truetype");
}}
html,body{{margin:0;padding:0;background:transparent;}}
svg{{display:block;}}
</style></head><body>
<svg id="mark" viewBox="0 0 64 64" width="512" height="512" xmlns="http://www.w3.org/2000/svg">{svg_inner}</svg>
</body></html>"""

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    page = browser.new_page(viewport={"width": 512, "height": 512})
    for card_id, svg_inner in LOGOS.items():
        page.set_content(PAGE_TEMPLATE.format(svg_inner=svg_inner))
        el = page.locator("#mark")
        out_path = os.path.join(OUT_DIR, f"{card_id}.png")
        el.screenshot(path=out_path, omit_background=True)
        print("gerado:", out_path)
    browser.close()
