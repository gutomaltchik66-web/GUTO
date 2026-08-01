# -*- coding: utf-8 -*-
"""
Jogo dos 10 Cartões (Aula 1) — versão digital/interativa em HTML único
(sem internet, sem impressão), para projetar em sala. Mesma base de dados
validada do gerador de PDF (dados_jogo_10_cartoes.py), com logos ilustrativos
(desenhados em SVG, não são os logotipos oficiais das marcas) como pista
visual extra para o jogo de adivinhação.

Uso: abrir o .html gerado direto no navegador — não depende de internet
nem de nenhum arquivo externo (fonte e ícones estão embutidos no arquivo).
"""
import base64
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
sys.path.insert(0, HERE)
from dados_jogo_10_cartoes import CARTOES, GABARITO, FONTE_NOTA
from logos_svg import LOGOS


def font_b64(filename):
    with open(os.path.join(ASSETS, filename), "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


FONT_REGULAR = font_b64("MontserratMedium-regular.ttf")
FONT_BOLD = font_b64("MontserratMedium-bold.ttf")
FONT_ITALIC = font_b64("MontserratMedium-italic.ttf")

FLAGS = {"Israel": "🇮🇱", "Suécia": "🇸🇪", "Suécia/Dinamarca": "🇸🇪🇩🇰"}


def esc(s):
    return html.escape(s, quote=True)


def build_card(idx, card_id, nome, problema, solucao):
    is_israel, pais, fato = GABARITO[card_id]
    flag = FLAGS.get(pais, "🌍")
    logo_svg = LOGOS[card_id]
    verdict_word = "ISRAELENSE" if is_israel else "NÃO É ISRAELENSE"
    return f"""
      <li class="card" data-id="{card_id}" data-israel="{"1" if is_israel else "0"}" tabindex="0" role="button"
          aria-pressed="false" aria-label="Cartão {idx}, {esc(nome)}. Clique para marcar como pegadinha.">
        <div class="card-inner">
          <div class="card-face card-front">
            <div class="card-top">
              <span class="card-index">{idx:02d}</span>
              <svg class="card-logo" viewBox="0 0 64 64" aria-hidden="true">{logo_svg}</svg>
            </div>
            <h3 class="card-name">{esc(nome)}</h3>
            <p class="card-field"><span class="card-label">Problema</span>{esc(problema)}</p>
            <p class="card-field"><span class="card-label">Solução</span>{esc(solucao)}</p>
            <div class="card-pick">
              <span class="pick-dot" aria-hidden="true"></span>
              <span class="pick-text">Marcada como pegadinha</span>
            </div>
          </div>
          <div class="card-face card-back">
            <div class="back-flag" aria-hidden="true">{flag}</div>
            <p class="back-verdict">{verdict_word}</p>
            <p class="back-country">{esc(pais)}</p>
            <p class="back-fact">{esc(fato)}</p>
            <div class="back-result" aria-hidden="true"></div>
          </div>
        </div>
      </li>"""


def build_gabarito_row(nome, card_id):
    is_israel, pais, fato = GABARITO[card_id]
    pais_label = pais if is_israel else f"{pais} — pegadinha"
    return f"""
        <tr>
          <td>{esc(nome)}</td>
          <td>{esc(pais_label)}</td>
          <td>{esc(fato)}</td>
        </tr>"""


cards_html = "\n".join(
    build_card(i + 1, cid, nome, problema, solucao)
    for i, (cid, nome, problema, solucao) in enumerate(CARTOES)
)
gabarito_html = "\n".join(
    build_gabarito_row(nome, cid) for (cid, nome, _p, _s) in CARTOES
)

HTML = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jogo dos 10 Cartões — Aula 1 — StartUp Nation</title>
<style>
@font-face {
  font-family: "Montserrat";
  font-weight: 400;
  font-style: normal;
  src: url(data:font/ttf;base64,__FONT_REGULAR__) format("truetype");
}
@font-face {
  font-family: "Montserrat";
  font-weight: 700;
  font-style: normal;
  src: url(data:font/ttf;base64,__FONT_BOLD__) format("truetype");
}
@font-face {
  font-family: "Montserrat";
  font-weight: 400;
  font-style: italic;
  src: url(data:font/ttf;base64,__FONT_ITALIC__) format("truetype");
}

:root {
  --bg: #F7F6F2;
  --surface: #FFFFFF;
  --surface-2: #F0EFE9;
  --ink: #1B1B18;
  --ink-soft: #5B594F;
  --line: #E2DFD3;
  --accent: #1955C7;
  --accent-soft: #E7EEFC;
  --accent-ink: #0E2E6E;
  --good: #1F8A57;
  --good-soft: #E4F5EC;
  --bad: #C1392B;
  --bad-soft: #FBEAE7;
  --radius-lg: 18px;
  --radius-md: 12px;
  --shadow: 0 1px 2px rgba(20,20,10,.04), 0 8px 24px -12px rgba(20,20,10,.18);
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #15161A;
    --surface: #1E1F24;
    --surface-2: #26272D;
    --ink: #F1F0EA;
    --ink-soft: #ACA99D;
    --line: #34353C;
    --accent: #6C97F2;
    --accent-soft: #202B45;
    --accent-ink: #CBDBFB;
    --good: #45C186;
    --good-soft: #17301F;
    --bad: #E2695D;
    --bad-soft: #3A1E1B;
    --shadow: 0 1px 2px rgba(0,0,0,.3), 0 8px 24px -12px rgba(0,0,0,.55);
  }
}
:root[data-theme="dark"] {
  --bg: #15161A; --surface: #1E1F24; --surface-2: #26272D; --ink: #F1F0EA; --ink-soft: #ACA99D;
  --line: #34353C; --accent: #6C97F2; --accent-soft: #202B45; --accent-ink: #CBDBFB;
  --good: #45C186; --good-soft: #17301F; --bad: #E2695D; --bad-soft: #3A1E1B;
  --shadow: 0 1px 2px rgba(0,0,0,.3), 0 8px 24px -12px rgba(0,0,0,.55);
}
:root[data-theme="light"] {
  --bg: #F7F6F2; --surface: #FFFFFF; --surface-2: #F0EFE9; --ink: #1B1B18; --ink-soft: #5B594F;
  --line: #E2DFD3; --accent: #1955C7; --accent-soft: #E7EEFC; --accent-ink: #0E2E6E;
  --good: #1F8A57; --good-soft: #E4F5EC; --bad: #C1392B; --bad-soft: #FBEAE7;
  --shadow: 0 1px 2px rgba(20,20,10,.04), 0 8px 24px -12px rgba(20,20,10,.18);
}

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  background: var(--bg);
  color: var(--ink);
  font-family: "Montserrat", "Segoe UI", system-ui, sans-serif;
  font-weight: 400;
  line-height: 1.45;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}
.wrap { max-width: 1180px; margin: 0 auto; padding: 0 24px 64px; }

.masthead {
  border-bottom: 1px solid var(--line);
  background: var(--surface);
  position: sticky;
  top: 0;
  z-index: 20;
}
.masthead-inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: 18px 24px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px 28px;
}
.eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--ink-soft);
  display: block;
  margin: 0 0 4px;
}
.masthead h1 {
  font-size: clamp(20px, 2.6vw, 27px);
  font-weight: 700;
  margin: 0;
  letter-spacing: -0.01em;
  text-wrap: balance;
}
.masthead-meta { flex: 1 1 auto; min-width: 220px; }

.status {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13.5px;
  color: var(--ink-soft);
  font-variant-numeric: tabular-nums;
}
.status strong { color: var(--ink); font-weight: 700; }
.status-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 30px;
  height: 30px;
  padding: 0 9px;
  border-radius: 999px;
  background: var(--accent-soft);
  color: var(--accent-ink);
  font-weight: 700;
  font-size: 14px;
  transition: transform .15s ease;
}
.status-badge.pulse { transform: scale(1.14); }

.controls { display: flex; gap: 10px; flex-wrap: wrap; }
button {
  font-family: inherit;
  font-weight: 700;
  font-size: 13.5px;
  border-radius: 999px;
  padding: 10px 18px;
  border: 1px solid transparent;
  cursor: pointer;
  transition: background .15s ease, border-color .15s ease, transform .1s ease, color .15s ease;
}
button:active { transform: scale(.97); }
button:focus-visible, .card:focus-visible, summary:focus-visible {
  outline: 2.5px solid var(--accent);
  outline-offset: 2px;
}
.btn-primary { background: var(--accent); color: #fff; }
.btn-primary:hover { background: var(--accent-ink); }
.btn-primary:disabled { background: var(--surface-2); color: var(--ink-soft); cursor: not-allowed; }
.btn-ghost { background: transparent; border-color: var(--line); color: var(--ink); }
.btn-ghost:hover { border-color: var(--ink-soft); }

.section-gap { margin-top: 28px; }

details.panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 4px 22px;
  margin-top: 18px;
}
details.panel summary {
  cursor: pointer;
  list-style: none;
  padding: 16px 0;
  font-weight: 700;
  font-size: 14.5px;
  display: flex;
  align-items: center;
  gap: 10px;
}
details.panel summary::-webkit-details-marker { display: none; }
details.panel summary::before {
  content: "";
  width: 8px; height: 8px;
  border-right: 2px solid var(--ink-soft);
  border-bottom: 2px solid var(--ink-soft);
  transform: rotate(-45deg);
  transition: transform .15s ease;
  flex: none;
}
details.panel[open] summary::before { transform: rotate(45deg); }
.panel-body { padding: 0 0 20px; color: var(--ink-soft); font-size: 14px; }
.panel-body ol { margin: 0; padding-left: 20px; display: grid; gap: 10px; }
.panel-body li::marker { color: var(--accent); font-weight: 700; }
.panel-body strong { color: var(--ink); }
.panel-note {
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid var(--line);
  font-style: italic;
  font-size: 12.5px;
}

.grid {
  list-style: none;
  margin: 22px 0 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
  perspective: 1400px;
}

.card {
  position: relative;
  height: 300px;
  border-radius: var(--radius-lg);
  cursor: pointer;
  outline-offset: 3px;
}
.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform .55s cubic-bezier(.4,.2,.2,1);
  transform-style: preserve-3d;
}
.card[data-revealed="1"] .card-inner { transform: rotateY(180deg); }
.card[data-flipped="1"] .card-inner { transform: rotateY(180deg); }
.card[data-revealed="1"][data-flipped="1"] .card-inner { transform: rotateY(0deg); }

.card-face {
  position: absolute;
  inset: 0;
  border-radius: var(--radius-lg);
  border: 1.5px solid var(--line);
  background: var(--surface);
  box-shadow: var(--shadow);
  backface-visibility: hidden;
  padding: 16px 17px 15px;
  display: flex;
  flex-direction: column;
}
.card-back {
  transform: rotateY(180deg);
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 6px;
  background: var(--surface-2);
}
.card:not([data-revealed="1"]):hover .card-face.card-front { border-color: var(--accent); }
.card.is-selected .card-face.card-front { border-color: var(--accent); background: var(--accent-soft); }
.card[data-revealed="1"].is-correct .card-face.card-back { border-color: var(--good); background: var(--good-soft); }
.card[data-revealed="1"].is-wrong .card-face.card-back { border-color: var(--bad); background: var(--bad-soft); }

.card-top { display: flex; align-items: flex-start; justify-content: space-between; }
.card-index {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  color: var(--ink-soft);
  font-variant-numeric: tabular-nums;
}
.card-logo { width: 46px; height: 46px; flex: none; }
.card-name { font-size: 16.5px; font-weight: 700; margin: 10px 0 8px; letter-spacing: -0.01em; }
.card-field { margin: 0 0 7px; font-size: 12.6px; color: var(--ink-soft); line-height: 1.4; }
.card-field:last-of-type { margin-bottom: auto; }
.card-label {
  display: block;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--ink);
  margin-bottom: 2px;
}
.card-pick {
  display: flex;
  align-items: center;
  gap: 7px;
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px dashed var(--line);
  font-size: 11.5px;
  font-weight: 700;
  color: var(--ink-soft);
}
.pick-dot {
  width: 15px; height: 15px;
  border-radius: 50%;
  border: 1.5px solid var(--ink-soft);
  flex: none;
  transition: background .15s ease, border-color .15s ease;
}
.card.is-selected .pick-dot { background: var(--accent); border-color: var(--accent); }
.card.is-selected .pick-text { color: var(--accent-ink); }

.back-flag { font-size: 30px; line-height: 1; }
.back-verdict {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .08em;
  color: var(--ink-soft);
  margin: 2px 0 0;
}
.back-country { font-size: 17px; font-weight: 700; margin: 0; }
.back-fact { font-size: 12px; color: var(--ink-soft); margin: 2px 0 0; max-width: 46ch; }
.back-result { font-size: 11.5px; font-weight: 700; margin-top: 4px; }
.card.is-correct .back-result::before { content: "✓ seu grupo acertou esta"; color: var(--good); }
.card.is-wrong .back-result::before { content: "✗ seu grupo errou esta"; color: var(--bad); }

.hint {
  margin-top: 14px;
  font-size: 13px;
  color: var(--ink-soft);
  min-height: 20px;
}
.hint.show-warn { color: var(--bad); font-weight: 700; }

.summary {
  margin-top: 22px;
  padding: 20px 24px;
  border-radius: var(--radius-lg);
  background: var(--accent-soft);
  border: 1px solid var(--accent);
  display: none;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
}
.summary.show { display: flex; }
.summary-score { font-size: 30px; font-weight: 700; color: var(--accent-ink); font-variant-numeric: tabular-nums; }
.summary-text { color: var(--ink); font-size: 14px; max-width: 52ch; }
.summary-text strong { color: var(--accent-ink); }

.gabarito-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.gabarito-table caption { text-align: left; font-size: 12px; font-style: italic; color: var(--ink-soft); margin-bottom: 10px; }
.gabarito-table th, .gabarito-table td { text-align: left; padding: 9px 12px 9px 0; border-bottom: 1px solid var(--line); vertical-align: top; }
.gabarito-table th { font-size: 10.5px; text-transform: uppercase; letter-spacing: .06em; color: var(--ink-soft); }
.gabarito-table td:first-child { font-weight: 700; white-space: nowrap; }
.table-scroll { overflow-x: auto; }
.teacher-warn {
  display: inline-block;
  margin-bottom: 12px;
  padding: 3px 10px;
  border-radius: 999px;
  background: var(--bad-soft);
  color: var(--bad);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .04em;
  text-transform: uppercase;
}

footer {
  margin-top: 40px;
  padding-top: 18px;
  border-top: 1px solid var(--line);
  font-size: 12px;
  font-style: italic;
  color: var(--ink-soft);
}

@media (prefers-reduced-motion: reduce) {
  .card-inner, .status-badge { transition: none !important; }
}
</style>
</head>
<body>
<header class="masthead">
  <div class="masthead-inner">
    <div class="masthead-meta">
      <span class="eyebrow">Ensino Fundamental 2 · Eletiva StartUp Nation · Aula 1</span>
      <h1>Jogo dos 10 Cartões</h1>
    </div>
    <div class="status">
      <span class="status-badge" id="counterBadge">0/2</span>
      <span>pegadinhas marcadas</span>
    </div>
    <div class="controls">
      <button type="button" class="btn-ghost" id="btnReset">Reiniciar</button>
      <button type="button" class="btn-primary" id="btnReveal">Revelar respostas</button>
    </div>
  </div>
</header>

<main class="wrap">
  <details class="panel section-gap" open>
    <summary>Como jogar</summary>
    <div class="panel-body">
      <ol>
        <li>Turma de ~20 alunos: <strong>5 grupos de 4</strong>. Cada rodada, um grupo por vez decide em voz alta com a turma.</li>
        <li>Os 10 cartões abaixo trazem logo, nome, problema e solução de cada produto — <strong>sem o país de origem</strong>.</li>
        <li>Sem celular, sem pesquisar: só leitura, observação do logo e argumentação em grupo (25 min).</li>
        <li>Cliquem nos <strong>2 cartões</strong> que o grupo acredita <strong>NÃO serem israelenses</strong> — é a pegadinha.</li>
        <li>Quando todos os grupos tiverem decidido, cliquem em <strong>“Revelar respostas”</strong> para conferir cartão a cartão (15 min).</li>
        <li>“Reiniciar” zera as marcações para jogar de novo com outra turma ou turno.</li>
      </ol>
      <p class="panel-note">Objetivo pedagógico: não é “decorar que Israel é inovador” — é treinar o raciocínio de problema → solução em qualquer produto, e só depois perceber a escala do fenômeno (8 em cada 10 produtos do dia a dia dos alunos, neste jogo, vieram de Israel).</p>
    </div>
  </details>

  <ul class="grid" id="grid">__CARDS__
  </ul>

  <p class="hint" id="hint" aria-live="polite"></p>

  <div class="summary" id="summary" role="status" aria-live="polite">
    <div class="summary-score" id="summaryScore">0/10</div>
    <div class="summary-text" id="summaryText"></div>
  </div>

  <details class="panel section-gap" id="teacherPanel">
    <summary>Modo professor — gabarito completo</summary>
    <div class="panel-body">
      <span class="teacher-warn">Não mostrar aos alunos antes da rodada</span>
      <div class="table-scroll">
        <table class="gabarito-table">
          <caption>Fundadores, ano de fundação e valor de aquisição checados em fontes públicas.</caption>
          <thead>
            <tr><th>Produto</th><th>País</th><th>Fato validado</th></tr>
          </thead>
          <tbody>__GABARITO_ROWS__
          </tbody>
        </table>
      </div>
    </div>
  </details>

  <footer>__FONTE_NOTA__ Os logos são ilustrações próprias (não os logotipos oficiais das marcas), usadas só como pista visual do jogo.</footer>
</main>

<script>
(function () {
  "use strict";
  var grid = document.getElementById("grid");
  var cards = Array.prototype.slice.call(grid.querySelectorAll(".card"));
  var counterBadge = document.getElementById("counterBadge");
  var hint = document.getElementById("hint");
  var btnReveal = document.getElementById("btnReveal");
  var btnReset = document.getElementById("btnReset");
  var summary = document.getElementById("summary");
  var summaryScore = document.getElementById("summaryScore");
  var summaryText = document.getElementById("summaryText");

  var selected = new Set();
  var revealed = false;

  function pulseCounter() {
    counterBadge.classList.remove("pulse");
    void counterBadge.offsetWidth;
    counterBadge.classList.add("pulse");
  }

  function setHint(msg, warn) {
    hint.textContent = msg || "";
    hint.classList.toggle("show-warn", !!warn);
  }

  function updateCounter() {
    counterBadge.textContent = selected.size + "/2";
  }

  function toggleSelect(card) {
    if (revealed) {
      var isFlipped = card.getAttribute("data-flipped") === "1";
      card.setAttribute("data-flipped", isFlipped ? "0" : "1");
      return;
    }
    var id = card.dataset.id;
    if (selected.has(id)) {
      selected.delete(id);
      card.classList.remove("is-selected");
      card.setAttribute("aria-pressed", "false");
      setHint("");
    } else {
      if (selected.size >= 2) {
        setHint("Vocês já marcaram 2 cartões — desmarquem um antes de escolher outro.", true);
        return;
      }
      selected.add(id);
      card.classList.add("is-selected");
      card.setAttribute("aria-pressed", "true");
      setHint("");
    }
    updateCounter();
    pulseCounter();
  }

  cards.forEach(function (card) {
    card.addEventListener("click", function () { toggleSelect(card); });
    card.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        toggleSelect(card);
      }
    });
  });

  btnReveal.addEventListener("click", function () {
    if (revealed) return;
    revealed = true;
    var correctCount = 0;
    var pegadinhaCerta = 0;
    cards.forEach(function (card) {
      var isIsrael = card.dataset.israel === "1";
      var wasSelected = selected.has(card.dataset.id);
      var isCorrect = wasSelected === !isIsrael;
      if (isCorrect) correctCount++;
      if (!isIsrael && wasSelected) pegadinhaCerta++;
      card.classList.toggle("is-correct", isCorrect);
      card.classList.toggle("is-wrong", !isCorrect);
      card.setAttribute("data-revealed", "1");
      card.setAttribute("aria-label", card.querySelector(".card-name").textContent + ", revelado.");
    });
    btnReveal.disabled = true;
    setHint("Clique em qualquer cartão para ver a frente ou o verso de novo.");
    summary.classList.add("show");
    summaryScore.textContent = correctCount + "/10";
    summaryText.innerHTML = "classificações corretas. Pegadinhas certas: <strong>" + pegadinhaCerta + "/2</strong>.";
  });

  btnReset.addEventListener("click", function () {
    revealed = false;
    selected.clear();
    btnReveal.disabled = false;
    summary.classList.remove("show");
    setHint("");
    updateCounter();
    cards.forEach(function (card) {
      card.classList.remove("is-selected", "is-correct", "is-wrong");
      card.removeAttribute("data-revealed");
      card.removeAttribute("data-flipped");
      card.setAttribute("aria-pressed", "false");
      var nome = card.querySelector(".card-name").textContent;
      card.setAttribute("aria-label", "Cartão " + card.querySelector(".card-index").textContent + ", " + nome + ". Clique para marcar como pegadinha.");
    });
  });
})();
</script>
</body>
</html>
"""

HTML = (HTML
        .replace("__FONT_REGULAR__", FONT_REGULAR)
        .replace("__FONT_BOLD__", FONT_BOLD)
        .replace("__FONT_ITALIC__", FONT_ITALIC)
        .replace("__CARDS__", cards_html)
        .replace("__GABARITO_ROWS__", gabarito_html)
        .replace("__FONTE_NOTA__", esc(FONTE_NOTA)))

OUT_PATH = os.path.join(HERE, "Jogo dos 10 Cartoes - Aula 1.html")
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(HTML)

print("HTML gerado com sucesso:", OUT_PATH)
