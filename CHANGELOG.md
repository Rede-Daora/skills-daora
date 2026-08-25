# Histórico de mudanças

Todas as mudanças importantes do Kit Skill Daora ficam anotadas aqui.

O formato é baseado em [Mantenha um Changelog](https://keepachangelog.com/pt-BR/1.1.0/)
e as versões seguem o [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Não lançado]

## [1.2.0] - 2026-08-25

### Adicionado

- `.vscode/extensions.json`: 8 extensões do VS Code recomendadas para
  iniciantes (tradução pt-BR, Prettier, Live Server, Auto Rename Tag,
  Path Intellisense, Error Lens, Color Highlight e Git Autoconfig).
- README atualizado com nova seção "Extensões do VS Code (opcional)"
  e contagem de arquivos ajustada.

## [1.1.0] - 2026-08-24

### Adicionado

- Repositório marcado como modelo: o botão "Use this template" do GitHub cria
  uma cópia completa do kit na conta de quem clicar.
- README ganhou seção explicando o caminho pelo botão "Use this template".
- `INSTALAR.md` ganhou nota para projetos já criados pelo modelo.
- Comandos prontos para o OpenCode: `/comecar` (entrevista guiada) e
  `/progresso` (painel do projeto).
- Verificação automática de qualidade (`.github/workflows/validar.yml`),
  que confere configuração, habilidades e comandos a cada mudança.
- Formulários guiados de issue em pt-BR: "Reportar um problema" e
  "Sugerir uma habilidade nova".
- `CONTRIBUTING.md`: guia curto de contribuição.

## [1.0.0] - 2026-08-25

### Adicionado

- `AGENTS.md`: regras absolutas de comunicação em português do Brasil simples.
- `opencode.json`: segurança no modo cauteloso (nada roda sem aprovação,
  comandos perigosos bloqueados) com reforço de pt-BR nos agentes `build` e `plan`.
- Habilidades: `faf-wizard`, `design-visual-facil`, `ai-loop`,
  `diagrama-do-projeto`, `explica-tudo`, `superpm` e `anti-slop-ptbr`.
- `INSTALAR.md`: protocolo para agentes de IA instalarem o kit via chat.
- README com instalação manual em 4 passos.
