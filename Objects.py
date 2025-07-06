# Em python, tudo eh um objeto. Isso significa que numeros, strings, listas, funcoes
# classes e ate modulos sao tratados com objetos

# objeto = instncia de uma class

# possui: identidade(endereco unico)
#         tipo
#         estado(atributos que seram utilizados)
#         comportamento(metodos)

numero = 10
print(id(numero))
print(type(numero))

lista = [1, 2, 3]
print(id(lista))
print(type(lista))

outra_lista = lista
print(id(outra_lista))

outra_lista.append(4)
print(lista)

s = "Python"
print(s.upper()) # metodo
print(s.count('o')) # metodo que usa o atributo