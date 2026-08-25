# Kit para Iniciantes no OpenCode — Skill Daora

Arquivos prontos que ensinam o OpenCode a conversar com você como um professor paciente: tudo em português simples, uma coisa por vez, sem palavras difíceis.

## Para agentes de IA

Se você é um agente (OpenCode, Claude Code ou similar) instalando este kit no projeto de alguém: **siga o protocolo em [INSTALAR.md](INSTALAR.md)**. Fale com a pessoa em português do Brasil simples, uma coisa por vez, e nunca sobrescreva os arquivos dela sem perguntar.

## Para quem é este kit

Para qualquer pessoa que quer criar um site ou aplicativo.Você descreve o que quer — e o OpenCode constrói, explica cada passo e pede a sua aprovação antes de fazer qualquer coisa importante.

## O que vem no kit

Quatro tipos de arquivo, que você vai copiar para dentro da pasta do **seu** projeto:

| Arquivo | O que faz |
|---|---|
| `AGENTS.md` | Regras de bom comportamento: português do Brasil sempre, linguagem simples, uma coisa por vez. |
| `opencode.json` | Configuração de segurança: nada roda sem você permitir; comandos perigosos ficam bloqueados para sempre. |
| `.opencode/skills/` | As 7 habilidades que o OpenCode aprende (veja a tabela abaixo). |
| `.vscode/extensions.json` | 8 extensões do VS Code recomendadas: tradução, formatação, servidor local e mais (veja abaixo). |

### As 7 habilidades

| Habilidade | Quando ela entra em ação |
|---|---|
| `faf-wizard` | Você ainda não sabe explicar o que quer? Ela entrevista você, uma pergunta por vez, até entender sua ideia. |
| `design-visual-facil` | Hora de deixar bonito. Ela decide cores, fontes e organização sozinha — você só diz o que quer ver. |
| `ai-loop` | Modo caprichoso: anota os combinados, constrói, confere item por item antes de dizer "pronto". |
| `diagrama-do-projeto` | Desenha mapas simples ("caixinhas e setas") para mostrar como seu projeto funciona. |
| `explica-tudo` | Apareceu um erro estranho ou arquivo desconhecido? Traduz tudo para português de gente. |
| `superpm` | O gerente do projeto: mantém o painel do que já ficou pronto e do que falta, e avisa antes de problemas. |
| `anti-slop-ptbr` | Caça textos com "cara de robô" (frases batidas, enrolação) e limpa para ficar com a sua voz. |

### Extensões do VS Code (opcional)

Quando você abrir o projeto no VS Code, ele pergunta se quer instalar extensões recomendadas. São 8 extensões que facilitam a vida:

| Extensão | O que faz |
|---|---|
| **Portuguese Language Pack** | Traduz o VS Code inteiro para português |
| **Prettier** | Formata o código automaticamente (deixa tudo alinhado) |
| **Live Server** | Cria um servidor local para ver seu site atualizando em tempo real |
| **Auto Rename Tag** | Renomeia tags HTML junto (muda `<div>` e o `</div>` muda junto) |
| **Path Intellisense** | Autocompleta caminhos de arquivo (ajuda a não errar nome de pasta) |
| **Error Lens** | Mostra erros direto no código (não precisa ficar procurando) |
| **Color Highlight** | Mostra cores no código (vê que cor é `#ff5733` sem abrir nada) |
| **Git Autoconfig** | Configura nome e email do Git automaticamente em cada projeto |

## Jeito mais fácil: use este modelo

Na página deste repositório no GitHub existe o botão verde **"Use this template"** (Usar este modelo). Apertando ele, o GitHub cria uma cópia completa do kit na SUA conta, num repositório novo só seu. Depois:

1. Traga essa cópia para o computador: botão **Code** → **Download ZIP** (e descompacte), ou `git clone` do SEU repositório novo;
2. Abra o OpenCode dentro dessa pasta;
3. Pronto: tudo já vem instalado — pode conversar e criar!

Se preferir o caminho manual (colocar os arquivos dentro de um projeto que você já tem), siga os passos abaixo.

## Instalação em 4 passos

1. **Baixe o kit.** Na página deste repositório no GitHub, aperte o botão verde **Code** e escolha **Download ZIP**. Depois descompacte o arquivo baixado.
   *(Se preferir usar o terminal: `git clone https://github.com/SEU-USUARIO/skills-daora.git`)*

2. **Copie 4 coisas para a pasta do SEU projeto:** o arquivo `AGENTS.md`, o arquivo `opencode.json`, a pasta inteira `.opencode/` e a pasta `.vscode/`. Cole na raiz do seu projeto (a mesma pasta onde você abre o OpenCode).

3. **Abra o OpenCode** dentro da pasta do seu projeto.

4. **Se o OpenCode já estava aberto, feche e abra de novo.** A configuração só é lida quando ele inicia.

Pronto. Nada mais precisa ser instalado.

## Como começar

Basta conversar naturalmente. Exemplo de primeira mensagem:

> Quero criar um site para minha loja de bolos

A habilidade `faf-wizard` assume a conversa e começa a fazer perguntinhas, uma por vez. Responda com suas próprias palavras — não existe resposta errada.

## Sobre a segurança

Este kit vem configurado no modo mais cauteloso:

- **Nada acontece sem você apertar "permitir".** Criar arquivo, rodar comando, abrir site externo: o OpenCode sempre pergunta antes.
- **Comandos perigosos são bloqueados de verdade**, como apagar pastas (`rm -rf`) e enviar código para a internet sem você mandar.
- Se algum dia quiser menos perguntas, dá para relaxar as regras no `opencode.json`. Enquanto estiver começando, recomendamos manter assim.

## Dica de ouro

Se alguma resposta vier cheia de termos técnicos, diga apenas:

> Explique como se eu fosse leigo.

A regra está escrita nos arquivos do kit, mas reforçar ajuda.

## Créditos e fontes

Este kit adapta habilidades de projetos abertos da comunidade:

- [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) — fontes originais de `faf-wizard` e `anti-slop` / base para `ai-loop`
- Anthropic ([anthropics/skills](https://github.com/anthropics/skills), distribuído via claude-code) — fonte oficial do `frontend-design`, adaptado aqui como `design-visual-facil`
- Padrões C4/Mermaid da comunidade — base do `diagrama-do-projeto`
- [anti-slop-ptbr](https://mcpmarket.com) — incluída neste kit com sua licença original

Todas foram reescritas em linguagem simples para iniciantes.

## Licença

[MIT](LICENSE). As habilidades de terceiros mantêm suas licenças originais nas respectivas pastas.
