# Colecoes nao ordenadas de itens unicos. Onde a ordem nao importa e vc nao quer dados repetidos
meu_set = {1, 2, 3, 4, 5, 2} # os repetidos sao ignorados
print(meu_set)

set_vazio = set()
print(type(set_vazio))

letras = set("abracadabra")
print(letras)

# #principais usos
# -remover duplicatas de uma lista
# -realizar operacoes de conjuntos(uniao, intersecao, diferenca)
# -verificar a associacaoa de itens

# metodos
cores = {"vermelho", "azul"}
print(cores)
cores.add("verde")
print(cores)

cores.add("vermelho") #repetido
cores.remove("azul")
print(cores)

cores.discard("amarelo") 

#Operacoes de conjuntos
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a | set_b) #uniao
print(set_a.union(set_b)) #uniao

print(set_a & set_b) #inter
print(set_a.intersection(set_b))

print(set_a ^ set_b)#diferenca
print(set_a.symmetric_difference(set_b))

set_c = {1, 2}
print(set_c <= set_a) #subconnjunto
print(set_a >= set_c) #superconjunto
