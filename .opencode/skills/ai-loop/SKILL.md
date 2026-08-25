---
name: ai-loop
description: Use quando precisar construir um recurso ou arrumar algo no projeto e for importante conferir item por item se tudo ficou certo antes de dizer que terminou. Roda um ciclo de especificar, construir e conferir, com limite de tentativas.
---

# Ciclo de Trabalho Confiável

## O que é

Um jeito seguro de construir coisas em três voltas:

1. **Anotar** o que será feito (em um arquivo de combinados).
2. **Fazer** exatamente o que foi anotado.
3. **Conferir** item por item se deu certo. Se falhou, volta ao passo 2.

Repete até tudo passar na conferência — com um limite de tentativas
para não girar em falso para sempre.

## Passo 1 — Anotar (os combinados)

Use a entrevista gentil (veja a habilidade `faf-wizard`) e descubra o que
a pessoa precisa. Depois salve um arquivo em `specs/[nome-da-coisa].md`
escrito EM PORTUGUÊS SIMPLES, com:

- O objetivo, em uma frase ("uma página para mostrar meus bolos").
- A lista do que é essencial (cada item começa com "deve...").
- Os casos especiais ("se não tiver foto, mostrar um espaço reservado").
- Como saber que terminou ("a pessoa abre a página e vê X, Y e Z").
- O limite de tentativas (comece com 2) e o que exige pedir ajuda.

NÃO construa nada ainda. Mostre os combinados e peça um "sim".

## Passo 2 — Fazer

- Releia os combinados e construa exatamente aquilo. Nem mais, nem menos.
- NÃO invente recursos extras. NÃO mexa em partes que não estão nos
  combinados.
- Vá contando cada etapa concluída em uma frase simples.

## Passo 3 — Conferir

Compare o que foi feito com os combinados, item por item:

```
Item: deve mostrar a lista de bolos -> OK
Item: deve funcionar no celular     -> OK
Item: botão de WhatsApp             -> FALHOU (botão sumiu no celular)
```

- Se algo falhou e ainda há tentativas: volte ao Passo 2 e conserte.
- Se esgotaram as tentativas: PARE. Conte à pessoa o que falta, em
  linguagem simples, e proponha o próximo caminho juntos.
- Só diga "pronto!" quando TODOS os itens estiverem OK.

## Cuidados de segurança

- Antes de qualquer ação que apaga coisas, muda o site que já está no ar,
  ou envia dados para fora, PARE e peça permissão clara.
- Nunca coloque senhas ou chaves secretas dentro dos arquivos.

## Erros a evitar

- Tentar construir tudo de uma vez. Prefira várias voltas pequenas.
- Dizer "pronto" sem ter conferido todos os itens dos combinados.
- Repetir o mesmo conserto que falhou sem tentar um caminho diferente.
