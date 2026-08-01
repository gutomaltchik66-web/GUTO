# -*- coding: utf-8 -*-
"""
Logos ilustrativos das empresas do Jogo dos 10 Cartões (desenho próprio em
SVG — não são os logotipos oficiais das marcas). Fonte única, usada pelo
jogo em HTML (gerar_jogo_html.py) e pelo gerador de PNGs para a
apresentação de slides (gerar_logos_png.py), para o mesmo visual aparecer
em todos os materiais da Aula 1.

Cada valor é o conteúdo interno de um <svg viewBox="0 0 64 64">.
"""

LOGOS = {
    "waze": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#EAF8FF"/>
<path d="M32 14c-8.6 0-15.5 6.6-15.5 15.5 0 11 15.5 22.5 15.5 22.5s15.5-11.5 15.5-22.5C47.5 20.6 40.6 14 32 14z" fill="#3FCBFF" stroke="#0EA5E9" stroke-width="2"/>
<circle cx="26.5" cy="28" r="2.4" fill="#0B2540"/><circle cx="37.5" cy="28" r="2.4" fill="#0B2540"/>
<path d="M25 34.5c3 2.6 11 2.6 14 0" fill="none" stroke="#0B2540" stroke-width="2.2" stroke-linecap="round"/>""",

    "icq": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#EFF8E3"/>
<circle cx="32" cy="32" r="8.5" fill="#7AC142"/><circle cx="32" cy="15" r="4.6" fill="#7AC142"/>
<circle cx="32" cy="49" r="4.6" fill="#7AC142"/><circle cx="15" cy="32" r="4.6" fill="#7AC142"/>
<circle cx="49" cy="32" r="4.6" fill="#7AC142"/>""",

    "mobileye": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#EAF0FB"/>
<path d="M11 32c5.6-8.6 14.4-13 21-13s15.4 4.4 21 13c-5.6 8.6-14.4 13-21 13S16.6 40.6 11 32z" fill="#FFFFFF" stroke="#12203A" stroke-width="2.2"/>
<circle cx="32" cy="32" r="7.4" fill="#12203A"/><circle cx="34" cy="29.4" r="2.1" fill="#00AEEF"/>""",

    "wix": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#F2F2F0"/>
<text x="32" y="39" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="19" fill="#0D0D0D">wix</text>""",

    "solaredge": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#FFF3E9"/>
<circle cx="32" cy="32" r="10" fill="#F5821F"/>
<g stroke="#F5821F" stroke-width="3" stroke-linecap="round">
<line x1="32" y1="10" x2="32" y2="16"/><line x1="32" y1="48" x2="32" y2="54"/>
<line x1="10" y1="32" x2="16" y2="32"/><line x1="48" y1="32" x2="54" y2="32"/>
<line x1="16.5" y1="16.5" x2="20.5" y2="20.5"/><line x1="43.5" y1="43.5" x2="47.5" y2="47.5"/>
<line x1="47.5" y1="16.5" x2="43.5" y2="20.5"/><line x1="20.5" y1="43.5" x2="16.5" y2="47.5"/></g>""",

    "fiverr": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#1DBF73"/>
<text x="32" y="37" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="13.5" fill="#FFFFFF">fiverr</text>""",

    "pendrive": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#F0F0EE"/>
<rect x="22" y="13" width="20" height="10" rx="2" fill="#9C9C97"/>
<rect x="18" y="23" width="28" height="27" rx="4" fill="#5B5B57"/>
<rect x="27" y="30" width="10" height="4" rx="1" fill="#F0F0EE"/>""",

    "sisense": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#F3EEFB"/>
<rect x="14" y="32" width="7" height="17" rx="2" fill="#6C3FC5"/>
<rect x="25" y="22" width="7" height="27" rx="2" fill="#6C3FC5"/>
<rect x="36" y="14" width="7" height="35" rx="2" fill="#6C3FC5"/>
<rect x="47" y="26" width="7" height="23" rx="2" fill="#8B5FE0"/>""",

    "spotify": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#1DB954"/>
<path d="M17 26c9-3 19.5-3 28.5 2.3" fill="none" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>
<path d="M19 34.5c7.7-2.6 16.4-2.6 23.6 1.7" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
<path d="M21 42.5c6-2 12.3-2 17.4 1" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>""",

    "skype": """<rect x="2" y="2" width="60" height="60" rx="14" fill="#E8F7FE"/>
<path d="M16 24c0-6.6 5.4-12 12-12h8c9.9 0 18 8.1 18 18s-8.1 18-18 18c-2 0-3.9-.3-5.7-.9L20 51l2.3-9.6C18.3 38 16 32.9 16 27z" fill="#00AFF0"/>
<circle cx="26" cy="27" r="2.6" fill="#FFFFFF"/><circle cx="34" cy="27" r="2.6" fill="#FFFFFF"/><circle cx="42" cy="27" r="2.6" fill="#FFFFFF"/>""",
}
