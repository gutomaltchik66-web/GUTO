# Ferramenta 0 — Diário do Empreendedor

**Para que serve:** é a tarefa que se repete em **todas as 17 aulas**, sempre no mesmo formato — não são fichas soltas e diferentes a cada semana, mas **um único caderno/booklet que cada aluno mantém e preenche do início ao fim do semestre**. Isso dá à turma uma rotina idêntica (menos bagunça no fechamento da aula) e, ao mesmo tempo, uma citação da Torá conectada ao tema de cada dia.

**Quando usar:** no fechamento de todas as aulas, sem exceção — é o "ritual" fixo da eletiva. A pergunta 2 ("O que eu aprendi na aula de hoje?") só faz sentido depois do conteúdo da aula, então o Diário é preenchido nos últimos 10 minutos, não na entrada. Em algumas aulas a citação é lida em voz alta já na abertura (como gancho motivacional) e revisitada no Diário ao final — ver o roteiro de cada plano de aula.

**Padronização CIB:** a versão impressa (PDF) segue o cabeçalho oficial obrigatório do colégio para material de Ensino Fundamental 2 — ver especificação completa em [`../padronizacao/README.md`](../padronizacao/README.md) e o gerador em [`../padronizacao/gerar_diario_pdf.py`](../padronizacao/gerar_diario_pdf.py). Toda página traz "Ensino Fundamental 2" + logo do CIB, campos "Aluno(a) / Ano Escolar / Turma / Data" e moldura de página, no padrão dos modelos oficiais (Cabeçalho Editável EF2 e Pauta Pequena). A capa traz o título, o escudo do colégio e uma caixa grande em branco para o aluno desenhar/personalizar o próprio caderno.

## Montagem (antes da Aula 1)

Cada aluno recebe (ou monta, grampeando folhas) um caderno simples de 17 páginas numeradas, uma por aula, com o mesmo modelo de página abaixo. Pode ser um caderno físico dedicado só à eletiva, ou uma seção separada do caderno da disciplina.

## Modelo de página (repetido em toda aula)

```
AULA Nº: ___   DATA: ___/___   TEMA: _______________________

┌─────────────────────────────────────────────────────┐
│  "[citação livre da Torá — diferente em cada uma      │
│  das 17 aulas, centralizada, sem rótulo]"              │
│    — [livro em português]  [livro em hebraico]  [cap:versículo] │
└─────────────────────────────────────────────────────┘

1) [pergunta ligada ao trecho — diferente em cada aula]



2) O que eu aprendi na aula de hoje?

```

## As duas perguntas

1. **Pergunta 1 — ligada ao trecho** — diferente em cada uma das 17 aulas, conecta a citação da Torá ao tema do dia (ex: Êxodo 17:6, Moshé faz água sair da rocha, ligado à pergunta "que obstáculo você já viu virar solução?", na aula de escassez/inovação). O repertório completo das 17 citações e perguntas está em [`../padronizacao/gerar_diario_pdf.py`](../padronizacao/gerar_diario_pdf.py).
2. **Pergunta 2 — fixa** — sempre a mesma nas 17 páginas: *"O que eu aprendi na aula de hoje?"*. Respondida no fechamento da aula (não faz sentido perguntar isso na entrada, antes do conteúdo do dia).

## Sobre as citações

Todas as 17 citações são exclusivamente da **Torá** (os cinco livros de Moshé: Gênesis, Êxodo, Levítico, Números e Deuteronômio) — sem Mishná, Pirkei Avot ou Talmud. A citação aparece direto na página, sem rótulo, centralizada e enquadrada numa caixa. Na linha de referência, o nome do livro em português vem acompanhado do nome em hebraico (ex: "Gênesis בְּרֵאשִׁית", "Êxodo שְׁמוֹת"), reforçando o vínculo com a fonte original.

## Por que funciona com turma agitada

- Rotina idêntica em toda aula = menos tempo de instrução, menos brecha para dispersão.
- Tarefa individual e silenciosa no fechamento da aula cria um momento de foco depois das atividades em grupo, que são mais barulhentas por natureza.
- Por ser um caderno único (não folhas soltas), não se perde entre uma aula e outra, e vira material de consulta para o próprio aluno.
- Substitui qualquer necessidade de celular: é só papel e caneta.
- A citação da Torá reforça, aula após aula, que a Startup Nation e a tradição judaica caminham juntas — não é um "tema bônus" isolado, mas o fio condutor de cada página.
