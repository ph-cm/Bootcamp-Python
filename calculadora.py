PI = 3.14159

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Nao eh possivel dividir por zero")
    return a / b

class Calculadora:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial
        
    def adicionar(self, num):
        self.valor += num
    
    def obter_valor(self):
        return self.valor
print("Modulo calculadora carregado")