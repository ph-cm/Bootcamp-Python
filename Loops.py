# Estruturas de controle que permitem executar um bloco de codigo repetidamente

# for eh usado para iterar sobre uma sequencia(lista, tuplas, strings, dicionarios, sets)

# for variavel_iteracao in iteravel:
    #COdigo a ser executado
    
frutas = ["Maca", "banana", "uva"]
for i in frutas:
    print(i)
    
nome = "Python"
for letra in nome:
    print(letra)
    
numeros = (1, 2, 3)
for num in numeros:
    print(num)

aluno = {"nome": "pedro", "idade": 22}
for chave in aluno:
    print(chave)

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)
    
for i in range(0, 10, 2):
    print(i)
    
# While executa enquanto a condicao for verdadeira

# while condicao:
    # codigo

contador = 0
while contador < 5:
    print(contador)
    contador += 1

resposta = ""
while resposta != "sair":
    resposta = input("Digite 'sair' para encerrar: ").lower()
    if resposta != "sair":
        print("VOce nao digitou 'sair'")

# break e continue
for i in range(10):
    if i == 5:
        print("NUmero 5 encontrado, saindo do loop.")
        break
    print(i)

for i in range(5):
    if i == 2:
        print("Pulando o numero 2.")
        continue
    print(i)
    
    