# funcoes anonimas que podem ter qualquer numero de argumentos, mas apenas uma unica expressao
#  sao definidas com a palavra chave lambda
 
# lambda argumentos: expressao

somar = lambda a, b: a + b
print(somar(2, 3))

eh_par = lambda x: x % 2 == 0
print(eh_par(4))
print(eh_par(5))

estudantes = [("Alice", 20), ("Bob", 15), ("Pedro", 22)]
estudantes_ordenados = sorted(estudantes, key=lambda estudante: estudante[1])
print(estudantes_ordenados)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

quadrados = list(map(lambda x: x * x, numeros))
print(quadrados)
