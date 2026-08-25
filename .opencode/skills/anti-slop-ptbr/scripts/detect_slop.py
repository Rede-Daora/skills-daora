#!/usr/bin/env python3
"""Detector de slop de IA para português brasileiro.

Analisa arquivos de texto em busca de "slop de IA": padrões genéricos e de
baixa qualidade que denunciam conteúdo gerado por inteligência artificial.
Gera uma pontuação de slop (0-100) e imprime um relatório por categoria.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List
from collections import defaultdict


# Frases de alto risco: fórmulas quase determinísticas de texto gerado.
# "mergulhar" literal (esporte, piscina) não é distinguível por regex;
# por isso só entram as formas compostas do calco de "let's dive in".
HIGH_RISK_PHRASES = [
    r"vamos (?:mergulhar|nos aprofundar)(?: fundo| de cabeça)?",
    r"mergulhar de cabeça",
    r"mergulh(?:ar|e|amos|ando) (?:ness[ea]|nest[ea]|no|na) (?:tema|assunto|universo|tópico|conceito|ciência)",
    r"desvend(?:ar|e|amos|ando) (?:os |as )?(?:mistérios|segredos)",
    r"pront[oa]s? para desvendar",
    r"em um[a]? (?:mundo|sociedade|era|cenário|contexto) cada vez mais",
    r"no (?:cenário|contexto) atual",
    r"no atual cenário",
    r"na era (?:digital|da informação|da IA|da inteligência artificial|da tecnologia)",
    r"vivemos em (?:um mundo|uma sociedade|uma era|um tempo) (?:onde|em que)",
    r"no mundo (?:acelerado|dinâmico|digital|moderno|corporativo) de hoje",
    r"na sociedade contemporânea",
    r"na contemporaneidade",
    r"espero que est[ae] (?:mensagem|e-?mail) (?:o|a|te|lhe|os|as) encontre bem",
    r"você já parou para pensar",
    r"e se eu (?:te|lhe) dissesse que",
    r"(?:aqui está|aqui estão|eis) (?:o que|como|por que|uma análise)",
    r"desempenham? um papel (?:crucial|fundamental|vital|essencial|central|decisivo)",
    r"insights valiosos",
    r"não hesite em",
    r"(?:tenho|é com) (?:o |grande |imenso )?(?:prazer|orgulho|honra|alegria|satisfação) (?:de|em|que) (?:anunciar|compartilhar)",
    r"(?:a chave|o segredo) (?:é|está em|para)",
]

# Muletas de transição: português legítimo em dose única; o sinal é a
# densidade (um conectivo por parágrafo é assinatura de texto gerado).
MEDIUM_RISK_PHRASES = [
    r"\balém disso\b",
    r"\bademais\b",
    r"\boutrossim\b",
    r"\bdestarte\b",
    r"\bdessarte\b",
    r"\badicionalmente\b",
    r"\bnesse sentido\b",
    r"\bnessa perspectiva\b",
    r"\bdessa forma\b",
    r"\bdesse modo\b",
    r"\bdiante disso\b",
    r"\bem suma\b",
    r"\bem síntese\b",
    r"\bem resumo\b",
    r"\bem conclusão\b",
    r"\bem última (?:análise|instância)\b",
    r"\bvale (?:ressaltar|destacar|lembrar|mencionar|salientar|frisar)\b",
    r"\bcabe (?:ressaltar|destacar|salientar|mencionar|frisar)\b",
    r"\bpor fim\b",
    r"\bprimeiramente\b",
    r"\bé (?:fundamental|crucial)\b",
    r"\bno que (?:tange|concerne) a\b",
    r"\bno tocante a\b",
]

# Buzzwords e jargões corporativos. Exceções documentadas em comentário;
# "alavancagem" (finanças) fica de fora de propósito.
BUZZWORDS = [
    # sem a forma "alavanca" isolada, que casaria o substantivo literal
    # (a peça mecânica); a 3ª pessoa entra só com objeto típico
    r"\balavanc(?:ar|am|ando|ou|aram|amos)\b|\balavanca (?:o|a|os|as|resultados|vendas|crescimento|negócios)\b",
    r"\bsinergias?\b",
    r"\bsinérgic[oa]s?\b",
    r"\bdisruptiv[oa]s?\b",
    r"\bdisrupção\b",
    # "inovador" só em colocações buzz, para não punir "estudo inovador"
    r"\b(?:soluç(?:ão|ões)|abordagens?|propostas?|plataformas?|metodologias?|estratégias?) inovador(?:a|as|es)?\b",
    # "robusto" é legítimo em engenharia, estatística e software
    r"\brobust[oa]s?\b",
    r"\bescaláve(?:l|is)\b",
    r"\bimpulsion(?:ar|a|am|ando|ou|aram)\b",
    r"\bpotencializ\w+",
    r"\bempoder\w+",
    # "otimizar" é legítimo em contexto técnico (SEO, performance)
    r"\botimiz(?:ar|a|am|ando|ou|aram|ad[oa]s?)\b",
    r"(?:agregar|agrega[mr]?|agregando|gerar|entregar) valor\b",
    r"\bvalor agregado\b",
    r"(?:mudança|quebra) de paradigmas?",
    r"(?:abordagem|visão|olhar) holístic[oa]",
    r"\bdivisor de águas\b",
    r"(?:tecnologias?|soluç(?:ão|ões)|ferramentas?|equipamentos?|recursos) de ponta",
    r"\brevolucionári[oa]s?\b",
    # "transformador" também nomeia o equipamento elétrico; risco aceito
    r"\btransformador(?:a|es|as)?\b",
    # ambos os gêneros só em colocações típicas, para não punir
    # "a dinâmica do grupo" nem "sistema dinâmico não linear"
    r"\b(?:ambientes?|mercados?|cenários?) dinâmicos?\b",
    r"\b(?:equipe|cultura|ambiente|mercado|abordagem|experiência) dinâmicas?\b",
    r"\bvibrantes?\b",
    r"\bmindset\b",
    # "jornada" solta é português legítimo (sentido de expediente ou
    # percurso); o sinal de slop fica nas formas compostas em TRANSLATIONESE
    r"\bseamless\b",
    r"\bsem costura\b",
    r"game[- ]?changer",
    r"virada de (?:chave|jogo)",
]

# Meta-comentário: o texto falando sobre o próprio texto.
META_COMMENTARY = [
    r"nest[ea] (?:artigo|post|texto|guia|seção|documento|capítulo),? (?:vamos|iremos|você vai|veremos|abordaremos|exploraremos|apresentaremos)",
    r"ao longo (?:deste|desse|do) (?:texto|artigo|guia|post|capítulo)",
    r"como vimos (?:anteriormente|acima|no início)",
    r"é importante (?:ressaltar|destacar|notar|frisar|salientar|mencionar|lembrar|observar|pontuar) que",
    r"vale a pena (?:notar|mencionar|lembrar|destacar|ressaltar)",
    r"antes de (?:prosseguir|prosseguirmos|continuar|continuarmos|avançar|avançarmos)",
    r"agora que (?:já )?(?:vimos|entendemos|sabemos|conhecemos|cobrimos)",
    r"a seguir,? (?:apresentaremos|veremos|vamos)",
    r"tenha em mente que",
]

# Atenuação excessiva: evasão de compromisso com a afirmação.
HEDGE_WORDS = [
    r"pode(?:m)? ou não",
    r"poderia(?:m)? potencialmente",
    r"de certa (?:forma|maneira)",
    r"em certa medida",
    r"até certo ponto",
    r"de (?:modo|forma|maneira) geral",
    r"geralmente falando",
    r"pode-se (?:argumentar|dizer) que",
    r"alguns (?:diriam|poderiam dizer|argumentam) que",
    # só como marcador de discurso: "parece que" abrindo frase no meio do
    # parágrafo (após pontuação final; lookbehind de tamanho fixo), para
    # não punir o uso corriqueiro fora dessa posição
    r"(?<=[.!?]\s)parece que\b",
    # "aparentemente" só seguido de vírgula (marcador de discurso);
    # solto, modificando adjetivo, é português corriqueiro
    r"\baparentemente,",
    r"você pode considerar",
    r"uma possibilidade é",
]

# Calcos de tradução: expressões que só existem em pt-BR como decalque
# direto do inglês de LLM.
TRANSLATIONESE = [
    # "rich tapestry"; o figurado praticamente não existe em pt-BR
    r"(?:rica )?tapeçaria de",
    # "is a testament to"; "testamento" é erro objetivo de tradução
    r"é um (?:testemunho|testamento) d[eoa]",
    # "in the realm of"; exclui os sentidos literais mais comuns
    # (lista de exceções idêntica à do clean_slop.py)
    r"no reino d(?:e|a|o) (?!Deus\b|Portugal\b|Espanha\b)",
    # "at the heart of" figurado (texto turístico-promocional gerado)
    r"no coração d[eoa]",
    r"uma (?:ampla |vasta )?gama de",
    r"um (?:vasto |amplo )?leque(?: diversificado)? de",
    r"(?:cenário|panorama|paisagem)(?: \w+)? em constante (?:evolução|mudança|transformação)",
    r"\b(?:lev(?:e|ar)|elev(?:e|ar))\b.{0,30}(?:próximo|novo|outro) (?:nível|patamar)",
    r"(?:desbloque|destrav)\w+ (?:todo )?(?:o |seu |sua )?potencial",
    r"quando se trata de",
    r"\bdito isso\b",
    r"no que diz respeito a",
    r"naveg\w+ (?:por |pel[oa]s? )?(?:as |os )?(?:complexidades|desafios|incertezas)",
    r"aproveit\w+ (?:todo )?o poder d[eoa]",
    r"embarc\w+ (?:em|ness[ae]|nest[ae])(?: uma)? jornada",
    r"jornada de (?:transformação|descoberta|aprendizado)",
    r"resso(?:ar|a|am) com (?:o público|a audiência|as pessoas)",
    r"aninhad[oa] (?:em|no|na)",
    r"integra(?:-se)? perfeitamente",
]

# Clichês de redação escolar (dialeto ENEM) que os LLMs reproduzem em massa,
# inclusive fora do contexto de vestibular.
CLICHE_REDACAO = [
    r"desde os primórdios(?: da humanidade)?",
    r"desde os tempos mais remotos",
    r"desde tempos imemoriais",
    r"\bhodiern(?:amente|[oa]s?)\b",
    r"é notório que",
    r"diante (?:desse|deste|de tal) cenário",
    r"diante do exposto",
    r"perante o exposto",
    r"em face do exposto",
    r"\bnesse ínterim\b",
    r"à luz (?:disso|do exposto|do pensamento|dess[ae] (?:ótica|perspectiva|teoria))",
    # exige artigo ou verbo depois, para não punir "consoante" (a letra)
    r"\bconsoante (?:o |a |os |as |afirma|aponta|defende|preceitua)",
    r"sob ess[ae] (?:ótica|perspectiva|prisma)",
    r"\bness[ea] viés\b",
    r"faz-se (?:necessári[oa]|mister)",
    r"medidas cabíveis",
    r"é de suma importância",
    r"modernidade líquida",
    r"(?:segundo|conforme|consoante) o sociólogo polonês",
    r"em primeira análise",
    r"\burge que\b",
    r"(?:ess[ea]|tal) problemática",
    r"(?:mitigar|sanar|dirimir) (?:ess[ea]|tal|a) (?:problemática|questão)",
    r"sociedade mais justa e igualitária",
    r"(?:só|somente) assim será possível",
    r"cabe ao (?:governo|estado|poder público)",
    r"conscientizar a população",
]

# Resíduos determinísticos de chat/modelo: em texto final publicado, uma
# única ocorrência já é quase-prova de geração por IA sem revisão.
RESIDUO_IA = [
    # recusas e autorreferência de modelo; a continuação em 1ª pessoa
    # evita punir títulos humanos como "como uma IA pode ajudar sua empresa"
    r"como (?:um[a]? )?(?:IA|inteligência artificial|modelo de linguagem)(?: de IA)?,? (?:eu )?não (?:posso|tenho|consigo)",
    r"sou (?:um |uma )?(?:modelo de linguagem|inteligência artificial|IA\b)",
    r"desculpe, (?:mas )?não posso ajudar",
    r"não posso atender a essa solicitação",
    r"(?:lamento|sinto muito), mas não posso",
    r"não tenho acesso a (?:dados|informações) em tempo real",
    r"isso vai contra as minhas diretrizes",
    # preâmbulos e fechos de chat colados
    r"^\s*(?:claro|certamente|com certeza|absolutamente|perfeito)[!,.]?\s*aqui (?:está|estão|vai)",
    r"espero que (?:isso )?(?:te )?ajude",
    r"espero ter ajudado",
    r"fico feliz em ajudar",
    r"(?:ótima|excelente|que ótima) pergunta!",
    r"você (?:está|tem) (?:absolutamente|totalmente) (?:cert[oa]|razão)",
    # disclaimers de data de corte
    r"minha (?:última atualização|data de corte)",
    r"a partir da minha última atualização",
    r"com base no meu treinamento",
    r"minhas informações estão atualizadas até",
    r"(?:atualização|corte|conhecimento|informações).{0,30}(?:até|em).{0,10}(?:setembro de 2021|janeiro de 2022|abril de 2023|outubro de 2023)",
    # placeholders não editados
    r"\[(?:inserir|insira) [^\]]{1,40}\]",
    r"\[(?:seu nome|nome da empresa|nome do cliente|cargo|data|cidade|valor|link)\]",
    # resíduos de interface
    r"resposta regenerada",
    r"regenerate response",
    r"como posso ajudar hoje\?",
]

# Pesos por categoria (pontuação normalizada por 1000 palavras, teto 100)
WEIGHTS = {
    'high_risk': 15,
    'medium_risk': 8,
    'buzzwords': 5,
    'meta_commentary': 10,
    'hedging': 6,
    'translationese': 8,
    'cliche_redacao': 10,
    'residuo_ia': 40,
    'em_dash': 4,
    'structure': 20,
}

# Conectivos que denunciam quando abrem parágrafo em série
TRANSITION_STARTERS = (
    'além disso', 'ademais', 'outrossim', 'adicionalmente', 'nesse sentido',
    'nessa perspectiva', 'nesse contexto', 'dessa forma', 'desse modo',
    'diante disso', 'diante desse cenário', 'no entanto', 'contudo',
    'todavia', 'portanto', 'consequentemente', 'ou seja', 'primeiramente',
    'em primeira análise', 'em suma', 'em síntese', 'em resumo', 'por fim',
    'sob essa ótica', 'assim sendo', 'sendo assim',
)

# Aberturas panorâmicas (verificadas só na primeira linha não vazia)
PANORAMIC_OPENINGS = (
    r"^(?:#+\s*)?em um[a]? (?:mundo|sociedade|era|cenário|contexto)\b",
    r"^(?:#+\s*)?no mundo (?:\w+ )?de hoje",
    r"^(?:#+\s*)?no cenário atual",
    r"^(?:#+\s*)?na era d[aeo]",
    r"^(?:#+\s*)?na sociedade contemporânea",
    r"^(?:#+\s*)?na contemporaneidade",
    r"^(?:#+\s*)?na atualidade",
    r"^(?:#+\s*)?nos dias (?:de hoje|atuais)",
    r"^(?:#+\s*)?hoje em dia",
    r"^(?:#+\s*)?vivemos em",
    r"^(?:#+\s*)?desde os primórdios",
    r"^(?:#+\s*)?você já parou para pensar",
)

# Fórmula de contraste "não é X, é Y" (avaliada no documento inteiro)
CONTRAST_PATTERN = (
    r"não (?:é|se trata|era)(?: só| apenas| somente)?(?: sobre| de)?\s+"
    r"[^.,;:\n]{1,60}[,.;:—–-]\s*(?:é|e sim|mas sim|trata-se de)\b"
)

# Emojis típicos de lista gerada (3+ linhas abrindo com eles = sinal)
EMOJI_BULLETS = ('🚀', '✅', '💡', '🔥', '👉', '✨')


class SlopDetector:
    def __init__(self, filepath: str, ignore_placeholders: bool = False,
                 ignore_contrast: bool = False):
        self.filepath = Path(filepath)
        self.ignore_placeholders = ignore_placeholders
        self.ignore_contrast = ignore_contrast
        self.text = self._load_file()
        self.lines = self.text.split('\n')
        self.findings = defaultdict(list)

    def _load_file(self) -> str:
        """Carrega e retorna o conteúdo do arquivo."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def _find_patterns(self, patterns: List[str], category: str):
        """Registra todas as ocorrências dos padrões, linha a linha."""
        for i, line in enumerate(self.lines, 1):
            for pattern in patterns:
                matches = re.finditer(pattern, line, re.IGNORECASE)
                for match in matches:
                    self.findings[category].append({
                        'line': i,
                        'text': line.strip(),
                        'match': match.group(),
                        'position': match.start()
                    })

    def analyze(self) -> Dict:
        """Roda todas as análises e retorna os achados."""
        self._find_patterns(HIGH_RISK_PHRASES, 'high_risk')
        self._find_patterns(MEDIUM_RISK_PHRASES, 'medium_risk')
        self._find_patterns(BUZZWORDS, 'buzzwords')
        self._find_patterns(META_COMMENTARY, 'meta_commentary')
        self._find_patterns(HEDGE_WORDS, 'hedging')
        self._find_patterns(TRANSLATIONESE, 'translationese')
        self._find_patterns(CLICHE_REDACAO, 'cliche_redacao')
        self._find_patterns(RESIDUO_IA, 'residuo_ia')
        if self.ignore_placeholders:
            self._drop_bracketed_placeholders()

        self._find_em_dashes()
        self._analyze_structure()

        score = self._calculate_slop_score()

        return {
            'findings': dict(self.findings),
            'score': score,
            'summary': self._generate_summary(score)
        }

    def _drop_bracketed_placeholders(self):
        """Remove de 'residuo_ia' os placeholders entre colchetes ([DATA],
        [SEU NOME], [valor] etc.), que em templates didáticos são intencionais."""
        kept = []
        for f in self.findings.get('residuo_ia', []):
            text = f['text']
            m = f['match']
            pos = f['position']
            # só descarta quando o match é exatamente um token [X]
            if m.startswith('[') and m.endswith(']'):
                continue
            kept.append(f)
        self.findings['residuo_ia'] = kept

    def _find_em_dashes(self):
        """Encontra travessão (U+2014) e meia-risca (U+2013) no meio da frase.

        Ignora linhas que começam com travessão (diálogo pt-BR), linhas de
        atribuição de citação em blockquote ("> — Fonte") e travessão
        imediatamente entre dígitos (intervalos como 1990-2000).
        """
        for i, line in enumerate(self.lines, 1):
            # Indentação e marcadores de blockquote não contam como início
            # da linha: "> — Autor" é atribuição de citação, uso convencional.
            stripped = re.sub(r'^(?:\s*>)*\s*', '', line)
            if stripped.startswith('—') or stripped.startswith('–'):
                continue
            for match in re.finditer(r"[—–]", line):
                pos = match.start()
                before = line[pos - 1] if pos > 0 else ''
                after = line[pos + 1] if pos + 1 < len(line) else ''
                if before.isdigit() and after.isdigit():
                    continue
                self.findings['em_dash'].append({
                    'line': i,
                    'text': line.strip(),
                    'match': match.group(),
                    'position': pos
                })

    def _analyze_structure(self):
        """Analisa padrões de slop no nível do documento."""
        # (a) abertura panorâmica na primeira linha não vazia
        first_line = next((l.strip() for l in self.lines if l.strip()), '')
        if first_line:
            for pattern in PANORAMIC_OPENINGS:
                if re.search(pattern, first_line, re.IGNORECASE):
                    self.findings['structure'].append({
                        'issue': 'Abertura panorâmica',
                        'description': 'o documento abre com ambientação genérica em vez de conteúdo concreto'
                    })
                    break

        # (b) proporção de parágrafos iniciando com conectivo de transição.
        # Parágrafos reais: blocos separados por linha em branco, excluindo
        # títulos (#), itens de lista (-, *, dígito+.), citações (>) e
        # tabelas (|), que não são prosa corrida.
        blocks = [b.strip() for b in re.split(r'\n\s*\n', self.text) if b.strip()]
        paragraphs = [
            b for b in blocks
            if not re.match(r'(?:[#\-*>|]|\d+\.)', b)
        ]
        if paragraphs:
            transition_starters = sum(
                1 for p in paragraphs
                if any(p.lower().startswith(t) for t in TRANSITION_STARTERS)
            )
            transition_ratio = transition_starters / len(paragraphs)
            if transition_ratio > 0.3:
                self.findings['structure'].append({
                    'issue': 'Excesso de transições',
                    'description': f'{transition_ratio:.0%} dos parágrafos começam com conectivo de transição'
                })

        # (c) fórmula de contraste "não é X, é Y" repetida no texto
        contrast_count = len(re.findall(CONTRAST_PATTERN, self.text, re.IGNORECASE))
        if contrast_count >= 2 and not self.ignore_contrast:
            self.findings['structure'].append({
                'issue': 'Contraste "não é X, é Y" repetido',
                'description': f'{contrast_count} ocorrências da fórmula de contraste no texto'
            })

        # (d) emoji como marcador de lista
        emoji_lines = sum(
            1 for line in self.lines
            if line.strip().startswith(EMOJI_BULLETS)
        )
        if emoji_lines >= 3:
            self.findings['structure'].append({
                'issue': 'Emoji como marcador de lista',
                'description': f'{emoji_lines} linhas abrem com emoji de lista (padrão de post gerado)'
            })

    def _calculate_slop_score(self) -> int:
        """Calcula a pontuação de slop (0-100, quanto maior, pior)."""
        score = 0
        for category, weight in WEIGHTS.items():
            score += len(self.findings[category]) * weight

        # normaliza pelo tamanho do documento (por 1000 palavras), com piso
        # de 500 palavras no denominador: sem o piso, um texto curto satura
        # a escala (um único achado em 195 palavras já renderia 41/100)
        word_count = len(self.text.split())
        if word_count > 0:
            score = int(score / max(word_count, 500) * 1000)

        return min(score, 100)

    def _generate_summary(self, score: int) -> str:
        """Gera um resumo legível da avaliação."""
        if score < 20:
            return "✅ Slop baixo: a escrita parece autêntica e objetiva"
        elif score < 40:
            return "⚠️  Slop moderado: alguns padrões genéricos presentes"
        elif score < 60:
            return "🚨 Slop alto: muitos padrões de texto gerado por IA"
        else:
            return "💀 Slop severo: o documento depende fortemente de padrões genéricos de IA"

    def print_report(self, verbose: bool = False):
        """Imprime o relatório formatado dos achados."""
        results = self.analyze()

        print(f"\n{'='*70}")
        print(f"Relatório de detecção de slop de IA: {self.filepath.name}")
        print(f"{'='*70}\n")

        print(f"Pontuação de slop: {results['score']}/100")
        if len(self.text.split()) < 100:
            print("Aviso: texto curto (< 100 palavras); a pontuação é pouco "
                  "confiável, considere as contagens brutas.")
        print(f"Avaliação: {results['summary']}\n")

        findings = results['findings']

        if findings.get('high_risk'):
            n = len(findings['high_risk'])
            print(f"🔴 FRASES DE ALTO RISCO ({n} ocorrência{'s' if n != 1 else ''}):")
            for f in findings['high_risk'][:5 if not verbose else None]:
                print(f"  Linha {f['line']}: '{f['match']}' em: {f['text'][:60]}...")
            if n > 5 and not verbose:
                print(f"  ... e mais {n - 5}")
            print()

        if findings.get('medium_risk'):
            n = len(findings['medium_risk'])
            print(f"📊 MULETAS DE TRANSIÇÃO ({n} ocorrência{'s' if n != 1 else ''}):")
            if not verbose:
                unique_matches = sorted(set(f['match'].lower() for f in findings['medium_risk']))
                print(f"  {', '.join(unique_matches[:10])}")
                if len(unique_matches) > 10:
                    print(f"  ... e mais {len(unique_matches) - 10} muletas distintas")
            else:
                for f in findings['medium_risk']:
                    print(f"  Linha {f['line']}: '{f['match']}'")
            print()

        if findings.get('buzzwords'):
            n = len(findings['buzzwords'])
            print(f"📢 BUZZWORDS E JARGÕES ({n} ocorrência{'s' if n != 1 else ''}):")
            if not verbose:
                unique_buzzwords = sorted(set(f['match'].lower() for f in findings['buzzwords']))
                print(f"  {', '.join(unique_buzzwords[:10])}")
                if len(unique_buzzwords) > 10:
                    print(f"  ... e mais {len(unique_buzzwords) - 10} buzzwords distintas")
            else:
                for f in findings['buzzwords']:
                    print(f"  Linha {f['line']}: '{f['match']}'")
            print()

        if findings.get('meta_commentary'):
            n = len(findings['meta_commentary'])
            print(f"📝 META-COMENTÁRIO ({n} ocorrência{'s' if n != 1 else ''}):")
            for f in findings['meta_commentary'][:3 if not verbose else None]:
                print(f"  Linha {f['line']}: {f['text'][:70]}...")
            if n > 3 and not verbose:
                print(f"  ... e mais {n - 3}")
            print()

        if findings.get('hedging'):
            n = len(findings['hedging'])
            print(f"🤔 ATENUAÇÃO EXCESSIVA (HEDGING) ({n} ocorrência{'s' if n != 1 else ''}):")
            if not verbose:
                lines_count = len(set(f['line'] for f in findings['hedging']))
                print(f"  Encontrada em {lines_count} linha{'s' if lines_count != 1 else ''}")
            else:
                for f in findings['hedging'][:5]:
                    print(f"  Linha {f['line']}: '{f['match']}'")
            print()

        if findings.get('translationese'):
            n = len(findings['translationese'])
            print(f"⚠️  CALCOS DE TRADUÇÃO ({n} ocorrência{'s' if n != 1 else ''}):")
            for f in findings['translationese'][:5 if not verbose else None]:
                print(f"  Linha {f['line']}: '{f['match']}' em: {f['text'][:60]}...")
            if n > 5 and not verbose:
                print(f"  ... e mais {n - 5}")
            print()

        if findings.get('cliche_redacao'):
            n = len(findings['cliche_redacao'])
            print(f"🚨 CLICHÊS DE REDAÇÃO ({n} ocorrência{'s' if n != 1 else ''}):")
            for f in findings['cliche_redacao'][:5 if not verbose else None]:
                print(f"  Linha {f['line']}: '{f['match']}' em: {f['text'][:60]}...")
            if n > 5 and not verbose:
                print(f"  ... e mais {n - 5}")
            print()

        if findings.get('residuo_ia'):
            n = len(findings['residuo_ia'])
            print(f"💀 RESÍDUOS DE IA (QUASE-PROVA) ({n} ocorrência{'s' if n != 1 else ''}):")
            for f in findings['residuo_ia']:
                print(f"  Linha {f['line']}: '{f['match']}' em: {f['text'][:60]}...")
            print("  Atenção: uma única ocorrência já é forte indício de texto gerado por IA.")
            print()

        if findings.get('em_dash'):
            n = len(findings['em_dash'])
            print(f"⚠️  TRAVESSÕES ({n} no meio de frase):")
            lines_with = sorted(set(f['line'] for f in findings['em_dash']))
            if not verbose:
                shown = ', '.join(str(l) for l in lines_with[:15])
                print(f"  Linhas: {shown}")
                if len(lines_with) > 15:
                    print(f"  ... e mais {len(lines_with) - 15} linhas")
            else:
                for f in findings['em_dash']:
                    print(f"  Linha {f['line']}: {f['text'][:70]}")
            print("  Travessões de diálogo/atribuição de citação e intervalos numéricos foram ignorados.")
            print()

        if findings.get('structure'):
            print("🏗️  PROBLEMAS ESTRUTURAIS:")
            for f in findings['structure']:
                print(f"  • {f['issue']}: {f['description']}")
            print()

        # Recomendações: sempre que a pontuação passa de 20 ou há resíduo de IA
        if results['score'] > 20 or findings.get('residuo_ia'):
            print("💡 RECOMENDAÇÕES:")
            if findings.get('high_risk'):
                print("  • Substitua as frases de alto risco por linguagem direta e específica")
            if findings.get('medium_risk'):
                print("  • Reduza a densidade de conectivos: 'além disso' e afins são português legítimo; um por parágrafo vira assinatura de IA")
            if findings.get('buzzwords'):
                print("  • Troque buzzwords por termos concretos: número, exemplo, nome próprio")
            if findings.get('meta_commentary'):
                print("  • Apague o meta-comentário e comece pelo conteúdo em si")
            if findings.get('hedging'):
                print("  • Reduza a atenuação: afirme direto ou corte a ressalva")
            if findings.get('translationese'):
                print("  • Reescreva os calcos de tradução com a expressão natural do português")
            if findings.get('cliche_redacao'):
                print("  • Corte os clichês de redação escolar; prefira dado datado e agente nomeado")
            if findings.get('residuo_ia'):
                print("  • Remova os resíduos de IA e revise o documento inteiro antes de publicar")
            if findings.get('em_dash'):
                print("  • Reescreva sem travessão (vírgula, dois-pontos, parênteses ou ponto); mantenha apenas quando indispensável")
            if findings.get('structure'):
                print("  • Reestruture o documento para evitar padrões genéricos de IA")
            print()


def main():
    if len(sys.argv) < 2:
        print("Uso: python detect_slop.py <arquivo> [--verbose] [--ignore-placeholders] [--ignore-contrast]")
        print("Analisa arquivos de texto em busca de padrões de conteúdo gerado por IA")
        print("  --verbose: relatório detalhado")
        print("  --ignore-placeholders: ignora placeholders entre colchetes ([DATA], [SEU NOME])")
        print("  --ignore-contrast: ignora a fórmula de contraste 'não é X, é Y' repetida")
        sys.exit(1)

    filepath = sys.argv[1]
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    ignore_placeholders = '--ignore-placeholders' in sys.argv
    ignore_contrast = '--ignore-contrast' in sys.argv

    if not Path(filepath).exists():
        print(f"Erro: arquivo '{filepath}' não encontrado")
        sys.exit(1)

    detector = SlopDetector(filepath, ignore_placeholders=ignore_placeholders,
                            ignore_contrast=ignore_contrast)
    detector.print_report(verbose=verbose)


if __name__ == '__main__':
    main()
