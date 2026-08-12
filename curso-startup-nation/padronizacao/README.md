# Padronização de materiais didáticos — CIB

Especificação extraída dos modelos oficiais do Colégio Israelita Brasileiro (recebidos por e-mail): `PAUTA_PEQUENA.pdf`, `FOLHATIMBRADA.docx` e `CABEÇALHO EDITÁVEL EF2.docx`. Todo material didático produzido para a eletiva StartUp Nation segue este padrão.

## Cabeçalho obrigatório — Ensino Fundamental 2

Reproduz o modelo de `CABEÇALHO EDITÁVEL EF2.docx`, repetido no topo de toda página do material:

1. **"Ensino Fundamental 2"** — negrito, alinhado à esquerda.
2. **Logo do CIB** — recorte horizontal (ícone + "Colégio Israelita ישראלית", sem o slogan), alinhado no canto superior direito, mesma altura da linha do título.
3. **"Aluno(a): ______________________________"** — linha em branco, largura total.
4. **"Ano Escolar: ____ Turma: ____ Data: ____"** — os três campos na mesma linha, todos em branco para o professor/aluno completar (nenhum campo vem pré-preenchido, já que as datas das aulas podem mudar ao longo do semestre).
5. Linha fina horizontal fechando o bloco de cabeçalho.

## Moldura de página

Reproduz `PAUTA_PEQUENA.pdf`: uma borda retangular fina emoldurando toda a página impressa (margem de 10mm da borda física do papel).

## Tipografia

Fonte oficial: **Montserrat Medium** (regular, negrito, itálico) — arquivos em [`assets/`](assets/), extraídos do `.docx` oficial do colégio.

## Cores

Nenhuma cor de marca além de preto/branco/cinza é usada nesses dois modelos de referência — por padrão, materiais impressos devem seguir a mesma sobriedade (texto preto, linhas cinza-claro, sem faixas coloridas).

## Ativos disponíveis (`assets/`)

- `cib-logo-header.png` — logo já recortado no formato usado no cabeçalho (ícone + wordmark, sem slogan).
- `MontserratMedium-regular.ttf`, `MontserratMedium-bold.ttf`, `MontserratMedium-italic.ttf`, `MontserratMedium-boldItalic.ttf` — fonte oficial.

## Gerador de referência

[`gerar_diario_pdf.py`](gerar_diario_pdf.py) implementa esse padrão em Python (reportlab) e serve de modelo para gerar qualquer novo material em PDF já dentro das normas do CIB — cabeçalho, moldura e tipografia inclusos. Reutilizar essa base para os próximos materiais da eletiva.

[`dividir_diario_pdf.py`](dividir_diario_pdf.py) gera o Diário completo e divide em PDFs avulsos (capa + Aula 1 + Aula 2 juntas; Aulas 3 a 17 uma por PDF) em `diario_avulso/`, para pedir impressão semanal à secretaria em vez do caderno inteiro de uma vez. Requer `qpdf` instalado (`apt-get install -y qpdf`).

## Jogo dos 10 Cartões (`dados_jogo_10_cartoes.py`, `logos_svg.py`)

Fonte única dos dados (empresas, país, fatos validados) e dos logos ilustrativos (desenho próprio em SVG, não os logotipos oficiais) usados tanto no PDF do jogo (`gerar_jogo_cartoes_pdf.py`) quanto na versão digital (`gerar_jogo_html.py`) e na apresentação de slides — assim os três materiais nunca ficam dessincronizados.

- `gerar_logos_png.py` — renderiza `logos_svg.py` como PNG 512×512 (`assets/logos/`) via Playwright/Chromium, para uso em formatos que não aceitam SVG (como PPTX). Rodar de novo sempre que `logos_svg.py` mudar.

## Apresentações de slides (`apresentacao_base.js`, `gerar_apresentacao_aulaN_pptx.js`)

`apresentacao_base.js` centraliza o sistema visual das apresentações (Node.js, `pptxgenjs`): paleta (navy + terracota), fontes (Cambria/Calibri), logo do CIB e os helpers de layout (`eyebrow`, `cibLogo`, `dotCluster`, `statColumn`, `imagePlaceholder`, `footer`). **Não** segue o padrão de cabeçalho/moldura do CIB usado no material impresso do aluno (seção acima) — é uma identidade própria para projeção em sala. Cada `gerar_apresentacao_aulaN_pptx.js` importa esse módulo e só define o conteúdo daquela aula, para toda apresentação do semestre manter a mesma cara.

- `gerar_apresentacao_aula1_pptx.js` → `Aula 1 - Apresentacao.pptx` — números de impacto de Israel + as 8 empresas do Jogo dos 10 Cartões.
- `gerar_apresentacao_aula2_pptx.js` → `Aula 2 - Apresentacao.pptx` — 3 inovações israelenses reais (irrigação por gotejamento/Netafim, Moovit, PillCam), cada uma nascida de alguém que escolheu o caminho mais trabalhoso; é inspiração real, não o "gabarito" dos problemas fictícios de `ferramentas/problemas-caminhos-aula2.md`. Cada slide de inovação tem um quadrante (`imagePlaceholder`) para o professor colar uma foto própria — não há como buscar imagens reais neste ambiente — e um vídeo sugerido (link encontrado por busca, não assistido por aqui: conferir antes de exibir em sala).
- `gerar_apresentacao_aula3_pptx.js` → `Aula 3 - Apresentacao.pptx` — apoio conceitual da aula sobre chutzpah: reenquadra a palavra como atitude (com o exemplo do soldado que pode questionar um general), explica chevruta e beit midrash, e mostra a mecânica do rodízio em duplas com as 3 perguntas-guia. Não repete o conteúdo das fichas de `ferramentas/fichas-produtos-israelenses.md` — cada dupla recebe uma delas na hora.

Dados checados em fontes públicas (ver rodapé/citações nos próprios slides). Texto sem travessões (—) de propósito, para não ficar com "cara de IA"; usar vírgula, dois-pontos ou parênteses no lugar. Depende de `npm install` dentro de `padronizacao/` (só `pptxgenjs`, ver `package.json`).

## PDF de Problemas e Caminhos (`gerar_problemas_caminhos_pdf.py`)

Gera `Problemas e Caminhos - Aula 2.pdf` (reportlab, texto simples, **sem** o cabeçalho institucional do CIB usado nos outros PDFs, a pedido do professor): guia rápido para o professor + 3 problemas fictícios (uma página cada), cada um com espaço para o grupo escrever a própria ideia ("Como eu resolvo?") antes de ler os 3 caminhos possíveis e a consequência de cada um, terminando numa pergunta de reflexão. Texto sincronizado manualmente com `ferramentas/problemas-caminhos-aula2.md`.
