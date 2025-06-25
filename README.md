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

