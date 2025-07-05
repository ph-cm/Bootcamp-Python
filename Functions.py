# Blocos de codigo reutilizaveis que realizam uma tarefa especifica.
# Promovem modularidade, organizacao e reutilizacao de codigo

def saudacao():
    """Esta funcao imprime uma saudadcao simples"""
    print("Ola! Bem-vindo")
    
saudacao()

def cumprimentar(nome, idade):
    """Esta funcao imprime uma saudacao dado o nome e idade como parametros"""
    print(f"Ola {nome} voce tem {idade} anos")

cumprimentar("Pedro", 22)
cumprimentar(idade=22, nome="Joao")

print("--------------------------------------------------")

def somar(a, b):
    """Calcular a soma de dois termos dados pelos parametros da funcao"""
    resultado = a + b
    return resultado

soma_total = somar(10, 5)
print(f"A soma eh: {soma_total}")

def eh_par(numero):
    """Verificar se o numero eh par, se sobra resto ou nao"""
    if numero % 2 == 0:
        return True
    else:
        return False

print(eh_par(10))
print(eh_par(15))

# Argumentos padroes
def saudacao_personalizada(nome="Visitante", mensagem="Ola"):
    print(f"{mensagem}, {nome}")

saudacao_personalizada()
saudacao_personalizada("Pedro")
saudacao_personalizada("Ana", "e ai!")

# argumentos de comprimento variavel 
# *args = argumento posicionais variaveis

def somar_tudo(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(somar_tudo(1, 2, 3))
print(somar_tudo(10, 20, 30, 40, 50))

#**kwargs = argumento de palavra-chave variaveis

def exibir_info(**info):
    for chave, valor in info.items():
        print(f"{chave.capitalize()}: {valor}")
    
exibir_info(nome="Pedro", idade=22, cidade="Rio")

# # Escopo de Variavel
# define onde ela pode ser acessada e usada dentro de um programa
# -LOcal
def minha_funcao():
    x = 10
    print(x)
    
minha_funcao()

# -Global
y = 20

def outra_funcao():
    print(y)
    
outra_funcao()
print(y)

# caso precise mudar o valor de uma variavel global em uma funcao, usar a palavra chave global(mas nao modifique == boas praticas)

#FUncoes aninhadas
def funcao_externa(mensagem_base):
    complemento = "(interna)"
    
    def funcao_interna(nome):
        print(f"{mensagem_base}, {nome}{complemento}")
    
    return funcao_interna

saudacao = funcao_externa("Bem vindo")
saudacao("Joao")

#Importante para closures
# closures = eh uma funcao interna que se lembra do ambiente (variaveis locais da funcao externa) em que foi criada, mesmo depois que a funcao externa ja terminou sua execucao

def criar_multiplicador(fator):
    def multiplicador(numero):
        return numero * fator
    return multiplicador

dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(dobrar(5))
print(triplicar(5))

def calcular_area_retangulo(largura, altura):
    area = largura * altura
    return area

print(calcular_area_retangulo(4, 5))
