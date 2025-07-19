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
# 🧱 Classes (Programação Orientada a Objetos - POO)

Classes são os pilares da Programação Orientada a Objetos (POO) em Python.  
Elas servem como **modelos** para criar objetos (instâncias), encapsulando dados (*atributos*) e comportamentos (*métodos*).

---

## 🔑 Conceitos-Chave da POO

| Conceito        | Descrição |
|----------------|-----------|
| **Classe**     | Modelo ou blueprint para criar objetos. |
| **Objeto**     | Instância concreta de uma classe. |
| **Atributo**   | Dado associado ao objeto ou classe. |
| **Método**     | Função associada a um objeto ou classe. |
| **`self`**     | Referência à instância atual (equivalente ao `this` em Java). |
| **`__init__`** | Método construtor, executado ao criar um novo objeto. |

---

## 🧱 Definindo uma Classe

```python
class Carro:
    rodas = 4  # Atributo de classe

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print(f"O {self.marca} {self.modelo} está ligado.")

    def exibir_detalhes(self):
        pr
````

### INstanciando Objetos
````python
meu_carro = Carro("Toyota", "Corolla", 2020)
carro_amigo = Carro("Honda", "Civic", 2022)

meu_carro.ligar()
carro_amigo.exibir_detalhes()
print(Carro.rodas)
````

## Herança
Permite que uma classe herde atributos e metodos de outra

````python
class Veiculo:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor

    def descrever(self):
        print(f"Este é um veículo {self.tipo} da cor {self.cor}.")

class Moto(Veiculo):
    def __init__(self, cor, cilindrada):
        super().__init__("moto", cor)
        self.cilindrada = cilindrada

    def empinar(self):
        print(f"A moto {self.cor} de {self.cilindrada}cc está empinando!")

    def descrever(self):  # Sobrescrevendo
        print(f"Esta é uma Moto da cor {self.cor} com {self.cilindrada}cc.")

minha_moto = Moto("Preta", 600)
minha_moto.descrever()
minha_moto.empinar()
````

## Polimorfismo
Capacidade de objetos de diferentes classes responderem de maneiras diferentes ao mesmo metodo, mantendo uma interface comum.

## Encapsulamento
Agrupa dados e comportamentos em um unica unidade, controlando o acesso externo.

````python
class MinhaClasse:
    def __init__(self):
        self.publico = "acessível"
        self._protegido = "uso interno sugerido"
        self.__privado = "oculto externamente"

obj = MinhaClasse()
print(obj.publico)
print(obj._protegido)
print(obj._MinhaClasse__privado)  # Name mangling
````

## Metodos Especiais

### `@classmethod`
Metodo que opera sobre a classe em vez da instancia.

````python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def de_ano_nascimento(cls, nome, ano):
        idade = 2025 - ano
        return cls(nome, idade)

p = Pessoa.de_ano_nascimento("Ana", 2000)
print(f"{p.nome} tem {p.idade} anos.")
````

### `@staticmethod`
Meodo independente da instancia ou classe. Funciona como uma funcao comum, mas agrupada na classe.

````python
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def eh_par(n):
        return n % 2 == 0

print(Matematica.somar(5, 3))
print(Matematica.eh_par(4))
````
# 📦 Módulos em Python

Módulos são arquivos `.py` que contêm código reutilizável como funções, classes e variáveis.  
Eles ajudam a organizar e reaproveitar o código, mantendo-o limpo e modular.

---

## 🎯 Por que usar Módulos?

- 🔁 **Reusabilidade**: Escreva uma vez, use várias vezes.
- 📂 **Organização**: Quebra programas grandes em partes menores.
- 🧠 **Namespace isolado**: Evita conflitos entre nomes de funções ou variáveis.

---

## ✏️ Criando um Módulo

Crie um arquivo chamado `calculadora.py`:

```python
# calculadora.py

PI = 3.14159

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

class Calculadora:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial

    def adicionar(self, num):
        self.valor += num

    def obter_valor(self):
        return self.valor

print("Módulo calculadora carregado.")  # Executado na importação
````

### Importando Modulos
`import modulo_nome`
````python
import calculadora

print(calculadora.somar(5, 3))       # 8
print(calculadora.PI)                # 3.14159
minha_calc = calculadora.Calculadora(10)
minha_calc.adicionar(5)
print(minha_calc.obter_valor())      # 15
````

`import modulo_nome as alias`
````python
import calculadora as calc

print(calc.multiplicar(4, 2))        # 8
````

`from modulo_nome import elemento1, elemento2`
````python
from calculadora import dividir, Calculadora

print(dividir(10, 2))                # 5.0
outra_calc = Calculadora()
````

### Pacotes 
Pacotes sao diretorios contendo modulos. Um pacote precisa de um arquivo `__init__.py` para ser reconhecido como tal.

````markdown
meu_projeto/
├── main.py
└── utilidades/
    ├── __init__.py
    ├── string_utils.py
    └── math_utils.py
````
## Biblioteca Padrao do Python
| Biblioteca       | Categoria               | Funcionalidade Principal                                                            |
| ---------------- | ----------------------- | ----------------------------------------------------------------------------------- |
| `math`           | Matemática              | Operações matemáticas básicas (sqrt, ceil, floor, etc).                             |
| `random`         | Aleatoriedade           | Geração de números aleatórios, escolha aleatória de elementos.                      |
| `datetime`       | Data e Hora             | Manipulação de datas, horas, tempo e cronogramas.                                   |
| `os`             | Sistema Operacional     | Interação com o sistema de arquivos e variáveis de ambiente.                        |
| `sys`            | Sistema                 | Acesso a parâmetros e funções do interpretador Python.                              |
| `re`             | Expressões Regulares    | Busca, substituição e análise de strings com padrões regulares.                     |
| `json`           | Formato de Dados        | Leitura e escrita de dados no formato JSON.                                         |
| `csv`            | Arquivos CSV            | Leitura e escrita de arquivos CSV (Comma-Separated Values).                         |
| `shutil`         | Sistema de Arquivos     | Cópia, movimentação e remoção de arquivos e diretórios.                             |
| `subprocess`     | Execução de Comandos    | Executar comandos e processos do sistema operacional.                               |
| `collections`    | Estruturas de Dados     | Tipos de dados adicionais como `deque`, `Counter`, `defaultdict`.                   |
| `itertools`      | Iteradores              | Ferramentas para criar iteradores eficientes.                                       |
| `functools`      | Funções de Alta Ordem   | Funções como `reduce`, `lru_cache`, `partial`.                                      |
| `operator`       | Operadores Funcionais   | Permite usar operadores como funções (`add`, `itemgetter`, etc).                    |
| `typing`         | Tipagem Estática        | Especificar tipos de variáveis e funções (Python 3.5+).                             |
| `time`           | Tempo                   | Pausar a execução, obter tempo atual, medir duração.                                |
| `statistics`     | Estatística Básica      | Média, mediana, desvio padrão, variância, etc.                                      |
| `decimal`        | Precisão Numérica       | Cálculos com números decimais com precisão exata.                                   |
| `fractions`      | Números Racionais       | Trabalhar com frações em vez de floats.                                             |
| `hashlib`        | Criptografia            | Geração de hashes (MD5, SHA1, SHA256).                                              |
| `uuid`           | Identificadores Únicos  | Gerar UUIDs (identificadores únicos universais).                                    |
| `tkinter`        | Interface Gráfica (GUI) | Criar interfaces gráficas (botões, janelas, menus).                                 |
| `unittest`       | Testes                  | Testes automatizados (TDD) com casos de teste estruturados.                         |
| `argparse`       | Linha de Comando        | Parser para argumentos passados via terminal.                                       |
| `logging`        | Logs                    | Gerenciamento e registro de logs do programa.                                       |
| `sqlite3`        | Banco de Dados Embutido | Conectar e operar bancos SQLite.                                                    |
| `requests`       | Web / HTTP              | Enviar requisições HTTP (GET, POST, etc).                                           |
| `beautifulsoup4` | Web Scraping            | Extração e parsing de dados HTML e XML.                                             |
| `pandas`         | Dados Tabulares         | Estrutura de dados (DataFrame), análise e manipulação de dados.                     |
| `numpy`          | Computação Numérica     | Vetores, arrays multidimensionais, operações vetoriais eficientes.                  |
| `matplotlib`     | Visualização de Dados   | Criação de gráficos e visualizações em 2D.                                          |
| `seaborn`        | Visualização Avançada   | Gráficos estatísticos com estilo baseado em `matplotlib` e integração com `pandas`. |
| `scikit-learn`   | Machine Learning        | Modelos preditivos, regressão, classificação, clustering, etc.                      |
| `tensorflow`     | Deep Learning           | Redes neurais, aprendizado profundo e modelos treináveis.                           |
| `keras`          | Deep Learning           | Interface de alto nível para redes neurais (geralmente sobre o TensorFlow).         |
| `flask`          | Web Framework           | Microframework para APIs e aplicativos web leves.                                   |
| `django`         | Web Framework           | Framework completo para desenvolvimento web escalável.                              |
| `fastapi`        | Web / API Moderno       | Criação de APIs rápidas e modernas com tipagem e validação.                         |
| `pytest`         | Testes                  | Framework de testes avançado, simples de usar.                                      |
| `openpyxl`       | Excel                   | Leitura e escrita de arquivos `.xlsx` (Excel moderno).                              |
| `pyautogui`      | Automação de Interface  | Controle do mouse, teclado e automação da tela.                                     |
| `pygame`         | Jogos                   | Desenvolvimento de jogos 2D e multimídia interativa.                                |


# Funcoes Lambda 
Funcoes `lambda` são **funções anônimas** e **concisas**, ideais para tarefas rápidas. ELas são frequentemente usadas com funções como `map()`, `filter()` e `sorted()`.

````python
lambda argumentos: expressao
````

## Caracteristicas
| Característica      | Descrição                                                    |
| ------------------- | ------------------------------------------------------------ |
| **Anônimas**        | Não têm nome definido com `def`                              |
| **Concisas**        | Escritas em uma única linha                                  |
| **Expressão Única** | Contêm apenas uma expressão (sem múltiplas instruções)       |
| **Uso comum**       | Em funções como `map()`, `filter()`, `sorted()`, `key=` etc. |

### Exemplos de Uso:
````python
# Lambda simples para somar
somar = lambda a, b: a + b
print(somar(2, 3))  # Saída: 5

# Verificação de numero par
eh_par = lambda x: x % 2 == 0
print(eh_par(4))  # True
print(eh_par(5))  # False

# Lambda com sorted()
estudantes = [("Alice", 20), ("Bob", 25), ("Carlos", 18)]
estudantes_ordenados = sorted(estudantes, key=lambda estudante: estudante[1])
print(estudantes_ordenados)
# Saída: [('Carlos', 18), ('Alice', 20), ('Bob', 25)]

# Lambda com filter()
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Lambda com map()
quadrados = list(map(lambda x: x * x, numeros))
print(quadrados)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
````

## Quando Usar x Não Usar
| Situação                                                      | Recomendação    |
| ------------------------------------------------------------- | --------------- |
| Função curta de uma linha                                     | ✅ Use `lambda`  |
| Usada como argumento em `map()`, `filter()`, `sorted()`, etc. | ✅ Use `lambda`  |
| Funções complexas com múltiplas instruções                    | ❌ Prefira `def` |
| Precisa de docstring ou tipagem explícita                     | ❌ Prefira `def` |
| Código precisa ser mais legível e mantido por terceiros       | ❌ Prefira `def` |

# `map()`, `filter()` e `reduce()`
Estas são funções de ordem superior (Higher-Order Functions), fundamentais na programação funcional em Python. Elas recebem outras funções como argumentos e operam sobre coleções iteráveis.

## `map()`
Aplica uma funcao a cada elemento de um iteravel(como uma lista)

### Sintaxe:
````python
map(funcao, iteravel
````

#### Exemplo:
````python
numeros = [1, 2, 3, 4, 5]

def dobro(x):
    return x * 2

dobros = list(map(dobro, numeros))
print(dobros)  # [2, 4, 6, 8, 10]

triplos = list(map(lambda x: x * 3, numeros))
print(triplos)  # [3, 6, 9, 12, 15]

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
somas = list(map(lambda x, y: x + y, lista1, lista2))
print(somas)  # [5, 7, 9]
````

## `filter()`
Filtra os elementos de um iteravel, mantendo apenas os que satisfazem uma condicao (funcao retorna `True`).

### Sintaxe:
````python
filter(funcao, iteravel)
````

#### Exemplo:
````python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def eh_par(x):
    return x % 2 == 0

pares = list(filter(eh_par, numeros))
print(pares)  # [2, 4, 6, 8, 10]

palavras = ["maçã", "abacaxi", "banana", "amora"]
comeca_com_a = list(filter(lambda palavra: palavra.startswith('a'), palavras))
print(comeca_com_a)  # ['abacaxi', 'amora']
````

## `reduce()`
Aplica uma funcao acumulativamente aos elementos de um iteravel, reduzindo-o a um unico valor.

### Sintaxe:
````python
from functools import reduce
reduce(funcao, iteravel, [valor_inicial])
````

#### Exemplo:
````python
from functools import reduce

numeros = [1, 2, 3, 4, 5]

soma_total = reduce(lambda x, y: x + y, numeros)
print(soma_total)  # 15

produto_total = reduce(lambda x, y: x * y, numeros)
print(produto_total)  # 120

maior_numero = reduce(lambda x, y: x if x > y else y, numeros)
print(maior_numero)  # 5
````

## Comparativo:
| Tarefa               | Melhor escolha          | Exemplo rápido                     |
| -------------------- | ----------------------- | ---------------------------------- |
| Transformar dados    | `map()` ou list comp    | `[x * 2 for x in lista]`           |
| Filtrar elementos    | `filter()` ou list comp | `[x for x in lista if x % 2 == 0]` |
| Acumular valor único | `reduce()`              | `reduce(lambda x,y: x+y, lista)`   |

### Quando Usar?
- Usar `map()` e `filter()` se voce ja tem funcoes reutilizaveis.
- Usar `reduce()` para agregacoes(como soma, produto, maximo, concatenacao).
- Usar list comprehensions para operacoes simples

# Recursao
**Recursao** é uma tecnica inde uma função chama a si mesma para resolver subproblemas menores do mesmo problema original.

## Estrutura de uma função Recursiva
Toda funcção recursiva deve conter:
| Conceito              | Descrição                                                                  |
| --------------------- | -------------------------------------------------------------------------- |
| **Caso Base**         | Condição de parada. Quando satisfeita, a função retorna sem se autochamar. |
| **Chamada Recursiva** | A função chama a si mesma com um valor menor que se aproxima do caso base. |

### Quando Usar Recursão 
- Quando o problema pode ser dividido em subproblemas menores.
- Para escrever soluções mais elegantes e consisas.
- Exemplos clássiscos: fatorial, fibonacci, percorrer arvore, pesquisa binária

#### Cuidado ao usar a recursão:
| Problema           | Descrição                                                             |
| ------------------ | --------------------------------------------------------------------- |
| **Stack Overflow** | Cada chamada ocupa a pilha. Pode estourar o limite (\~1000 chamadas). |
| **Desempenho**     | Algumas soluções recursivas são menos eficientes que iterativas.      |

#### Exemplos:
````python
def fatorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:  # Chamada recursiva
        return n * fatorial(n - 1)

print(fatorial(5))  # 120
print(fatorial(0))  # 1

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(2))  # 1
print(fibonacci(6))  # 8 (0,1,1,2,3,5,8)


def soma_lista_recursiva(lista):
    if not lista:  # Caso base: lista vazia
        return 0
    else:  # Chamada recursiva: remove o primeiro elemento
        return lista[0] + soma_lista_recursiva(lista[1:])

print(soma_lista_recursiva([1, 2, 3, 4, 5]))  # 15
print(soma_lista_recursiva([]))              # 0
````

### Resumo:
| Critério       | Recursão                     | Iteração                  |
| -------------- | ---------------------------- | ------------------------- |
| Clareza        | Mais clara em alguns casos   | Mais verbosa              |
| Performance    | Pode ser mais lenta          | Geralmente mais eficiente |
| Uso de memória | Usa pilha de chamadas        | Usa variáveis locais      |
| Exemplo típico | Fatorial, Fibonacci, árvores | Loops tradicionais        |


# Decoradores

Decoradores são uma característica poderosa de Python que permitem modificar o comportamento de funções ou métodos de classe **sem alterar seu código original**.  
Eles são essencialmente funções que **recebem outra função como argumento**, adicionam alguma funcionalidade e retornam uma nova função (ou modificam a existente).

## Usos comuns de decoradores:

- Logging (registro de informações)
- Medição de tempo de execução
- Cache
- Validação de permissões/autenticação
- Alterar o comportamento de funções antes ou depois da execução

---

## 📌 Sintaxe Básica

```python
@decorador
def minha_funcao():
    pass
````
Isso é equivalente a:
````python
minha_funcao = decorador(minha_funcao)
````

### Criando um Decorador 
````python
def meu_primeiro_decorador(func):
    def wrapper():
        print("Antes da função ser chamada.")
        func()
        print("Depois da função ser chamada.")
    return wrapper

@meu_primeiro_decorador
def saudacao():
    print("Olá, mundo!")

saudacao()
````

### Decoradores com Argumentos
````python
def medir_tempo(func):
    import time
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"A função '{func.__name__}' levou {fim - inicio:.4f} segundos para executar.")
        return resultado
    return wrapper

@medir_tempo
def calcular_soma_grande(n):
    total = 0
    for i in range(n):
        total += i
    return total

@medir_tempo
def saudacao_personalizada(nome):
    import time
    time.sleep(0.5)
    print(f"Olá, {nome}!")

print(calcular_soma_grande(1000000))
saudacao_personalizada("Alice")
````

### Preservando Metadados com `functools.wraps`
Ao usar decoradores, a função original pode perder seus metadados como `__name__` e `__doc__`. Para evitar isso, use `@functools.wraps`;

````python
import functools

def meu_decorador_melhorado(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__}...")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} concluída.")
        return resultado
    return wrapper

@meu_decorador_melhorado
def somar_numeros(a, b):
    """Soma dois números."""
    return a + b

print(somar_numeros(10, 20))
print(somar_numeros.__name__)  # 'somar_numeros'
print(somar_numeros.__doc__)   # 'Soma dois números.'
````

### Decoradores com Argumentos Proprios
````python
def repetir_n_vezes(n):
    def decorador_real(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador_real

@repetir_n_vezes(3)
def gritar(mensagem):
    print(mensagem.upper() + "!!!")

gritar("socorro")
````

# Exceções (Tratamento de Erros)

Exceções são eventos que ocorrem durante a execução de um programa e que interrompem o fluxo normal das instruções.  
Quando um erro acontece, uma **exceção é levantada (raised)**. Se não for tratada, o programa para e exibe um **traceback**.

---

## Tipos Comuns de Exceções

| Exceção              | Descrição                                                  |
|----------------------|------------------------------------------------------------|
| `NameError`          | Variável não definida.                                     |
| `TypeError`          | Operação com tipo incorreto.                               |
| `ValueError`         | Tipo correto, mas valor inválido.                          |
| `ZeroDivisionError`  | Divisão por zero.                                          |
| `FileNotFoundError`  | Arquivo não encontrado ao tentar abrir.                    |
| `IndexError`         | Índice inválido em listas ou outras sequências.            |
| `KeyError`           | Chave inexistente em um dicionário.                        |

---

## Blocos de Tratamento: `try`, `except`, `else`, `finally`

### Sintaxe:

```python
try:
    # Código que pode gerar uma exceção
except TipoDeExcecao:
    # Tratamento da exceção
except OutroTipoDeExcecao as e:
    # A variável 'e' contém detalhes do erro
except:
    # Captura qualquer exceção (uso genérico, com cautela)
else:
    # Executado se NENHUMA exceção ocorrer
finally:
    # Sempre executado (ideal para limpeza de recursos)
````

### Exemplos:
````python
#Divisao por zero
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")

print("Programa continua...")

#Multiplos `except`
try:
    numero = int(input("Digite um número: "))
    divisor = int(input("Digite um divisor: "))
    resultado = numero / divisor
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.")
except ZeroDivisionError:
    print("Erro: O divisor não pode ser zero.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
else:
    print(f"O resultado da divisão é: {resultado}")
finally:
    print("Fim da tentativa de divisão.")

#else e finally
def abrir_arquivo(nome_arquivo):
    try:
        f = open(nome_arquivo, 'r')
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    else:
        conteudo = f.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
    finally:
        if 'f' in locals() and not f.closed:
            f.close()
            print("Arquivo fechado.")

# Teste com arquivos:
# abrir_arquivo("exemplo.txt")
# abrir_arquivo("arquivo_inexistente.txt")
````

### Levantando excecoes com `raise`
É possivel forçar a ocorrencia de erros personalizados
````python
def validar_idade(idade):
    if not isinstance(idade, int):
        raise TypeError("A idade deve ser um número inteiro.")
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")
    print(f"Idade válida: {idade}")

try:
    validar_idade(-5)
except ValueError as e:
    print(f"Erro de validação: {e}")

try:
    validar_idade("vinte")
except TypeError as e:
    print(f"Erro de tipo: {e}")
````

# Gerenciadores de Contexto (`with`)

A declaração `with` é usada para gerenciar recursos externos (como arquivos, conexões de banco de dados, locks) de forma **segura e eficiente**.  
Ela garante que o recurso será **corretamente inicializado e limpo** (fechado/liberado), mesmo que ocorra um erro durante seu uso.

---

## O Problema que `with` Resolve

### Sem `with`: Risco de esquecer de fechar

```python
f = open("meu_arquivo.txt", "w")
try:
    f.write("Olá, mundo!")
    # Se ocorrer um erro aqui, f.close() pode nunca ser chamado!
except Exception as e:
    print(f"Erro: {e}")
finally:
    f.close()
````

### Com `with`: Seguro e conciso

````python
with open("meu_arquivo.txt", "w") as f:
    f.write("Olá, com with!")
# f é fechado automaticamente, mesmo se um erro ocorrer

print("Arquivo gravado e fechado automaticamente.")

#Leitura do arquivo
with open("meu_arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)
````

## Como o `with` funciona:
Um **gerenciador de contexto** é um onjeto que implementa os metodos especiais:
 - `__enter__(self)`: Chamado no inicio do bloco `with`. O valor retornado é atribuido a variavel apos `as`
 - `__exit__(self, exc_type, exc_val, exc_tb)`: Chamado ao sair do bloco, **mesmo se ocorrer uma excecao**.

### Criando seus proprios context managers

````python
class MinhaConexao:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conexao = None

    def __enter__(self):
        print(f"Abrindo conexão com o banco de dados: {self.db_name}")
        self.conexao = f"Conexão com {self.db_name}"
        return self.conexao

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Fechando conexão com o banco de dados: {self.db_name}")
        self.conexao = None
        if exc_type:
            print(f"Uma exceção foi capturada: {exc_val}")
            return False  # Se True, suprime a exceção

with MinhaConexao("minha_base_de_dados") as db:
    print(f"Usando a conexão: {db}")
    # raise ValueError("Simulando erro...")

print("Fora do bloco with.")
````

### Criando context managers com `contextlib`

O modulo `contextlib` permite criar context managers com menos codigo usando geradores:

````python
from contextlib import contextmanager

@contextmanager
def temporizador():
    import time
    inicio = time.time()
    try:
        yield  # Código do bloco with será executado aqui
    finally:
        fim = time.time()
        print(f"Tempo decorrido: {fim - inicio:.4f} segundos.")

with temporizador():
    print("Iniciando uma operação demorada...")
    for _ in range(10000000):
        pass
    print("Operação concluída.")
````

### Vantagens de uso de `with`
 - **Evitar vazamentos de recursos**(arquivos abertos, conexões esquecidas etc);
 - **Codigo limpo e conciso**
 - Facilita **tratamento de exceções**
 - Permite criar **blocos reutilizaveis** e **seguros**

Use `with` sempre que estiver lidando com recursos que precisam ser liberados-como arquivos, conexoes, bloqueios(locks), ou operacoes temporarias.

# Instalando Pacotes com `pip` e Gerenciando Ambientes Virtuais com `venv`

## 🔧 O que é o `pip`?

`pip` (Pip Installs Packages) é o **gerenciador de pacotes padrão para Python**. Ele permite instalar e gerenciar bibliotecas de terceiros disponíveis no [PyPI](https://pypi.org/), o repositório oficial da comunidade Python.

---

## Por que usar `pip`?

- **Extensão de Funcionalidade**: Acesso a milhares de bibliotecas para desenvolvimento web, ciência de dados, machine learning, automação, etc.
- **Gerenciamento de Dependências**: Instala, atualiza e remove pacotes necessários para seu projeto.

---

## Comandos Básicos do `pip`

### Verificar a versão do `pip`

```bash
pip --version
# ou
pip3 --version  # Garante o uso do pip do Python 3
````

### Instalar um pacote

````bash
pip install nome_do_pacote
````

### Instalar uma versao especifica

````bash
pip install nome_do_pacote==versao
````

### Atualizar um pacote

````bash
pip install --upgrade nome_do_pacote
````

### Desinstalar um pacote 

````bash
pip uninstall nome_do_pacote
````

### Listae pacotes instalados

````bash
pip list
````

## Requirements.txt: slavando dependencias

Crie um arquivo com as dependencias exatas do projeto

````bash
pip freeze > requirements.txt
````

Instale as dependencias listadas com:

````bash
pip install -r requirements.txt
````

## Ambientes Virtuais com `venv`

Um ambiente virtual é uma **instancia isolada do Python** com seus proprios paoctes. Ideal para evitar conflitos entre projetos.

### Vantagens:
 - Isolamento de dependencias
 - Organização e limpeza
 - Facilidade para colaboração

## Criando e Usando um Ambiente Virtual

### Crie o ambiente virtual:

````bash
python3 -m venv .venv
````
### Ative o mabiente virtual:

**Windows:**
````bash
.venv\Scripts\activate
````

**Linux:**
````bash
source .venv/bin/activate
````

### Instale pacotes no ambiente virtual:
````bash
pip install requests beautifulsoup4
````

### Salve os pacotes instalados:
````bash
pip freeze > requirements.txt
````

### Desative o ambiente virtual:
````bash
deactivate
````

## Fluxo de trabalho resumido:
````bash
cd meu_projeto/
python3 -m venv .venv
source .venv/bin/activate         # ou .venv\Scripts\activate no Windows
pip install nome_do_pacote
pip freeze > requirements.txt
# Desenvolva seu código...
deactivate
````

# 🧠 Estruturas de Dados Essenciais para LeetCode

Para se destacar no LeetCode e em competições de programação, é fundamental dominar as estruturas de dados. Python oferece várias delas de forma nativa, enquanto outras exigem implementação manual ou compreensão de seus conceitos internos.

---

## 1️⃣ Arrays / Listas

### 📘 Teoria

- **Coleções ordenadas** de elementos.
- Acesso por índice: `O(1)`
- Inserções/remoções no **meio**: `O(N)` (elementos precisam ser realocados)
- Inserção/remoção no **final**: `O(1)` em média (amortizado)

### 🛠️ Aplicações no LeetCode

- Problemas de **busca** e **ordenação**
- Técnicas de **sliding window**
- Armazenamento de **dados sequenciais**
- Representação de **matrizes** (listas de listas)

---

### 📌 Exemplo de Uso

```python
# Criação
arr = [1, 2, 3, 4, 5]

# Acesso (O(1))
print(arr[0])  # 1
print(arr[2])  # 3

# Inserção no meio (O(N))
arr.insert(1, 99)  # arr = [1, 99, 2, 3, 4, 5]

# Remoção no meio (O(N))
arr.pop(2)         # arr = [1, 99, 3, 4, 5]

# Adição no final (amortized O(1))
arr.append(6)      # arr = [1, 99, 3, 4, 5, 6]

# Remoção no final (amortized O(1))
arr.pop()          # arr = [1, 99, 3, 4, 5]

# Slicing (subarrays)
sub_arr = arr[1:4]  # sub_arr = [99, 3, 4]
````

## Strings 

### Teoria

- **Sequências imutáveis de caracteres**
- Similar a um array de caracteres, mas **não pode ser modificada diretamente**
- Cada operação que altera uma string retorna uma nova string

### 🛠️ Aplicações no LeetCode

- Verificação de **anagramas** e **palíndromos**
- Problemas de **substrings**
- Análise de **frequência de caracteres**
- **Manipulação de texto**, **regex**, e formatação

---

### 📌 Exemplo de Uso

```python
s = "hello"

# Acesso por índice (O(1))
print(s[0])      # 'h'

# Slicing
print(s[1:4])    # 'ell'

# Imutabilidade
# s[0] = 'j'     # Erro! Strings são imutáveis
````

### Metodos Uteis
````python
s = "LeetCode"

# Tamanho
len(s)                        # 8

# Verificações
s.startswith("Lee")          # False
s.endswith("Code")           # True
s.isalpha()                  # True se todos os caracteres forem letras

# Transformações
s.lower()                    # "leetcode"
s.upper()                    # "LEETCODE"
s.replace("e", "3")          # "L33tCod3"

# Divisão e junção
"abc def".split()            # ['abc', 'def']
"-".join(["a", "b", "c"])    # "a-b-c"

# Remoção de espaços
"  texto  ".strip()          # "texto"
````

### Problema Rapido (Palindromo)

````python
# Verificar palíndromo
def eh_palindromo(s):
    return s == s[::-1]

# Contar frequência
from collections import Counter
freq = Counter("banana")  # {'a': 3, 'b': 1, 'n': 2}
````
## Hash Tables / Dicionários 

###  Teoria

- Estrutura de dados baseada em **pares chave-valor**
- Operações de **pesquisa, inserção e remoção** com **tempo médio `O(1)`**
- Pior caso `O(N)` (colisões de hash), mas **raro com boas funções de hash**
- **Chaves devem ser imutáveis** (`int`, `str`, `tuple`, etc.)

---

### 🛠️ Aplicações no LeetCode

- Contagem de **frequência de elementos** (`collections.Counter`)
- Mapear valores/índices/IDs
- Verificar se um **elemento existe rapidamente**
- **Memoization** (cache de chamadas recursivas)
- Problemas como **Two Sum**, **Group Anagrams**, **Top K Elements**, etc.

---

### 📌 Exemplo de Uso

```python
# Criação
d = {"a": 1, "b": 2}

# Acesso (O(1) médio)
print(d["a"])           # 1
print(d.get("c", 0))    # 0 (retorna valor padrão se chave não existe)

# Inserção / Atualização
d["c"] = 3              # Insere nova chave
d["a"] = 10             # Atualiza valor existente

# Remoção
del d["b"]

# Iteração
for key, value in d.items():
    print(key, value)
````

### Exemplos uteis

````python
# Contar frequência
from collections import Counter
freq = Counter(["a", "b", "a", "c", "b", "a"])
# {'a': 3, 'b': 2, 'c': 1}

# Memoization em recursão
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
````

#### Considere:
 - Prefira `dict.get(key, default)` para evitar `KeyError`
 - Use `collections.defaultdict`para contadores automaticos.
 - Use `collections.Counter`para contar frequencia de elementos.
 - Use `dict` para simular hash maps/sets em problemas classicos de LeetCode

##  Sets

### Teoria

- **Coleções não ordenadas de elementos únicos**
- Baseadas em **hash table**, como `dict`
- Operações de **busca, inserção e remoção** têm tempo médio `O(1)`
- Ideal para remoção de duplicatas e verificação de existência rápida

---

###  Aplicações no LeetCode

- **Remover duplicatas** de listas
- **Verificar presença** de elementos com alta performance
- Operações de **interseção, união, diferença**
- **Detecção de ciclos** em grafos ou listas ligadas
- Problemas como **Longest Consecutive Sequence**, **Happy Number**, etc.

---

### Exemplo de Uso

```python
s = {1, 2, 3}

# Adicionar elementos
s.add(4)
s.add(2)  # Ignorado, pois 2 já existe

print(s)  # {1, 2, 3, 4}

# Verificar existência
print(3 in s)  # True (O(1) médio)

# Remover elemento
s.remove(1)
print(s)  # {2, 3, 4}

# Operações entre conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.intersection(set2))  # {3}
print(set1.union(set2))         # {1, 2, 3, 4, 5}
print(set1.difference(set2))    # {1, 2}
````
### Exemplo pratico

````python
# Detectar se há elementos duplicados
def tem_duplicados(nums):
    return len(nums) != len(set(nums))

# Exemplo
print(tem_duplicados([1, 2, 3, 1]))  # True
print(tem_duplicados([1, 2, 3]))     # False
````

#### Dicas
  - Use `set()` para ocnverter listas e eliminar duplicatas:
    ````python
    unique = set([1, 1, 2, 3])
    ````
  - Verificar exixtencia com `in` em `set` é mais rapido que em `list`
  - Sets nao mantem ordem. Para conjuntos ordenados, use `SortedSet` de bibliotecas extern como `sortedcontainers`.

## 5️⃣ Pilhas (`Stack` em Python)

### 📘 Teoria

- Estrutura de dados **LIFO** (*Last-In, First-Out*)
- **`Push`**: adiciona elemento no topo
- **`Pop`**: remove o elemento do topo
- **`Peek` / `Top`**: acessa o topo sem remover

---

### 🛠️ Aplicações no LeetCode

- **Validação de parênteses**, colchetes e chaves
- **Avaliação de expressões** (ex: notação polonesa reversa - RPN)
- Algoritmos com **backtracking**
- **Busca em profundidade (DFS)** de forma iterativa
- Problemas clássicos como:
  - Valid Parentheses
  - Evaluate Reverse Polish Notation
  - Daily Temperatures

---

### ⚙️ Implementação com `list` em Python

A estrutura de `list` em Python funciona eficientemente como pilha:

```python
stack = []

# Push
stack.append(10)
stack.append(20)
print(stack)         # [10, 20]

# Peek (ver o topo)
top_element = stack[-1]
print(top_element)   # 20

# Pop (remover do topo)
popped_element = stack.pop()
print(popped_element)  # 20
print(stack)           # [10]
````

### Exemplo: Validação de Parenteses

````python
def validar_parenteses(s):
    stack = []
    mapa = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapa.values():
            stack.append(char)
        elif char in mapa:
            if not stack or stack[-1] != mapa[char]:
                return False
            stack.pop()
    return not stack

print(validar_parenteses("()[]{}"))     # True
print(validar_parenteses("([)]"))       # False
print(validar_parenteses("{[]}"))       # True
````

### Dicas
  - Evite usar `.insert(0, . . .)
  - Se quiser evitar o uso de listas, pode usar `collections.deque`, mas para pilhas simples `list` ja é o suficiente.
  - Acompanhe o tamanho da pilha com `len(stack)` se necessário.


