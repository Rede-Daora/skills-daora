# Anti-Slop: kit de qualidade de conteúdo (pt-BR)

> **Nota**: este repositório é um fork da skill [anti-slop original](https://github.com/rand/cc-polymath/tree/main/skills/anti-slop), do repositório [rand/cc-polymath](https://github.com/rand/cc-polymath), adaptado para o português brasileiro.

Skill de Claude Code para detectar e eliminar "slop de IA": padrões genéricos e de baixa qualidade que denunciam conteúdo gerado por inteligência artificial. Esta versão cobre linguagem natural, código e design com padrões específicos do português brasileiro.

## O que você recebe

### 1. Skill anti-slop-ptbr

Pacote de skill para Claude Code contendo:

- **SKILL.md**: documentação principal, com fluxos de trabalho e boas práticas
- **3 guias de referência**:
  - `text-patterns.md`: padrões de slop em linguagem natural pt-BR (frases denunciadoras, calcos de tradução, clichês de redação escolar, linkedinês, resíduos de IA)
  - `code-patterns.md`: antipadrões de programação, com seção sobre slop de código no contexto brasileiro
  - `design-patterns.md`: padrões de slop visual e de UX, com copy de marketing genérico em pt-BR
- **2 scripts Python**:
  - `detect_slop.py`: detecção automática de slop em arquivos de texto
  - `clean_slop.py`: limpeza automática com recursos de segurança

### 2. Atualizações para o CLAUDE.md (`CLAUDE_MD_UPDATES.md`)

Propostas de integração no nível de sistema:

- Ajustes de comportamento para prevenir a geração de slop em pt-BR
- Padrões de qualidade para texto, código e design
- Política de travessão (reescrever sem travessão quando possível)
- Gatilhos proativos para acionar a skill
- Integração com os fluxos de trabalho existentes do Claude

## O que é slop de IA

Slop de IA é o conjunto de padrões denunciadores que sinalizam conteúdo genérico gerado por máquina. Em português brasileiro:

### Slop de texto

- Frases desgastadas: "vamos mergulhar", "em um mundo cada vez mais digital", "no cenário atual"
- Buzzwords em excesso: "alavancar", "sinergia", "disruptivo", "agregar valor"
- Meta-comentário: "Neste artigo, vamos explorar...", "é importante ressaltar que"
- Atenuação excessiva (hedging): "pode ou não", "poderia potencialmente", "de certa forma"
- Calcos de tradução: "tapeçaria de" (uso figurado), "cenário em constante evolução", "desbloquear o potencial"
- Clichês de redação escolar fora do vestibular: "desde os primórdios", "hodiernamente", "diante do exposto"
- Resíduos de IA: "Claro! Aqui está...", "espero que ajude", "até minha data de corte"
- Travessão em excesso no meio das frases

### Slop de código

- Nomes genéricos: `dados`, `resultado`, `temp`, `item`
- Comentários óbvios em português que repetem o código
- Mistura de português e inglês no mesmo identificador (`getUsuario`, `processarData`)
- Camadas de abstração desnecessárias
- Soluções superdimensionadas para problemas simples

### Slop de design

- Layouts de template e estruturas repetidas de landing page
- Fundos com gradiente roxo/rosa/ciano
- Copy de marketing genérico: "Eleve seu negócio ao próximo nível"
- CTAs sem objeto: "Saiba mais", "Comece agora"
- Efeitos da moda sem propósito

## Início rápido

### Instalação

1. **Instale a skill no Claude Code:**
   ```bash
   git clone https://github.com/zanonicode/anti-slop-ptbr.git
   # Importe no Claude Code pelo menu de skills
   # ou copie a pasta para ~/.claude/skills/anti-slop-ptbr
   ```

2. **Teste o script de detecção:**
   ```bash
   python scripts/detect_slop.py seu_arquivo.txt
   ```

3. **Veja a prévia da limpeza:**
   ```bash
   python scripts/clean_slop.py seu_arquivo.txt
   ```

### Uso básico

**Detectar slop em um arquivo de texto:**
```bash
python scripts/detect_slop.py artigo.md --verbose
```

**Limpar slop (com backup):**
```bash
python scripts/clean_slop.py artigo.md --save
```

**Pedir ao Claude para usar a skill:**
```
"Pode revisar este artigo em busca de padrões de texto de IA?"
"Me ajuda a tirar os padrões genéricos de IA do meu código"
"Esse texto está com cara de ChatGPT?"
```

## Uso detalhado

### Análise de texto

O script `detect_slop.py` analisa arquivos de texto e informa:

**Pontuação de slop (0-100)**, normalizada por 1.000 palavras (textos com menos de 500 palavras usam piso de 500 no denominador):

- 0-20: slop baixo (escrita autêntica)
- 20-40: slop moderado (alguns padrões presentes)
- 40-60: slop alto (muitos padrões encontrados)
- 60+: slop severo (texto fortemente genérico)

**Categorias de padrões** (títulos como aparecem no relatório):

- FRASES DE ALTO RISCO: fórmulas quase determinísticas ("vamos mergulhar", "em um mundo cada vez mais", "espero que esta mensagem o encontre bem")
- MULETAS DE TRANSIÇÃO: conectivos de preenchimento ("além disso", "nesse sentido", "outrossim", "vale ressaltar")
- BUZZWORDS E JARGÕES: "alavancar", "sinergia", "disruptivo", "mudança de paradigma", "sem costura"
- META-COMENTÁRIO: "neste artigo vamos", "é importante ressaltar que"
- ATENUAÇÃO EXCESSIVA (HEDGING): "pode-se argumentar que", "de certa forma", "aparentemente," (com vírgula, como marcador de discurso)
- CALCOS DE TRADUÇÃO: "tapeçaria de", "no reino de", "panorama em constante evolução"
- CLICHÊS DE REDAÇÃO: dialeto redação ENEM ("desde os primórdios", "hodiernamente", "nesse ínterim", "medidas cabíveis")
- RESÍDUOS DE IA (QUASE-PROVA): indícios de geração sem revisão ("Claro! Aqui está", "sou um modelo de linguagem", placeholders como "[inserir nome]")
- TRAVESSÕES: travessão e meia-risca no meio da frase (diálogo no início da linha, atribuição de citação em blockquote e intervalos numéricos são ignorados)
- PROBLEMAS ESTRUTURAIS: abertura panorâmica, parágrafos que começam com conectivo, contraste "não é X, é Y" repetido, listas com emoji

Exemplo de saída real ao analisar um texto de teste curto, carregado de slop (a seção RECOMENDAÇÕES é impressa quando a pontuação passa de 20 ou quando há resíduo de IA):

```
======================================================================
Relatório de detecção de slop de IA: teste-texto-slop.md
======================================================================

Pontuação de slop: 100/100
Avaliação: 💀 Slop severo: o documento depende fortemente de padrões genéricos de IA

🔴 FRASES DE ALTO RISCO (5 ocorrências):
  Linha 3: 'Desvendando os segredos' em: # Desvendando os segredos do marketing digital...
  Linha 5: 'vamos mergulhar' em: Neste artigo, vamos mergulhar nas complexidades do marketing...
  Linha 5: 'Em um mundo cada vez mais' em: Neste artigo, vamos mergulhar nas complexidades do marketing...
  ...

📊 MULETAS DE TRANSIÇÃO (7 ocorrências):
  ademais, além disso, em suma, nesse sentido, outrossim, vale destacar, é fundamental

📢 BUZZWORDS E JARGÕES (5 ocorrências):
  alavancar, divisor de águas, empoderar, mudança de paradigma, potencializar

📝 META-COMENTÁRIO (2 ocorrências):
  Linha 5: Neste artigo, vamos mergulhar nas complexidades do marketing digital. ...
  ...

🤔 ATENUAÇÃO EXCESSIVA (HEDGING) (3 ocorrências):
  Encontrada em 1 linha

⚠️  CALCOS DE TRADUÇÃO (3 ocorrências):
  Linha 11: 'elevar seu negócio ao próximo nível' em: Nesse sentido, poderia potencialmente parecer que, de modo g...
  Linha 11: 'jornada de transformação' em: Nesse sentido, poderia potencialmente parecer que, de modo g...
  Linha 13: 'cenário em constante evolução' em: Outrossim, a fim de tomar uma decisão informada, é fundament...

🚨 CLICHÊS DE REDAÇÃO (3 ocorrências):
  Linha 9: 'desde os primórdios da humanidade' em: Ademais, desde os primórdios da humanidade, o ser humano bus...
  Linha 9: 'é notório que' em: Ademais, desde os primórdios da humanidade, o ser humano bus...
  Linha 9: 'Diante desse cenário' em: Ademais, desde os primórdios da humanidade, o ser humano bus...

💀 RESÍDUOS DE IA (QUASE-PROVA) (2 ocorrências):
  Linha 1: 'Claro! Aqui está' em: Claro! Aqui está o artigo solicitado:...
  Linha 17: 'Espero que isso ajude' em: Entre 1990–2000, a internet cresceu de forma exponencial. Em...
  Atenção: uma única ocorrência já é forte indício de texto gerado por IA.

⚠️  TRAVESSÕES (3 no meio de frase):
  Linhas: 7
  Travessões de diálogo/atribuição de citação e intervalos numéricos foram ignorados.

🏗️  PROBLEMAS ESTRUTURAIS:
  • Excesso de transições: 50% dos parágrafos começam com conectivo de transição
  • Contraste "não é X, é Y" repetido: 2 ocorrências da fórmula de contraste no texto

💡 RECOMENDAÇÕES:
  • Substitua as frases de alto risco por linguagem direta e específica
  • Reduza a densidade de conectivos: 'além disso' e afins são português legítimo; um por parágrafo vira assinatura de IA
  • Troque buzzwords por termos concretos: número, exemplo, nome próprio
  • Apague o meta-comentário e comece pelo conteúdo em si
  • Reduza a atenuação: afirme direto ou corte a ressalva
  • Reescreva os calcos de tradução com a expressão natural do português
  • Corte os clichês de redação escolar; prefira dado datado e agente nomeado
  • Remova os resíduos de IA e revise o documento inteiro antes de publicar
  • Reescreva sem travessão (vírgula, dois-pontos, parênteses ou ponto); mantenha apenas quando indispensável
  • Reestruture o documento para evitar padrões genéricos de IA
```

### Limpeza de texto

O script `clean_slop.py` remove automaticamente os padrões mais comuns:

**Modo prévia (padrão):**
```bash
python scripts/clean_slop.py artigo.md
# Mostra o que mudaria, sem alterar o arquivo
```

**Modo salvar (cria backup):**
```bash
python scripts/clean_slop.py artigo.md --save
# Cria artigo.md.backup e sobrescreve o original
```

**Modo agressivo:**
```bash
python scripts/clean_slop.py artigo.md --save --aggressive
# Limpeza mais profunda; pode alterar levemente o sentido
```

**Saída em outro arquivo:**
```bash
python scripts/clean_slop.py artigo.md --output artigo_limpo.md
```

**O que a limpeza faz:**

- Frases de alto risco → removidas ou simplificadas
- Construções prolixas → alternativas curtas ("a fim de" → "para", "devido ao fato de que" → "porque", "tem a capacidade de" → "pode")
- Meta-comentário → removido por inteiro
- Atenuação excessiva → reduzida a um qualificador
- Buzzwords → termos específicos ("alavancar" → "usar", "sinergia" → "cooperação", "divisor de águas" → "marco")
- Redundâncias (pleonasmos) → corrigidas ("certeza absoluta" → "certeza", "elo de ligação" → "elo", "há anos atrás" → "há anos")
- Intensificadores vazios → removidos diante de adjetivos comuns ("extremamente importante" → "importante"; "muito único" → "único")
- Calcos de tradução → substituição segura ("elevar ao próximo nível", "quando se trata de")
- Travessões → pares de aparte viram parênteses no modo normal; travessão solitário no meio da frase só vira vírgula no modo agressivo; linhas de diálogo e atribuições de citação (primeiro caractere útil da linha é travessão, mesmo indentado ou em blockquote) e intervalos numéricos (`1990–2000`) nunca são tocados

**Proteções contra falso positivo:**

- "utilizar" não é capturado dentro de "reutilizar" (borda de palavra)
- "jornada" solta ("jornada de trabalho", "jornada escolar") não é detectada nem substituída (sentido legítimo); o detector aponta apenas as formas compostas típicas de calco, como "embarcar em uma jornada" e "jornada de transformação"
- Substituições que dependem de gênero usam alternativa neutra na dúvida

### Revisão de código

Para código, a skill orienta uma revisão manual:

```bash
# Leia a referência primeiro
view references/code-patterns.md

# Depois revise o código contra os padrões:
# - Nomes genéricos de variáveis
# - Comentários óbvios
# - Superengenharia
# - Abstrações desnecessárias
# - Mistura de português e inglês em identificadores
```

**Correções comuns:**

- `dados` → `preferenciasUsuario`, `historicoTransacoes`, `resultadosBusca`
- `resultado` → `documentoAnalisado`, `itensFiltrados`, `erroValidacao`
- Remover comentários como `# Cria um usuário` antes de `usuario = Usuario()`
- Simplificar implementações complexas de tarefas simples

### Revisão de design

Para trabalho de design, consulte a referência de padrões visuais:

```bash
view references/design-patterns.md
```

**Verificações centrais:**

- A paleta é genérica (roxo/rosa/ciano)?
- O layout segue um template ou serve ao conteúdo?
- O copy é específico ou marketing genérico ("Transforme sua rotina", "Não perca!")?
- Os efeitos visuais têm propósito ou são decoração?
- O design reflete a marca ou parece qualquer startup de IA?

## Guias de referência

### text-patterns.md

Guia de slop em linguagem natural pt-BR:

- Frases de alto risco e ganchos de abertura
- Muletas de transição e arcaísmos de cursinho
- Buzzwords corporativas e linkedinês
- Meta-comentário e resíduos de IA
- Atenuação excessiva e falsa autoridade
- Redundâncias e intensificadores vazios
- Construções prolixas e de enchimento
- Calcos de tradução do inglês
- Clichês do dialeto redação ENEM
- Padrões estruturais e tipográficos (travessão, emoji de lista, "não é X, é Y")
- Estratégias de detecção e limpeza

### code-patterns.md

Antipadrões de programação em várias linguagens:

- Antipadrões de nomenclatura
- Antipadrões de comentário (incluindo comentários em português que repetem o código)
- Antipadrões de estrutura
- Antipadrões de implementação
- Antipadrões de documentação
- Slop específico por linguagem (Python, JS, Java)
- Sinais de detecção e estratégias de refatoração

### design-patterns.md

Padrões de slop em design visual e UX:

- Slop visual (gradientes, efeitos, motivos repetidos)
- Problemas de cor e tipografia
- Antipadrões de layout
- Uso excessivo de componentes
- Slop de UX writing e copy genérico em pt-BR
- Padrões de animação e interação
- Problemas específicos por plataforma
- Estratégias de melhoria

## Integração com o CLAUDE.md

O arquivo `CLAUDE_MD_UPDATES.md` contém propostas de mudança no nível de sistema para que o Claude evite slop por padrão.

**Atualizações principais:**

1. **Consciência anti-slop**: padrões centrais de pt-BR a evitar
2. **Política de travessão**: reescrever sem travessão quando possível
3. **Princípios de qualidade**: escrita direta, específica e autêntica
4. **Padrões de qualidade de código**: nomes com significado, comentários com propósito
5. **Padrões de qualidade de design**: conteúdo primeiro, escolhas intencionais
6. **Gatilhos proativos**: quando acionar a skill automaticamente

**Formas de adoção** (o arquivo documenta em detalhe a adoção gradual; as opções 2 e 3 são alternativas sugeridas por este README):

**Opção 1: integração gradual**
- Comece informando ao Claude que a skill existe
- Adicione gatilhos proativos para os cenários comuns
- Integre os princípios de qualidade com o tempo
- Acompanhe e refine conforme o uso

**Opção 2: integração total**
- Adicione todas as atualizações ao CLAUDE.md de uma vez
- O Claude passa a evitar slop em todas as saídas
- A skill vira prevenção e correção ao mesmo tempo

**Opção 3: controle do usuário**
- Mantenha a skill como ferramenta opcional
- O usuário aciona quando precisar
- Nenhuma mudança no comportamento padrão

## Boas práticas

### Para prevenção

Ao criar conteúdo:

1. Escreva para um público específico
2. Prefira exemplos concretos a abstrações
3. Comece pelo ponto; pule o preâmbulo
4. Escolha palavras pela precisão, não pela impressão
5. Revise contra os padrões de slop antes de finalizar

### Para detecção

Rode a detecção quando:

- O conteúdo parecer genérico ou "com cara de IA"
- For entregar trabalho a um cliente
- Houver processo de revisão de conteúdo
- For definir padrões de qualidade
- For treinar uma equipe em qualidade de escrita

### Para limpeza

Fluxo de limpeza:

1. Rode a detecção para entender o tamanho do problema
2. Veja a prévia da limpeza automática
3. Aplique as mudanças seguras
4. Revise e refine manualmente
5. Confirme que o sentido foi preservado

Notas de segurança:

- Sempre veja a prévia antes de salvar
- Revise as mudanças automáticas com atenção
- Use o modo normal (não agressivo) em conteúdo importante
- Guarde backups dos originais
- Julgue caso a caso os padrões que dependem de contexto (jargão técnico legítimo, diálogo, texto jurídico)

## Cenários comuns

### Cenário 1: revisão de conteúdo
```
Usuário: "Pode revisar este artigo em busca de slop de IA?"

Claude:
1. Lê text-patterns.md como referência
2. Roda o script detect_slop.py
3. Revisa os achados manualmente
4. Opcionalmente roda clean_slop.py
5. Sugere as correções manuais restantes
6. Confere a qualidade do texto final
```

### Cenário 2: limpeza de código
```
Usuário: "Me ajuda a remover padrões genéricos do meu código"

Claude:
1. Lê code-patterns.md
2. Revisa os arquivos de código manualmente
3. Identifica nomes genéricos para renomear
4. Aponta superengenharia para simplificar
5. Sugere remover comentários óbvios
6. Orienta a refatoração
```

### Cenário 3: auditoria de design
```
Usuário: "Esse design está genérico demais?"

Claude:
1. Lê design-patterns.md
2. Confere os indicadores de alta confiança
3. Identifica os problemas específicos
4. Dá recomendações concretas
5. Sugere alternativas
6. Prioriza a necessidade do usuário, não o template
```

### Cenário 4: padrões de qualidade
```
Usuário: "Me ajuda a criar padrões de qualidade para o time"

Claude:
1. Revisa os três guias de referência
2. Seleciona os padrões relevantes para o domínio do usuário
3. Cria diretrizes específicas do projeto
4. Configura a detecção no pipeline
5. Documenta as exceções aceitáveis
6. Produz material de treinamento
```

## Limitações

**Escopo atual:**

- Os scripts de detecção só funcionam em arquivos de texto
- A detecção de slop em código é manual
- A detecção de slop em design é manual
- Os padrões foram calibrados para português brasileiro
- Os padrões de código focam Python, JS e Java

**Sensibilidade a contexto:**

- Os scripts não entendem todos os contextos
- Alguns "padrões de slop" são legítimos em domínios específicos ("robusto" em engenharia, "alavancagem" em finanças, "jornada do cliente" em marketing, conectivos formais em petição jurídica)
- Nenhum sinal isolado prova geração por IA (exceto os resíduos determinísticos, como recusas coladas e disclaimers de data de corte); o que pesa é o acúmulo
- Sempre revise as mudanças automáticas

**Não substitui:**

- Conhecimento do domínio
- Julgamento humano
- Revisão editorial
- Processo de revisão de código
- Crítica de design

## Detalhes técnicos

### Requisitos dos scripts

- Python 3.6+
- Sem dependências externas
- Funciona em Linux, macOS e Windows
- Flags de CLI em inglês (`--save`, `--output`, `--aggressive`, `--verbose`), saída em pt-BR

### Arquitetura dos scripts

**detect_slop.py:**

- Classe `SlopDetector`, análise por regex linha a linha
- 10 categorias de padrões com peso próprio por categoria (resíduos de IA pesam mais: são quase-prova)
- Pontuação normalizada por 1.000 palavras, com piso de 500 palavras no denominador e teto de 100
- Regexes cobrem variações de gênero, número e conjugação
- Relatório detalhado com linha, trecho e recomendações em pt-BR (a seção RECOMENDAÇÕES é impressa quando a pontuação passa de 20 ou quando há resíduo de IA)

**clean_slop.py:**

- Classe `SlopCleaner`, substituição por regex em ordem fixa
- Modos: prévia (padrão), salvar com backup, agressivo, saída em outro arquivo
- Regras de travessão conservadoras (pares viram parênteses; solitários só no modo agressivo)
- Normalização de espaçamento e pontuação ao final

### Desempenho

- Detecção: cerca de 50 ms por 1.000 palavras
- Limpeza: cerca de 100 ms por 1.000 palavras
- Memória: mínima (carrega o arquivo uma vez)
- Saída: relatório detalhado ou texto limpo

## Exemplos

### Exemplo 1: texto antes/depois

**Antes (pontuação: 100/100):**
```
Neste artigo, vamos mergulhar nas complexidades da inteligência
artificial. No mundo acelerado de hoje, é importante ressaltar que
alavancar soluções de ponta pode empoderar empresas a impulsionar
a inovação.
```

**Depois (pontuação: 0/100):**
```
Sistemas de IA modernos equilibram precisão, velocidade e custo.
Este artigo examina esses trade-offs com exemplos de implantações
em produção.
```

### Exemplo 2: código antes/depois

**Antes:**
```python
# Processa os dados
def processar_dados(dados):
    resultado = []
    # Percorre os itens
    for item in dados:
        resultado.append(item)
    return resultado
```

**Depois:**
```python
def filtrar_transacoes_concluidas(transacoes):
    return [t for t in transacoes if t.status == 'concluida']
```

### Exemplo 3: design antes/depois

**Antes:**
```
Fundo com gradiente roxo
"Eleve Seu Negócio ao Próximo Nível"
"Transforme seu fluxo de trabalho com soluções de ponta"
Botão [Comece Agora]
Formas 3D genéricas flutuando
```

**Depois:**
```
Fundo com cor da marca
"Automatize o Processamento de Notas Fiscais"
"Extraia itens de PDFs e sincronize com o ERP em segundos"
Botão [Teste com 50 notas grátis]
Captura de tela da interface real
```

## Contribuindo

Para estender a skill:

1. **Adicione padrões novos** aos guias de referência
2. **Atualize as regexes de detecção** em detect_slop.py
3. **Adicione regras de limpeza** em clean_slop.py
4. **Teste com exemplos reais**, incluindo os falsos positivos conhecidos (acentos, "reutilizar", diálogo com travessão)
5. **Documente cada padrão** com exemplo e substituição sugerida

## Suporte

Para dúvidas ou problemas:

- Consulte os guias de referência
- Veja os cenários de exemplo no SKILL.md
- Teste com os scripts fornecidos
- Considere o contexto antes de aplicar as regras

## Licença

Este kit em pt-BR deriva da skill anti-slop original de [rand/cc-polymath](https://github.com/rand/cc-polymath), distribuída sob a licença MIT. O arquivo LICENSE deste repositório preserva a licença original.

---

## Resumo

A skill anti-slop-ptbr oferece:

- **Detecção**: varredura automática de padrões de slop em texto pt-BR
- **Limpeza**: remoção automática e segura dos padrões mais comuns
- **Prevenção**: guias de referência para texto, código e design
- **Integração**: atualizações de sistema para o Claude
- **Flexibilidade**: uso pontual como ferramenta ou integração ao comportamento

O objetivo: produzir conteúdo autêntico e específico, que serve ao leitor em vez de repetir os tiques do texto de máquina.
