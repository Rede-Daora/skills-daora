#!/usr/bin/env python3
"""
Limpador de slop de IA para português brasileiro.

Remove automaticamente do texto os padrões de "slop de IA": padrões
genéricos e de baixa qualidade que denunciam conteúdo gerado por
inteligência artificial. Mantém a arquitetura do clean_slop.py original
em inglês, com os padrões trocados pelos equivalentes pt-BR do catálogo
do projeto.

Uso:
    python clean_slop.py <arquivo>                 # prévia (padrão)
    python clean_slop.py <arquivo> --save          # salva com backup
    python clean_slop.py <arquivo> --aggressive    # limpeza mais agressiva
    python clean_slop.py <arquivo> --output novo.txt
"""

import difflib
import re
import sys
from pathlib import Path
from typing import List


class SlopCleaner:
    def __init__(self, filepath: str, aggressive: bool = False):
        self.filepath = Path(filepath)
        self.aggressive = aggressive
        self.text = self._load_file()
        self.changes_made: List[str] = []

    def _load_file(self) -> str:
        """Carrega e retorna o conteúdo do arquivo."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def clean(self) -> str:
        """Aplica todas as operações de limpeza e retorna o texto limpo."""
        cleaned = self.text

        # Operações na ordem canônica do projeto; resíduos
        # determinísticos de chat saem primeiro por serem a limpeza
        # mais segura de todas
        cleaned = self._remove_ai_residues(cleaned)
        cleaned = self._remove_high_risk_phrases(cleaned)
        cleaned = self._simplify_wordy_phrases(cleaned)
        cleaned = self._remove_meta_commentary(cleaned)
        cleaned = self._reduce_hedging(cleaned)
        cleaned = self._clean_buzzwords(cleaned)
        cleaned = self._fix_redundant_qualifiers(cleaned)
        cleaned = self._remove_empty_intensifiers(cleaned)
        cleaned = self._fix_translationese(cleaned)
        cleaned = self._handle_em_dashes(cleaned)

        if self.aggressive:
            cleaned = self._aggressive_cleanup(cleaned)

        # Corrige o espaçamento que as remoções deixam para trás
        cleaned = self._normalize_spacing(cleaned)

        return cleaned

    def _apply(self, text, pattern, replacement, label, flags=re.IGNORECASE):
        """Aplica uma substituição e registra cada ocorrência no log.

        Se o trecho original começava com maiúscula e o substituto vem
        em minúscula, a primeira letra do substituto sobe para
        maiúscula, preservando o início da frase.
        """
        def repl_func(match):
            if callable(replacement):
                out = replacement(match)
            else:
                out = match.expand(replacement)
            if out and match.group(0)[:1].isupper() and out[:1].islower():
                out = out[0].upper() + out[1:]
            return out

        new_text, count = re.subn(pattern, repl_func, text, flags=flags)
        if count:
            self.changes_made.extend(['{}: {}'.format(label, pattern)] * count)
        return new_text

    def _remove_ai_residues(self, text: str) -> str:
        """Remove resíduos determinísticos de chat de IA.

        Primeira operação da cadeia: preâmbulos de assistente ("Claro!
        Aqui está..."), fechos ("Espero que isso ajude!") e disclaimers
        de modelo nunca pertencem ao texto final.
        """
        label = 'Resíduo de IA removido'

        # (a) Linha inteira que é só preâmbulo de chat terminado em ':'
        text = self._apply(
            text,
            r'^(?:Claro|Certamente|Com certeza|Sem problemas?|Ótimo)[!,.]? ?'
            r'(?:aqui (?:está|estão|vai)|segue[m]?)?.{0,60}:$\n?',
            '', label, flags=re.IGNORECASE | re.MULTILINE)

        # (b) Fechos de assistente
        closers = [
            r'Espero que (?:isso |este .{1,30})?(?:ajude|seja útil)[!.]?',
            r'Fico feliz em ajudar[!.]?',
            r'Se precisar de (?:mais )?(?:alguma coisa|ajuda|ajustes)'
            r'[^.!\n]{0,40}[.!]?',
        ]
        for pattern in closers:
            text = self._apply(text, pattern, '', label)

        # (c) Disclaimer de modelo de linguagem
        text = self._apply(
            text,
            r'Como (?:uma? )?(?:IA|inteligência artificial|modelo de linguagem)'
            r'(?: desenvolvid[oa] pela \w+)?, (?:eu )?não (?:posso|tenho|consigo)'
            r'[^.!\n]{0,80}[.!]',
            '', label)

        return text

    def _remove_high_risk_phrases(self, text: str) -> str:
        """Remove ou substitui as frases de alto risco do catálogo pt-BR."""
        label = 'Frase de alto risco'
        rules = [
            # "Vamos mergulhar" e família (calco de "let's dive in")
            (r'\bvamos (?:mergulhar|nos aprofundar)(?: fundo| de cabeça)?'
             r' n(o|a|os|as|esse|essa|este|esta|isso|isto)\b', r'vamos ver \1'),
            (r'\bvamos (?:mergulhar|nos aprofundar)(?: fundo| de cabeça)? em\b',
             'vamos ver'),
            (r'\bbora mergulhar(?: fundo| de cabeça)?'
             r' n(o|a|os|as|esse|essa|este|esta|isso|isto)\b', r'bora ver \1'),
            # Sentido literal (piscina, mar) fica de fora para evitar
            # falso positivo em texto sobre mergulho de verdade
            (r'\bmergulhar de cabeça n(o|a|os|as) '
             r'(?!piscina\b|mar\b|água\b|rio\b|lago\b|oceano\b)', r'começar \1 '),
            (r'\bmergulhar de cabeça em\b', 'começar'),
            # "Desvendar os mistérios/segredos"
            (r'\bdesvendar os (?:mistérios|segredos) d(o|a|os|as)\b', r'entender \1'),
            (r'\bdesvendar os (?:mistérios|segredos) de\b', 'entender'),
            (r'\bdesvende os (?:mistérios|segredos) d(o|a|os|as)\b', r'entenda \1'),
            # Aberturas panorâmicas: só em início de frase/parágrafo
            # (no meio da frase o adjunto pode ter valor real); quando
            # abre a frase, o adjunto inteiro até a vírgula é consumido
            # (cap de 60 chars) para não deixar fragmento órfão
            (r'(?m)(?:^|(?<=[.!?]\s))em um(?:a)? (?:mundo|sociedade|era'
             r'|cenário|contexto) cada vez mais [^,\n]{0,60},\s*', ''),
            (r'(?m)(?:^|(?<=[.!?]\s))no mundo (?:acelerado|dinâmico|digital'
             r'|moderno|corporativo) de hoje[^,\n]{0,60}?,\s*', ''),
            (r'(?m)(?:^|(?<=[.!?]\s))no cenário atual[^,\n]{0,60}?,\s*', ''),
            (r'(?m)(?:^|(?<=[.!?]\s))na era (?:digital|da informação|da IA'
             r'|da inteligência artificial)[^,\n]{0,60}?,\s*', ''),
            (r'(?m)(?:^|(?<=[.!?]\s))na sociedade contemporânea'
             r'[^,\n]{0,60}?,\s*', ''),
            (r'(?m)(?:^|(?<=[.!?]\s))vivemos em (?:um mundo|uma sociedade'
             r'|uma era|um tempo) (?:onde|em que)\s+', ''),
            # Saudação de e-mail gerado
            (r'\bespero que est[ae] (?:mensagem|e-?mail)'
             r' (?:o |a |te |lhe )?encontre bem[.!,]?\s*', ''),
            # "Desempenha um papel crucial" (calco de "plays a crucial role")
            (r'\bdesempenha um papel (?:crucial|fundamental|vital|essencial'
             r'|central|decisivo|importante) n(o|a|os|as)\b', r'é essencial para \1'),
            (r'\bdesempenham um papel (?:crucial|fundamental|vital|essencial'
             r'|central|decisivo|importante) n(o|a|os|as)\b', r'são essenciais para \1'),
            (r'\bdesempenha um papel (?:crucial|fundamental|vital|essencial'
             r'|central|decisivo|importante) em\b', 'é essencial para'),
            (r'\bdesempenham um papel (?:crucial|fundamental|vital|essencial'
             r'|central|decisivo|importante) em\b', 'são essenciais para'),
            (r'\bdesempenha um papel (?:crucial|fundamental|vital|essencial'
             r'|central|decisivo|importante)\b', 'é essencial'),
            (r'\bdesempenham um papel (?:crucial|fundamental|vital|essencial'
             r'|central|decisivo|importante)\b', 'são essenciais'),
            # Fecho-padrão de e-mail gerado (calco de "don't hesitate to")
            (r'\bnão hesite em\b', 'pode'),
            (r'\bnão hesitem em\b', 'podem'),
        ]
        for pattern, replacement in rules:
            text = self._apply(text, pattern, replacement, label)
        return text

    def _simplify_wordy_phrases(self, text: str) -> str:
        """Troca construções prolixas por alternativas curtas."""
        label = 'Construção prolixa'
        rules = [
            (r'\ba fim de\b', 'para'),
            (r'\bcom o (?:objetivo|intuito|propósito) de\b', 'para'),
            (r'\bcom a finalidade de\b', 'para'),
            (r'\bdevido ao fato de que\b', 'porque'),
            (r'\bpelo fato de que\b', 'porque'),
            (r'\bneste momento\b', 'agora'),
            (r'\bno momento atual\b', 'agora'),
            (r'\btem a capacidade de\b', 'pode'),
            (r'\btêm a capacidade de\b', 'podem'),
            (r'\bé capaz de\b', 'pode'),
            (r'\bsão capazes de\b', 'podem'),
            (r'\bser capaz de\b', 'poder'),
            (r'\bapesar do fato de que\b', 'embora'),
            (r'\blevar em consideração\b', 'considerar'),
            (r'\bleva em consideração\b', 'considera'),
            (r'\blevam em consideração\b', 'consideram'),
            (r'\blevando em consideração\b', 'considerando'),
            (r'\blevou em consideração\b', 'considerou'),
            # Só quando não há adjetivo depois de "decisão": a troca
            # pelo verbo deixaria o adjetivo órfão
            (r'\btomar uma decisão(?=\s*(?:[.,;:!?)]|sobre\b))', 'decidir'),
            (r'\brealizar uma análise d(o|a|os|as)\b', r'analisar \1'),
            (r'\brealizar uma análise de\b', 'analisar'),
            (r'\brealizar uma análise\b', 'analisar'),
            # "No caso de" vira "se" apenas quando introduz oração com
            # infinitivo ("no caso de o servidor falhar"); antes de
            # substantivo isolado a troca quebraria a frase
            (r'\bno caso de (?=(?:o|a|os|as|um|uma) \w+ (?:não )?\w+(?:ar|er|ir)\b)', 'se '),
            (r'\banteriormente à\b', 'antes da'),
            (r'\banteriormente ao\b', 'antes do'),
            (r'\banteriormente a\b', 'antes de'),
            (r'\bposteriormente à\b', 'depois da'),
            (r'\bposteriormente ao\b', 'depois do'),
            (r'\bposteriormente a\b', 'depois de'),
            (r'\bde forma a (\w+(?:ar|er|ir))\b', r'para \1'),
            (r'\bde modo a (\w+(?:ar|er|ir))\b', r'para \1'),
            (r'\bno sentido de (\w+(?:ar|er|ir))\b', r'para \1'),
            (r'\bpor meio da utilização d(o|a|os|as)\b', r'com \1'),
            (r'\bpor meio da utilização de\b', 'com'),
            (r'\bhodiernamente\b', 'hoje'),
            (r'\badicionalmente\b', 'além disso'),
            (r'\bpor (?:último|fim), mas não menos importante\b', 'por fim'),
            (r'\bconforme supracitado\b', 'como dito acima'),
        ]
        # Gerundismo de futuro: gerúndios irregulares primeiro
        # (pondo vira "pôr", não a preposição "por"), depois a regra
        # genérica preservando a vogal temática (ando/endo/indo viram
        # ar/er/ir); gerúndios fora desses moldes ficam intactos
        irregulares = {
            'pondo': 'pôr', 'compondo': 'compor', 'propondo': 'propor',
            'dispondo': 'dispor', 'indo': 'ir', 'vindo': 'vir',
            'trazendo': 'trazer', 'fazendo': 'fazer', 'dizendo': 'dizer',
        }
        irreg_alt = '(' + '|'.join(irregulares) + r')\b'
        for aux_pat, aux_rep in [(r'\bestarei ', 'vou '),
                                 (r'\bestaremos ', 'vamos '),
                                 (r'\bvou estar ', 'vou '),
                                 (r'\bvamos estar ', 'vamos ')]:
            rules.append((
                aux_pat + irreg_alt,
                lambda m, rep=aux_rep: rep + irregulares[m.group(1).lower()],
            ))
            rules.append((aux_pat + r'(\w+)([aei])ndo\b', aux_rep + r'\1\2r'))
        for pattern, replacement in rules:
            text = self._apply(text, pattern, replacement, label)
        return text

    def _remove_meta_commentary(self, text: str) -> str:
        """Remove meta-comentário sobre o próprio documento."""
        label = 'Meta-comentário'
        patterns = [
            # O lookahead (?=\s|$) garante que a pontuação encerra a
            # frase de verdade (um ponto decimal como "3.5" não conta)
            r'\bnest[ea] (?:artigo|post|guia|texto|documento|seção|capítulo),?'
            r' (?:vamos|iremos|você vai|nós vamos|veremos|exploraremos'
            r'|abordaremos|apresentaremos).*?[.!:](?=\s|$)\s*',
            r'\bao longo dest[ea] (?:texto|artigo|guia|post|capítulo|documento),?\s*',
            r'\bcomo vimos anteriormente,?\s*',
            r'\bcomo (?:mencionado|dito|citado) (?:anteriormente|acima),?\s*',
            r'\b(?:é|torna-se|se faz|faz-se) (?:importante|fundamental|essencial'
            r'|crucial|válido|imprescindível|necessário) (?:ressaltar|destacar'
            r'|notar|frisar|salientar|lembrar|mencionar|observar|pontuar) que\s*',
            r'\bvale (?:a pena )?(?:ressaltar|destacar|notar|mencionar|lembrar'
            r'|salientar|observar|frisar) que\s*',
            r'\b(?:cabe|cumpre|convém) (?:ressaltar|destacar|notar|mencionar'
            r'|lembrar|salientar|observar|frisar) que\s*',
            r'\btenha em mente que\s*',
            # Só a oração introdutória sai; a instrução real que vem
            # depois é preservada (e recapitalizada na normalização)
            r'(?:^|(?<=[.!?]\s))antes de (?:prosseguir|prosseguirmos'
            r'|continuar|continuarmos),?\s*',
            r'\bagora que (?:já )?(?:vimos|entendemos|conhecemos|cobrimos|exploramos) .*?,\s*',
        ]
        for pattern in patterns:
            text = self._apply(text, pattern, '', label,
                               flags=re.IGNORECASE | re.MULTILINE)
        return text

    def _reduce_hedging(self, text: str) -> str:
        """Reduz atenuação excessiva (hedging)."""
        label = 'Atenuação excessiva'
        rules = [
            (r'\bpode ou não\b', 'pode'),
            (r'\bpodem ou não\b', 'podem'),
            (r'\bpoderia potencialmente\b', 'poderia'),
            (r'\bpode potencialmente\b', 'pode'),
            (r'\bpodem potencialmente\b', 'podem'),
            # A vírgula anterior é absorvida para não sobrar vírgula
            # órfã ("os dados, de modo geral, mostram" vira "os dados
            # mostram"); [ \t] em vez de \s para não colar parágrafos.
            # O espaço restante fica por conta de _normalize_spacing.
            (r',?[ \t]*\bde certa forma,?', ''),
            (r',?[ \t]*\bem certa medida,?', ''),
            (r',?[ \t]*\baté certo ponto,?', ''),
            (r',?[ \t]*\bde (?:modo|forma|maneira) geral,?', ''),
            (r',?[ \t]*\bgeralmente falando,?', ''),
            # "Parece que", "pode-se argumentar que" e "alguns diriam
            # que" mudam o valor de verdade da frase: só saem no modo
            # agressivo (ver _aggressive_cleanup)
            # A vírgula final sinaliza uso como marcador de discurso;
            # sem ela, o advérbio modifica um adjetivo e é legítimo
            (r',?[ \t]*\baparentemente,', ''),
        ]
        for pattern, replacement in rules:
            text = self._apply(text, pattern, replacement, label)
        return text

    def _clean_buzzwords(self, text: str) -> str:
        """Substitui buzzwords corporativas por termos diretos.

        "Jornada" fica de fora de propósito: "jornada de trabalho" é
        legítimo e a troca cega quebraria o sentido (só o detector
        aponta). "Robusto" também fica de fora: é legítimo em
        engenharia, estatística e software.
        """
        label = 'Buzzword'
        rules = [
            (r'\balavancar\b', 'usar'),
            (r'\balavancando\b', 'usando'),
            # Contrações primeiro: "utilização" é feminino e "uso" é
            # masculino, então o artigo precisa acompanhar a troca
            (r'\bda utilização\b', 'do uso'),
            (r'\bna utilização\b', 'no uso'),
            (r'\bpela utilização\b', 'pelo uso'),
            (r'\bsua utilização\b', 'seu uso'),
            (r'\ba utilização\b', 'o uso'),
            # \b impede casar dentro de "reutilizar"
            (r'\butiliz(ar|a|am|amos|ando|ou|e|ei)\b', r'us\1'),
            (r'\butilizad([oa]s?)\b', r'usad\1'),
            (r'\bsinergias?\b', 'cooperação'),
            (r'\bsinérgic([oa]s?)\b', r'cooperativ\1'),
            (r'\bdisruptiv([oa]s?)\b', r'nov\1'),
            (r'\bdisrupção\b', 'ruptura'),
            (r'\bmudança de paradigmas?\b', 'grande mudança'),
            (r'\bquebra de paradigmas?\b', 'grande mudança'),
            # "De ponta" exige concordância com o substantivo anterior;
            # só os pares mais comuns entram, o resto fica para o detector
            (r'\btecnologia(s?) de ponta\b', r'tecnologia\1 avançada\1'),
            (r'\bsolução de ponta\b', 'solução avançada'),
            (r'\bsoluções de ponta\b', 'soluções avançadas'),
            (r'\brecurso(s?) de ponta\b', r'recurso\1 avançado\1'),
            (r'\bequipamento(s?) de ponta\b', r'equipamento\1 avançado\1'),
            (r'\bdivisor de águas\b', 'marco'),
            (r'\bvirada de (?:chave|jogo)\b', 'grande mudança'),
            (r'\bgame[- ]?changer\b', 'marco'),
            (r'\bpotencializ(ar|a|am|ando|ou)\b', r'aument\1'),
            (r'\bimpulsion(ar|a|am|ando|ou)\b', r'aument\1'),
            # Contrações antes do fallback: "dar autonomia a" + artigo
            # precisa virar crase/combinação (aos, às, ao, à)
            (r'\bempoderar os\b', 'dar autonomia aos'),
            (r'\bempoderar as\b', 'dar autonomia às'),
            (r'\bempoderar o\b', 'dar autonomia ao'),
            (r'\bempoderar a\b', 'dar autonomia à'),
            (r'\bempoderar\b', 'dar autonomia a'),
            # "Mindset" é masculino e "mentalidade" é feminino: os
            # determinantes mais comuns entram no padrão
            (r'\bo mindset\b', 'a mentalidade'),
            (r'\bum mindset\b', 'uma mentalidade'),
            (r'\bdo mindset\b', 'da mentalidade'),
            (r'\bno mindset\b', 'na mentalidade'),
            (r'\bseu mindset\b', 'sua mentalidade'),
            (r'\besse mindset\b', 'essa mentalidade'),
            (r'\beste mindset\b', 'esta mentalidade'),
            # Fallback masculino invariável: cobre casos com modificador
            # no meio ("um novo mindset") sem quebrar a concordância
            (r'\bmindset\b', 'modo de pensar'),
        ]
        for pattern, replacement in rules:
            text = self._apply(text, pattern, replacement, label)
        return text

    def _fix_redundant_qualifiers(self, text: str) -> str:
        """Corrige redundâncias (pleonasmos)."""
        label = 'Redundância'
        rules = [
            (r'\bcerteza absoluta\b', 'certeza'),
            (r'\bconsenso geral\b', 'consenso'),
            (r'\bplanos futuros\b', 'planos'),
            (r'\bresultado final\b', 'resultado'),
            (r'\bconclusão final\b', 'conclusão'),
            (r'\belo de ligação\b', 'elo'),
            (r'\btotalmente únic([oa]s?)\b', r'únic\1'),
            (r'\bcompletamente únic([oa]s?)\b', r'únic\1'),
            (r'\bcriar um novo\b', 'criar um'),
            (r'\bcriar uma nova\b', 'criar uma'),
            (r'\bcriar nov(?:o|a|os|as) ', 'criar '),
            (r'\bhá ((?:\w+ ){0,3}(?:anos?|m[eê]s|meses|dias?|semanas?'
             r'|décadas?|séculos?|tempo)) atrás\b', r'há \1'),
        ]
        for pattern, replacement in rules:
            text = self._apply(text, pattern, replacement, label)
        return text

    def _remove_empty_intensifiers(self, text: str) -> str:
        """Remove intensificadores vazios diante de adjetivos comuns."""
        label = 'Intensificador vazio'
        rules = [
            (r'\b(?:extremamente|incrivelmente|absolutamente) '
             r'(importantes?|essencia(?:l|is)|fundamenta(?:l|is)'
             r'|necessári[oa]s?|crucia(?:l|is)|únic[oa]s?'
             r'|difíc(?:il|eis)|fác(?:il|eis)|simples|grandes?'
             r'|eficaz(?:es)?|eficientes?|valios[oa]s?|poderos[oa]s?'
             r'|rápid[oa]s?|complex[oa]s?)\b', r'\1'),
            (r'\bmuito únic([oa]s?)\b', r'únic\1'),
            (r'\bmuito important(es?)\b', r'important\1'),
            (r'\brealmente important(es?)\b', r'important\1'),
        ]
        for pattern, replacement in rules:
            text = self._apply(text, pattern, replacement, label)
        return text

    def _fix_translationese(self, text: str) -> str:
        """Corrige calcos de tradução do inglês com substituição segura."""
        label = 'Calco de tradução'
        rules = [
            (r'\b(?:rica )?tapeçaria de\b', 'mistura de'),
            (r'\bé um (?:testemunho|testamento) de que\b', 'mostra que'),
            (r'\bé um (?:testemunho|testamento) d(o|a|os|as)\b', r'mostra \1'),
            (r'\bé um (?:testemunho|testamento) de\b', 'mostra'),
            # "No reino de" / "no coração de" migraram para o modo
            # agressivo (_aggressive_cleanup): o uso literal é comum
            # demais para reescrita automática no modo normal
            (r'\buma (?:ampla |vasta )?gama de\b', 'uma variedade de'),
            (r'\bum (?:vasto |amplo )?leque(?: diversificado)? de\b',
             'uma variedade de'),
            (r'\buma miríade de\b', 'uma infinidade de'),
            (r'\b(cenário|panorama|paisagem|mercado|mundo)( \w+)?'
             r' em constante (?:evolução|mudança|transformação)\b',
             r'\1\2 em mudança'),
            (r'\b(?:elevar|levar) (?:ao|para o|a um) (?:próximo|outro|novo)'
             r' (?:nível|patamar)\b', 'melhorar'),
            (r'\b(?:desbloquear|destravar) (?:todo )?o potencial\b',
             'aproveitar o potencial'),
            (r'\b(?:desbloquear|destravar) (?:todo o )?seu potencial\b',
             'aproveitar seu potencial'),
            (r'\b(?:desbloqueie|destrave) (?:todo )?o potencial\b',
             'aproveite o potencial'),
            (r'\b(?:desbloqueie|destrave) (?:todo o )?seu potencial\b',
             'aproveite seu potencial'),
            (r'\baproveitar (?:todo )?o poder d(o|a|os|as)\b', r'usar \1'),
            (r'\baproveitar (?:todo )?o poder de\b', 'usar'),
            (r'\bquando se trata de\b', 'quando o assunto é'),
            # Vírgula anterior absorvida para não deixar vírgula órfã
            (r',?[ \t]*\bdito isso,?', ''),
            (r'\bno que (?:diz respeito|tange|concerne) à\b', 'sobre a'),
            (r'\bno que (?:diz respeito|tange|concerne) ao\b', 'sobre o'),
            (r'\bno que (?:diz respeito|tange|concerne) às\b', 'sobre as'),
            (r'\bno que (?:diz respeito|tange|concerne) aos\b', 'sobre os'),
            (r'\bno que (?:diz respeito|tange|concerne) a\b', 'sobre'),
            (r'\bno tocante à\b', 'sobre a'),
            (r'\bno tocante ao\b', 'sobre o'),
            (r'\bno tocante a\b', 'sobre'),
            (r'\bnavegar pel(as|os) (complexidades|dificuldades'
             r'|incertezas|desafios)\b', r'lidar com \1 \2'),
            (r'\babraçar (a|as) (mudanças?|transformação|tecnologia'
             r'|inovação|IA)\b', r'adotar \1 \2'),
            (r'\bserve como um lembrete de que\b', 'lembra que'),
            (r'\bdestaca-se como\b', 'é'),
            (r'\b(integração|experiência) sem costura\b', r'\1 sem atrito'),
            (r'\bseamless\b', 'sem atrito'),
            (r'\bde forma fluida e sem esforço\b', 'com fluidez'),
        ]
        for pattern, replacement in rules:
            text = self._apply(text, pattern, replacement, label)
        return text

    def _handle_em_dashes(self, text: str) -> str:
        """Trata o travessão (U+2014) e a meia-risca (U+2013).

        Regra do projeto: no modo normal, o par de travessões que
        delimita um aparte vira parênteses (transformação segura). O
        travessão solitário no meio da frase só vira vírgula no modo
        agressivo. Linhas de diálogo em pt-BR (lstrip() começando com
        travessão ou meia-risca, mesma regra do detector) são puladas
        por inteiro: os travessões de atribuição no meio delas também
        são diálogo. Traço entre dígitos (intervalos como 1990-2000)
        nunca é alterado, e o miolo do par exclui .!? para o aparte
        não atravessar fronteira de frase.
        """
        def to_parens(match):
            return ' ({}) '.format(match.group(1).strip())

        # Par com espaços: "x — aparte — y" vira "x (aparte) y"
        pair_spaced = r'(?<=\S)(?<![0-9]) [—–] ([^—–\n.!?]{2,80}?) [—–] (?=\S)'

        # Par colado entre letras: "x—aparte—y" (só U+2014; a meia-risca
        # colada costuma ser intervalo numérico ou composto)
        pair_tight = r'(?<=[^\W\d_])—([^—\n.!?]{2,80}?)—(?=[^\W\d_])'

        solitary = r'(?<=\S)(?<![0-9]) [—–] (?![0-9])(?=\S)'

        out_lines = []
        for line in text.split('\n'):
            # Indentação e marcadores de blockquote não contam como início
            # da linha: "> — Fonte" é atribuição de citação e não deve ser tocada.
            sem_quote = re.sub(r'^(?:\s*>)*\s*', '', line)
            if sem_quote.startswith(('—', '–')):
                out_lines.append(line)
                continue
            line = self._apply(line, pair_spaced, to_parens,
                               'Travessão em par', flags=0)
            line = self._apply(line, pair_tight, to_parens,
                               'Travessão em par', flags=0)
            if self.aggressive:
                line = self._apply(line, solitary, ', ',
                                   'Travessão solitário', flags=0)
            out_lines.append(line)

        return '\n'.join(out_lines)

    def _aggressive_cleanup(self, text: str) -> str:
        """Limpeza mais agressiva; pode alterar levemente o sentido."""
        label = 'Limpeza agressiva'
        paragraph_starts = [
            r'^Além disso,\s+',
            r'^Ademais,\s+',
            r'^Outrossim,\s+',
            r'^Nesse sentido,\s+',
            r'^Nesse contexto,\s+',
            r'^Dessa forma,\s+',
            r'^Diante disso,\s+',
            r'^Em suma,\s+',
            r'^Em resumo,\s+',
            r'^Por fim,\s+',
            r'^Vale ressaltar que\s+',
            r'^É importante destacar que\s+',
        ]
        for pattern in paragraph_starts:
            text = self._apply(text, pattern, '', label,
                               flags=re.IGNORECASE | re.MULTILINE)

        text = self._apply(
            text,
            r'\bé (?:importante|crucial|fundamental) (?:notar que|que)\s+',
            '', label)

        # Hedges que mudam o valor de verdade da frase ("parece que o
        # sistema falhou" não afirma a falha): só no modo agressivo
        for pattern in [r'\bpode-se argumentar que\s*',
                        r'\balguns diriam que\s*',
                        r'\bparece que\s+']:
            text = self._apply(text, pattern, '', label)

        # Calcos "no reino de" / "no coração de": o uso literal é comum
        # demais para o modo normal; exceções alinhadas com o detector.
        # Para "coração", referente humano ou nome próprio (maiúscula,
        # caso-sensível via (?-i:...)) indica sentido literal.
        text = self._apply(
            text,
            r'\bno reino d(o|a|os|as|e) (?!Deus\b|Portugal\b|Espanha\b)',
            r'no campo d\1 ', label)
        text = self._apply(
            text,
            r'\bno coração d(o|a|os|as|e) (?!paciente\b|soldado\b|homem\b'
            r'|mulher\b|criança\b|bebê\b|atleta\b|d[eo]la?\b|(?-i:[A-ZÀ-Ú]))',
            r'no centro d\1 ', label)

        return text

    def _normalize_spacing(self, text: str) -> str:
        """Corrige o espaçamento afetado pelas remoções."""
        # Espaços múltiplos
        text = re.sub(r' {2,}', ' ', text)

        # Espaço antes de pontuação
        text = re.sub(r' +([.,;:!?])', r'\1', text)

        # Vírgulas duplicadas
        text = re.sub(r',(\s*,)+', ',', text)

        # Vírgula colada em pontuação final
        text = re.sub(r',+([.!?])', r'\1', text)

        # Vírgula órfã logo depois do fim de uma frase
        text = re.sub(r'([.!?])\s+,\s*', r'\1 ', text)

        # Vírgula órfã no início da linha
        text = re.sub(r'(?m)^,[ \t]*', '', text)

        # Linhas em branco múltiplas
        text = re.sub(r'\n{3,}', '\n\n', text)

        # Recapitaliza depois de ponto que encerra frase de verdade.
        # Heurística: o ponto de abreviação comum (etc., ex., Sr., Dr.)
        # e o de sigla pontuada (letra maiúscula isolada, como em
        # "S.A.") não encerram frase, então não disparam a
        # recapitalização. Limites conhecidos: abreviações fora da
        # lista ainda recapitalizam a palavra seguinte, e uma frase
        # legítima que termina em sigla pontuada deixa de recapitalizar
        # a seguinte (nos dois casos o texto original é preservado).
        # Lookbehind de re exige tamanho fixo, por isso a inspeção do
        # trecho anterior é feita por função de substituição.
        abreviacoes = {'etc', 'ex', 'p', 'sr', 'sra', 'dr', 'dra',
                       'prof', 'profa', 'art', 'pág', 'tel', 'obs'}

        def recapitaliza(m):
            if m.group(1) == '.':
                anterior = m.string[:m.start()]
                # Reticências ("..." ou "…") marcam omissão dentro de uma
                # citação, não fim de frase; a palavra seguinte fica como está.
                if anterior.endswith('..') or anterior.endswith('…'):
                    return m.group(0)
                token = re.search(r'([^\W\d_]+)$', anterior)
                if token:
                    palavra = token.group(1)
                    if palavra.lower() in abreviacoes:
                        return m.group(0)
                    if len(palavra) == 1 and palavra.isupper():
                        return m.group(0)
            return m.group(1) + m.group(2) + m.group(3).upper()

        text = re.sub(r'([.!?])(\s+)([a-zàáâãçéêíóôõúü])', recapitaliza, text)

        # Recapitaliza início de parágrafo
        text = re.sub(
            r'(\n[ \t]*\n[ \t]*)([a-zàáâãçéêíóôõúü])',
            lambda m: m.group(1) + m.group(2).upper(),
            text,
        )

        text = text.strip()

        # Recapitaliza o primeiro caractere do texto
        if text and text[:1].islower():
            text = text[0].upper() + text[1:]

        return text

    def save(self, output_path: str = None):
        """Salva o texto limpo em arquivo."""
        cleaned = self.clean()

        if output_path is None:
            # Cria backup e sobrescreve o original
            backup_path = self.filepath.with_suffix(self.filepath.suffix + '.backup')
            self.filepath.rename(backup_path)
            output_path = self.filepath
            print(f"✅ Backup criado: {backup_path}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned)

        print(f"✅ Texto limpo salvo em: {output_path}")
        print(f"\n📊 Mudanças aplicadas: {len(self.changes_made)}")

        if self.changes_made:
            print("\nResumo das mudanças:")
            # Agrupa mudanças parecidas
            change_counts = {}
            for change in self.changes_made:
                category = change.split(':')[0]
                change_counts[category] = change_counts.get(category, 0) + 1

            for category, count in change_counts.items():
                print(f"  • {category}: {count} ocorrência(s)")

    def preview(self, context_lines: int = 2):
        """Mostra as mudanças sem salvar."""
        cleaned = self.clean()

        # A comparação com strip() evita falso alarme quando a única
        # diferença é o espaço em branco nas pontas do arquivo
        if cleaned == self.text or cleaned == self.text.strip():
            print("✅ Nenhuma mudança necessária: o texto já está limpo!")
            return

        print(f"\n{'=' * 70}")
        print(f"Prévia das mudanças para: {self.filepath.name}")
        print(f"{'=' * 70}\n")

        # Prévia com difflib: mantém o alinhamento mesmo quando a
        # limpeza remove ou adiciona linhas (zip desalinharia)
        diff_lines = list(difflib.unified_diff(
            self.text.split('\n'), cleaned.split('\n'),
            fromfile='original', tofile='limpo',
            lineterm='', n=context_lines))

        max_hunks_to_show = 10
        total_hunks = sum(1 for line in diff_lines if line.startswith('@@'))
        hunks_shown = 0

        for line in diff_lines:
            if line.startswith('@@'):
                if hunks_shown == max_hunks_to_show:
                    break
                hunks_shown += 1
            print(line[:100])

        if total_hunks > max_hunks_to_show:
            print(f"\n... e mais {total_hunks - max_hunks_to_show} trecho(s)"
                  f" (mostrando os {max_hunks_to_show} primeiros"
                  f" de {total_hunks})")

        print(f"\n📊 Total de mudanças: {len(self.changes_made)}")
        print("\nExecute com --save para aplicar as mudanças")


def main():
    if len(sys.argv) < 2:
        print("Uso: python clean_slop.py <arquivo> [opções]")
        print("\nOpções:")
        print("  --save            Salva as mudanças (cria backup)")
        print("  --output ARQUIVO  Salva em outro arquivo")
        print("  --aggressive      Limpeza mais agressiva")
        print("  --preview         Mostra as mudanças sem salvar (padrão)")
        sys.exit(1)

    filepath = sys.argv[1]

    if not Path(filepath).exists():
        print(f"Erro: arquivo '{filepath}' não encontrado")
        sys.exit(1)

    aggressive = '--aggressive' in sys.argv
    save_mode = '--save' in sys.argv
    output_file = None

    if '--output' in sys.argv:
        output_idx = sys.argv.index('--output')
        if (output_idx + 1 >= len(sys.argv)
                or sys.argv[output_idx + 1].startswith('--')):
            print("Erro: --output exige um nome de arquivo")
            sys.exit(1)
        output_file = sys.argv[output_idx + 1]
        save_mode = True

    cleaner = SlopCleaner(filepath, aggressive=aggressive)

    if save_mode:
        cleaner.save(output_file)
    else:
        cleaner.preview()


if __name__ == '__main__':
    main()
