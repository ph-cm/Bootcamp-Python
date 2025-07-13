# Permitem modificar o comportamento de fncoes ou metodos de classe
# sem alterar seu codigo original. Funcoes que pegam outra funcao como 
# argumento, adicionam alguma funcionalidade e retornam uma nova funcaao

# usadas para:
#     logging
#     medir tempo de execucao
#     cache 
#     validacao de autenticacao
#     alterar o comportamento de funcoes
    
# sintaxe:
#     @decorador
#     def minha_funcao():
#         pass

# igual a minha_funcao = decorador(minha_funcao)

def meu_primeiro_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da funcao ser chamada")
    
    return wrapper

@meu_primeiro_decorador
def saudacao():
    print("Ola mundo")
    
saudacao()


