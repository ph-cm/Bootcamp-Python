# Eventos que interrompem o fluxo normal das instrucoes

# Tipos:
#     NameError
#     TypeError
#     ValueError
#     ZeroDivisionError
#     FileNotFoundError
#     IndexError
#     KeyError

# try: codigo dentro tem potencial de excecao
# , except: se excecao ocorrer no try , python procura um bloco except para lidar com a excecao
# , else: executado caso n haja nenhuma excecao
# # , finally: codigo dentro do finally sempre eh executado, ocorra ou nao a excecao

#sintaxe:

# try:
#     # Código que pode gerar uma exceção
#     # Ex: divisao = 10 / 0
# except TipoDeExcecao:
#     # Código para lidar com essa exceção
# except OutroTipoDeExcecao as e:
#     # Código para lidar com outra exceção, 'e' contém a instância da exceção
# except: # Captura qualquer exceção (uso não recomendado para fins gerais)
#     # Código genérico para qualquer erro
# else:
#     # Código executado SE NENHUMA exceção ocorrer no try
# finally:
#     # Código que sempre será executado, independente de exceções

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("ERRO: Nao eh possivel dividir por zero")
print("Programa continua")

try:
    numero = int(input("Digite um numero"))
    divisor = int(input("Digite um divisor: "))
    resultado = numero / divisor
except ValueError:
    print("Entrada invalida, apenas inteiros sao aceitos")
except ZeroDivisionError:
    print("Nao pode dividir por zero")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
else:
    print(f"O resultado eh: {resultado}")
finally:
    print("O programa acabou")

# usando raise
def validar_idade(idade):
    if not isinstance(idade, int):
        raise TypeError("A idade deve ser um numero inteiro.")
    if idade < 0:
        raise ValueError("A idade nao pode ser negativa")
    print(f"Idade valida: {idade}")

try:
    validar_idade(-5)
except ValueError as e:
    print(f"Erro de validacao: {e}")

try:
    validar_idade("vinte")
except TypeError as e:
    print(f"Erro de tipo: {e}")
    
    
