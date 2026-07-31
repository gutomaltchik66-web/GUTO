# Padronização de materiais didáticos — CIB

Especificação extraída dos modelos oficiais do Colégio Israelita Brasileiro (recebidos por e-mail): `PAUTA_PEQUENA.pdf`, `FOLHATIMBRADA.docx` e `CABEÇALHO EDITÁVEL EF2.docx`. Todo material didático produzido para a eletiva Start Up Nation segue este padrão.

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
