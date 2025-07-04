# COlecoes ordenadas e imutaveis de itens. Diferenca da lista = imutabilidade

minha_tuplaa = (1, 2, 3, "quatro", False)
tupla_vazia = ()
tupla_um_elemento = (1,)

# garantia de integridade de dados
# chaves de dicionarios
# desempenho
# retorno de multiplos valores

# Acessando Elementos e Slicing

coordenadas = (10, 20, 30)
print(coordenadas[0])
print(coordenadas[1:])
print(coordenadas[::2])

minha_tuplaa = (1, 2, 3)

# minha_tuplaa[0] = 99 ERROR

# Empacotamento
ponto = (3, 4)

# Desempacotsamento
x, y = ponto
print(f"X: {x}, Y: {y}")

#trtoca de valores
a = 10
b = 20
a, b = b, a #Equivalente a (a, b) = (b, a)
print(f"a: {a}, b: {b}")

#Retorna de muultiplos valores de uma funcao
def obter_nome_idade():
    return "Maria", 30

nome, idade = obter_nome_idade()
print(f"{nome} temm {idade} anos")