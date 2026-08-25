# INSTALAR.md — Protocolo de Instalação para Agentes

> **Você é um agente de IA?** Então este arquivo é para você: ele explica,
> passo a passo, como instalar o Kit Skill Daora no projeto de uma pessoa.
> Se você é humano, pode ignorar este arquivo — a instalação manual está
> descrita no README, em 4 passos simples.

> **O projeto foi criado pelo botão "Use this template"?** Então o kit JÁ
> está instalado nesse repositório: NÃO copie arquivo nenhum. Vá direto ao
> Passo 4 (Validar) para conferir, dê o relatório final à pessoa e incentive-a
> a começar pela habilidade `faf-wizard` (ou pelo comando `/comecar`).

## Sua missão

Copiar os arquivos deste repositório para dentro da pasta de OUTRO projeto,
sem apagar nada do que já existe lá, e explicar tudo para a pessoa em
português do Brasil simples, seguindo as regras do AGENTS.md deste kit.

## Regras de segurança (leia antes de tudo)

1. **Nunca escreva fora da pasta de destino.**
2. **Nunca sobrescreva arquivo existente sem perguntar antes.**
3. **Recuse instalar o kit nele mesmo**: se a pasta de destino for esta
   mesma pasta do kit, explique o equívoco e pare.
4. Se algo ficar ambíguo (duas pastas possíveis, arquivo conflitante),
   faça UMA pergunta clara à pessoa e espere a resposta.
5. Todo comando que for rodar, explique antes em uma frase simples.

## Passo 0 — Descobrir o destino

Pergunte à pessoa (ou deduza pelo contexto) qual é a pasta do projeto dela.
Confirme mostrando o caminho:

> "Vou instalar o kit na pasta `[caminho]`. É essa mesma?"

Só continue com confirmação positiva.

## Passo 1 — Inspecionar o que já existe lá

Verifique na pasta de destino:

- Existe `AGENTS.md`?
- Existe `opencode.json` (ou `opencode.jsonc`)?
- Existe `.opencode/skills/`? Quais pastas de habilidades já estão lá?

Conte o resultado à pessoa em uma frase antes de mexer em qualquer coisa.

## Passo 2 — Copiar as habilidades (pastas inteiras)

Copie CADA pasta abaixo por inteiro, preservando subpastas e licenças:

```
.opencode/skills/faf-wizard/
.opencode/skills/design-visual-facil/
.opencode/skills/ai-loop/
.opencode/skills/diagrama-do-projeto/
.opencode/skills/explica-tudo/
.opencode/skills/superpm/
.opencode/skills/anti-slop-ptbr/     <- ATENÇÃO: copiar a pasta INTEIRA
                                        (SKILL.md, LICENSE, README.md,
                                         references/ e scripts/)
```

**Se já existir pasta com o mesmo nome no destino:** compare o conteúdo.
Se for idêntica, pule. Se for diferente, pergunte: substituir, manter as
duas (renomeando a nova) ou pular esta habilidade.

## Passo 3 — Mesclar os arquivos de configuração

### AGENTS.md

- **Não existia:** copie o do kit sem alterações.
- **Já existia:** NÃO apague nada. Coloque a linha da Regra Absoluta do kit
  NA PRIMEIRA LINHA e acrescente a seção "Como falar com este usuário" logo
  abaixo, mantendo TODO o conteúdo anterior depois delas.

### opencode.json (ou .jsonc)

- **Não existia:** copie o do kit sem alterações.
- **Já existia:** leia o arquivo e mescle chave a chave, sem apagar nada:
  - `"instructions"`: garanta que `"AGENTS.md"` esteja na lista.
  - `"permission"`, `"agent"`, `"default_agent"`: se a chave não existir,
    traga a do kit; se existir com valor DIFERENTE, mostre as duas versões
    à pessoa e pergunte qual manter.
  - Preserve `$schema` e qualquer outra configuração que a pessoa já tinha
    (modelos, MCP, plugins).

## Passo 4 — Validar

Rode estas checagens (você mesmo, sem pedir nada à pessoa):

1. O `opencode.json` do destino abre como JSON válido.
2. Cada pasta em `.opencode/skills/` tem um `SKILL.md` começando com `---`
   e contendo `name:` e `description:` no cabeçalho.
3. A pasta `anti-slop-ptbr` tem scripts E references junto do SKILL.md.

Se algo falhar, conserte antes de avisar que terminou.

## Passo 5 — Relatório final

Conte à pessoa assim (adapte os nomes):

> Pronto! Instalei o Kit Skill Daora no seu projeto.
> ✅ Instalei: as 7 habilidades e as regras de português.
> 🔒 Mantive: [configurações que você já tinha].
>
> **Importante:** se o OpenCode estiver aberto agora, feche e abra de novo
> para ele ler as novidades. Depois é só me dizer o que você quer criar!

## Erros a evitar

- Sobrescrever `AGENTS.md` ou `opencode.json` existentes.
- Copiar só o `SKILL.md` da `anti-slop-ptbr` e esquecer scripts/referências.
- Terminar sem lembrar a pessoa de reiniciar o OpenCode.
- Usar jargão no relatório final ("merge", "deep-merge", "frontmatter").
