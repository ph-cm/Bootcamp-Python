# Um tipo de colecao versatil. Sao colecoes ordenadas e mutaveis de itens
# (itens podem ser de diferentes tipos de dados)

minha_lista = [1, 2, 3, "quatro", True, 5.0]
lista_vazia = []

frutas = ["maca", "banana", "laranja", "uva"]
print(frutas[0])
print(frutas[2])
print(frutas[3])
print(frutas[-1])

#slicing
numeros = [10, 20, 30, 40, 50, 60]
print(numeros[1:4])
print(numeros[:3])
print(numeros[3:])
print(numeros[::2])

#mutabilidade
minha_lista = ["um", "dois", "tres"]
print(minha_lista)
minha_lista[1] = "novo valor"
print(minha_lista)

minha_lista[0:2] = ["a", "b", "c"]
print(minha_lista)

print("-------------------------------")

# metodos
lista = [1, 2, 3]

lista.append(4)
lista.insert(1, 99)
print(lista)

lista.remove(2)
print(lista)

removido = lista.pop()
print(lista)
print(removido)

print("-------------------------------")

lista_numeros = [5, 1, 8, 2, 9]
lista_numeros.sort()
print(lista_numeros)

lista_numeros.reverse()
print(lista_numeros)


print("-------------------------------")


lista_original = [1, 2, 3]
lista_copia = lista_original.copy()
lista_original.append(4)
print(lista_original)
print(lista_copia)


print("-------------------------------")

lista1 = [1, 2]
lista2 = [3, 4]
lista1.extend(lista2)
print(lista1)

print("-------------------------------")

# Ordenando listas

number = [3, 1, 4, 1, 5, 9, 2]
number.sort()
print(number)

# decrescente
letras = ['c', 'a', 'b']
letras.sort(reverse=True)
print(letras)

lista_origem = [3, 1, 4, 1, 5, 9, 2]
lista_ordenada = sorted(lista_origem)
print(lista_origem)
print(lista_ordenada)

palavras = ["banana", "maca", "abacaxi"]
palavras_ordenadas_dec = sorted(palavras, reverse=True)
print(palavras_ordenadas_dec)

print("-------------------------------")
