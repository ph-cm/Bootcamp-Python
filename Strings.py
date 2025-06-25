# Strings são sequencias de caracteres, usadas para representar texto.
# Na criação, pode-se usar aspas simples, duplas ou triplas
name = "Pedro"
message = 'Hello world'
paragraph = """Olá mundo estou no paargrafo"""

# Strings são imutaveis
saudacoes = "Ola"
#saudacoes[0] = "A" -> Erro

nova_saudacao = saudacoes + " Mundo"
print(saudacoes)
print(nova_saudacao)

#Metodos de string
print(saudacoes.upper()) # Converter para maiuscula
print(saudacoes.lower()) # Converter para minuscula
print(saudacoes.capitalize()) # Converter a primeira letra para maiuscula
print(saudacoes.title()) # Converter cada primeira letra em maiuscula
print(saudacoes.strip()) # elimina espacos
print(saudacoes.lstrip()) #elimina espacos na esqueda
print(saudacoes.replace("O", "A"))
print(saudacoes.split("O"))
print(saudacoes.join(['a', 'b', 'c']))
print(saudacoes.startswith("O"))
print(saudacoes.endswith("a"))
print(saudacoes.find("l"))
print(saudacoes.count("a"))
print(saudacoes.isalnum())
print(saudacoes.isdigit())
print(saudacoes.isspace())

print("_______________________________\n")

# Raw strings, quando vamos usar um endereço do novo arquivo
caminho = r"C:\novo\diretorio\arquivo.txt"
print(caminho)

# # Caracteres de STring e Slicing
# indices da sua string

frase = "Python"
print(frase[0])
print(frase[1])
print(frase[2])
print(frase[3])

print("____________________\n")
# # sintaxe datiamento: start:end:step
# start = indice inicial[0]
# end = indice final
# step = incremento(padrao = 1)
texto = "Programação Python"
print(len(texto))
print(texto[0:9])
print(texto[:9])
print(texto[10:])
print(texto[:])
print(texto[::2])
print(texto[::-1])

print(texto[4:10:2])

print("____________________________\n")

# Formatando strings
nome = "Pedro"
age = 28
print("Meu nome é %s e tenho %d anos." % (nome, age))

print(f"Meu nome é {nome} e tenho {age} anos.") #melhor versao

