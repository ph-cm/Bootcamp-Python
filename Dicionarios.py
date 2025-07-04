# Colecoes nao ordenadas de pares chave-valor. Cada chave deve ser
# unica e imutavel(strings, numeros, tuplas sao bons; listas nao podem ser
#                  chaves)

# Sao extremamente uteis para mapear dados, como um dicionario do mundo
# real onde voce procura uma refeicao uma definicao por uma palavra.

# Criacao de Dicionario

pessoa = {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "Sao Paulo"
}

dicionario_vazio = {}

# Acessando Valores

print(pessoa["nome"])

# get() metodo de acesso seguro
print(pessoa.get("idade"))
print(pessoa.get("telefone"))
print(pessoa.get("endereco", "Nao informado"))

# Adicionando/Modificando elementos
pessoa["profissao"] = "Engenheiro" #adicionar nova chave-valor
pessoa["idade"] = 29 #modificar valor
print(pessoa)

# Removendo elemento
cadastro = {
    "id": 1,
    "nome": "Joao",
    "email": "joao@gmail.com"
}

del cadastro["email"]
print(cadastro)

nome_removido = cadastro.pop("nome")
print(cadastro)
print(nome_removido)
