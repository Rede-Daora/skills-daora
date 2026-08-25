---
name: design-patterns
description: Guia de referência para detectar padrões de slop de IA em design visual e UX, incluindo gradientes genéricos, layouts de template e copy cheio de buzzwords. Use como referência ao revisar qualidade de design.
---

# Padrões de slop em design

Esta referência documenta padrões comuns de "slop de IA" (padrões genéricos e de baixa qualidade que denunciam conteúdo gerado por inteligência artificial) em design visual e UX.

## Sumário
- Slop de design visual
- Cor e tipografia
- Antipadrões de layout
- Excesso de componentes
- Slop de UX writing
- Animação e interação

## Slop de design visual

### Fundos com gradiente genérico
**Padrões de alto risco:**
- Gradientes mesh roxo/rosa/azul (o gradiente "startup de IA")
- Gradientes holográficos em tudo
- Sobreposição de gradiente em toda imagem
- Gradiente como elemento principal do design, não como detalhe

**Abordagem melhor:**
- Use cores sólidas como base
- Gradientes com parcimônia, para dar ênfase
- Considere paletas específicas da marca
- Explore texturas, padrões ou ilustrações

### Motivos visuais desgastados
**Clichês comuns de design de IA:**
- Formas geométricas 3D flutuantes (cubos, esferas, toros)
- Glassmorphism em todo lugar
- Neumorphism (soft UI) em elementos onde não cabe
- Efeitos de desfoque em excesso
- Sistemas de partículas sem razão de existir
- Transformações de inclinação/perspectiva em cards

**Sinal de detecção:** se toda seção tem formas 3D flutuantes ou efeito de vidro, provavelmente é slop.

### Estética de banco de imagens
**Sinais de alerta:**
- Fotos genéricas de equipe diversa no escritório
- Espaço em branco excessivo com conteúdo mínimo
- Imagens de hero com pessoas apontando para telas com entusiasmo
- Executivos de terno apertando as mãos
- Fotos de cima do "espaço criativo" com MacBook e café

**Melhor:** use imagens autênticas e específicas, relacionadas ao conteúdo real.

## Cor e tipografia

### Slop de paleta de cores
**Paletas genéricas a evitar:**
- Roxo (#7F5AF0) + Ciano (#2CB67D) + Rosa (#FF6AC1)
- Paleta inteira de tons pastel
- Neon em tudo
- Preto puro (#000) e branco puro (#FFF) como cores principais

**Abordagem melhor:**
- Construa a paleta a partir da marca ou das necessidades do conteúdo
- Use teoria das cores com intenção
- Considere acessibilidade (razões de contraste WCAG)
- Limite a paleta a 2 ou 3 cores primárias mais neutros

### Slop de tipografia
**Combinações de fontes desgastadas:**
- Inter para tudo
- Montserrat + Open Sans
- Poppins + Roboto
- Mesma família de fonte para títulos e corpo de texto

**Escolhas genéricas de fonte:**
- Escolher sans-serif "moderna" por padrão para tudo
- Usar fontes display no corpo do texto
- Pesos e tamanhos de fonte inconsistentes
- Variação excessiva (5+ fontes diferentes)

**Melhor:**
- Escolha fontes que combinem com o tom do conteúdo
- Estabeleça hierarquia clara (H1, H2, corpo, legenda)
- Teste a legibilidade em vários tamanhos
- Use no máximo 2 ou 3 famílias de fontes

### Problemas de hierarquia tipográfica
**Indicadores de slop:**
- Todos os títulos do mesmo tamanho
- Corpo de texto pequeno demais (<16px)
- Altura de linha insuficiente (< 1,5 para corpo de texto)
- Razões de contraste ruins
- Texto centralizado em parágrafos longos

## Antipadrões de layout

### Estrutura genérica de landing page
**O template de landing page de IA:**
```
1. Hero com fundo em gradiente + "Eleve Seu Negócio ao Próximo Nível"
2. Três cards de recursos com ícones
3. Seção de estatísticas com números grandes
4. Depoimentos (quase sempre com cara de inventados)
5. Cards de preços genéricos
6. Seção de FAQ
7. Botão de CTA "Comece Agora"
```

**Melhor:** desenhe o layout com base na jornada do usuário e nas necessidades reais do conteúdo.

### Slop de espaçamento
**Sinais de alerta:**
- Tudo com exatamente o mesmo espaçamento
- Espaço em branco excessivo sem propósito
- Seções apertadas alternando com vãos enormes
- Nenhum agrupamento visual (tudo flutuando por igual)

**Melhor:**
- Use espaçamento para criar hierarquia visual
- Aproxime elementos relacionados
- Varie o espaçamento com intenção
- Siga grades de 8px ou 4px

### Excesso de cards
**Quando cards viram slop:**
- Tudo está dentro de um card
- Cards dentro de cards dentro de cards
- Cards com sombras e bordas exageradas
- Todos os cards do mesmo tamanho, independentemente do conteúdo

**Melhor:**
- Use cards para agrupar informação relacionada
- Varie o estilo do card conforme a importância
- Considere alternativas: bordas simples, cores de fundo, espaçamento

### Tudo centralizado
**Padrão de slop:**
- Todo texto centralizado
- Todos os elementos centralizados na página
- Simetria forçada onde ela não cabe

**Melhor:**
- Use alinhamento com intenção
- Alinhe corpo de texto à esquerda para legibilidade
- Centralize quando servir a um propósito
- Considere layouts assimétricos

## Excesso de componentes

### Slop de botões
**Padrões genéricos de botão:**
- Todo botão com border radius exagerado (totalmente arredondado)
- Botões flutuando com sombras enormes
- Botões com gradiente em todo lugar
- "Ghost buttons" como CTAs primários
- Botões com ícone e sem rótulo de texto

**Melhor:**
- Estilize botões conforme a hierarquia (primário, secundário, terciário)
- Use tamanhos adequados ao contexto
- Garanta área de toque suficiente (mínimo de 44x44px)
- Rótulos claros e orientados a ação

### Slop de ícones
**Sinais de alerta:**
- Ícones de linha genéricos para tudo
- Ícones sem rótulo em contextos ambíguos
- Ícones decorativos que não agregam significado
- Estilos de ícone inconsistentes (misturar contorno e preenchido)
- Ícones de conjuntos diferentes

**Melhor:**
- Use ícones para esclarecer, não para decorar
- Mantenha estilo de ícone consistente
- Inclua rótulo de texto quando o significado não for óbvio
- Use um único sistema de ícones

### Slop de formulários
**Padrões genéricos de formulário:**
- Todo campo com um ícone dentro
- Texto de placeholder em excesso
- Rótulos flutuantes que não agregam valor
- Nenhum estado de erro claro
- Mensagens de validação genéricas

**Melhor:**
- Rótulos claros fora dos campos
- Mensagens de erro que ajudam
- Agrupamento lógico de campos
- Revelação progressiva em formulários complexos

## Slop de UX writing

### Headlines vazias
**Frases desgastadas do institucional brasileiro gerado por IA:**
- "Eleve seu negócio ao próximo nível"
- "Transforme sua rotina" / "Transforme sua vida"
- "Descomplique sua gestão"
- "Soluções personalizadas para suas necessidades"
- "Desvende os segredos que ninguém te conta"
- "Rumo ao sucesso"

**Teste rápido:** troque o nome da empresa e veja se a frase continua valendo. Se continua, é slop.

**Melhor:**
- Prometa o resultado concreto e mensurável ("dobre seus leads em 90 dias", se for verdade)
- Nomeie a mudança específica ("automatize a emissão de notas")
- Liste 2 ou 3 entregas reais ("site, tráfego pago e CRM configurado")

### CTAs genéricos
**Padrões de alto uso e baixo significado:**
- "Saiba mais"
- "Comece agora"
- "Clique aqui"
- "Não perca!"
- "Garanta já o seu"
- "Confira!"

**Melhor:**
- Verbo + objeto + benefício: "Baixe o guia de precificação", "Teste com 50 notas grátis"
- Diga ao usuário exatamente o que acontece ao clicar
- Exceções aceitáveis: "Saiba mais" como botão nativo obrigatório de anúncio (Meta) e "Comece agora" como botão padrão de SaaS, se a ação for essa mesmo

### Urgência falsa
**Microcopy que dispara filtro de spam e desconfiança:**
- "Últimas vagas!"
- "Por tempo limitado"
- "Imperdível"
- "Não perca essa oportunidade única"
- "Corra, é só até hoje!"

**Melhor:** diga o que acaba e quando, de verdade: "Inscrições até sexta, 20 vagas."

### Autoelogio sem prova (jargão de landing page BR)
**Frases que qualquer empresa poderia assinar:**
- "Qualidade incomparável"
- "O melhor do mercado" / "Referência no mercado" / "Líder no segmento"
- "Comprometidos com a excelência"
- "Atendimento humanizado"
- Fecho motivacional "Vamos juntos nessa jornada!"

**Melhor:**
- Prova concreta: nota de avaliação, número de clientes, prêmio nomeado, garantia
- Descreva a prática em vez do adjetivo: "você fala com uma pessoa em até 5 minutos"
- Termine com um CTA específico ou simplesmente termine

### Estados vazios e mensagens de erro
**Slop genérico:**
- "Ops! Algo deu errado"
- "Nenhum item encontrado"
- "Nada por aqui ainda"
- Mensagens de erro que não ajudam a resolver nada

**Melhor:**
- Explique por que o estado está vazio
- Ofereça próximos passos ou ações de recuperação
- Use tom adequado (nada de gracinha em erro grave)

### Exemplo antes/depois (hero de landing page)

**Antes (slop):**
> Fundo com gradiente roxo · "Eleve Seu Negócio ao Próximo Nível" · "Transforme seu fluxo de trabalho com soluções de ponta" · Botão [Comece Agora]

**Depois:**
> Fundo com cor da marca · "Automatize o Processamento de Notas Fiscais" · "Extraia itens de PDFs e sincronize com o ERP em segundos" · Botão [Teste com 50 notas grátis]

## Animação e interação

### Slop de animação
**Padrões desgastados:**
- Tudo aparece com fade-in no scroll
- Efeito parallax em todo elemento
- Animações de deslizamento em excesso
- Elementos quicando
- Elementos 3D girando sem razão

**Melhor:**
- Use animação para direcionar a atenção
- Mantenha animações sutis e com propósito
- Respeite prefers-reduced-motion
- Duração menor que 300ms para a maioria das interações

### Slop de interação
**Padrões genéricos:**
- Efeito de hover em tudo
- Cursor vira pointer em elemento não clicável
- Sinais confusos entre o que é interativo e o que não é
- Padrões de interação inconsistentes

**Melhor:**
- Sinais claros do que é clicável (affordances)
- Padrões de interação consistentes
- Feedback adequado para toda interação
- Considere usuários de toque e de teclado

## Slop por plataforma

### Design web
- Templates de dashboard com métricas genéricas
- Scroll infinito desnecessário
- Pop-ups e modais para tudo
- Banners de consentimento de cookies que escondem o conteúdo

### Design mobile
- Navegação inferior com 5+ itens
- Menu hambúrguer escondendo navegação importante
- Tratamento inconsistente de gestos
- Ignorar convenções da plataforma (iOS vs Android)

### Design de apresentações
- Todo slide com o mesmo template
- Excesso de bullet points
- Texto minúsculo e ilegível
- Fotos genéricas de banco de imagens como fundo
- Transições exageradas entre slides

## Sinais de detecção

### Indicadores de slop de alta confiança
1. O design parece idêntico a outros designs gerados por IA
2. Nenhuma hierarquia visual clara
3. Paleta de cores genérica (roxo/rosa/ciano)
4. Copy composto só de buzzwords e CTAs genéricos
5. Layout segue o template à risca, sem nenhuma customização

### Indicadores de confiança média
1. Uso excessivo de glassmorphism ou neumorphism
2. Todos os componentes com o mesmo peso visual
3. Uso excessivo de padrões de design da moda
4. Nenhuma arquitetura de informação clara
5. Design que ignora as necessidades reais do conteúdo

## Estratégias de limpeza

### Auditoria visual
1. Remova elementos decorativos sem propósito
2. Simplifique a paleta para 2 ou 3 cores principais mais neutros
3. Estabeleça hierarquia tipográfica clara
4. Garanta contraste suficiente para acessibilidade
5. Remova animações e efeitos em excesso

### Redesign a partir do conteúdo
1. Comece pelo conteúdo real e pelas necessidades do usuário
2. Desenhe a hierarquia de informação com base na importância
3. Escolha um estilo visual que combine com o tom do conteúdo
4. Crie layouts que sirvam ao conteúdo, não a templates
5. Teste com conteúdo real, não com lorem ipsum

### Passada de acessibilidade
1. Verifique razões de contraste de cor (mínimo WCAG AA)
2. Garanta que elementos interativos sejam acessíveis por teclado
3. Adicione rótulos ARIA adequados onde necessário
4. Teste com leitores de tela
5. Verifique se todo texto é legível em vários tamanhos

## O contexto importa

Alguns padrões são apropriados no contexto certo:

- **Fundos com gradiente:** ok em sites de marketing, se combinarem com a marca
- **Cards:** apropriados para exibir itens distintos e comparáveis
- **CTAs genéricos:** "Comece agora" é aceitável se for exatamente isso que acontece
- **Animações:** movimento com propósito pode melhorar a UX
- **Fotos de banco de imagens:** às vezes uma imagem genérica é o que se precisa

O problema é a **aplicação irrefletida de padrões**, sem considerar se eles servem às necessidades do usuário ou aos objetivos do design.

## Checklist de sinais de alerta

Seu design pode ser slop se:
- [ ] Poderia ser de qualquer produto ou empresa
- [ ] Parece template da comunidade do Figma
- [ ] Todos os elementos visuais são decorativos, nenhum é informativo
- [ ] O copy é feito só de buzzwords
- [ ] As decisões de design não podem ser justificadas
- [ ] O layout não se adapta ao conteúdo real
- [ ] Nenhuma hierarquia visual clara
- [ ] Parece moderno, mas não serve a propósito nenhum
- [ ] Todo elemento recebe o mesmo tratamento de design
- [ ] O design ignora a marca e o contexto do usuário
