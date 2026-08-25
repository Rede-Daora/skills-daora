---
name: anti-slop-ptbr
description: Conjunto de ferramentas para detectar e eliminar "slop de IA" (padrões genéricos e de baixa qualidade que denunciam conteúdo gerado por inteligência artificial) em linguagem natural, código e design, com padrões voltados a conteúdo em português brasileiro. Use ao revisar ou melhorar a qualidade de conteúdo, prevenir padrões genéricos de IA, limpar conteúdo existente ou definir padrões de qualidade em escrita, código ou design.
metadata:
  mcpmarket-version: 1.0.0
---
# Skill Anti-Slop pt-BR

> **Nota do Kit Skill Daora:** Neste kit, VOCÊ (o agente) é quem executa os
> comandos de detecção e limpeza descritos abaixo. O usuário nunca digita
> comandos Python: ele apenas pede em linguagem simples ("esse texto ficou
> com cara de robô?") e você roda os scripts, interpreta o resultado e
> explica tudo em português do Brasil simples, seguindo o AGENTS.md.

Detecta e elimina "slop de IA": padrões genéricos e de baixa qualidade que denunciam conteúdo gerado por inteligência artificial, em linguagem natural, código e design, com foco em português brasileiro.

## O que é slop de IA

Slop de IA são as marcas que entregam conteúdo genérico produzido por máquina:

- **Texto**: frases batidas como "vamos mergulhar", excesso de buzzwords, meta-comentário, calcos de tradução do inglês, clichês de redação escolar, travessões em série
- **Código**: nomes de variáveis genéricos, comentários óbvios, abstração desnecessária
- **Design**: layouts de template, gradientes genéricos, padrões visuais repetidos à exaustão

Esta skill identifica e remove esses padrões para produzir conteúdo autêntico e de qualidade.

## Quando usar esta skill

Aplique as técnicas anti-slop quando:
- For revisar conteúdo gerado por IA antes da entrega
- For criar conteúdo original e quiser evitar padrões genéricos
- For limpar conteúdo existente que soa genérico
- For definir padrões de qualidade para um projeto
- O usuário pedir detecção ou limpeza de slop
- O conteúdo tiver sinais típicos de geração por IA sem revisão

## Fluxo principal

### 1. Detectar slop

**Para arquivos de texto:**
```bash
python scripts/detect_slop.py <arquivo> [--verbose] [--ignore-placeholders] [--ignore-contrast]
```

A análise retorna:
- Pontuação de slop (0-100; quanto maior, pior)
- Ocorrências específicas por padrão, com linha e trecho
- Recomendações práticas

Flags opcionais:
- `--ignore-placeholders`: ignora placeholders entre colchetes (`[DATA]`, `[SEU NOME]`), que em templates didáticos são intencionais
- `--ignore-contrast`: ignora a fórmula de contraste "não é X, é Y" repetida, quando o contraste é a voz do documento (recursos pedagógicos)

**Detecção manual:**
Leia o arquivo de referência da área:
- `references/text-patterns.md`: padrões de slop em linguagem natural pt-BR
- `references/code-patterns.md`: padrões de slop em programação
- `references/design-patterns.md`: padrões de slop em design visual e UX

### 2. Limpar slop

**Limpeza automática (só texto):**
```bash
# Prévia das mudanças
python scripts/clean_slop.py <arquivo>

# Aplicar mudanças (cria backup)
python scripts/clean_slop.py <arquivo> --save

# Modo agressivo (pode alterar levemente o sentido)
python scripts/clean_slop.py <arquivo> --save --aggressive
```

**Limpeza manual:**
Aplique as estratégias dos arquivos de referência conforme os padrões detectados.

## Detecção e limpeza de slop em texto

### Alvos prioritários

**Remova de imediato:**
- "vamos mergulhar em" → remover; entre direto no assunto
- "no cenário atual" / "em um mundo cada vez mais..." → remover
- "na era digital" / "no mundo acelerado de hoje" → remover
- "é importante ressaltar que" → remover; afirme direto
- "desvendar os segredos" → "explicar"
- Meta-comentário sobre o próprio texto ("neste artigo vamos...")

**Simplifique construções prolixas:**
- "a fim de" → "para"
- "devido ao fato de que" → "porque"
- "tem a capacidade de" → "pode"
- "levar em consideração" → "considerar"
- "realizar uma análise" → "analisar"

**Substitua buzzwords:**
- "alavancar" → "usar"
- "sinergia" → "cooperação"
- "mudança de paradigma" → "grande mudança"
- "de ponta" → "avançado"
- "divisor de águas" → "marco"

**Corte calcos de tradução:**
- "cenário em constante evolução" → "o mercado muda rápido", ou cortar
- "elevar ao próximo nível" → resultado concreto e mensurável
- "desbloquear o potencial" → dizer o que a pessoa passa a conseguir fazer
- "uma gama de" / "um leque de" → número real, ou "vários"

### Princípios de qualidade

**Seja direto:**
- Corte preâmbulos e meta-comentário
- Abra com o ponto central
- Corte conectivos que não acrescentam sentido ("nesse sentido", "dessa forma")

**Seja específico:**
- Troque termos genéricos por exemplos concretos
- Nomeie coisas específicas em vez de "itens", "coisas", "dados"
- Use verbos precisos em vez de verbos vagos

**Seja autêntico:**
- Varie a estrutura e o comprimento das frases
- Prefira voz ativa
- Escreva na voz adequada ao contexto, não no genérico corporativo

## Política de travessão

O travessão em excesso é hoje um dos sinais mais reconhecíveis de texto de IA em pt-BR. Regra do projeto:

1. Se o texto funciona sem travessão, remova o travessão. Reescreva com vírgula, dois-pontos, parênteses ou ponto final, o que couber melhor.
2. Use travessão apenas quando indispensável: fala de diálogo em narrativa (travessão no início da linha) e raros apartes em que nenhuma outra pontuação preserva o sentido.
3. Intervalos numéricos como `1990–2000` não contam como slop.

Os scripts tratam pares e solitários de forma diferente: `detect_slop.py` reporta todo travessão no meio da frase e recomenda reescrever; `clean_slop.py` converte pares de aparte em parênteses no modo normal e só converte travessão solitário em vírgula no modo agressivo. Linhas de diálogo (que começam com travessão) são puladas por inteiro pelos dois scripts: nenhum travessão dessas linhas é reportado ou alterado, incluindo os de atribuição no meio da fala. Travessão entre dígitos também nunca é alterado.

## Detecção e limpeza de slop em código

### Alvos prioritários

**Renomeie variáveis genéricas:**
- `data` / `dados` → nomeie o que os dados representam
- `result` / `resultado` → nomeie o que o resultado contém
- `temp` → nomeie o que está guardando temporariamente
- `item` → nomeie o tipo de item

**Remova comentários óbvios:**
```python
# Ruim
# Cria um usuário
usuario = Usuario()

# Melhor: deixe o código falar
usuario = Usuario()
```

**Simplifique código superengenheirado:**
- Remova camadas de abstração desnecessárias
- Troque padrões de projeto usados sem propósito
- Simplifique implementações complexas de tarefas simples

**Melhore nomes de funções:**
- `handleData()` → o que você faz com os dados?
- `processarItens()` → que processamento, especificamente?
- `gerenciarUsuarios()` → qual ação de gerenciamento?

### Princípios de qualidade

**Clareza acima de esperteza:**
- Escreva código fácil de entender
- Otimize apenas quando o profiling mostrar necessidade
- Prefira soluções simples às complexas

**Nomes com significado:**
- Nome de variável descreve o conteúdo
- Nome de função descreve ação + objeto
- Nome de classe descreve a responsabilidade

**Documentação na medida:**
- Documente o porquê, não o quê
- Dispense documentação de código autoexplicativo
- Concentre a documentação em APIs públicas e lógica complexa

## Detecção e limpeza de slop em design

### Alvos prioritários

**Slop visual:**
- Fundos com gradiente genérico (roxo/rosa/ciano)
- Excesso de glassmorphism ou neumorphism
- Formas 3D flutuantes sem propósito
- Todos os elementos com o mesmo tratamento visual

**Slop de layout:**
- Layout de template que ignora as necessidades do conteúdo
- Tudo em cards, independentemente do tipo de conteúdo
- Espaço em branco excessivo sem hierarquia
- Tudo centralizado

**Slop de copy:**
- Manchetes tipo "Eleve seu negócio ao próximo nível"
- CTAs genéricos como "Saiba mais" ou "Comece agora" sem contexto
- Descrições carregadas de buzzwords
- Estética de banco de imagens

### Princípios de qualidade

**Design orientado pelo conteúdo:**
- Projete a partir do conteúdo real
- Crie hierarquia por importância
- O conteúdo determina o layout, não o template

**Escolhas intencionais:**
- Toda decisão de design deve ser justificável
- Use padrões porque servem ao usuário, não porque estão na moda
- Varie o tratamento visual conforme a importância do elemento

**Voz autêntica:**
- O copy deve refletir a personalidade da marca
- Evite o marketês genérico
- Seja específico na proposta de valor

## Arquivos de referência

Consulte estes guias ao trabalhar em cada área:

- **[text-patterns.md](references/text-patterns.md)**: catálogo completo de padrões de slop em linguagem natural pt-BR, com regras de detecção e estratégias de limpeza

- **[code-patterns.md](references/code-patterns.md)**: antipadrões de programação em várias linguagens, com orientação de refatoração

- **[design-patterns.md](references/design-patterns.md)**: padrões de slop em design visual e UX, com estratégias de melhoria

Cada referência inclui:
- Definições e exemplos dos padrões
- Sinais de detecção (confiança alta/média)
- Contextos em que o padrão é aceitável
- Estratégias específicas de limpeza

## Scripts

### detect_slop.py

Analisa arquivos de texto em busca de padrões de slop de IA em pt-BR. A classe `SlopDetector` aplica regexes linha a linha e soma pontos por categoria; a pontuação final é normalizada por 1000 palavras, com teto de 100.

**Uso:**
```bash
python scripts/detect_slop.py <arquivo> [--verbose|-v] [--ignore-placeholders] [--ignore-contrast]
```

`--ignore-placeholders` ignora placeholders entre colchetes (`[DATA]`, `[SEU NOME]`), intencionais em templates didáticos. `--ignore-contrast` ignora a fórmula "não é X, é Y" repetida, quando o contraste é voz do documento.

**Categorias e pesos:**

| Chave interna | O que cobre | Peso |
|---|---|---|
| `high_risk` | Frases de alto risco pt-BR: "vamos mergulhar", "desvendar os mistérios/segredos", "em um mundo cada vez mais", "no cenário atual", "na era digital", "vivemos em uma sociedade onde", "no mundo acelerado de hoje", "na sociedade contemporânea", "espero que esta mensagem o encontre bem", "você já parou para pensar", "e se eu te dissesse que", "aqui está o que", "eis o que", "mergulhar de cabeça" | 15 |
| `medium_risk` | Muletas de transição: "além disso", "ademais", "outrossim", "nesse sentido", "dessa forma", "diante disso", "em suma", "em resumo", "vale ressaltar", "vale destacar", "cabe destacar", "por fim", "primeiramente", "é fundamental", "é crucial" | 8 |
| `buzzwords` | Buzzwords: "alavancar", "sinergia", "disruptivo", "inovador", "robusto", "escalável", "impulsionar", "potencializar", "empoderar", "otimizar", "agregar valor", "mudança de paradigma", "abordagem holística", "divisor de águas", "de ponta", "revolucionário", "transformador", "dinâmico", "vibrante", "mindset", "seamless"/"sem costura", "game-changer" | 5 |
| `meta_commentary` | Meta-comentário: "neste artigo vamos", "ao longo deste texto", "como vimos anteriormente", "é importante ressaltar/destacar/notar/frisar/salientar/mencionar que", "vale a pena notar/mencionar/lembrar", "antes de prosseguir", "agora que já vimos" | 10 |
| `hedging` | Atenuação excessiva (hedging): "pode ou não", "poderia potencialmente", "de certa forma", "em certa medida", "de modo geral", "geralmente falando", "pode-se argumentar que", "alguns diriam que", "parece que", "aparentemente," (com vírgula, como marcador de discurso) | 6 |
| `translationese` | Calcos de tradução: "tapeçaria de" (uso figurado), "testemunho de" figurado, "no reino de", "no coração de" figurado, "uma gama de", "um leque de", "panorama em constante evolução", "cenário em constante mudança/evolução", "elevar ao próximo nível", "desbloquear o potencial", "quando se trata de", "dito isso", "no que diz respeito a", "embarcar em uma jornada", "jornada de transformação/descoberta/aprendizado" | 8 |
| `cliche_redacao` | Clichês de redação escolar/ENEM: "desde os primórdios", "hodiernamente", "é notório que", "diante desse cenário", "diante do exposto", "nesse ínterim", "à luz de", "consoante", "sob essa ótica/perspectiva", "faz-se necessário", "medidas cabíveis", "é de suma importância", citação genérica de Bauman/"modernidade líquida" | 10 |
| `residuo_ia` | Resíduos de IA (quase-prova): "como uma IA/inteligência artificial/modelo de linguagem, não posso..." e "sou um modelo de linguagem", "desculpe, não posso ajudar", "claro! aqui está", "certamente! aqui", "espero que (isso) ajude", "fico feliz em ajudar", "até minha data de corte", "com base no meu treinamento", placeholder "[inserir ...]", "ótima pergunta!", "você está absolutamente cert..." | 40 |
| `em_dash` | Travessões: `—` (U+2014) e `–` (U+2013) no meio da frase; pula por inteiro linhas cujo primeiro caractere útil (após indentação e marcadores de blockquote) é travessão (diálogo pt-BR e atribuição de citação) e ignora travessão entre dígitos (intervalos como `1990–2000`) | 4 |
| `structure` | Estrutura do documento: abertura panorâmica na primeira linha não vazia; mais de 30% dos parágrafos iniciando com conectivo de transição; 2+ contrastes "não é X ... é Y" no texto; emoji de lista em 3+ linhas | 20 |

**Saída:**
- Pontuação geral de slop (0-100)
- Ocorrências por categoria, com número da linha e trecho
- Seção RECOMENDAÇÕES em pt-BR cobrindo cada categoria encontrada (impressa quando a pontuação passa de 20 ou quando há resíduo de IA)
- Para travessões (título impresso: TRAVESSÕES), a recomendação é reescrever sem travessão (vírgula, dois-pontos, parênteses ou ponto) e manter apenas quando indispensável

**Faixas de pontuação:**
- 0-20: slop baixo (escrita autêntica)
- 20-40: slop moderado (alguns padrões)
- 40-60: slop alto (muitos padrões)
- 60+: slop severo (genérico do início ao fim)

### clean_slop.py

Remove automaticamente padrões comuns de slop em arquivos de texto pt-BR, com a classe `SlopCleaner`.

**Uso:**
```bash
# Prévia das mudanças
python scripts/clean_slop.py <arquivo>

# Salvar mudanças (cria backup)
python scripts/clean_slop.py <arquivo> --save

# Salvar em outro arquivo
python scripts/clean_slop.py <arquivo> --output arquivo_limpo.txt

# Modo agressivo
python scripts/clean_slop.py <arquivo> --save --aggressive
```

**O que limpa, nesta ordem:**
- Resíduos de IA (primeira operação, já no modo normal): preâmbulos de chat ("Claro! Aqui está..."), fechos de assistente ("Espero que isso ajude", "Fico feliz em ajudar", "Se precisar de mais alguma coisa...") e disclaimers de modelo ("Como uma IA, não posso...")
- Frases de alto risco
- Construções prolixas: "a fim de" → "para", "devido ao fato de que" → "porque", "neste momento" → "agora", "com o objetivo de" → "para", "tem a capacidade de" → "pode", "é capaz de" → "pode", "apesar do fato de que" → "embora", "levar em consideração" → "considerar", "tomar uma decisão" → "decidir", "realizar uma análise" → "analisar", "no caso de" → "se", "de forma a" → "para", "no sentido de" → "para", "por meio da utilização de" → "com"
- Meta-comentário
- Atenuação excessiva (hedging)
- Buzzwords: "alavancar" → "usar", "utilizar" → "usar", "sinergia" → "cooperação", "mudança de paradigma" → "grande mudança", "de ponta" → "avançado", "divisor de águas" → "marco", "potencializar" → "aumentar", "impulsionar" → "aumentar", "empoderar" → "dar autonomia a"
- Redundâncias (pleonasmos): "certeza absoluta" → "certeza", "consenso geral" → "consenso", "planos futuros" → "planos", "resultado final" → "resultado", "elo de ligação" → "elo", "totalmente único" → "único", "conclusão final" → "conclusão", "criar novo" → "criar", "há anos atrás" → "há anos"
- Intensificadores vazios: "extremamente", "incrivelmente", "absolutamente" antes de adjetivo comum; "muito único" → "único"
- Calcos de tradução com substituição segura
- Travessões: pares de aparte (`x — aparte — y`) viram parênteses no modo normal; travessão solitário no meio da frase só vira vírgula no modo agressivo; linhas de diálogo ou atribuição de citação (primeiro caractere útil, após indentação e marcadores de blockquote, é travessão) são puladas por inteiro, sem alterar nenhum travessão da linha; intervalos entre dígitos nunca são alterados
- Modo agressivo: remove conectivos no início de parágrafo ("Além disso, ", "Ademais, ", "Nesse sentido, ", "Dessa forma, ", "Vale ressaltar que ", "É importante destacar que ") e molduras "É importante/crucial/fundamental (que | notar que)"
- Normalização final de espaçamento: colapsa espaços e vírgulas duplas, remove espaço antes de pontuação, recapitaliza após ponto

**Cuidados com falsos positivos:**
- "utilizar" não casa dentro de "reutilizar" (o script usa borda de palavra)
- "jornada" solta é português legítimo ("jornada de trabalho", "jornada escolar") e não é detectada nem substituída; o detector aponta apenas as formas compostas do calco, como "embarcar em uma jornada" e "jornada de transformação/descoberta/aprendizado", e o limpador nunca mexe em "jornada"
- Substituições respeitam gênero quando a palavra seguinte depende disso; na dúvida, o script escolhe substituto neutro

**Segurança:**
- Sempre cria arquivo `.backup` ao sobrescrever
- O modo prévia mostra as mudanças antes de aplicar
- Preserva o sentido do conteúdo (modo não agressivo)

## Boas práticas

### Prevenir antes de remediar

**Ao criar conteúdo:**
1. Escreva com um público específico em mente
2. Use exemplos concretos em vez de abstrações
3. Abra com o ponto central, sem preâmbulos
4. Escolha palavras pela precisão, não pela pose
5. Revise antes de dar por pronto

### Limpeza sensível ao contexto

Nem todo padrão é sempre slop:

**Contextos aceitáveis:**
- Escrita acadêmica pede mais atenuação
- Documentos jurídicos exigem fraseado específico
- Documentação interna pode usar atalhos
- Documentação técnica tem convenções da área
- Conectivos formais como "ademais" e "outrossim" são legítimos em petição jurídica e texto acadêmico formal

**Sempre pergunte:**
- Quem é o público?
- Qual é o propósito?
- Esse padrão cumpre alguma função?
- Existe alternativa melhor?

### Melhoria iterativa

1. **Detectar**: rode os scripts ou faça revisão manual
2. **Analisar**: entenda quais padrões são problema de verdade
3. **Limpar**: aplique a limpeza automática onde for seguro
4. **Revisar**: confira manualmente se as mudanças preservam o sentido
5. **Refinar**: corrija o restante à mão

### Julgamento acima de automação

Os scripts são ferramentas, não substitutos de critério:
- Use a detecção automática para achar candidatos
- Aplique a limpeza automática em padrões óbvios
- Revise manualmente tudo que muda o sentido
- Decida conforme o contexto

## Padrões de integração

### Revisão antes do commit

```bash
# Verificar arquivos antes de commitar
python scripts/detect_slop.py src/documentacao.md --verbose

# Limpar automaticamente
python scripts/clean_slop.py src/documentacao.md --save
```

### Pipeline de conteúdo

1. Criar o conteúdo inicial
2. Rodar a detecção de slop
3. Aplicar a limpeza automática
4. Revisar e refinar manualmente
5. Verificação final de qualidade

### Aplicação de padrões de qualidade

Defina limites específicos do projeto:
- Pontuação de slop máxima aceitável: 30
- Revisão manual obrigatória para pontuações acima de 20
- Rejeição automática de envios com pontuação acima de 50

## Limitações

**Os scripts só tratam texto:**
- A detecção de slop em código é manual (use code-patterns.md)
- A detecção de slop em design é manual (use design-patterns.md)

**Sensibilidade a contexto:**
- Os scripts não entendem todos os contextos
- Parte do "slop" pode ser adequada em certas áreas
- Sempre revise as mudanças automáticas

**Cobertura de idioma:**
- Padrões de detecção otimizados para português brasileiro
- Para textos em inglês, use a skill anti-slop original em inglês
- Padrões de código focam linguagens comuns (Python, JS, Java)
- Padrões de design independem de plataforma

## Cenários comuns

### Cenário 1: revisar conteúdo gerado por IA

```bash
# Pedido do usuário: "Revise este artigo procurando padrões de IA"
1. Leia references/text-patterns.md para saber o que procurar
2. Rode: python scripts/detect_slop.py artigo.txt --verbose
3. Analise os achados e aplique limpeza manual
4. Se quiser: python scripts/clean_slop.py artigo.txt --save
5. Faça a revisão manual final do texto limpo
```

### Cenário 2: limpar uma base de código

```bash
# Pedido do usuário: "Me ajude a limpar padrões genéricos de IA no meu código"
1. Leia references/code-patterns.md
2. Revise os arquivos manualmente em busca dos padrões
3. Liste os nomes genéricos a renomear
4. Refatore seguindo os princípios de code-patterns.md
5. Remova comentários óbvios e abstrações em excesso
```

### Cenário 3: revisão de design

```bash
# Pedido do usuário: "Esse design ficou com cara de template?"
1. Leia references/design-patterns.md
2. Compare com os indicadores de alta confiança
3. Identifique problemas específicos (gradientes, layout, copy)
4. Traga recomendações específicas de design-patterns.md
5. Sugira alternativas concretas
```

### Cenário 4: definir padrões de qualidade

```bash
# Pedido do usuário: "Ajude a criar padrões de qualidade para o nosso time"
1. Revise os três arquivos de referência
2. Identifique os padrões mais relevantes para a área do usuário
3. Crie diretrizes específicas do projeto
4. Configure os scripts de detecção no pipeline de desenvolvimento
5. Documente as exceções aceitáveis
```

## Dicas

**Para limpeza de texto:**
- Rode a detecção primeiro para dimensionar o trabalho
- Use o modo não agressivo em conteúdo importante
- Sempre revise as mudanças automáticas
- Comece pelos resíduos de IA e pelas frases de alto risco

**Para limpeza de código:**
- Comece renomeando variáveis genéricas
- Depois remova comentários óbvios
- Deixe a refatoração de código superengenheirado por último
- Teste após cada mudança relevante

**Para limpeza de design:**
- Audite os elementos visuais contra os padrões catalogados
- Priorize problemas estruturais sobre os estéticos
- Toda mudança deve servir ao usuário
- Mantenha a consistência da marca

**Princípios gerais:**
- Qualidade > uniformidade
- Contexto > regras
- Clareza > esperteza
- Especificidade > generalidade
