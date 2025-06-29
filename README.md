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
