---
name: code-patterns
description: Guia de referência para detectar padrões de slop de IA em código, incluindo nomes de variáveis genéricos, comentários óbvios e abstrações desnecessárias. Use como referência ao revisar a qualidade de código.
---

# Padrões de slop em código

Esta referência documenta padrões comuns de "slop de IA" em código: padrões genéricos e de baixa qualidade que denunciam conteúdo gerado por inteligência artificial e que devem ser limpos.

## Sumário
- Antipadrões de nomenclatura
- Antipadrões de comentários
- Antipadrões de estrutura
- Antipadrões de implementação
- Antipadrões de documentação
- Slop por linguagem
- Slop de código em contexto brasileiro
- Sinais de detecção
- Estratégias de limpeza

## Antipadrões de nomenclatura

### Nomes genéricos demais
**Ruim:** `data`, `result`, `temp`, `value`, `item`, `thing`, `obj`, `info`

Esses nomes aparecem com frequência em código gerado por IA e não carregam significado nenhum.

**Melhor:** nomeie as coisas pelo que elas representam:
- `userData` → `currentUser`, `userProfile`, `activeSession`
- `result` → `parsedDocument`, `sortedItems`, `validationError`
- `temp` → `formattedDate`, `normalizedInput`, `previousValue`

### Nomes prolixos sem necessidade
**Ruim:** `getUserDataFromDatabaseByUserIdAndReturnResult()`, `calculateTotalSumOfAllItemPricesInCart()`

**Melhor:** `getUser(userId)`, `calculateCartTotal()`

A assinatura da função e o contexto já fornecem informação suficiente.

### Padrões de placeholder genérico
Fique atento ao uso repetido de:
- `foo`, `bar`, `baz` em código de produção
- `test1`, `test2`, `test3` como nomes de função
- Prefixos `MyClass`, `MyFunction`, `MyVariable`
- Sufixos `Helper`, `Manager`, `Handler` sem especificidade

## Antipadrões de comentários

### Comentários óbvios
Comentários que repetem o que o código já diz com clareza:

```python
# Ruim
# Cria um usuário
user = User()

# Incrementa o contador
counter += 1

# Retorna o resultado
return result

# Percorre os itens
for item in items:
    process(item)
```

**Regra:** se o código se explica sozinho, apague o comentário.

### Comentários TODO genéricos
```python
# Ruim
# TODO: Implementar esta função
# TODO: Adicionar tratamento de erros
# TODO: Otimizar este código
# TODO: Refatorar isto

# Melhor
# TODO(usuario): Tratar o caso em que a API retorna 429 (rate limit)
# TODO(usuario): Fazer profiling deste loop; suspeita de gargalo O(n²) com n>10000
```

Inclua QUEM deve fazer, O QUE especificamente e POR QUE, se não for óbvio.

### Lógica simples explicada demais
```python
# Ruim
# Verifica se o usuário está autenticado examinando o token de sessão
# e conferindo se ele corresponde aos tokens armazenados no banco de dados
if session.token in valid_tokens:
    # Se autenticado, prossegue com a requisição
    process_request()
```

**Melhor:** escreva código claro. Se a lógica for realmente complexa, explique a regra de negócio, não a sintaxe.

### Blocos de comentário que anunciam seções
```python
# Ruim
########################################
# INICIALIZAÇÃO
########################################

########################################
# LÓGICA PRINCIPAL DE PROCESSAMENTO
########################################
```

**Melhor:** organize o código com funções ou classes. A estrutura não deveria depender de comentários para aparecer.

## Antipadrões de estrutura

### Camadas de abstração desnecessárias
```python
# Ruim: superengenharia típica de IA
class UserManagerFactory:
    def create_user_manager(self):
        return UserManager()

class UserManager:
    def get_user_repository(self):
        return UserRepository()

class UserRepository:
    def get_user(self, user_id):
        return db.query(User).filter(User.id == user_id).first()

# Melhor
def get_user(user_id):
    return db.query(User).filter(User.id == user_id).first()
```

**Regra:** não adicione camadas de abstração antes de precisar delas. YAGNI.

### Uso excessivo de padrões de projeto
Nem tudo precisa ser:
- Factory
- Singleton
- Observer
- Strategy
- Adapter

Use padrões quando eles resolverem problemas reais, não porque você aprendeu sobre eles.

### Tratamento de erros genérico
```python
# Ruim
try:
    result = dangerous_operation()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    pass  # Continua mesmo assim
```

**Melhor:** capture exceções específicas e trate cada uma adequadamente.

### Blocos catch vazios
```python
# Ruim
try:
    risky_operation()
except:
    pass
```

Isso está errado em quase todos os casos. Se realmente precisar ignorar uma exceção, explique o motivo em um comentário.

## Antipadrões de implementação

### Implementações complexas sem necessidade
```python
# Ruim: IA complicando uma tarefa simples
def is_even(n):
    """Verifica se um número é par usando propriedades matemáticas."""
    return (n / 2) == (n // 2)

# Melhor
def is_even(n):
    return n % 2 == 0
```

### Otimização prematura
```python
# Ruim: otimizar antes de medir com profiling
# Usando manipulação de bits por "performance"
def multiply_by_two(n):
    return n << 1

# Melhor: claro e correto
def multiply_by_two(n):
    return n * 2
```

**Regra:** primeiro código claro, depois otimização baseada em dados de profiling.

### Blocos de código copiados e colados
Fique atento a:
- Funções parecidas com pequenas variações
- Lógica condicional repetida
- Tratamento de erros duplicado

**Melhor:** extraia a lógica comum para funções compartilhadas.

### Números mágicos sem explicação
```python
# Ruim
if len(input) > 255:
    raise ValueError()

# Melhor
MAX_INPUT_LENGTH = 255  # Limite da coluna no banco de dados
if len(input) > MAX_INPUT_LENGTH:
    raise ValueError(f"Entrada excede o comprimento máximo de {MAX_INPUT_LENGTH}")
```

## Antipadrões de documentação

### Docstrings genéricas
```python
# Ruim
def process_data(data):
    """Processa os dados.

    Args:
        data: os dados a processar

    Returns:
        os dados processados
    """
    pass
```

Isso não acrescenta informação nenhuma. Documente de verdade ou não documente.

### Boilerplate de README
Fique atento a:
- "Este projeto tem como objetivo..."
- "Bem-vindo ao nosso incrível projeto!"
- Instruções de instalação genéricas que não correspondem ao projeto real
- Seções de placeholder nunca preenchidas
- Excesso de emoji e citações "inspiradoras"

### APIs internas documentadas em excesso
Nem tudo precisa de documentação exaustiva:

```python
# Ruim: função auxiliar interna
def _format_date(date_obj):
    """Formata um objeto de data em uma string.

    Esta função recebe um objeto de data e o formata de acordo com
    o padrão ISO 8601. Ela é usada internamente pela classe
    DateProcessor para garantir formatação de datas consistente
    em toda a aplicação.

    Args:
        date_obj (datetime): um objeto datetime representando a data
                            a ser formatada. Deve ser uma instância
                            válida de datetime com fuso horário.

    Returns:
        str: representação da data em formato ISO 8601. O formato
             inclui ano, mês, dia, hora, minuto e segundo, com o
             deslocamento de fuso horário.

    Raises:
        ValueError: se date_obj for None ou não for uma instância de datetime.
        TypeError: se date_obj for de um tipo incompatível.

    Example:
        >>> dt = datetime.now()
        >>> _format_date(dt)
        '2024-01-15T14:30:00+00:00'

    Note:
        Esta é uma função interna e não deve ser chamada diretamente
        por código externo. Use o método público DateProcessor.format().

    See Also:
        - DateProcessor.format()
        - parse_date()
        - validate_date()
    """
    return date_obj.isoformat()

# Melhor para uma auxiliar interna
def _format_date(date_obj):
    """Retorna a data como string no formato ISO 8601."""
    return date_obj.isoformat()
```

## Slop por linguagem

### Python
- `lambda` desnecessário quando uma função seria mais clara
- List comprehensions onde um loop simples seria mais legível
- Abuso de `*args, **kwargs` sem necessidade clara
- Captura genérica de exceções: `except Exception:`

### JavaScript/TypeScript
- Arrow functions em todo lugar, sem critério
- Encadeamento excessivo de métodos de array para operações simples
- Tipos `any` genéricos em TypeScript
- Uso excessivo de operador ternário para lógica complexa

### Java
- Boilerplate excessivo de getters/setters para classes que só carregam dados
- Interfaces desnecessárias com uma única implementação
- Tipos `Object` genéricos no lugar de generics
- Dependência exagerada de herança em vez de composição

## Slop de código em contexto brasileiro

Código gerado por IA em projetos brasileiros tem sinais próprios, que nascem do choque entre o prompt em português e o corpus de treino em inglês.

### Mistura de português e inglês em identificadores
**Ruim:** `getUsuario()`, `processarData()`, `ClienteService.fetchDados()`, `setEndereco()`, `usuarioList`, `isAtivo`

A IA costuma colar verbos em inglês (`get`, `set`, `fetch`, `handle`) em substantivos do domínio em português, ou vice-versa. Além de inconsistente, a mistura cria ambiguidade real: em `processarData()`, "data" é a data do calendário ou os dados?

**Critério:** escolha UM idioma por projeto e mantenha. Ambas as opções abaixo são válidas; a mistura não é:
- Tudo em inglês: `getUser()`, `processPayload()`, `CustomerService.fetchOrders()`
- Tudo em português: `obterUsuario()`, `processarPedidos()`, `ServicoDeCliente.buscarPedidos()`

Se o projeto já tem uma convenção, código novo deve segui-la, mesmo quando a IA sugerir outra.

### Comentários em português que repetem o código
A versão brasileira do comentário óbvio. O identificador está em inglês e o comentário traduz o que a linha já diz:

```python
# Ruim
counter += 1  # incrementa o contador
users = fetch_users()  # busca os usuários
return total  # retorna o total
```

O comentário-tradução é um sinal forte de geração por IA: humanos raramente traduzem a própria linha. Vale a mesma regra dos comentários óbvios: apague.

### Docstrings genéricas em português
```python
# Ruim
def calculate_discount(order):
    """Esta função processa os dados e retorna o resultado."""

# Ruim
def validate_cpf(cpf):
    """Método responsável por realizar a validação."""

# Melhor
def validate_cpf(cpf):
    """Valida o CPF pelos dígitos verificadores; aceita com ou sem pontuação."""
```

Fórmulas denunciadoras: "Esta função é responsável por...", "Este método tem como objetivo...", "realiza o processamento de...". Se a docstring serve para qualquer função, ela não serve para nenhuma.

### Mensagens de commit genéricas
**Ruim:** `ajustes`, `correções`, `melhorias no código`, `alterações`, `atualização de arquivos`, `mudanças solicitadas`, `fix`

**Melhor:** diga o que mudou e, quando não for óbvio, por quê:
- `ajustes` → `corrige cálculo de frete para CEP com dígito zero à esquerda`
- `melhorias no código` → `extrai validação de CPF para módulo compartilhado`

Uma sequência de commits genéricos e uniformes ("ajustes", "mais ajustes", "correções finais") é sinal de fluxo automatizado sem revisão.

### Abreviações ambíguas em português
**Ruim:** `qtd`, `vlr`, `dt`, `cad`, `usr`, `ped`, `func`, `desc`, `end`

Cada uma esconde uma ambiguidade: `dt` (data ou delta?), `func` (funcionário ou função?), `desc` (descrição ou desconto?), `cad` (cadastro ou cadeia?), `end` (endereço, colidindo com palavra reservada em várias linguagens).

**Melhor:** escreva por extenso no idioma escolhido para o projeto: `quantidade`/`quantity`, `valorTotal`/`totalAmount`, `dataEmissao`/`issueDate`, `usuario`/`user`.

### Resíduos de chat colados no código
Restos da conversa com o modelo que sobraram no arquivo entregue. Em código commitado, cada um é quase-prova de geração sem revisão:

```python
# Ruim
# Claro! Aqui está a função solicitada:
def send_email(recipient):
    api_key = "[SUA_CHAVE_API]"  # Lembre-se de substituir pela sua chave real
    ...
# Espero que este código ajude! Qualquer dúvida, estou à disposição.
```

Sinais da família: preâmbulo de aquiescência ("Claro! Aqui está..."), fecho de chat ("Espero que ajude!"), placeholders não editados em colchetes (`[Seu Nome]`, `[SUA_CHAVE_API]`) e a instrução residual "lembre-se de substituir X pelos seus dados reais". Exceção: templates e exemplos didáticos que se apresentam como templates, onde o placeholder é proposital.

## Sinais de detecção

### Indicadores de slop de alta confiança
1. Variável chamada `result` que guarda tipos diferentes
2. Funções com verbos genéricos: `handleData`, `processInfo`, `manageItems`
3. Comentários que explicam a sintaxe em vez da intenção
4. Toda função tem docstring, até as triviais
5. Superengenharia consistente pelo código inteiro

### Indicadores de confiança média
1. Nomes de função/variável muito longos, que embutem o contexto completo
2. Programação defensiva excessiva (verificação de condições impossíveis)
3. Implementações vazias ou mínimas com comentários "TODO"
4. Estrutura uniforme em todas as funções (os mesmos padrões em toda parte)

## Estratégias de limpeza

### Ações imediatas
1. Apagar comentários óbvios
2. Renomear variáveis genéricas no escopo imediato
3. Remover blocos catch vazios ou adicionar tratamento de verdade
4. Apagar imports e funções não usados

### Refatoração
1. Extrair código repetido para funções
2. Simplificar condicionais complexas
3. Remover camadas de abstração desnecessárias
4. Trocar nomes genéricos por nomes do domínio

### Mudanças que exigem testes
1. Remover tratamento de erros (confirme que é seguro remover)
2. Simplificar algoritmos (verifique que o comportamento se mantém)
3. Remover verificações "defensivas" de nulo (confirme que são de fato desnecessárias)

## O contexto importa

Às vezes padrões que parecem slop são, na verdade, apropriados:

- **Nomes genéricos em escopos pequenos:** `i`, `x`, `acc` em uma função de 3 linhas não é problema
- **Nomes longos em APIs públicas:** melhor claro demais do que críptico demais
- **Programação defensiva:** em APIs expostas ao público ou sistemas críticos
- **Docstrings detalhadas:** em bibliotecas públicas e algoritmos complexos
- **Padrões de projeto:** em bases de código grandes, onde ajudam de verdade
- **Identificadores em inglês em projeto brasileiro:** é a convenção dominante em código aberto; o problema é a mistura, não a escolha

Distinga **decisões de engenharia intencionais** de **repetição mecânica de padrões**.
