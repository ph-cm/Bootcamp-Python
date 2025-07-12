# funcoes de ordem superior = elas podem aceitar outras funcoes como argumentos
# Sao conceitos da programacao funcional que podem simplificar o codigo ao idar com colecoes

# # map()
# aplica uma funcao a cada item de um iteravel(como lista) e retorna um map object(que eh um iterador)

# map(funcao, iteravel)
numeros = [1, 2, 3, 4, 5]

def dobro(x):
    return x * 2

dobros = list(map(dobro, numeros))
print(dobros)

triplos = list(map(lambda x: x * 3, numeros))
print(triplos)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
soma = list(map(lambda x, y: x + y, lista1, lista2))
print(soma)

# # filter()
# constroi um iterador a partir de elementos de um iteravel para os quais 
# uma funcao retorna true == filtra os elementos
# filter(funcao, iteravel)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def eh_par(x):
    return x % 2 == 0

pares = list(filter(eh_par, numeros))
print(pares)

palavras = ["maca", "abacaxi", "banana", "amora"]
comeca_com_a = list(filter(lambda palavra: palavra.startswith('a'), palavras))
print(comeca_com_a)

# reduce()
# aplica uma funcao de dois argumentos acumulativamente aos itens de um iteravel da esqueda para a direita, para reduzir o iteravel a um unico valor. (precisa do modulo functools)
# reduce(funcao, iteravel, [inicializador])

from functools import reduce

numeros_reduce = [1, 2, 3, 4, 5]

# soma de todos os elementos
soma_total = reduce(lambda x, y: x + y, numeros_reduce)
print(soma_total)

produto_total = reduce(lambda x, y: x * y, numeros_reduce)
print(produto_total)

maior_numero = reduce(lambda x, y: x if x > y else y, numeros_reduce)
print(maior_numero)