# Fundamentos de Python

Este repositório é dedicado à introdução e prática dos fundamentos da linguagem Python. Ideal para quem está começando ou deseja revisar os principais conceitos da linguagem.

Python é uma linguagem de programação de alto nível, interpretada, orientada a objetos e com tipagem dinâmica. É conhecida por sua sintaxe clara e legível, o que a torna uma excelente escolha para iniciantes e para o desenvolvimento rápido de aplicações em diversas áreas, como:

- Desenvolvimento web  
- Ciência de dados  
- Inteligência artificial  
- Automação  
- Entre outras

## Principais Características

- **Simples e legível**  
  A sintaxe de Python se assemelha muito à linguagem natural, facilitando o aprendizado e a leitura do código.

- **Multi-paradigma**  
  Suporta programação orientada a objetos, imperativa e funcional.

- **Interpretada**  
  O código Python não precisa ser compilado antes de ser executado, agilizando o ciclo de desenvolvimento.

- **Tipagem dinâmica**  
  Você não precisa declarar o tipo de uma variável; Python infere o tipo em tempo de execução.

- **Grande comunidade e bibliotecas**  
  Python possui uma vasta comunidade de desenvolvedores e um ecossistema rico em bibliotecas e frameworks para quase todas as necessidades.

---
## Variáveis

Em Python, uma **variável** é um nome que se refere a um valor. Pense nela como uma “caixa” ou “rótulo” que armazena dados na memória do computador.

### Características das Variáveis

- **Nomenclatura**:
  - Devem começar com uma letra (`a-z`, `A-Z`) ou um sublinhado (`_`).
  - Podem conter letras, números e sublinhados.
  - São *case-sensitive*: `idade` é diferente de `Idade`.
  - Não podem ser palavras-chave reservadas do Python, como `if`, `for`, `while`, etc.
  - Convenção: usa-se o estilo `snake_case` (letras minúsculas com sublinhados), como em `minha_variavel`.

- **Atribuição**:
  - Use o operador `=` para atribuir um valor a uma variável.  
    Exemplo:
    ```python
    idade = 25
    nome = "Maria"
    ```

- **Tipagem Dinâmica**:
  - Você **não precisa declarar** o tipo da variável.
  - O tipo é inferido automaticamente com base no valor atribuído.
  - O tipo de uma variável pode **mudar durante a execução** do programa.  
    Exemplo:
    ```python
    x = 10        # x é um inteiro
    x = "dez"     # agora x é uma string
    ```

---
##  Expressões e Declarações (Statements)

Em programação, é crucial entender a diferença entre **expressões** e **declarações (statements)**.

### Expressões

Uma **expressão** é uma combinação de valores, variáveis, operadores e chamadas de função que o interpretador Python pode avaliar para **produzir um resultado** (um valor).

> Expressões **produzem** algo.

**Exemplos de expressões:**

```python
5 + 3                 # Avalia para 8
"Olá" + " " + "Mundo" # Avalia para "Olá Mundo"
idade * 2             # Avalia para o dobro do valor de 'idade'
len("Python")         # Avalia para 6
True and False        # Avalia para False

```
---
## Tipos de Dados

Python possui vários tipos de dados embutidos para representar diferentes tipos de informações. Compreender os tipos de dados é fundamental, pois eles determinam as operações que podem ser realizadas com os valores.

### Tipos de Dados Fundamentais

- **int** (Inteiros):  
  Números inteiros, positivos ou negativos, sem casas decimais.  
  Ex: `5`, `-100`, `0`

- **float** (Ponto Flutuante):  
  Números reais com casas decimais.  
  Ex: `3.14`, `-0.5`, `2.0`

- **complex** (Complexos):  
  Números com parte real e imaginária.  
  Ex: `1 + 2j` (menos comum)

- **bool** (Booleanos):  
  Representam valores de verdade: `True` ou `False`.  
  Usados em lógica e controle de fluxo.

- **str** (Strings):  
  Sequência de caracteres (texto).  
  Delimitadas por aspas simples `' '` ou duplas `" "`.  
  Ex: `"Olá, Mundo!"`, `'Python'`

---

### Tipos de Coleção (Estruturas de Dados)

- **list** (Listas):  
  Coleções **ordenadas e mutáveis**.  
  Ex: `[1, 2, "três"]`

- **tuple** (Tuplas):  
  Coleções **ordenadas e imutáveis**.  
  Ex: `(1, 2, 3)`

- **dict** (Dicionários):  
  Coleções de **pares chave-valor**, não ordenadas.  
  Ex: `{"nome": "Ana", "idade": 25}`

- **set** (Conjuntos):  
  Coleções **não ordenadas** de **itens únicos**.  
  Ex: `{1, 2, 3}`

---

### Como Verificar o Tipo de Dado

Use a função embutida `type()`:

```python
x = 10
y = 3.14
z = "Python"
a = True
b = [1, 2, 3]
c = (4, 5)
d = {"chave": "valor"}
e = {1, 2, 3}

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'list'>
print(type(c))  # <class 'tuple'>
print(type(d))  # <class 'dict'>
print(type(e))  # <class 'set'>
```

# Operadores em Python

Operadores são símbolos especiais que realizam operações sobre um ou mais valores (operandos).

---

##  Operadores Aritméticos

Usados para operações matemáticas.

| Operador | Nome             | Exemplo   | Resultado |
|----------|------------------|-----------|-----------|
| `+`      | Adição           | 5 + 2     | 7         |
| `-`      | Subtração        | 5 - 2     | 3         |
| `*`      | Multiplicação    | 5 * 2     | 10        |
| `/`      | Divisão          | 5 / 2     | 2.5       |
| `%`      | Módulo (resto)   | 5 % 2     | 1         |
| `**`     | Exponenciação    | 5 ** 2    | 25        |
| `//`     | Divisão inteira  | 5 // 2    | 2         |

### Exemplos em Python:

```python
print(10 + 3)    # 13
print(10 - 3)    # 7
print(10 * 3)    # 30
print(10 / 3)    # 3.333...
print(10 % 3)    # 1
print(2 ** 4)    # 16
print(10 // 3)   # 3
```
## Operadores de Comparação

Usados para comparar valores. Sempre retornam um valor booleano

| Operador | Nome             | Exemplo  | Resultado |
| -------- | ---------------- | -------- | --------- |
| `==`     | Igual a          | 5 == 5   | True      |
| `!=`     | Diferente de     | 5 != 10  | True      |
| `>`      | Maior que        | 10 > 5   | True      |
| `<`      | Menor que        | 5 < 10   | True      |
| `>=`     | Maior ou igual a | 10 >= 10 | True      |
| `<=`     | Menor ou igual a | 5 <= 10  | True      |

### Exemplos em Python:

```
print(10 == 10)          # True
print(10 != 5)           # True
print(10 > 5)            # True
print(5 < 10)            # True
print(10 >= 10)          # True
print(5 <= 10)           # True

print("Python" == "python")  # False (case-sensitive)
print("apple" < "banana")    # True (ordem alfabética)
```

## Operadores Booleanos

Usados para combinar expressões booleanas

| Operador | Descrição                                 | Exemplo          | Resultado |
| -------- | ----------------------------------------- | ---------------- | --------- |
| `and`    | Retorna `True` se ambas forem verdadeiras | `True and False` | False     |
| `or`     | Retorna `True` se pelo menos uma for      | `True or False`  | True      |
| `not`    | Inverte o valor booleano                  | `not True`       | False     |

#### Prioridade: NOT > AND > OR

## Exemplos em Python:

```
idade = 20
tem_cnh = True

print(idade > 18 and tem_cnh)  # True
print(idade < 18 or tem_cnh)   # True
print(not tem_cnh)             # False
```
## Operadores Bitwise(Bit a Bit)

Operam sobre os bits de numeros inteiros

| Operador | Nome                    | Exemplo      |        |
| -------- | ----------------------- | ------------ | ------ |
| `&`      | AND bit a bit           | 5 & 3        |        |
| \`       | \`                      | OR bit a bit | 5 \| 3 |
| `^`      | XOR bit a bit           | 5 ^ 3        |        |
| `~`      | NOT bit a bit           | \~5          |        |
| `<<`     | Deslocamento à esquerda | 5 << 1       |        |
| `>>`     | Deslocamento à direita  | 5 >> 1       |        |

### Explicacao com binario:

-> 5 = 0101
-> 3 = 0011

| Operação | Binário            | Decimal |             |   |
| -------- | ------------------ | ------- | ----------- | - |
| `5 & 3`  | 0101 & 0011 = 0001 | 1       |             |   |
| \`5      | 3\`                | 0101    | 0011 = 0111 | 7 |
| `5 ^ 3`  | 0101 ^ 0011 = 0110 | 6       |             |   |
| `~5`     | inverte bits → -6  | -6      |             |   |
| `5 << 1` | 0101 → 1010        | 10      |             |   |
| `5 >> 1` | 0101 → 0010        | 2       |             |   |

### Exemplos em Python

```
print(5 & 3)    # 1
print(5 | 3)    # 7
print(5 ^ 3)    # 6
print(~5)       # -6
print(5 << 1)   # 10
print(5 >> 1)   # 2
```

## Operadores `is` e `in`

### `is` -Operador de Identidade

Verifica se dois objetos ocupam o mesmo espaco na memoria

```
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)  # True  (valores iguais)
print(lista1 is lista2)  # False (objetos diferentes)
print(lista1 is lista3)  # True  (mesma referência)

a = None
print(a is None)         # True
```

### `in` -Operador de Associacao

Verifica se um valor esta presente em uma sequencia (lista, string, dicionario).

```
frutas = ["maçã", "banana", "laranja"]

print("maçã" in frutas)         # True
print("uva" in frutas)          # False

texto = "Olá, mundo Python!"
print("Python" in texto)       # True
print("java" in texto)         # False

dicionario = {"nome": "Maria", "idade": 30}
print("nome" in dicionario)            # True (chave)
print("Maria" in dicionario)           # False
print("Maria" in dicionario.values())  # True
```

## Operador Ternario

Forma consisa de um if. . .else em uma unica linha

#### Sintaxe:

```
valor = valor_se_verdadeiro if condição else valor_se_falso

```

### Exemplo em Python: 

```

idade = 17
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)  # Menor de idade

temperatura = 25
clima = "Quente" if temperatura > 20 else "Frio"
print(clima)   # Quente

```

# 9. Strings em Python

Strings são sequências de caracteres utilizadas para representar texto. São **imutáveis** e fundamentais na linguagem Python.

---

## Criação de Strings

Strings podem ser criadas com:

- Aspas simples: `'texto'`
- Aspas duplas: `"texto"`
- Aspas triplas: `'''texto'''` ou `"""texto"""` (permitem múltiplas linhas)

```python
nome = "Alice"
mensagem = 'Olá, mundo!'
paragrafo = """Este é um parágrafo
que abrange várias linhas."""
```
### Imutabilidade das Strings

STrings não podem ser modificadas após serem criadas

```python
saudacao = "Olá"
saudacao[0] = "A"  # TypeError!

nova_saudacao = saudacao + " Mundo"
print(saudacao)       # Olá
print(nova_saudacao)  # Olá Mundo
```

## Métodos de String

Python oferece diversos métodos para a manipulação de strings.

| Método            | Descrição                         | Exemplo                          | Resultado         |
| ----------------- | --------------------------------- | -------------------------------- | ----------------- |
| `upper()`         | Converte para maiúsculas          | `"hello".upper()`                | `"HELLO"`         |
| `lower()`         | Converte para minúsculas          | `"HELLO".lower()`                | `"hello"`         |
| `capitalize()`    | Primeira letra maiúscula          | `"python".capitalize()`          | `"Python"`        |
| `title()`         | Primeira letra de cada palavra    | `"hello world".title()`          | `"Hello World"`   |
| `strip()`         | Remove espaços nas extremidades   | `" olá ".strip()`                | `"olá"`           |
| `lstrip()`        | Remove espaços à esquerda         | `" olá ".lstrip()`               | `"olá "`          |
| `rstrip()`        | Remove espaços à direita          | `" olá ".rstrip()`               | `" olá"`          |
| `replace(a, b)`   | Substitui substrings              | `"banana".replace("a", "o")`     | `"bonono"`        |
| `split(sep)`      | Divide a string em lista          | `"a,b,c".split(",")`             | `['a', 'b', 'c']` |
| `join(iterable)`  | Junta elementos com separador     | `",".join(['a', 'b', 'c'])`      | `"a,b,c"`         |
| `startswith(sub)` | Verifica início                   | `"Python".startswith("Py")`      | `True`            |
| `endswith(sub)`   | Verifica fim                      | `"arquivo.txt".endswith(".txt")` | `True`            |
| `find(sub)`       | Índice da primeira ocorrência     | `"hello".find("l")`              | `2`               |
| `count(sub)`      | Contagem de ocorrências           | `"banana".count("a")`            | `3`               |
| `isalnum()`       | Verifica se é alfanumérico        | `"Python123".isalnum()`          | `True`            |
| `isalpha()`       | Verifica se é alfabético          | `"Python".isalpha()`             | `True`            |
| `isdigit()`       | Verifica se é numérico            | `"123".isdigit()`                | `True`            |
| `isspace()`       | Verifica se contém apenas espaços | `" ".isspace()`                  | `True`            |

```python
texto = "  Python é divertido!  "

print(texto.strip())                         # "Python é divertido!"
print(texto.upper())                         # "  PYTHON É DIVERTIDO!  "
print(texto.lower())                         # "  python é divertido!  "
print(texto.replace("divertido", "incrível"))# "  Python é incrível!  "

palavras = texto.strip().split(" ")
print(palavras)                              # ['Python', 'é', 'divertido!']

nova_frase = "-".join(palavras)
print(nova_frase)                            # "Python-é-divertido!"
```

### Escapando Caracteres

Caractere de escape `\` permite incluir símbolos especiais dentro de strings.

| Escape | Descrição       |
| ------ | --------------- |
| `\'`   | Aspa simples    |
| `\"`   | Aspa dupla      |
| `\\`   | Barra invertida |
| `\n`   | Nova linha      |
| `\t`   | Tabulação       |

#### Exemplos:

```python
print('Eu disse: \'Olá!\'')
print("O caminho é C:\\Users\\Documentos")
print("Linha 1\nLinha 2")
print("Nome:\tJoão")
```

### Raw STrings:

Use `r". . ."` para ignorar os caracteres de escape

```python
caminho = r"C:\novo\diretorio\arquivo.txt"
print(caminho)  # Saída literal do caminho
```

## Caracteres de STring e Slicing

Strings podem ser manipuladas como sequencias de caracteres

#### Indexação:

Começa no indice `0`

Indices negativos começam do final

```python
frase = "Python"

print(frase[0])   # P
print(frase[2])   # t
print(frase[-1])  # n
print(frase[-6])  # P
```

### Slicing [start:end:step]

```python
texto = "Programação Python"

print(texto[0:9])     # Programaç
print(texto[:9])      # Programaç
print(texto[10:])     # Python
print(texto[:])       # Programação Python
print(texto[::2])     # PogaçoPto
print(texto[::-1])    # nohtyP oãçamargorP
print(texto[4:10:2])  # ra
```

### Comprimento da String

Use `len()` para contar os caracteres

```python
nome = "Mundo"
print(len(nome))
```

### Formatação de Strings

```python
nome = "Maria"
idade = 22
salario = 5000.75

print(f"Meu nome é {nome} e tenho {idade} anos.")
print(f"Salário: R${salario:.2f}")
print(f"O dobro de 5 é {5 * 2}.")
```
#  Booleanos em Python

Booleanos são um tipo de dado fundamental em Python, representando **valores de verdade**: `True` (verdadeiro) ou `False` (falso).

---

## Características Gerais

- Os valores booleanos são: `True` e `False` (com a primeira letra maiúscula).
- Tipo de dado: `bool`
- Usados em estruturas condicionais, laços e expressões lógicas.

```python
x = True
y = False

print(x)          # True
print(type(x))    # <class 'bool'>
```

### Contextoo Booleano

EM Python, muitos valores podem ser avaliados como booleanos automaticamente

#### Valores "Falsy":

| Tipo       | Valor   |
| ---------- | ------- |
| None       | `None`  |
| Booleano   | `False` |
| Inteiro    | `0`     |
| Float      | `0.0`   |
| String     | `""`    |
| Lista      | `[]`    |
| Tupla      | `()`    |
| Dicionário | `{}`    |
| Conjunto   | `set()` |

#### Valores "Truthy":

- Qualquer numero diferente de zero
- Qualquer string nao vazia
- Qualquer lista,tupla, dicionario ouy conjunto nao vazio

#### Revisao: Operadores Booleanos:

| Operador | Descrição                                         | Exemplo          | Resultado |
| -------- | ------------------------------------------------- | ---------------- | --------- |
| `and`    | Retorna `True` se ambos os operandos forem `True` | `True and False` | `False`   |
| `or`     | Retorna `True` se pelo menos um for `True`        | `True or False`  | `True`    |
| `not`    | Inverte o valor booleano                          | `not True`       | `False`   |

#### Exemplo:

```python
x = True
y = False

print(x and y)   # False
print(x or y)    # True
print(not x)     # False
```
#  Tipos de Dados Numéricos em Python

Python oferece suporte nativo a três tipos numéricos principais:

- `int`: Números inteiros
- `float`: Números de ponto flutuante
- `complex`: Números complexos

---

## `int` – Inteiros

Representam números inteiros (positivos, negativos ou zero).

- Sem limite de tamanho (exceto a memória do sistema).
- Armazenam números como `-100`, `0`, `42`, `12345678901234567890`

### Exemplo:

```python
numero_inteiro = 42
numero_negativo = -100
zero = 0
grande_numero = 12345678901234567890

print(type(numero_inteiro))  # <class 'int'>
```

## `float` - Ponto Flutuante

Representam numeros reais com casas decimais.
- Precisao dupla(64 bits), o que pode causar pequenas imprecisoes.

#### Exemplo:
```python
numero_decimal = 3.14
salario = 2500.50
notacao_cientifica = 1.23e-5  # Equivale a 0.0000123

print(type(numero_decimal))  # <class 'float'>
```

## `complex` - Numeros Complexos

Representam numeros na forma a + bj onde:
- `a` e a parte real
- `b` e a parte imaginaria
- `j` representa a raiz quadrada de -1

#### Exemplo:
```python
numero_complexo = 2 + 3j

print(type(numero_complexo))     # <class 'complex'>
print(numero_complexo.real)      # 2.0
print(numero_complexo.imag)      # 3.0
```

## Conversao de Tipos (Type Casting)
Forma de converter entre tipos numericos e strings com funcoes embutidas:
| Função    | Conversão             |
| --------- | --------------------- |
| `int()`   | Converte para inteiro |
| `float()` | Converte para float   |
| `str()`   | Converte para string  |

#### Exemplos:
```python
numero_float = 5.9
numero_inteiro_convertido = int(numero_float)
print(numero_inteiro_convertido)  # 5 (truncado)

numero_str = "123"
numero_inteiro_de_str = int(numero_str)
print(numero_inteiro_de_str)  # 123

numero_int = 7
numero_float_convertido = float(numero_int)
print(numero_float_convertido)  # 7.0
```

# Funções Built-in (Embutidas) em Python

Python possui diversas funções embutidas (`built-in`) que podem ser utilizadas diretamente, sem necessidade de importar módulos. Essas funções são extremamente úteis para manipular dados, interagir com o usuário, realizar conversões e muito mais.

---

## 📋 Principais Funções Built-in

| Função             | Descrição                                                                 |
|--------------------|---------------------------------------------------------------------------|
| `print()`          | Exibe uma saída no console.                                               |
| `input()`          | Lê uma entrada do usuário (como string).                                 |
| `len()`            | Retorna o comprimento de uma sequência (string, lista, tupla, etc.).     |
| `type()`           | Retorna o tipo de um objeto.                                              |
| `int()`, `float()`, `str()`, `bool()` | Funções de conversão de tipo.                        |
| `sum()`            | Soma os elementos de um iterável.                                         |
| `min()`, `max()`   | Retornam o menor e o maior elemento de um iterável, respectivamente.      |
| `abs()`            | Retorna o valor absoluto de um número.                                   |
| `round()`          | Arredonda um número para o inteiro mais próximo.                         |
| `dir()`            | Lista os atributos e métodos de um objeto.                               |
| `help()`           | Fornece ajuda/documentação sobre o objeto especificado.                   |
| `range()`          | Gera uma sequência de números.                                            |
| `enumerate()`      | Retorna pares (índice, valor) de um iterável.                             |
| `zip()`            | Agrupa elementos de múltiplos iteráveis em tuplas.                        |
| `sorted()`         | Retorna uma nova lista ordenada a partir de um iterável.                  |
| `map()`, `filter()`, `reduce()` | Funções de ordem superior (detalhadas posteriormente).     |

---

## 💡 Exemplos Práticos

```python
lista_numeros = [10, 5, 20, 15]

print(f"Comprimento da lista: {len(lista_numeros)}")     # 4
print(f"Soma dos números: {sum(lista_numeros)}")         # 50
print(f"Menor número: {min(lista_numeros)}")             # 5
print(f"Maior número: {max(lista_numeros)}")             # 20

print(f"Valor absoluto de -7: {abs(-7)}")                # 7
print(f"Arredondamento de 3.7: {round(3.7)}")            # 4
print(f"Arredondamento de 3.2: {round(3.2)}")            # 3
print(f"Arredondamento de 3.5: {round(3.5)}")            # 4 (para o par mais próximo)
```

#### `enumerate()`: Iterando com indice

```python
for i, valor in enumerate(["a", "b", "c"]):
    print(f"Índice: {i}, Valor: {valor}")
```

### `zip()`: Combina dois ou mais iteraveis

```python
nomes = ["Ana", "Beto"]
idades = [25, 30]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")
```

# Enums (Enumerações) em Python

Enums (enumerações) são **conjuntos de nomes simbólicos associados a valores constantes únicos**. Eles ajudam a tornar o código mais claro, organizado e seguro.

> 📦 Enums são definidos usando a classe `Enum` do módulo `enum`.

---

## ✅ Por que usar Enums?

- **Legibilidade**: nomes simbólicos são mais fáceis de entender que números ou strings soltas.
- **Manutenibilidade**: altera-se o valor de um único lugar sem afetar o resto do código.
- **Segurança**: restringe os valores válidos — reduz erros de digitação.
- **Autocompletar**: ferramentas como VS Code e PyCharm facilitam o uso com sugestões.

---

## 🧪 Exemplo Básico

```python
from enum import Enum

class DiaDaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DOMINGO = 7

# Acessando membros:
print(DiaDaSemana.SEGUNDA)        # DiaDaSemana.SEGUNDA
print(DiaDaSemana.SEGUNDA.name)   # 'SEGUNDA'
print(DiaDaSemana.SEGUNDA.value)  # 1
```

#### Comparacao:

```python
meu_dia = DiaDaSemana.SEXTA

if meu_dia == DiaDaSemana.SEXTA:
    print("É sexta-feira!")  # Será impresso
```

#### Iteracao:

```python
for dia in DiaDaSemana:
    print(f"{dia.name} tem o valor {dia.value}")
```

#### Buscar por valor:

```python
dia_por_valor = DiaDaSemana(3)
print(dia_por_valor)  # DiaDaSemana.QUARTA
```

#### Buscar por nome:

```python
dia_por_nome = DiaDaSemana["DOMINGO"]
print(dia_por_nome)  # DiaDaSemana.DOMINGO
```

## `auto()` para valores automaticos

Pode-se usar auto() para que o Python atribua valores sequenciais automaticamente:

```python
from enum import Enum, auto

class StatusPedido(Enum):
    PENDENTE = auto()
    PROCESSANDO = auto()
    ENVIADO = auto()
    ENTREGUE = auto()
    CANCELADO = auto()

print(StatusPedido.PENDENTE.value)     # 1
print(StatusPedido.PROCESSANDO.value)  # 2
```

##### Enums sao usadas para representar estados fixos(categorias, opcoes de menu, dias da semana). Evite usar valores magicos como `"ativo"` ou `1`, prefira usar `Status.ATIVO`.

# Entrada do Usuário com `input()`

A função embutida `input()` permite que o programa **receba dados digitados pelo usuário** no terminal.

---

## 📌 Características

- A função `input()` **sempre retorna uma `string`**, mesmo que o usuário digite um número.
- Você pode passar uma **mensagem (prompt)** como argumento.

### 🔠 Sintaxe:

```python
variavel = input("Seu prompt aqui: ")
```

#### Exemplo:

```python
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
```

### Conversao de Tipos

Como `input()` retorna uma string, e necessario converter para outros tipos se necessario:

```python
idade_str = input("Quantos anos você tem? ")
idade = int(idade_str)

print(f"Daqui a um ano, você terá {idade + 1} anos.")
```

ou:

```python
idade = int(input("Digite sua idade: "))
```

#### Exemplo com NUmeros Reais

```python
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

soma = primeiro_numero + segundo_numero
print(f"A soma é: {soma}")
```

# Declarações de Controle (Control Statements)

As declarações de controle permitem **alterar o fluxo de execução** do programa, baseando-se em condições ou decisões lógicas.

---

## 1. `if`, `elif`, `else` (Condicionais)

Essas estruturas controlam a execução de **blocos de código diferentes dependendo de condições booleanas**.

---

### Sintaxe Básica

```python
if condicao1:
    # Código executado se condicao1 for True
elif condicao2:
    # Código executado se condicao1 for False E condicao2 for True
else:
    # Código executado se nenhuma das condições anteriores for True
```

#### Exemplo:

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

temperatura = 28

if temperatura > 30:
    print("Está muito quente!")
elif temperatura > 20:
    print("Está agradável.")
else:
    print("Está frio.")

saldo = 1000
saque = 500

if saque <= saldo:
    if saque % 50 == 0:
        print("Saque realizado com sucesso.")
        saldo -= saque
    else:
        print("Valor do saque inválido. Apenas múltiplos de 50.")
else:
    print("Saldo insuficiente.")

print(f"Saldo atual: {saldo}")
```

# Listas

Listas são um dos tipos de coleção mais versáteis em Python. São **coleções ordenadas e mutáveis**, e podem conter elementos de diferentes tipos.

---

##  Criação de Listas

```python
minha_lista = [1, 2, 3, "quatro", True, 5.0]
lista_vazia = []
```

### Acessando Elementos (Indexacao)
```python
frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas[0])   # maçã
print(frutas[2])   # laranja
print(frutas[-1])  # uva (último elemento)
```

### Fatiamento (Slicing)
```python
numeros = [10, 20, 30, 40, 50, 60]
print(numeros[1:4])   # [20, 30, 40]
print(numeros[:3])    # [10, 20, 30]
print(numeros[3:])    # [40, 50, 60]
print(numeros[::2])   # [10, 30, 50]
```

### Mutabilidade
```python
minha_lista = ["um", "dois", "três"]
minha_lista[1] = "novo valor"
print(minha_lista)  # ['um', 'novo valor', 'três']

minha_lista[0:2] = ["a", "b", "c"]
print(minha_lista)  # ['a', 'b', 'c', 'três']
```

## Metodos Comuns de Lista
| Método             | Descrição                                 | Exemplo                   |
| ------------------ | ----------------------------------------- | ------------------------- |
| `append(item)`     | Adiciona item ao final                    | `lista.append(4)`         |
| `insert(i, item)`  | Insere item no índice `i`                 | `lista.insert(1, 'novo')` |
| `remove(item)`     | Remove a **primeira** ocorrência do item  | `lista.remove(2)`         |
| `pop(i)`           | Remove e retorna item (último por padrão) | `lista.pop()` ou `pop(1)` |
| `del lista[i]`     | Remove item ou fatia                      | `del lista[0:2]`          |
| `clear()`          | Limpa a lista                             | `lista.clear()`           |
| `index(item)`      | Retorna índice da primeira ocorrência     | `lista.index("a")`        |
| `count(item)`      | Conta ocorrências do item                 | `lista.count(3)`          |
| `sort()`           | Ordena no local                           | `lista.sort()`            |
| `reverse()`        | Inverte no local                          | `lista.reverse()`         |
| `copy()`           | Retorna uma cópia rasa                    | `lista.copy()`            |
| `extend(iterável)` | Adiciona elementos de outro iterável      | `lista.extend([4, 5])`    |

#### Exemplos de Metodos

```python
minha_lista = [1, 2, 3]

minha_lista.append(4)
minha_lista.insert(1, 99)
print(minha_lista)  # [1, 99, 2, 3, 4]

minha_lista.remove(2)
print(minha_lista)  # [1, 99, 3, 4]

removido = minha_lista.pop()
print(removido)     # 4
print(minha_lista)  # [1, 99, 3]
```

### Iterando sobre Listas
```python
alunos = ["Ana", "Beto", "Carlos"]

# Forma simples
for aluno in alunos:
    print(aluno)

# Com índice
for i in range(len(alunos)):
    print(f"Aluno {i}: {alunos[i]}")

# Com enumerate
for i, aluno in enumerate(alunos):
    print(f"Índice {i}: {aluno}")
```

## Ordenando Listas

`list.sort()` -- Ordenacao no local

Modeifica a lista original. Mais eficiente em termo de memoria
```python
numeros = [3, 1, 4, 1, 5, 9, 2]
numeros.sort()
print(numeros)  # [1, 1, 2, 3, 4, 5, 9]

letras = ['c', 'a', 'b']
letras.sort(reverse=True)
print(letras)  # ['c', 'b', 'a']
```

`sorted()`-- Cria um nova lista ordenada

Mantem a lista original inalterada
```python
numeros_originais = [3, 1, 4, 1, 5, 9, 2]
ordenada = sorted(numeros_originais)
print(numeros_originais)  # [3, 1, 4, 1, 5, 9, 2]
print(ordenada)           # [1, 1, 2, 3, 4, 5, 9]
```

##### Ordenando com `key`

Usa uma funcao de transformacao como base da ordenacao

```python
# Ordenar por segundo item da tupla
pares = [(1, 'b'), (3, 'a'), (2, 'c')]
pares_ordenados = sorted(pares, key=lambda x: x[1])
print(pares_ordenados)  # [(3, 'a'), (1, 'b'), (2, 'c')]

# Ordenar strings por comprimento
nomes = ["João", "Maria", "José", "Ana"]
ordenados = sorted(nomes, key=len)
print(ordenados)  # ['Ana', 'João', 'Maria', 'José']
```

# Tuplas

Tuplas são **coleções ordenadas e imutáveis**. Diferente das listas, **não podem ser modificadas** após a criação.

---

## Criação de Tuplas

```python
minha_tupla = (1, 2, 3, "quatro", False)
tupla_vazia = ()
tupla_um_elemento = (1,)  # A vírgula é obrigatória!
```

## Por que usar Tuplas?

**Imutabilidade:** Protege os dados de midificacoes acidentais.
**Desempenho:** Mais rapidas que listas em algumas operacoes.
**Chaves de Dicionarios:** Tuplas podem ser usadas como chaves(sao hashble)
**Retorno multiplo:** Funcoes frequentemente retornam tuplas com multiplos valores.

### Acessando Elementos e SLicing
```python
coordenadas = (10, 20, 30)
print(coordenadas[0])    # 10
print(coordenadas[1:])   # (20, 30)
```

### Imutabilidade

Tuplas **nao permitem** alteracoes apos a criacao:
```python
minha_tupla = (1, 2, 3)

# minha_tupla[0] = 99      # TypeError
# minha_tupla.append(4)    # AttributeError
```

## Metodos Comuns

| Método        | Descrição                                    | Exemplo            |
| ------------- | -------------------------------------------- | ------------------ |
| `count(item)` | Conta quantas vezes um item aparece na tupla | `tupla.count(2)`   |
| `index(item)` | Retorna o índice da **primeira** ocorrência  | `tupla.index("a")` |

### Empacotamento e Desempacotamento
Atribuicao de multiplos valores com facilidade:

```python
# Empacotamento
ponto = (3, 4)

# Desempacotamento
x, y = ponto
print(f"X: {x}, Y: {y}")  # X: 3, Y: 4
```

### Troca de Valores com Tuplas
```python
a = 10
b = 20

a, b = b, a
print(f"a: {a}, b: {b}")  # a: 20, b: 10
```

### Retorno multiplo com funcoes
Funcoes em python retornam tuplas com facilidade
```python
def obter_nome_idade():
    return "Maria", 30

nome, idade = obter_nome_idade()
print(f"{nome} tem {idade} anos.")  # Maria tem 30 anos.
```

# Dicionários (dict)

Dicionários são **coleções de pares chave-valor**, onde cada chave deve ser **única e imutável**. Extremamente úteis para organizar dados estruturados.

---

## Criação de Dicionários

```python
pessoa = {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "São Paulo"
}

dicionario_vazio = {}
```

### Acessando Valores
```python
print(pessoa["nome"])  # Carlos
# print(pessoa["telefone"])  # KeyError!
```

### Acesso Seguro com `get()`
```python
print(pessoa.get("idade"))        # 28
print(pessoa.get("telefone"))     # None
print(pessoa.get("endereco", "Não informado"))  # Não informado
```

### Adicionando ou Atualizando Dados
```python
pessoa["profissão"] = "Engenheiro"  # Novo par
pessoa["idade"] = 29               # Atualiza valor
```

### Removendo Elementos
```python
cadastro = {"id": 1, "nome": "João", "email": "joao@exemplo.com"}

del cadastro["email"]
nome_removido = cadastro.pop("nome")
cadastro.clear()  # Remove tudo

# Evita erro se chave não existir
cadastro.pop("telefone", "Chave não encontrada")
```

## Metodos Comuns de Dicionario

| Método            | Descrição                                                | Exemplo                  |
| ----------------- | -------------------------------------------------------- | ------------------------ |
| `dict.keys()`     | Retorna todas as chaves                                  | `produto.keys()`         |
| `dict.values()`   | Retorna todos os valores                                 | `produto.values()`       |
| `dict.items()`    | Retorna todos os pares (chave, valor)                    | `produto.items()`        |
| `dict.update()`   | Adiciona/atualiza pares a partir de outro dicionário     | `config.update(usuário)` |
| `dict.pop(chave)` | Remove e retorna o valor de uma chave                    | `dict.pop("nome")`       |
| `dict.popitem()`  | Remove e retorna o **último par inserido** (Python 3.7+) | `dict.popitem()`         |
| `dict.clear()`    | Remove todos os pares do dicionário                      | `dict.clear()`           |

### Exemplo de Uso
```python
produto = {
    "nome": "Teclado",
    "preço": 150.00,
    "estoque": 50
}

print(produto.keys())     # dict_keys(['nome', 'preço', 'estoque'])
print(produto.values())   # dict_values(['Teclado', 150.0, 50])
print(produto.items())    # dict_items([('nome', 'Teclado'), ('preço', 150.0), ('estoque', 50)])

# Iterando
for chave in produto:
    print(chave, produto[chave])

for chave, valor in produto.items():
    print(f"{chave}: {valor}")
```

### Usando `update()`
```python
config_padrao = {"tema": "escuro", "fonte": "Arial"}
config_usuario = {"fonte": "Verdana", "idioma": "pt-br"}

config_padrao.update(config_usuario)
print(config_padrao)
# {'tema': 'escuro', 'fonte': 'Verdana', 'idioma': 'pt-br'}
```

# Dicionários

Dicionários são coleções **não ordenadas** (em Python 3.7+ eles **mantêm a ordem de inserção**) de pares **chave-valor**.  
Cada chave deve ser **única e imutável** (strings, números, tuplas são válidos; listas **não podem** ser chaves).

São extremamente úteis para mapear dados, como em um dicionário do mundo real, onde você busca a definição por uma palavra.

---

## Criação de Dicionários

Delimitados por chaves `{}`, com pares `chave: valor` separados por dois-pontos e pares separados por vírgulas:

```python
pessoa = {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "São Paulo"
}

dicionario_vazio = {}
```

#### Acessando Valores

Use a chave entre colchetes. Se a chave nao existir, resulta em `KeyError`

```python
print(pessoa["nome"])   # Carlos
# print(pessoa["telefone"])  # KeyError: 'telefone'
```

### Acesso com `get()`

Use `get()` para acessar valores de forma segura. Retorna `None` se a chave nao existir ou um valor padrao, se especificado:

```python
print(pessoa.get("idade"))                # 28
print(pessoa.get("telefone"))             # None
print(pessoa.get("endereco", "Não informado")) # Não informado
```

### Adicionando/Modificando Elementos

Atribua um valor a uma chave. Se ela existir, o valor sera atualizado; senao, sera criada:

```python
pessoa["profissão"] = "Engenheiro"  # Adiciona nova chave-valor
pessoa["idade"] = 29                # Modifica valor existente
print(pessoa)
```

### Removendo Elementos

- `del dict[chave]`: remove a chave; resulta em erro se a chave nao existir
- `pop(chave)`: remove e retorna valor; resulta em erro se nao existir (pode usar valor padrao)
- `popitem()`: remove e retorna um par qualquer
- `clear()`: remove todos os itens

 ```python
cadastro = {"id": 1, "nome": "João", "email": "joao@exemplo.com"}

del cadastro["email"]
print(cadastro)  # {'id': 1, 'nome': 'João'}

nome_removido = cadastro.pop("nome")
print(cadastro)        # {'id': 1}
print(nome_removido)   # João

# cadastro.pop("telefone", "Chave não encontrada")  # Evita erro
```

## Metodos Comuns de Dicionarios
| Método          | Descrição                                          | Exemplo               |
| --------------- | -------------------------------------------------- | --------------------- |
| `keys()`        | Retorna uma view com todas as chaves               | `dict.keys()`         |
| `values()`      | Retorna uma view com todos os valores              | `dict.values()`       |
| `items()`       | Retorna uma view com todos os pares (chave, valor) | `dict.items()`        |
| `update(dict2)` | Adiciona/atualiza pares de outro dicionário        | `dict1.update(dict2)` |

### Exemplo:
```python
produto = {
    "nome": "Teclado",
    "preço": 150.00,
    "estoque": 50
}

print(produto.keys())    # dict_keys(['nome', 'preço', 'estoque'])
print(produto.values())  # dict_values(['Teclado', 150.0, 50])
print(produto.items())   # dict_items([('nome', 'Teclado'), ('preço', 150.0), ('estoque', 50)])

# Iterando sobre dicionários
for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f"{chave}: {valor}")
```

### Usando `update()`
```python
config_padrao = {"tema": "escuro", "fonte": "Arial"}
config_usuario = {"fonte": "Verdana", "idioma": "pt-br"}

config_padrao.update(config_usuario)
print(config_padrao)
# Saída: {'tema': 'escuro', 'fonte': 'Verdana', 'idioma': 'pt-br'}
```

# Sets (Conjuntos)

Sets são **coleções não ordenadas de itens únicos**.  
São úteis quando você deseja **evitar duplicatas** e **não se importa com a ordem dos elementos**.

---

## Criação de Sets

Sets são delimitados por `{}`.  
**Atenção**: `{}` vazio cria um **dicionário**. Para criar um **set vazio**, use `set()`.

```python
meu_set = {1, 2, 3, 2, 1}  # Duplicatas são ignoradas
print(meu_set)  # {1, 2, 3}

set_vazio = set()
print(type(set_vazio))  # <class 'set'>

letras = set("abracadabra")
print(letras)  # {'a', 'b', 'r', 'c', 'd'}
```

### Principais Usos
- Remover Duplicatas de Listas
- Operacoes de conjuntos(uniao, intersecao, diferenca)
- Verificacao rapida de existencia

### Adicionando e Removendo Elementos
| Método          | Descrição                                     |
| --------------- | --------------------------------------------- |
| `add(item)`     | Adiciona um item. Ignorado se já existir.     |
| `remove(item)`  | Remove item. Lança `KeyError` se não existir. |
| `discard(item)` | Remove item. Não lança erro se não existir.   |
| `pop()`         | Remove e retorna um item arbitrário.          |
| `clear()`       | Remove todos os itens do set.                 |

```python
cores = {"vermelho", "azul"}

cores.add("verde")
print(cores)  # {'vermelho', 'azul', 'verde'}

cores.add("vermelho")  # Já existe, nada muda
print(cores)

cores.remove("azul")
print(cores)  # {'vermelho', 'verde'}

cores.discard("amarelo")  # Nada acontece
print(cores)
```

### Operacoes de Conjuntos
| Operação            | Operador | Método                            | Descrição                                              |                            |
| ------------------- | -------- | --------------------------------- | ------------------------------------------------------ | -------------------------- |
| União               | \`       | \`                                | `set1.union(set2)`                                     | Elementos de ambos os sets |
| Interseção          | `&`      | `set1.intersection(set2)`         | Elementos comuns                                       |                            |
| Diferença (A - B)   | `-`      | `set1.difference(set2)`           | Elementos em A, mas não em B                           |                            |
| Diferença Simétrica | `^`      | `set1.symmetric_difference(set2)` | Elementos em um ou outro, mas não em ambos             |                            |
| Subconjunto         | `<=`     | `set1.issubset(set2)`             | Verifica se `set1` está contido em `set2`              |                            |
| Superconjunto       | `>=`     | `set1.issuperset(set2)`           | Verifica se `set1` contém todos os elementos de `set2` |                            |

#### Exmeplos de Operacoes com Conjuntos
```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a | set_b)        # União: {1, 2, 3, 4, 5, 6}
print(set_a.union(set_b))   # Mesmo resultado

print(set_a & set_b)        # Interseção: {3, 4}
print(set_a.intersection(set_b))

print(set_a - set_b)        # Diferença (A - B): {1, 2}
print(set_a.difference(set_b))

print(set_a ^ set_b)        # Diferença simétrica: {1, 2, 5, 6}
print(set_a.symmetric_difference(set_b))

set_c = {1, 2}
print(set_c <= set_a)  # True — set_c é subconjunto de set_a
print(set_a >= set_c)  # True — set_a é superconjunto de set_c
```

# Funções

Funções são **blocos de código reutilizáveis** que realizam uma tarefa específica.  
Promovem **modularidade**, **organização** e **reutilização** do código.

---

##  Definindo uma Função

Utilize a palavra-chave `def`, seguida pelo nome da função, parênteses `()` e dois-pontos `:`.  
O corpo da função deve ser indentado.

```python
def saudacao():
    """Esta função imprime uma saudação simples."""
    print("Olá! Bem-vindo(a) ao Python.")

# Chamando a função
saudacao()
```

### Parametros e Argumentos
- Parametros: variaveis na definicao da funcao
- Argumentos: valores passados na chamada da funcao

```python
def cumprimentar(nome, idade):
  print(f"Ola, {nome}! Voce tem {idade} anos")

cumprimentar("Alice", 22)
cumprimentar(idade=22, nome="Bob") #argumentos nomeados
```

### Valores de Retorno(return)
Usa-se `return` para retornar um valor. Sem ele, o valor padrao retornado eh `None`

```python
def somar(a, b):
    resultado = a + b
    return resultado

soma_total = somar(10, 5)
print(f"A soma é: {soma_total}")

def eh_par(numero):
    return numero % 2 == 0

print(eh_par(4))  # True
print(eh_par(7))  # False
````

### Argumentos Padrao (Default Arguments)
Permitem valores padrao se nehum argumento for passado

```python
def saudacao_personalizada(nome="Visitante", mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao_personalizada()                    # Olá, Visitante!
saudacao_personalizada("Pedro")            # Olá, Pedro!
saudacao_personalizada("Ana", "E aí")      # E aí, Ana!

# Parametros com valores padrao devem vir apos os parametros sem valor padrao

# def minha_funcao(arg1="default", arg2):  # ❌ Erro
def minha_funcao(arg1, arg2="default"):    # ✅ Correto
    pass
````

### Argumentos de Comprimento Variavel

`*args`- Argumentos Posicioanis Variaveis
````python
def somar_tudo(*numeros):
    total = sum(numeros)
    return total

print(somar_tudo(1, 2, 3))        # 6
print(somar_tudo(10, 20, 30, 40)) # 100
````

`**kwargs`- Argumentos Nomeados Variaveis
````python
def exibir_info(**info):
    for chave, valor in info.items():
        print(f"{chave.capitalize()}: {valor}")

exibir_info(nome="Fernanda", idade=28, cidade="Rio")
````

Combinando `*args` e `**kwargs`
````python
def funcao_mista(param1, *args, **kwargs):
    print(f"Param1: {param1}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

funcao_mista(10, 20, 30, a=1, b=2)
````

## Escopo de Variaveis

### - Escopo Local
````python
def minha_funcao():
    x = 10  # Local
    print(x)

minha_funcao()
# print(x)  # ❌ NameError
````

### - Escopo Global
````python
y = 20  # Global

def outra_funcao():
    print(y)

outra_funcao()
print(y)
````

### - Usando `global`
````python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1
````
## Funcoes Aninhadas
Funcoes definidas dentro de outras funcoes. Acessam variaveis da funcao externa.

````python
def funcao_externa(mensagem_base):
    complemento = " (interna)"

    def funcao_interna(nome):
        print(f"{mensagem_base}, {nome}{complemento}")

    return funcao_interna

saudacao = funcao_externa("Bem-vindo")
saudacao("João")  # Bem-vindo, João (interna)
saudacao("Maria") # Bem-vindo, Maria (interna)
````

## CLosures
Closures "lembram" do ambiente onde foram criadas:

````python
def criar_multiplicador(fator):
    def multiplicador(numero):
        return numero * fator
    return multiplicador

dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(dobrar(5))     # 10
print(triplicar(5))  # 15
````
Closures sao uteis para ocnfigurar funcoes dinamicamente e implementar *decoradores*

# Objetos

Em Python, **tudo é um objeto**.  
Isso inclui **números, strings, listas, funções, classes e até módulos**.  
Essa natureza orientada a objetos é uma das características mais poderosas da linguagem.

---

## O que é um Objeto?

Um **objeto** é uma **instância de uma classe** e possui:

- **Identidade**: Endereço único na memória (verificado com `id()`).
- **Tipo**: A classe à qual pertence (verificado com `type()`).
- **Estado**: Os dados (atributos) que ele armazena.
- **Comportamento**: As ações (métodos) que ele pode executar.

```python
numero = 10
print(id(numero))      # Identidade
print(type(numero))    # <class 'int'>

lista = [1, 2, 3]
print(id(lista))
print(type(lista))

outra_lista = lista
print(id(outra_lista))  # Mesmo ID da lista original

outra_lista.append(4)
print(lista)            # [1, 2, 3, 4] — o objeto original foi alterado
````

### Atributos e Metodos
- **Atributos:** VAriaveis associadas a um objeto (estado).
- **Metodos:** Funcoes associadas a um objeto (comporttamento).

````python
s = "Python"

print(s.upper())      # PYTHON — método: transforma em maiúsculas
print(s.count('o'))   # 1 — método: conta ocorrências de 'o'

# Strings também possuem atributos internos
# print(s.__len__)    # atributo que referencia o método len()
````

#### Sintaxe de acesso:
- `obejto.atributo`
- `objeto.metodo()`

## Programacao Orientada a Objetos (OOP)
A natureza orientada a objetos permite:
  - Modelar entidades do mundo real
  - Criar codigo modular, reutilizavel e organizado.
  - Trabalhar com classes e instancias (objetos).

# Loops

Loops são estruturas de controle que **permitem repetir blocos de código** diversas vezes.  
Python oferece dois tipos principais de laços: `for` e `while`.

---

## `for` Loop

Usado para **iterar sobre sequências** (`listas`, `tuplas`, `strings`, `dicionários`, `sets`) e objetos iteráveis.

### Sintaxe

```python
for variavel in iteravel:
    # código a ser executado
````

#### Exemplos
````python
# Lista
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# String
nome = "Python"
for letra in nome:
    print(letra)

# Tupla
numeros = (1, 2, 3)
for num in numeros:
    print(num)

# Dicionário (chaves)
aluno = {"nome": "Maria", "idade": 20}
for chave in aluno:
    print(chave)

# Dicionário (chave e valor)
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
````

#### Usando `range()`
````python
# range(stop)
for i in range(5):        # 0 a 4
    print(i)

# range(start, stop)
for i in range(1, 6):     # 1 a 5
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)
````

### `while` Loop
Executa o bloco **enquanto uma condicao for verdadeira**

### Sintaxe
````python
while condicao:
    # código a ser executado
````

#### Exemplo
````python
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Interação com o usuário
resposta = ""
while resposta != "sair":
    resposta = input("Digite 'sair' para encerrar: ").lower()
    if resposta != "sair":
        print("Você não digitou 'sair'.")

# CUIDADO: Loop infinito
# while True:
#     print("Loop infinito! Pressione Ctrl+C para parar.")
````

### `break` e `continue`
Controlam o fluxo de execucao dentro dos loops.

#### `break`: Interrompe o loop
````python
for i in range(10):
    if i == 5:
        print("Número 5 encontrado, saindo do loop.")
        break
    print(i)
# Saída: 0, 1, 2, 3, 4
````

#### `continue`: Pula para a proxima iteracao
````python
for i in range(5):
    if i == 2:
        print("Pulando o número 2.")
        continue
    print(i)
# Saída: 0, 1, 3, 4
````
