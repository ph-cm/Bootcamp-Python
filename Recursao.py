# Tecnica onde uma funcao chama ela mesma para resolver um problema

# Caso base: uma condicao de parada que nao requer mais chamadas recursivas, evitando um loop infinito.

# Chamada Recursiva: A funcao chama a si mesma com uma subproblema menor que eventualmente converge para o caso base.

# funcao fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))
print(fatorial(0))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(6))

# Soma de elementos em um Lista
def soma_lista_recursiva(lista):
    if not lista:
        return 0
    else: 
        return lista[0]

print(soma_lista_recursiva([1, 2, 3, 4, 5]))
print(soma_lista_recursiva([]))