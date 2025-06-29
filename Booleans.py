# Booleans sao cruciasi para a logica condicional e o 
# controle de fluxo em programas. Alguns valores podem ser
# avaliados em conmtexto booleano:
#     None
#     False
#     0
#     0.0
#     ""
#     []
#     {}
#     set()

x = True
y = False

print(x)
print(type(x))

if 0: 
    print("0 eh true")
else:
    print("0 eh false")
    
if "ola":
    print("String nao vazia eh true")
    
minha_lista = []

if minha_lista:
    print("Lista nao vazia eh true")
else:
    print("Lista vazia eh false")
    
# Operadores booleanos : AND, OR, NOT

if None:
    print("None eh true")
else:
    print("None eh false")
    