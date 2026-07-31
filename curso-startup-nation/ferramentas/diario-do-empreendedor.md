# Ferramenta 0 — Diário do Empreendedor

**Para que serve:** é a tarefa que se repete em **todas as 17 aulas**, sempre no mesmo formato — não são fichas soltas e diferentes a cada semana, mas **um único caderno/booklet que cada aluno mantém e preenche do início ao fim do semestre**. Isso dá à turma uma rotina idêntica (menos bagunça na entrada da aula) e, ao mesmo tempo, um fio contínuo que mostra a evolução da própria ideia, aula após aula — além de trazer, em toda página, uma conexão direta entre a fonte judaica e o conteúdo de empreendedorismo do dia.

**Quando usar:** no início de todas as aulas, sem exceção. É o "ritual" fixo da eletiva.

**Padronização CIB:** a versão impressa (PDF) segue o cabeçalho oficial obrigatório do colégio para material de Ensino Fundamental 2 — ver especificação completa em [`../padronizacao/README.md`](../padronizacao/README.md) e o gerador em [`../padronizacao/gerar_diario_pdf.py`](../padronizacao/gerar_diario_pdf.py). Toda página traz "Ensino Fundamental 2" + logo do CIB, campos "Aluno(a) / Ano Escolar / Turma / Data" e moldura de página, no padrão dos modelos oficiais (Cabeçalho Editável EF2 e Pauta Pequena).

## Montagem (antes da Aula 1)

Cada aluno recebe (ou monta, grampeando folhas) um caderno simples de 17 páginas numeradas, uma por aula, com o mesmo modelo de página abaixo. Pode ser um caderno físico dedicado só à eletiva, ou uma seção separada do caderno da disciplina.

## Modelo de página (repetido em toda aula)

```
AULA Nº: ___   DATA: ___/___   TEMA: _______________________

── TRECHO DA TRADIÇÃO JUDAICA ──

"[citação de uma fonte judaica — Torá, Neviim, Ketuvim, Mishná/Pirkei
Avot ou Talmud — diferente em cada uma das 17 aulas]"
— [referência da fonte]

── QUESTÕES DO DIA ──

1. Ligada ao trecho acima:
[pergunta que conecta a fonte judaica ao tema da aula]


2. Sobre o tema de hoje:
[pergunta sobre o conteúdo específico da aula — ver plano de cada aula]


── MINHA IDEIA HOJE (uma frase, mesmo que ainda não tenha certeza) ──


```

## As três partes

1. **Trecho da Tradição Judaica** — uma citação curta (frase ou parágrafo) de uma fonte judaica diferente em cada uma das 17 aulas, escolhida por sua conexão com o tema daquele dia (ex: Isaías 35:1 sobre o deserto florescer, na aula de escassez/inovação; Pirkei Avot 1:17 sobre ação, na aula de protótipo). O repertório completo das 17 fontes está em [`../padronizacao/gerar_diario_pdf.py`](../padronizacao/gerar_diario_pdf.py).
2. **Questões do Dia (2 perguntas, preenchidas no início da aula)** — a primeira sempre pede para o aluno relacionar o trecho judaico ao tema da aula; a segunda é uma pergunta direta sobre o conteúdo do dia (a mesma "pergunta do dia" indicada no roteiro de cada plano de aula). Substituem o antigo formato de Entrada/Saída por um único momento de reflexão mais rico, no começo da aula.
3. **Minha ideia hoje (1 frase, o fio contínuo do semestre)** — a mesma linha, em toda página, do início ao fim do semestre. Nas primeiras aulas pode ser só um palpite vago ("ainda não sei", "algo relacionado a..."); a partir da Aula 7 (lançamento do desafio) começa a ganhar forma; nas Aulas 8–13 acompanha a evolução direta do projeto. É o único item que compara diretamente a página de hoje com a de semanas atrás — vale reler o caderno inteiro na Aula 17.

## Por que funciona com turma agitada

- Rotina idêntica em toda aula = menos tempo de instrução, menos brecha para dispersão.
- Tarefa individual e silenciosa logo na entrada da aula cria uma "borda" de foco antes das atividades em grupo, que são mais barulhentas por natureza.
- Por ser um caderno único (não folhas soltas), não se perde entre uma aula e outra, e vira material de consulta para o próprio aluno.
- Substitui qualquer necessidade de celular: é só papel e caneta.
- A leitura do trecho judaico reforça, aula após aula, que a Startup Nation e a tradição judaica caminham juntas — não é um "tema bônus" isolado, mas o fio condutor de cada página.
