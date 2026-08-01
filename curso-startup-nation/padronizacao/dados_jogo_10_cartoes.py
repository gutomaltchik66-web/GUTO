# -*- coding: utf-8 -*-
"""
Dados do Jogo dos 10 Cartões (Aula 1) — fonte única usada tanto pelo
gerador de PDF (gerar_jogo_cartoes_pdf.py) quanto pelo gerador do jogo
em HTML (gerar_jogo_html.py), para os dois nunca ficarem dessincronizados.

Fundadores, anos de fundação e valores de aquisição checados em fontes
públicas (Wikipedia, Forbes, arquivos da SEC e histórico das próprias
empresas) em julho de 2026.
"""

# Cada cartão: (id, NOME, problema, solução). Ordem: 8 reais + 2 pegadinha.
CARTOES = [
    ("waze", "WAZE",
     "Motoristas perdiam tempo presos no trânsito sem saber de rotas melhores.",
     "Aplicativo de GPS colaborativo — os próprios motoristas avisam sobre trânsito, radares e buracos em tempo real."),
    ("icq", "ICQ",
     "Não dava para saber se um amigo estava online e falar com ele na hora, pela internet.",
     "O primeiro mensageiro instantâneo popular do mundo — base do que hoje são WhatsApp e Telegram."),
    ("mobileye", "MOBILEYE",
     "Acidentes de trânsito causados por distração ou reação lenta do motorista.",
     "Câmeras e inteligência artificial que ajudam o carro a “enxergar” o que está à frente e evitar batidas — base da tecnologia de carros autônomos."),
    ("wix", "WIX",
     "Criar um site era coisa só para quem sabia programar.",
     "Plataforma onde qualquer pessoa monta um site arrastando e soltando elementos, sem escrever código."),
    ("solaredge", "SOLAREDGE",
     "Painéis de energia solar perdiam eficiência quando parte deles ficava na sombra ou sujos.",
     "Tecnologia que otimiza cada painel solar individualmente, aproveitando mais energia."),
    ("fiverr", "FIVERR",
     "Era difícil encontrar e contratar freelancers confiáveis em qualquer lugar do mundo.",
     "Marketplace global onde qualquer pessoa oferece ou contrata serviços freelance (design, tradução, programação etc)."),
    ("pendrive", "PEN DRIVE (USB FLASH DRIVE)",
     "Levar arquivos de um computador para outro exigia CD ou disquete, lentos e frágeis.",
     "Memória portátil pequena e resistente, que se tornou padrão mundial."),
    ("sisense", "SISENSE",
     "Empresas tinham dados complicados e não conseguiam entendê-los de forma simples.",
     "Software de análise de dados (business intelligence) que transforma números complicados em gráficos fáceis de entender."),
    ("spotify", "SPOTIFY",
     "Era muito fácil baixar música pirata, e as gravadoras perdiam dinheiro; ao mesmo tempo, ninguém queria pagar por CD.",
     "Plataforma de streaming onde se paga uma assinatura para ouvir qualquer música, sem baixar nada."),
    ("skype", "SKYPE",
     "Ligações internacionais por telefone eram caríssimas.",
     "Chamadas de vídeo e voz gratuitas pela internet, entre qualquer lugar do mundo."),
]

# (id, é_israelense, país, fato validado)
GABARITO = {
    "waze": (True, "Israel", "Ehud Shabtai, Uri Levine e Amir Shinar (2006/2009). Comprado pelo Google em 2013 por ~970 milhões de dólares."),
    "icq": (True, "Israel", "Mirabilis — Yair Goldfinger, Arik Vardi, Sefi Vigiser e Amnon Amir (jul/1996). Comprado pela AOL em 1998 por 287 milhões de dólares."),
    "mobileye": (True, "Israel", "Amnon Shashua e Ziv Aviram (1999). Comprada pela Intel em 2017 por 15,3 bilhões de dólares."),
    "wix": (True, "Israel", "Avishai Abrahami, Nadav Abrahami e Giora Kaplan, em Tel Aviv (2006)."),
    "solaredge": (True, "Israel", "Guy Sella e equipe (2006) — hoje uma das maiores empresas de tecnologia de energia solar do mundo."),
    "fiverr": (True, "Israel", "Micha Kaufman e Shai Wininger, em Tel Aviv (2010)."),
    "pendrive": (True, "Israel", "Patente da M-Systems (Amir Ban, Dov Moran e Oron Ogdan) em 1999; DiskOnKey lançado em 2000. Há disputa histórica com empresas de Singapura/China, mas a patente israelense é a mais antiga."),
    "sisense": (True, "Israel", "Elad Israeli, Eldad Farkash, Aviad Harell, Guy Boyangu e Adi Azaria, em Tel Aviv (2004)."),
    "spotify": (False, "Suécia", "Daniel Ek e Martin Lorentzon, em Estocolmo (abril de 2006). Não é israelense."),
    "skype": (False, "Suécia/Dinamarca", "Fundada por Niklas Zennström (sueco) e Janus Friis (dinamarquês) em 2003; software desenvolvido por uma equipe de engenheiros estonianos. Não é israelense."),
}

FONTE_NOTA = ("Fontes: Wikipedia, Forbes, arquivos da SEC e histórico das próprias empresas "
              "(checado em julho de 2026). Valores de aquisição variam entre fontes — os números "
              "acima são os mais citados em registros públicos.")
