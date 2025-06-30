# Conjunto de funcoes embutidas que sempre estao disponiveis para uso
# sem precisar de importar algo. Combrem uma gama de tarefas comuns
lista_numeros = [10, 5, 20, 15]

print(f"Comprimento da lista: {len(lista_numeros)}")
print(f"Soma dos numeros: {sum(lista_numeros)}")
print(f"Menor numero: {min(lista_numeros)}")
print(f"Maior numero: {max(lista_numeros)}")

print(f"Valor absoluto de -7: {abs(-7)}")
print(f"Arredondamento de 3.7: {round(3.7)}")

for i, valor in enumerate(["a", "b", "c"]):
    print(f"Indice: {i}, Valor: {valor}")

nome = ["Ana", "Beto"]
idade = [25, 30]
for nome, idade in zip(nome, idade):
    print(f"{nome} tem {idade} anos.")