# Modulos sao arquivos .py que contem codigo Python. Permitem organizar o codigo
# em arquivos separados
import calculadora
# import calculadora as calc
# from calculadora import dividir, Calculadora

print(calculadora.somar(5, 3))
print(calculadora.PI)

minha_calc = calculadora.Calculadora(10)
minha_calc.adicionar(5)

print(minha_calc.obter_valor())
