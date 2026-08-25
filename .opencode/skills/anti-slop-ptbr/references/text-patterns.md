---
name: text-patterns
description: Guia de referência para detectar padrões de slop de IA em texto em português brasileiro, incluindo frases de alto risco, muletas de transição, buzzwords, calcos de tradução e padrões estruturais. Use como referência ao revisar a qualidade de textos.
---

# Padrões de slop textual

Catálogo dos padrões de "slop de IA" (padrões genéricos e de baixa qualidade que denunciam conteúdo gerado por inteligência artificial) mais comuns em texto corrido em português brasileiro. Cada padrão traz a forma canônica, variações, um exemplo e a substituição sugerida.

Escala de risco: **alto** = quase sempre slop, uma ocorrência já pesa; **médio** = depende de densidade, posição e contexto; **baixo** = só soma com outros sinais. Nenhum sinal isolado prova geração por IA, com uma exceção: os resíduos determinísticos da seção 11, individualmente quase-prova. A regra do acúmulo está na seção 14.

## Sumário

1. Frases de alto risco
2. Muletas de transição
3. Atenuação excessiva (hedging)
4. Meta-comentário
5. Buzzwords corporativas e linkedinês
6. Redundâncias e pleonasmos
7. Construções prolixas
8. Calcos de tradução do inglês
9. Padrões estruturais e tipográficos
10. Dialeto "redação ENEM"
11. Resíduos determinísticos de chat e modelo (quase-prova)
12. Informalidade performática
13. Sinais inversos (marcas humanas)
14. Padrões de detecção
15. Estratégias de limpeza
16. O contexto importa

## 1. Frases de alto risco

Fórmulas de frase quase determinísticas. Uma ocorrência é retórica tolerável; duas ou mais no mesmo texto formam assinatura.

**1.1 Contraste de negação "não é X, é Y"** (alto). A fórmula mais denunciada em pt-BR (Octans: 11,5% dos posts de LinkedIn, impacto negativo no engajamento). Variações: "não é sobre X, é sobre Y"; "não se trata de X, mas sim de Y"; "a questão não é X, e sim Y"; "mais do que um X, é um Y".
- Exemplo: "Não é sobre ferramentas. É sobre pessoas." → Afirmar Y diretamente, com o porquê: "Aumentar cliques só funciona quando há conexão real com o público."

**1.2 Pergunta-suspense de uma palavra** (alto). Custa alcance real (MagicPost: -4,8%). Variações: "O resultado?"; "O problema?"; "Por quê? Porque..."; "E sabe o que aconteceu?".
- Exemplo: "A solução? Simples." → Conectar as frases: "Com o baixo desempenho, perdem o negócio."

**1.3 Abertura panorâmica** (alto). Calco de "in today's fast-paced world", com herança do dialeto redação ENEM (seção 10). Variações: "em um mundo cada vez mais digital/conectado/competitivo"; "no cenário atual"; "na era digital"; "vivemos em uma sociedade onde"; "na contemporaneidade". Formas que brasileiros reais usam ("hoje em dia", "nos dias de hoje") são risco médio.
- Exemplo: "Em um mundo cada vez mais digital, as empresas precisam se adaptar." → Cortar a ambientação e abrir pelo fato concreto ou dado datado: "no Brasil de 2026", "desde a pandemia".

**1.4 "Vamos mergulhar"** (alto). Calco de "let's dive in"; a família de "delve", marcador número 1 pós-ChatGPT (Max Planck/Nature). Variações: "vamos nos aprofundar"; "bora mergulhar"; "mergulhar nesse universo".
- Exemplo: "Vamos mergulhar nesse tema." → Cortar e entrar direto no conteúdo. Aceitável só em sentido literal (mergulhar na piscina).

**1.5 "Desvendar os segredos"** (alto). Headline de infoproduto gerada em massa. Variações: "desvendar os mistérios de"; "decifrar o segredo"; "o que ninguém te conta sobre".
- Exemplo: "Desvendar os mistérios do marketing digital." → Explicar, mostrar, entender; prometer o conteúdo real: "5 configurações de campanha que reduzem CPC".

**1.6 "Aqui está o que / Eis"** (alto). MagicPost: de menos de 3% para mais de 16% dos posts pós-ChatGPT. Variações: "Aqui está o que aprendi"; "Aqui estão 5 formas de"; "Eis por que".
- Exemplo: "Aqui está o que ninguém te conta sobre contratação." → Entrar direto no conteúdo prometido. Precedido de "Claro!" é resíduo determinístico (seção 11).

**1.7 "Espero que esta mensagem o encontre bem"** (alto). Calco de "I hope this message finds you well". Variação: a tríade de saudação padrão do ChatGPT, "Olá, [Nome]! Tudo bem com você? Espero que sim.".
- Exemplo: "Olá, Maria! Tudo bem com você? Espero que sim. Gostaria de compartilhar uma oportunidade..." → "Oi, tudo bem?" ou direto ao assunto. A forma curta "espero que esteja bem" é comum em humanos (baixo); a forma longa e a tríade denunciam.

**1.8 Gancho retórico de abertura** (alto como primeira linha). Variações: "Você já parou para pensar..."; "E se eu te dissesse que...".
- Exemplo: "Você já parou para pensar em quanto tempo sua equipe perde?" → Abrir com o dado: "Sua equipe perde em média X horas por semana com..."

**1.9 Abertura cerimonial de anúncio** (alto). Calco de "I'm excited to announce". Variações: "É com grande satisfação que anuncio"; "Tenho o prazer/orgulho de compartilhar"; "Estou muito animado em anunciar".
- Exemplo: "Tenho o prazer de anunciar que estamos lançando um novo produto." → Anunciar o fato direto: "Lançamos hoje o X."

**1.10 "Desempenha um papel crucial"** (alto). Calco de "plays a crucial role". Variações: "papel fundamental/vital/essencial/central/decisivo". Em texto de IA, reaparece com sujeitos diferentes no mesmo documento.
- Exemplo: "A tecnologia desempenha um papel crucial na educação moderna." → Verbo direto, ou "é essencial para" seguido do efeito concreto.

**1.11 "Insights valiosos"** (alto). Evidência acadêmica direta: 6 de 17 trabalhos suspeitos no corpus UFMG/SciELO. Variações: "insights relevantes/preciosos/acionáveis"; "aprendizados valiosos". "Insight" sozinho é corrente no corporativo brasileiro (médio).
- Exemplo: "O relatório traz insights valiosos sobre o consumidor." → Conclusões, achados, "o que aprendi".

**1.12 "Não hesite em"** (alto). Calco de "don't hesitate to"; fecho padrão de e-mail gerado. Combinado com "Espero que isso ajude!" em texto publicado é resíduo determinístico (seção 11).
- Exemplo: "Não hesite em entrar em contato caso tenha dúvidas." → "Qualquer dúvida, é só chamar."

**1.13 Conselho enlatado** (alto). O maior custo de alcance medido (MagicPost: -6,7%). Variações: "A chave é"; "O segredo está em"; "Pare de X, comece a Y".
- Exemplo: "Pare de buscar curtidas, comece a resolver problemas." → Dar a ação concreta e específica em vez da receita.

**1.14 Conclusão-equilíbrio** (alto em texto opinativo). Neutralidade compulsória de assistente. Variações: "encontrar o equilíbrio entre X e Y"; "buscar o meio-termo"; "cabe a cada um decidir"; "vantagens e desvantagens que devem ser consideradas".
- Exemplo: "O segredo está em encontrar o equilíbrio entre tecnologia e humanidade." → Tomar posição real e justificar.

## 2. Muletas de transição

O sinal aqui raramente é a palavra; é a densidade e a posição. Um "além disso" é português normal. Um conectivo abrindo cada parágrafo é assinatura (SciELO/Folha PE: "uso excessivo de recursos coesivos principalmente no início dos parágrafos").

**2.1 "Além disso" abrindo parágrafos** (médio isolado; alto se abre 2+ parágrafos). Gatilho número 1 de abandono de leitura relatado no TabNews.
- Exemplo: "A IA melhora a análise. Além disso, contribui para vendas. Além disso, simplifica o atendimento." → Cortar; "também"; "e"; ou emendar sem conectivo.

**2.2 "Adicionalmente"** (alto). Calco de "additionally", raríssimo em pt-BR espontâneo. → "Além disso", "também", "e".

**2.3 Arcaísmos e pseudo-erudição de cursinho** (alto fora de texto jurídico ou acadêmico formal). Variações: "Outrossim"; "Destarte"; "Não obstante"; "Mormente"; "hodiernamente"; "faz-se mister"; "nesse ínterim". "Ademais" e "Todavia" são médio.
- Exemplo: "Hodiernamente, observa-se que a tecnologia permeia todas as esferas sociais." → "hodiernamente" vira "hoje"; "todavia" vira "mas". Fora de redação de vestibular, "hodiernamente" e "outrossim" são quase assinatura (seção 10).

**2.4 Conectores automáticos em série** (médio; forte quando abrem 2+ parágrafos do mesmo texto). Variações: "Nesse contexto"; "Nesse sentido"; "Nesse viés"; "Sob essa ótica"; "Diante disso"; "Diante desse cenário"; "Em face do exposto"; "Dessa forma". Costumam vir sem viés ou ótica alguma definida antes.
- Exemplo: "Diante desse cenário, medidas são necessárias para mitigar a problemática." → Cortar o conector (a frase quase sempre sobrevive) ou ligar por conteúdo; "diante disso" vira "por isso".

**2.5 Retomada robótica** (médio; "isso destaca a importância de" é alto, calco de "this highlights the importance of"). Variações: "Isso significa que"; "Em outras palavras"; "Como resultado"; "Outro ponto importante é".
- Exemplo: "Em outras palavras, a produtividade aumenta." → Remover; se a frase anterior precisa ser traduzida, reescrever a original.

**2.6 Fechos mecânicos** (médio; alto em texto curto). Variações: "Em suma"; "Em síntese"; "Em conclusão" (calco de "in conclusion"); "Em resumo"; "Em última análise"; "Conclui-se que". "Em suma" em texto de 3 parágrafos é o sinal denunciador (Gazeta do Povo).
- Exemplo: "Em suma, a tecnologia veio para ficar." → Apagar o rótulo e terminar com a conclusão concreta, ou cortar o parágrafo-resumo inteiro.

**2.7 "No que tange a"** (médio). Registro cartorial usado para simular formalidade. Variações: "no que concerne a"; "no tocante a"; "no âmbito de"; "na seara de". Uma ocorrência passa em texto formal; três é template.
- Exemplo: "No que tange à educação, o Brasil apresenta índices alarmantes." → "Sobre", "quanto a", ou reestruturar com o tema como sujeito.

**2.8 Transição animada "Bora lá?"** (médio). Equivalente informal do "let's dive in", onipresente em posts assistidos por IA no Brasil. Variações: "Vamos nessa!"; "Vem comigo!"; "Se joga!"; "Partiu!". Suspeito quando aparece isolado em uma linha, seguido de lista com emojis (seção 12).
- Exemplo: "Quer aprender a fazer sua IA escrever melhor? Bora lá?" → Remover e começar a explicação.

**2.9 Numeração mantida até o fim** (médio). "Em primeiro lugar... Em segundo lugar... Por fim", sem nunca quebrar. Humano abandona a numeração no meio; IA nunca. Ver 10.2 para a variante ENEM.

## 3. Atenuação excessiva (hedging)

**3.1 Evasão de compromisso** (médio). Variações: "pode-se dizer que"; "alguns diriam que"; "de certa forma"; "até certo ponto". Hedging moderado é aceitável em texto acadêmico.
- Exemplo: "Pode-se dizer que, de certa forma, o projeto avançou." → Assumir a afirmação ou cortá-la.

**3.2 Quantificadores vagos** (médio em série; formas pomposas são alto). Médio: "diversos"; "inúmeros"; "vários"; "grande parte da população". Alto (quase exclusivos de IA em texto casual): "uma ampla gama de"; "uma miríade de"; "um vasto leque de". A IA recorre a eles justamente quando não tem dado específico.
- Exemplo: "A plataforma oferece uma ampla gama de recursos." → Número real ("três motivos: X, Y e Z") ou cortar.

**3.3 Falsa autoridade sem fonte** (alto). Variações: "estudos demonstram"; "pesquisas recentes apontam"; "especialistas concordam"; "a ciência comprova"; "a Sociologia defende que". Em texto de IA, frequentemente acompanha dado inventado; checar se a fonte existe.
- Exemplo: "Estudos comprovam que a produtividade aumenta com o home office." → Citar o estudo real com nome, instituição e ano ("segundo o IBGE, 2024"), ou reformular como opinião.

**3.4 Assertividade oca** (médio isolado; várias no mesmo texto, ou "indubitavelmente" em texto casual, é alto). Variações: "é notório que"; "é inegável que"; "não há como negar"; "sem sombra de dúvidas"; "como todos sabem". Pressupõe consenso em vez de argumentar; herança do dialeto ENEM.
- Exemplo: "É notório que a educação brasileira enfrenta grandes desafios." → Cortar a moldura e afirmar com dado: "A evasão escolar cresceu X% segundo o INEP."

**3.5 Qualificadores empilhados** (médio). Dois ou mais amortecedores na mesma frase; o sinal é o empilhamento, não o qualificador isolado.
- Exemplo: "Em muitos casos, isso pode, até certo ponto, melhorar os resultados." → Escolher UMA ressalva ou assumir posição.

**3.6 Recomendação tímida** (médio). Tom de assistente prestativo. Variações: "você pode considerar"; "uma possibilidade é"; "é recomendável que".
- Exemplo: "Você pode considerar contratar um especialista." → Recomendar direto: "Contrate um especialista se X."

## 4. Meta-comentário

**4.1 Preâmbulo de ênfase "é importante ressaltar que"** (alto; 2+ ocorrências é quase certeza). Variações: "é fundamental/essencial/crucial destacar/notar/frisar/salientar/lembrar que"; "vale ressaltar que"; "cabe mencionar que"; "cumpre observar que"; "tenha em mente que".
- Exemplo: "É importante ressaltar que os dados são essenciais." → Apagar a moldura e afirmar direto. Se era importante, só diga.

**4.2 Sermão genérico** (alto). Variações: "é fundamental que as empresas/os profissionais/você...".
- Exemplo: "É crucial que as organizações se adaptem à transformação digital." → Afirmar sem tutela: "Empresas que não se adaptarem vão perder X."

**4.3 Abertura que anuncia o próprio texto** (alto em blog, post e e-mail; aceitável em gênero acadêmico formal). Variações: "Neste artigo, vamos explorar"; "Neste post, você vai descobrir"; "A seguir, apresentaremos".
- Exemplo: "Neste artigo, vamos explorar as principais tendências de IA." → Cortar. A primeira frase deve informar, não prometer.

**4.4 Bajulação de assistente** (alto; em resposta a crítica é quase prova). Variações: "Você está totalmente certo!"; "Ótima pergunta!"; "Excelente observação!"; "Entendo perfeitamente seu ponto". O esqueleto "elogio reflexo + transição para lista" é a espinha da resposta de LLM; em conversa real ninguém avalia a pergunta do outro antes de responder.
- Exemplo: "Que ótima pergunta! Vamos lá:" → Remover e ir direto à resposta.

**4.5 Markdown de chat colado fora de contexto** (alto; prova quase absoluta). Cabeçalhos `##`, `**negrito**` cru, tabelas e bullets aninhados em campo que não renderiza markdown (fórum, e-mail, WhatsApp). Detalhe: o ChatGPT emite negrito como `**texto**`; o negrito nativo do WhatsApp é `*texto*`. Asteriscos duplos visíveis no zap são evidência física de colagem. → Remover a formatação antes de publicar ou enviar.

**4.6 Seção que descreve a própria função** (médio). Documentado no corpus UFMG.
- Exemplo: "A metodologia da pesquisa incluirá a análise de dados coletados..." (no futuro, sem dados). → Cortar seções sem substância; a estrutura deve ser ditada pelo conteúdo.

## 5. Buzzwords corporativas e linkedinês

**5.1 "Crucial"** (alto quando repetido). O termo mais característico do slop em pt segundo Sabbatini, com pico estatístico pós-2023. → Importante, decisivo, ou reescrever mostrando por quê. Dose única é aceitável.

**5.2 "Robusto"** (alto fora de engenharia, estatística e software).
- Exemplo: "soluções robustas para o seu negócio" → Sólido, confiável, ou o atributo real: "aguenta X acessos".

**5.3 Adjetivos vazios de impacto** (médio isolados; alto empilhados no mesmo parágrafo). Variações: "vibrante"; "inovador"; "transformador"; "fascinante"; "poderoso"; "meticuloso"; "abrangente"; "significativo"; "otimizado". "Abrangente" e "detalhado" são tique do Gemini em pt-BR; "meticuloso" e "hábil" subiram 51% pós-ChatGPT.
- Exemplo: "uma solução inovadora, eficiente e otimizada" → Detalhe concreto ("cresceu 40% em um ano") ou cortar.

**5.4 Vocabulário raro-denunciador** (alto mesmo em ocorrência única). "Sinérgico"; "multifacetado"; "inestimável"; "louvável"; "indelével". → Descrever o aspecto específico.

**5.5 "Jornada" metafórica** (alto; um dos maiores marcadores em pt-BR). Variações: "jornada de aprendizado/transformação/sucesso"; "nessa jornada". Exceção: "jornada do cliente/do usuário" é jargão técnico estabelecido.
- Exemplo: "Comece hoje sua jornada de transformação digital." → Processo, caminho, ou a etapa concreta.

**5.6 "Agregar valor"** (alto como enchimento universal). Variações: "gerar valor"; "entregar valor"; "valor agregado". → Dizer qual valor: "reduz o custo de X", "ensina a fazer Y".

**5.7 Verbos corporativos de superlativo** (médio isolados; alto com 3+ no mesmo texto ou em tríade paralela). Variações: "potencializar"; "impulsionar"; "otimizar"; "maximizar"; "alavancar"; "fomentar"; "viabilizar"; "proporcionar". "Potencializar" quase não existe em fala espontânea; o par "otimizar e maximizar" na mesma frase é marcador de copy gerado.
- Exemplo: "A plataforma aprimora a comunicação, facilita a colaboração e otimiza processos." → Melhorar, aumentar, usar, ajudar, com número ou exemplo concreto.

**5.8 Linkedinês difuso** (médio; soma no conjunto). "Disruptivo"; "ecossistema"; "mindset"; "sinergia"; "escalável"; "mudança de paradigma"; "virada de chave"; "divisor de águas"; "tecnologia de ponta". → Novo, mercado, mentalidade, integrar equipes, "antes X, agora Y", nomear a tecnologia.

**5.9 Copy institucional genérico** (alto). Teste: trocando o nome da empresa, a frase continua valendo? Então é slop. Variações: "soluções personalizadas para suas necessidades"; "leve seu negócio ao próximo nível"; "transforme sua vida/carreira"; "qualidade incomparável"; "referência no mercado"; "não perca essa oportunidade única".
- Exemplo: "Oferecemos soluções completas e personalizadas para atender às suas necessidades." → Listar 2-3 entregas reais: "site, tráfego pago e CRM configurado"; "inscrições até sexta, 20 vagas".

## 6. Redundâncias e pleonasmos

**6.1 Sinônimos encadeados** (médio). A mesma ideia dita 2-3 vezes para "manter a fluidez".
- Exemplo: "A IA transforma empresas, altera negócios e modifica processos." → Dizer uma vez, com o verbo mais preciso.

**6.2 Promessa triplicada em copy** (médio).
- Exemplo: "aumente suas vendas, amplie seu faturamento e potencialize sua receita" → Uma promessa, com número.

**6.3 Pares redundantes** (médio). "Inovador e disruptivo"; "único e exclusivo"; "moderno e atual". → Manter um termo ou trocar por prova.

**6.4 Elogio vago autorreferente** (médio). Documentado no corpus UFMG. Teste da troca: se a frase sobrevive aplicada a outro livro ou empresa, é slop.
- Exemplo: "A obra apresenta uma análise crítica da literatura existente e confere credibilidade ao texto." → Nomear o estudo ou autor específico, ou cortar o elogio.

**6.5 Cabeçalho seguido de linha que o reafirma** (médio).
- Exemplo: "## Consistência é a chave / Ser consistente é fundamental para alcançar resultados." → Remover a linha redundante ou desenvolver conteúdo novo.

**6.6 Retomada excessiva do tema** (médio). Repetir o enunciado ("a inteligência artificial na educação") em todo parágrafo; abrir com definição de dicionário ("A inteligência artificial é uma tecnologia que..."). Útil para detectar redação de vestibular gerada. → Pronomes, elipses, sinônimos naturais; abrir com a tese.

**6.7 Generiquês** (médio; sinal de conjunto). Texto impessoal, sem opinião, sem nome próprio, sem número, sem referência cultural brasileira; poderia ter sido escrito sobre qualquer caso, por qualquer pessoa. → Inserir caso real, data, nome, número, opinião com dono.

**6.8 Intensificadores vazios** (baixo). "Extremamente", "incrivelmente", "absolutamente" diante de adjetivo comum; grau aplicado a adjetivo absoluto ("muito único", "totalmente essencial"). → Cortar o intensificador; se a intensidade importa, prová-la com número ou exemplo.

## 7. Construções prolixas

| Forma prolixa | Alternativa direta |
|---|---|
| É importante ressaltar que X | X |
| Vale a pena mencionar que X | X |
| Tenha em mente que X | X |
| É notório/inegável que X | X (com dado) |
| desempenha um papel crucial em | é essencial para / decide |
| serve como um lembrete de que | lembra que |
| destaca-se como referência em | é referência em |
| representa um marco na história de | marcou |
| É com grande satisfação que compartilho que X | X (anunciar direto) |
| aproveitar o poder de X | usar X |
| uma ampla gama de | vários / (número real) |
| no que se refere a / no que tange a | sobre |
| Diante do exposto, / Diante desse cenário, | Por isso, |
| Conforme supracitado | como dito acima / (cortar) |
| estarei enviando / estaremos analisando | vou enviar / analisamos |
| utilizar | usar |
| hodiernamente | hoje |
| Adicionalmente, | E / Além disso, |
| Em outras palavras, ... | (cortar; reescrever a frase original) |
| Neste artigo, vamos explorar X | (cortar; entrar em X) |
| não apenas X, mas também Y | X e Y |
| Por último, mas não menos importante, | Por fim, |
| faz-se necessário que [agente vago] | [sujeito nomeado] deve |
| mitigar essa problemática | resolver [o problema nomeado] |
| de forma fluida e sem esforço | funciona bem com X |
| impacta de maneira significativa | (quantificar: reduz X em 30%) |
| solução robusta e escalável | aguenta X acessos / cresce sem custo extra |

Teste do textão (TabNews): se o texto pode ser dito em cerca de 20% das palavras sem perda de conteúdo, é slop. Caso típico: duas páginas educadas para pedir o que caberia em uma frase. Corte até sobrar o pedido ou a tese, mais uma justificativa. Em mensageria a régua é mais dura ainda (ver 12.6).

## 8. Calcos de tradução do inglês

Construções que não existem em pt-BR espontâneo e entram por tradução literal do repertório em inglês dos modelos.

| Calco | Origem em inglês | Alternativa |
|---|---|---|
| (rica) tapeçaria de / mosaico de culturas | rich tapestry | mistura, variedade, conjunto |
| no reino de | in the realm of | na área de, no campo de |
| cenário/panorama em constante evolução | ever-evolving landscape | o setor muda rápido / (cortar) |
| navegar as complexidades/desafios | navigate the complexities | lidar com, enfrentar |
| alavancar (fora de finanças) | leverage | usar, aproveitar |
| desbloquear/destravar o potencial | unlock the potential | dizer o que a pessoa passa a conseguir |
| aproveitar o poder de | harness the power of | usar X para [resultado] |
| abraçar a mudança/tecnologia | embrace change | adotar, aderir a |
| embarcar em uma jornada | embark on a journey | começar |
| ressoar com o público | resonate with | fazer sentido para, conectar com |
| sem costura / de forma fluida e sem esforço | seamless / effortlessly | integrado, sem atrito |
| insights acionáveis | actionable insights | dados que viram decisão, práticos |
| é um testemunho/testamento de | is a testament to | mostra que, prova que |
| aninhado em / no coração de | nestled in / at the heart of | em, no centro de |
| legado duradouro / marca indelével | lasting legacy / indelible mark | o efeito concreto e verificável |
| serve como / atua como / destaca-se como | serves as / stands as | é |
| representa um marco / marca um momento | marks a milestone | marcou, foi |
| eventualmente (no sentido de "por fim") | eventually | por fim (erro objetivo de tradução) |
| endereçar uma questão | address an issue | tratar de, resolver |
| empoderar / capacitar (sem treino literal) | empower | dar autonomia, permitir que |
| fator-chave, benefício-chave | key factor / key benefit | principal fator ("palavra-chave" é consagrado) |
| quando se trata de | when it comes to | em [assunto], ... |
| por último, mas não menos importante | last but not least | por fim |
| em conclusão | in conclusion | (cortar; terminar com a conclusão concreta) |
| notavelmente | notably | (cortar) ou afirmar direto |
| à luz dessas informações | in light of | com isso |
| não apenas X, mas também Y | not only... but also | X e Y (suspeito com 2+ por página) |

Padrões sintáticos da mesma família:

- **Gerúndio conclusivo no fim da frase** (alto): "...automatiza processos, garantindo mais eficiência." Calco da participial phrase ("...ensuring/highlighting"). → Ponto final e nova frase com sujeito e verbo, ou cortar a conclusão vazia.
- **Gerundismo de futuro** (médio; também vício humano de telemarketing): "estarei enviando", "vamos estar analisando". → "Vou enviar", "analisaremos".
- **Vocabulário de português europeu em texto BR** (alto; vazamento de corpus, o Gemini derrapa mais): "utilizador", "ficheiro", "ecrã", "telemóvel". → Usuário, arquivo, tela, celular.
- **Mesóclise e formalidade fóssil** (alto em prosa de internet): "dar-lhe-ei", "ver-se-á", "mister se faz". → Reescrever coloquial.
- **Sinais fracos agregados** (baixo isolado; somatório): possessivo redundante espelhando "your" ("o seu negócio, a sua equipe" em toda frase); voz passiva analítica em excesso; "sendo que"; ponto dentro das aspas.

## 9. Padrões estruturais e tipográficos

### Travessão

**Regra deste projeto: se o texto pode ser escrito sem travessão, remova o travessão.** Reescreva com vírgula, dois-pontos, parênteses ou ponto final, o que couber melhor. Mantenha travessão apenas quando realmente necessário: diálogo em narrativa (no início da linha, convenção do pt-BR) e raros apartes em que nenhuma outra pontuação preserva o sentido.

**9.1 Travessão parentético denso** (médio isolado; alto encadeado com 2+ por parágrafo, em contexto casual ou em mensagem de chat). Formas: par no meio da frase; caractere `—` (U+2014) ou `–` (U+2013) colado sem espaço onde humano digitaria hífen; o molde retórico "X — não Y".
- Exemplo (ruim): "A IA — que já transformou o mercado — segue evoluindo. Não é moda — é mudança estrutural." → Vírgula, dois-pontos, parênteses ou duas frases; em chat, quebrar em duas mensagens.
- Evidência: meme nacional de 2025; MagicPost: de menos de 2% para mais de 15% dos posts; Octans: 18,7%. Em mensageria o sinal é mais forte: teclado de celular brasileiro produz hífen (`-`) ou meia-risca (`–`), não o travessão (`—`). Falso positivo conhecido: escritores e jornalistas usam legitimamente. O que denuncia é densidade e contexto, não o caractere em si.

### Tipografia

**9.2 Vírgula antes de "e" final em enumeração** (alto). A vírgula de Oxford (Oxford comma) não existe na norma do português; é vazamento direto do inglês.
- Exemplo: "maçãs, bananas, e laranjas" → Remover a vírgula antes do "e" final.

**9.3 Title Case em títulos** (alto). A norma pt-BR capitaliza só a primeira palavra e nomes próprios; o sinal é mais forte em português do que em inglês.
- Exemplo: "Como Transformar Sua Carreira Em 5 Passos" → "Como transformar sua carreira em 5 passos".

**9.4 Aspas curvas em texto plano digitado** (alto). Sinal quase perfeito em meios de aspas retas (posts, Markdown, código, comentários). Ressalva: Word, Google Docs e iOS convertem automaticamente; sem valor nesses meios.

**9.5 Emoji como marcador de lista** (alto). O padrão mais prevalente do estudo Octans (19,1% dos posts), com impacto negativo. Coreografia denunciante: 3+ linhas abrindo com emoji temático, sempre na mesma posição, um por linha, com regularidade perfeita. Humano usa emoji como reação pontual, em posição irregular.
- Exemplo (ruim): "🚀 Aumente suas vendas / ✨ Engaje seu público / 💡 Dica bônus" → Remover (ou no máximo um, com intenção); hífen simples ou prosa.

**9.6 Lista "termo em negrito + dois-pontos + explicação"** (alto). "Apresentação de slides fingindo ser artigo" (Wikipédia). Itens paralelos de mesma extensão, categoria em negrito seguida de dois-pontos. → Prosa contínua, ou lista sem o rótulo com dois-pontos.

**9.7 Negrito excessivo em palavras-chave pelo texto** (médio; também hábito de redator SEO humano). → Reservar negrito para um ou dois pontos centrais.

**9.8 Dois-pontos como "setup: payoff"** (médio dentro da frase; baixo em título).
- Exemplo: "O resultado: mais vendas." → Frase declarativa simples. Uma ocorrência é estilo; três no mesmo post é assinatura.

### Estrutura

**9.9 Fragmentação dramática** (alto). Octans: 12,8% dos posts, impacto fortemente negativo. Sequência de 3+ "frases" de 1-3 palavras.
- Exemplo: "Não é sorte. É método. É consistência." → Unir com vírgulas e conjunções; alternar frases curtas e longas.

**9.10 Regra de três (tríade de abstrações)** (médio; alto quando TODA enumeração do texto vem em trio).
- Exemplo: "clareza, consistência e propósito" → Um item concreto desenvolvido, ou 2 ou 4 itens conforme o material sustente.

**9.11 Parágrafos de tamanho uniforme** (médio; sinal de conjunto). Todos os parágrafos com 3-4 frases de 15-22 palavras, ordem sujeito-verbo-objeto constante. → Variar deliberadamente; parágrafo de uma linha convivendo com parágrafos longos.

**9.12 Arquitetura fixa com "Conclusão" obrigatória** (médio em blog e e-mail; alto em fórum e comentário). Introdução-anúncio, desenvolvimento em lista, seção "Conclusão" que recapitula. Sinal máximo: seções "Introdução/Desenvolvimento/Conclusão" em um comentário de fórum. → Entrar direto; terminar no último ponto forte, sem seção-resumo.

**9.13 Fecho com moral genérica e CTA de engajamento** (médio). A pergunta final genuína é hábito humano; o que denuncia é a moral vazia antes dela e a constância (a IA fecha todo texto assim).
- Exemplo: "E você, o que acha sobre isso? Deixa aqui nos comentários!" → Terminar no último fato, ou CTA específico sobre o conteúdo.

**9.14 Excesso de subtítulos e símiles didáticos** (médio). Um subtítulo por parágrafo em texto curto; uma analogia decorativa por parágrafo ("Pense no algoritmo como um garçom que anota seus pedidos"). Usuários brasileiros apontam que "a IA é viciada em símile". → Fundir seções em prosa; exemplo concreto do contexto real do autor.

## 10. Dialeto "redação ENEM"

O registro "redação nota 1000" virou um dialeto enlatado que os LLMs reproduzem em massa, treinados em milhares de redações-modelo. Regra de contexto dupla: fora do vestibular (blog, LinkedIn, e-mail, comentário), qualquer fatia deste template é um dos sinais mais fortes de IA em pt-BR; dentro de uma redação real, cada peça isolada é legítima e o sinal é o pacote completo (10.8).

**10.1 "Desde os primórdios da humanidade"** (alto). O clichê de introdução mais odiado pelos corretores. Variações: "desde os tempos mais remotos"; "ao longo da história da humanidade".
- Exemplo: "Desde os primórdios da humanidade, o homem busca viver em sociedade." → Marco histórico específico e datado: "Desde a promulgação da Constituição de 1988..."

**10.2 Grade fixa de conectivos por parágrafo** (alto). "Em primeira análise... Ademais... Portanto", sempre na primeira palavra, um slot por parágrafo. Cada conectivo é legítimo; a grade completa é o sinal. → Variar a posição dos conectivos, ligar parágrafos por retomada de ideia, cortar onde a sequência já está clara.

**10.3 Citação-curinga** (alto). Epíteto enciclopédico + conceito solto + conexão vaga. O baralho: Bauman ("modernidade líquida"), Kant sobre educação, Paulo Freire, Sartre, Voltaire, Byung-Chul Han ("sociedade do cansaço"), Orwell/1984 para tecnologia.
- Exemplo: "Segundo o sociólogo polonês Zygmunt Bauman, vivemos em uma 'modernidade líquida', na qual as relações são frágeis." → Repertório específico e verificável do tema (dado IBGE/IPEA, caso concreto, lei com artigo); se citar, dialogar com a citação.

**10.4 Template CF/88** (alto). A fórmula "a lei diz X, a realidade mostra Y" com a Constituição ou a DUDH como curinga universal. Marcadores: "Carta Magna"; "entretanto, na prática"; "não sai do papel".
- Exemplo: "A Constituição Federal de 1988 assegura a saúde como direito de todos. Entretanto, essa garantia não se concretiza na realidade brasileira." → Artigo específico (art. 196) e dado que quantifique a distância entre lei e realidade.

**10.5 Proposta de intervenção genérica** (alto). Agente vago + ação vaga + "conscientizar" (efeito, não ação). A IA a reproduz como fecho de QUALQUER texto opinativo em pt-BR, inclusive fora de redação.
- Exemplo: "Portanto, cabe ao governo criar políticas públicas que conscientizem a população acerca da problemática." → Agente específico + ação concreta + meio + finalidade: "o MEC deve promover oficinas semestrais com nutricionistas nas escolas públicas para reduzir a obesidade infantil".

**10.6 Urgência enlatada e "essa problemática"** (médio). Variações: "urge que"; "faz-se necessário"; "é imperioso que"; "medidas devem ser tomadas"; "as autoridades competentes"; "mitigar/sanar/dirimir essa problemática". A passiva sem agente esconde quem faz o quê.
- Exemplo: "Urge que o poder público adote medidas para sanar essa problemática." → Sujeito nomeado + verbo de ação ("as prefeituras devem ampliar..."); "esse problema" ou o problema nomeado.

**10.7 Fecho utópico e senso comum sentimental** (alto). Variações: "só assim será possível construir uma sociedade mais justa e igualitária"; "um futuro melhor para as próximas gerações"; "a educação é a base de tudo"; "juntos somos mais fortes". Também aparece em texto de IA não escolar como parágrafo final inspiracional.
- Exemplo: "Só assim será possível construir uma sociedade mais justa e igualitária." → Finalidade mensurável ligada ao problema, ou terminar na ação.

**10.8 Meta-padrão do template completo** (médio em redação escolar; alto em texto cotidiano). Quatro parágrafos de tamanho quase idêntico, cada um aberto por conectivo da grade, zero desvios ortográficos, nenhuma subjetividade, retomada mecânica da frase temática, repertório de bolso + proposta genérica + fecho utópico. Nenhum item isolado prova IA (é o ideal do gênero); o pacote completo em e-mail ou post é sinal forte.

## 11. Resíduos determinísticos de chat e modelo (quase-prova)

Cada padrão desta seção, em texto final publicado (post, listagem de e-commerce, PDF corporativo, artigo, e-mail enviado), é individualmente quase-prova de geração sem revisão: a exceção à regra do acúmulo. Exceções de contexto: tutoriais de prompt, modelos de documento compartilhados de propósito e citações deliberadas de respostas de IA. Todos têm casos brasileiros documentados (Mercado Livre, Magazine Luiza, Americanas, Airbnb, PDFs corporativos, artigos no Google Scholar).

**11.1 Disclaimers de cutoff** (alto; quase-prova). Formas: "até a minha última atualização em setembro de 2021"; "a partir da minha última atualização" (calco agramatical de "As of my last update" que localizou 115+ artigos no Google Scholar); "minha data de corte de conhecimento"; "minhas informações estão atualizadas até".
- Regex de assinatura de datas: `(atualização|corte|conhecimento|informações).{0,30}(até|em).{0,10}(setembro de 2021|janeiro de 2022|abril de 2023|outubro de 2023)`. A coocorrência em primeira pessoa é estatisticamente impossível em texto humano.
- Substituição: remover a frase inteira e verificar o dado em fonte atual; se a incerteza for real, datar ("em 2021, a regra era X").

**11.2 Hedge pós-cutoff** (médio isolado; alto junto de data-assinatura).
- Exemplo: "...esse limite era de R$ 81.000,00 por ano. No entanto, esse valor pode ter sido alterado. Recomendo consultar o site oficial." → Verificar o dado e afirmar com data; remover a recomendação genérica.

**11.3 Recusas coladas** (alto; quase-prova). Formas: "como um modelo de linguagem, não posso..."; "como uma IA desenvolvida pela OpenAI..." (a menção ao fornecedor dentro de texto de terceiros é o sinal mais forte da família); "Desculpe, não posso ajudar com isso." (encontrada como título de produto real no Mercado Livre e na Magazine Luiza); "não tenho acesso a informações em tempo real"; "isso vai contra as minhas diretrizes"; "Sou um modelo de linguagem grande, treinado pelo Google." (assinatura Gemini via pipelines de tradução). → Remover o parágrafo inteiro e escrever o conteúdo real.

**11.4 Preâmbulo de aquiescência colado** (alto; quase-prova). Buscar sempre na primeira linha ou no título. Regex: `^(Claro|Certamente|Com certeza|Absolutamente|Perfeito)[!,.]? ?[Aa]qui está`
- Exemplo real: "Claro, Aqui Está O Título E A Descrição Conforme Solicitado:" (título de produto no Mercado Livre). → Remover a primeira linha inteira; o texto deve começar no conteúdo.

**11.5 Fecho de chat colado** (alto em texto publicado). "Espero que ajude" isolado em fórum é humano comum (baixo); a combinação em copy publicado é quase-prova.
- Exemplo real: "Espero que isso ajude! Se você tiver mais alguma pergunta, estou à disposição." (descrição de produto na Americanas). → Remover o parágrafo final.

**11.6 Placeholders não editados** (alto em texto que se apresenta como final). Regex: `\[[A-ZÀ-Ú][^\]]{2,40}\]` para [Seu Nome], [Nome da Empresa], [Data], [valor]; complementar: `\[?insira (aqui|o \w+)\]?`. Exceção: modelos de documento compartilhados de propósito.
- Exemplo real: "Atenciosamente,[Seu Nome]" (avaliação na App Store). → Preencher com o dado real ou remover.

**11.7 Instrução residual** (médio; alto junto de placeholders). "Lembre-se de substituir [X] pelos seus dados reais." → Remover a instrução e efetivar a substituição. Documentação técnica humana também usa; pesar pelo contexto.

**11.8 Vazamento de prompt** (alto). O texto descreve as restrições do próprio pedido: contagem de palavras, formato, plataforma, tom.
- Exemplo real: "Aqui está um artigo completo com mais de 500 palavras, ideal para WordPress, sobre o tema..." (título de matéria em portal automatizado). → Remover toda menção à tarefa; publicar só o conteúdo.

**11.9 Rótulos estruturais do output colados** (médio; alto com preâmbulo de chat). "Título:", "Descrição:", "Hashtags:", "Opção 1:" publicados junto com o conteúdo. → Remover os rótulos e manter só uma das opções.

**11.10 Resíduos de interface** (alto; quase-prova). "Regenerate response" / "resposta regenerada" (encontrado em cerca de 2/3 dos artigos da lista do Retraction Watch); "Como posso ajudar hoje?". → Remover.

## 12. Informalidade performática

Duas faces: o modelo simula "brasileiro descontraído" com gírias e vocativos distribuídos mecanicamente sobre um esqueleto de redação; e a estrutura de documento é transplantada para o chat. Os sinais mais fortes são comparativos (mudança súbita contra o histórico da pessoa) e de colisão (registro casual com miolo formal).

**12.1 Saudação enlatada de abertura** (médio; alto seguida de texto perfeito com travessões e estrutura de redação). Variações: "Fala, galera!"; "E aí, pessoal!"; "Sejam bem-vindos a mais um...".
- Exemplo: "Fala galera, bom dia, boa tarde, boa noite! Hoje eu vou te passar cinco comandos secretos..." → Remover e entrar no assunto, ou usar a saudação real do autor.

**12.2 "né?" mecânico colado em frase perfeita** (médio). "né?" como enfeite de encerramento de cláusulas polidas e completas, repetido em 3+ frases. Humano usa "né" no meio de frase truncada, com erros ao redor.
- Exemplo: "E convenhamos: ninguém gosta de perder tempo, né?" → Remover ou reescrever em sintaxe falada de verdade.

**12.3 Vocativo distribuído pelo texto** (médio). "Galera, isso muda tudo. [...] E olha, galera, o resultado foi surpreendente. [...] Então é isso, galera!" → Cortar os vocativos; no máximo um, na abertura.

**12.4 Gírias datadas sorteadas** (médio; alto se a gíria convive com pontuação e crase perfeitas). Variações: "show de bola"; "top demais"; "irado"; "da hora". O ChatGPT erra cerca de 22% dos regionalismos brasileiros e sorteia gíria sem coerência regional ou etária (Preply/Forbes).
- Exemplo: "Essa dica é simplesmente top demais!" → Elogio específico, ou a gíria que a pessoa realmente usa.

**12.5 Colisão de registro** (alto; um dos sinais de maior precisão em pt-BR). Gíria e conectivo formal na mesma frase; humano quase nunca produz.
- Exemplo: "Bora lá! Outrossim, cabe destacar que..." → Escolher um registro só e reescrever a frase inteira nele.

**12.6 Textão estruturado para pergunta simples no WhatsApp** (alto). Pergunta de uma linha ("tem horário amanhã?") respondida com 4 parágrafos, bullets de opções e "Fico no aguardo do seu retorno!". Sinal composto: chegou rápido demais, longa demais, perfeita demais. → Responder em 1-2 frases diretas, no ritmo da conversa, em mensagens curtas.

**12.7 Bullets, numeração e negrito dentro de mensagem de chat** (alto). Estrutura de documento no zap; markdown cru é evidência física (ver 4.5).
- Exemplo: "Segue as opções: 1. **Plano Básico** 2. **Plano Pro**" → Escrever corrido, em mensagens separadas, sem hierarquia visual.

**12.8 Perfeição ortográfica sem nenhuma abreviação, em registro de chat** (médio; sinal contextual e comparativo). Acentuação e crase 100% corretas, zero "vc/pq/tb/kkk", especialmente como mudança súbita contra o histórico da pessoa na mesma conversa. Sozinho é fraco (gente formal existe); combinado com resposta instantânea ou mudança de padrão, fica alto. Ver seção 13.

**12.9 Tempero medido de calor humano** (baixo; útil em conjunto). Diminutivos genéricos ("tudinho", "rapidinho") ou risada higienizada ("haha" simétrico, sempre igual) como único recurso de informalidade num texto estruturalmente perfeito. → Manter só se for marca registrada real do autor.

## 13. Sinais inversos (marcas humanas)

Marcas que LLMs em pt-BR quase nunca produzem espontaneamente. Leitura invertida: a presença indica autor humano e reduz drasticamente a suspeita de IA.

- **Autocorreção com asterisco** (força altíssima): "vou levar o bolo / *bolo de cenoura". Só existe em produção humana sequencial em tempo real.
- **Palavrões abreviados** (altíssima): "pqp", "krl", "vsf kkkk". LLMs comerciais evitam por alinhamento.
- **"mais" no lugar de "mas"** (alta): "eu queria ir, mais não fui".
- **Grafias virais aglutinadas** (alta): "concerteza", "derrepente", "porisso", "apartir", "oque".
- **"menas"** (alta): flexão popular que a IA nunca produz espontaneamente.
- **a/há trocados em tempo** (alta): "isso aconteceu a dois dias"; "daqui há pouco"; "há anos atrás".
- **Crase errada** (alta): "à partir de hoje"; "de segunda à sexta". Crase é o que brasileiros mais erram; LLMs têm precisão altíssima.
- **Acentos suprimidos por digitação rápida** (alta, só em chat): "voce vem hj?", "nao sei".
- **kkkk irregular** (alta): comprimento aleatório conforme a intensidade ("kkkkkkkk para", "KKKKKK morri"). A IA, quando imita, usa "kkk" curto, fixo e protocolar.
- **Abreviações de internetês** (alta): vc, pq, tb, hj, msm, mto, vdd, blz, sla, sdds. Nota fina: humano MISTURA "vc" e "você" na mesma conversa; a inconsistência é o sinal. IA "humanizada" aplica a abreviação de forma consistente demais.
- **"para mim + infinitivo"** (alta): "difícil pra mim entender". LLM escreve "para eu fazer" por padrão.
- **Concordância popular quebrada** (alta): "as coisa tá cara"; "fazem dois anos"; "houveram muitos problemas".
- **Grafias populares específicas** (alta): "excessão", "previlégio", "ancioso", "mecher", "sombrancelha", "nada haver". Qualquer uma praticamente descarta IA sem pós-edição.
- **Minúscula inicial e sem ponto final em mensagem** (média): default humano em WhatsApp; IA capitaliza e pontua tudo.
- **Reduções orais** (média): tá, né, pra, tô, tava, cê. IA moderna instruída já usa, mas dosa uniformemente, sem variação.
- **Frase quebrada e anacoluto** (média): "é que eu ia falar isso mas enfim". Humano abandona frase no meio; IA fecha todas e amarra com conectivo.

Calibração do checklist inverso:

1. Marcas fortes (asterisco de correção, mas/mais, "concerteza", kkkk irregular, palavrão abreviado) reduzem drasticamente a suspeita.
2. A ausência delas só pesa como sinal de IA em registro onde eram esperadas (chat, comentário, DM); nunca em artigo ou e-mail formal.
3. Humanizadores de IA já injetam gírias e "erros": desconfiar de informalidade distribuída uniformemente, sem inconsistência interna.
4. Regra bidirecional de limpeza: nunca corrigir essas marcas em texto humano informal (vira slop) nem injetá-las em texto de IA (vira texto falso).

## 14. Padrões de detecção

Ordem prática de varredura:

1. **Grep determinístico primeiro** (seção 11): disclaimers de cutoff, recusas, preâmbulos de chat, placeholders, "resposta regenerada". Uma ocorrência encerra a questão.
2. Sinais estruturais e tipográficos (seção 9): travessões densos, emoji-lista, fragmentação, Title Case, vírgula de Oxford.
3. Acúmulo lexical e de fórmulas (seções 1 a 8 e 10).
4. Sinais inversos (seção 13) para reduzir a suspeita.

Sinais em nível de frase:

1. Frase que abre com "É importante ressaltar que" ou variação.
2. Dois ou mais amortecedores na mesma frase ("em muitos casos, pode, até certo ponto...").
3. "Navegar" junto de "complexidades/cenário/desafios" na mesma frase.
4. Primeira frase que promete o que o texto fará em vez de fazer.
5. Gerúndio conclusivo pendurado no fim do período ("...garantindo mais eficiência.").
6. Gíria e conectivo formal na mesma frase (colisão de registro, 12.5).

Sinais em nível de parágrafo:

1. Parágrafo de abertura que é pura ambientação panorâmica ou meta-comentário.
2. Todo parágrafo abrindo com conectivo (a grade fixa de 10.2 é o caso extremo).
3. Parágrafo final "Em suma..." que recapitula sem acrescentar nada.
4. Cabeçalho seguido de primeira linha que o reafirma.
5. Toda enumeração em trio de abstrações.

Sinais em nível de documento:

- **Regra do acúmulo**: 3+ padrões distintos no mesmo texto = quase certeza de IA. Exceção: os resíduos da seção 11 são quase-prova sozinhos.
- **Densidade e posição pesam mais que ocorrência**: um "além disso" é português normal; um por parágrafo é assinatura.
- **Burstiness baixa** (variação de ritmo e comprimento entre frases): 6+ frases consecutivas de 18-22 palavras, todas sujeito-verbo-objeto, sem frase curta de impacto nem período longo.
- **Riqueza lexical baixa**: mesmo substantivo repetido dezenas de vezes sem pronome ou sinônimo; mesmo trigrama em vários parágrafos. A característica mais robusta entre as 284 testadas em 27 LLMs (arXiv 2606.04177).
- **Densidade de conectivos**: uma transição a cada 3-4 frases, ou conectivo abrindo cada parágrafo.
- **Densidade tipográfica**: 2+ travessões por parágrafo; 3+ linhas com emoji-marcador; percentual alto de palavras em negrito.
- **Uniformidade de parágrafos**: todos com o mesmo número de frases e linhas.
- **Razão de compressão**: reescrevível em cerca de 20% das palavras sem perda = slop.
- **Contagem de especificidade**: entidades verificáveis (nomes próprios, números, datas, casos concretos, referências locais) próximas de zero = generiquês.
- **Uniformidade da informalidade** (anti-humanizador): gírias, "né", "pra" e emojis em intervalos regulares, sem a inconsistência interna humana (vc/você, tá/está alternados).
- **Sinais comparativos de chat**: resposta rápida demais, longa demais e perfeita demais contra o histórico do mesmo interlocutor. A mudança súbita de padrão é o sinal, não o estado absoluto.

Aviso sobre detectores automáticos: não são confiáveis em português. No estudo IFAL/SBC 2025, o ZeroGPT detectou cerca de 97% dos textos gerados, mas acusou cerca de 30% de falsos positivos em textos 100% humanos. Não usar a pontuação de detector como prova; usar as marcas linguísticas deste catálogo. Os marcadores relevantes são palavras de estilo (verbos, adjetivos, advérbios), não substantivos de conteúdo; o vocabulário isolado está enfraquecendo como sinal, enquanto a estrutura segue firme.

## 15. Estratégias de limpeza

Cortes imediatos (remover por inteiro):

- Meta-comentário sobre o que o texto vai discutir.
- Molduras de ênfase ("é importante ressaltar que") e rótulos de fecho ("em suma").
- Conectivos entre ideias já claramente conectadas.
- Redundâncias, pares redundantes e intensificadores vazios.
- Resíduos de chat (seção 11): o parágrafo inteiro, não só a frase.

Reescritas:

- Voz passiva para voz ativa; sujeito nomeado no lugar de agente vago.
- Buzzword para termo específico; promessa genérica para número ou entrega real.
- Pilha de hedges para UMA afirmação precisa (se a incerteza é real, declará-la concretamente).
- Construção prolixa para a alternativa curta (tabela da seção 7).
- Travessão para vírgula, dois-pontos, parênteses ou ponto (regra da seção 9).
- Calco de tradução para o equivalente natural (tabela da seção 8).

Melhorias estruturais:

- Abrir pelo ponto central, não por preâmbulo ou ambientação panorâmica.
- Exemplo concreto no lugar de afirmação abstrata; nome, data e número no lugar de "diversos casos".
- Variar comprimento de frase e de parágrafo deliberadamente.
- Quebrar tríades e listas paralelas perfeitas; remover emoji-marcador.
- Cortar a seção "Conclusão" que só recapitula; terminar no último ponto forte.

Testes rápidos:

- **Teste da troca**: a frase sobrevive se trocada para outra empresa, livro ou assunto? Então é slop.
- **Teste do textão**: dá para dizer em 20% das palavras? Corte até sobrar tese + justificativa.
- **Teste da fonte**: "estudos apontam" tem autor, instituição e ano? Se não, citar ou reformular.

Regra bidirecional: a limpeza nunca deve corrigir marcas humanas de texto humano informal (seção 13) nem injetar marcas humanas em texto de IA. As duas direções produzem texto falso.

## 16. O contexto importa

Nem todo padrão é sempre slop. Pesar:

- **Audiência**: texto acadêmico admite mais hedging que post de blog; estrutura introdução/desenvolvimento/conclusão e roadmap ("Neste artigo...") são exigidos em gênero acadêmico formal.
- **Propósito**: documento jurídico exige precisão e admite "no que tange a"; marketing admite energia, não promessa vazia.
- **Comprimento**: texto longo precisa de mais transições que texto curto; "em suma" cabe em dissertação longa, não em post de 3 parágrafos.
- **Domínio**: "robusto" é legítimo em engenharia e estatística, "alavancagem" em finanças, "otimizar" em SEO e performance, "escalável" e "disruptivo" em discussão real de startups e inovação, "jornada do cliente" em marketing.

Casos aceitáveis específicos do pt-BR:

- Travessão em diálogo de narrativa (convenção da língua) e em aparte pontual e deliberado de texto editorial; o problema é densidade e contexto.
- Conectivos do dialeto ENEM dentro de redação de vestibular real: legítimos peça a peça; o sinal é o pacote completo ou o registro dissertativo fora da escola.
- "Espero que ajude" isolado em fórum, "fico à disposição" em e-mail comercial, "espero que esteja bem" curto: hábitos humanos comuns; denunciam apenas nas combinações das seções 1 e 11.
- Placeholders em colchetes em modelos compartilhados de propósito e em conteúdo que ensina prompts; "Como um modelo de linguagem..." quando o texto cita deliberadamente uma resposta de IA.
- "Saiba mais" como botão nativo obrigatório de anúncio; "Comece agora" como convenção de botão SaaS.
- Ortografia impecável NÃO é prova de IA: falso positivo documentado (quem escreve bem é acusado injustamente). Só pesa em registro de chat, contra o histórico da própria pessoa.
- Texto técnico-científico é naturalmente previsível: não aplicar burstiness e perplexidade como prova isolada.
- Tríades, analogias e pergunta final de engajamento: retórica humana legítima em dose única; o sinal é a constância.

O que caracteriza slop é o excesso e a repetição inconsciente, não a existência isolada do padrão.
