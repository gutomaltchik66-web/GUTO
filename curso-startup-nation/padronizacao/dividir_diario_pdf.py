# -*- coding: utf-8 -*-
"""
Divide o Diário do Empreendedor (gerado por gerar_diario_pdf.py) em PDFs
avulsos, para impressão semanal aula a aula em vez do caderno inteiro de
uma vez: capa + Aula 1 + Aula 2 saem juntas num único PDF (primeira
semana), e cada aula seguinte (3 a 17) sai em um PDF de página única.

Requer o utilitário de linha de comando `qpdf` (apt-get install -y qpdf).

Uso: python3 dividir_diario_pdf.py
Saída: padronizacao/diario_avulso/ (não versionado — regenerar quando o
conteúdo do Diário mudar).
"""
import os
import re
import subprocess
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gerar_diario_pdf as diario  # regenera o PDF completo ao importar

SRC = os.path.join(HERE, "Diario do Empreendedor - Caderno do Aluno.pdf")
OUT_DIR = os.path.join(HERE, "diario_avulso")


def slugify(text, max_len=60):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", " ", text).strip()
    return text[:max_len].strip()


def qpdf_extract(pages_spec, out_path):
    subprocess.run(["qpdf", SRC, "--pages", ".", pages_spec, "--", out_path], check=True)


os.makedirs(OUT_DIR, exist_ok=True)
for f in os.listdir(OUT_DIR):
    os.remove(os.path.join(OUT_DIR, f))

# Página 1 = capa; página N (para aula de número N-1) = N-1 + 1.
aulas_por_numero = {n: tema for (n, tema, _fonte, _trecho, _p1) in diario.aulas}

qpdf_extract("1-3", os.path.join(OUT_DIR, "00 - Capa + Aula 1 e 2.pdf"))

for n in range(3, 18):
    page = n + 1
    nome = f"{n:02d} - Aula {n} - {slugify(aulas_por_numero[n])}.pdf"
    qpdf_extract(str(page), os.path.join(OUT_DIR, nome))

print(f"{len(os.listdir(OUT_DIR))} PDFs avulsos gerados em {OUT_DIR}")
