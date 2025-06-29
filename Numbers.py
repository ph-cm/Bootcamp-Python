# Python suporta 3 tipos numericos principais
# inteiros
# flutuantes
# complexos

numero_inteiro = 23
numero_negativo = -23
zero = 0
numero_grande = 12345678912345678912345

print(numero_grande)
print(type(numero_inteiro))

print("---------------------------")

numero_decimal = 3.14
salario = 2500.40
notacao_cientifica = 1.23e-5

print(type(numero_decimal))
print(notacao_cientifica)

print(0.1 + 0.2) #cuidado com precisao

print("--------------------------")

numero_complexo = 2 + 3j
print(type(numero_complexo))
print(numero_complexo.real)
print(numero_complexo.imag)

print("---------------------------")

#Conversao

numero_float = 5.9
numero_inteiro_convertido = int(numero_float)
print(f"{numero_float} convertido para {numero_inteiro_convertido}" )

numero_str = "123"
numero_inteiro_de_str = int(numero_str)
print(f"{numero_str} comvertido para {numero_inteiro_de_str}")

numero_int = 7
numero_float_convertido = float(numero_int)
print(f"{numero_int} convertido para {numero_float_convertido}")

#tentar converter uma string nao numerica para tipo numerico da erro
test_float = 42.7
test_float_conv = int(test_float)
print(f"{test_float} convertido para {test_float_conv}")