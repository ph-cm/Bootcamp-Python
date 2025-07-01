# Enums sao um conjunto de nomes simbolicos ligados a valores
# constantes unicos.

from enum import Enum, auto

class DiaDaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4 
    SEXTA = 5
    SABADO = 6
    DOMINGO = 7
    
#Acessar membros do Enum
print(DiaDaSemana.SEGUNDA)
print(DiaDaSemana.SABADO)
print(DiaDaSemana.SEGUNDA.name)
print(DiaDaSemana.SEGUNDA.value)
print(DiaDaSemana.SABADO.name)
print(DiaDaSemana.SABADO.value)

meu_dia = DiaDaSemana.SEXTA

# comparando membros
if meu_dia == DiaDaSemana.SEXTA:
    print("Eh sexta-feira")

print("---------------------------")

# iterando sobre membros
for dia in DiaDaSemana:
    print(f"{dia.name} tem o valor {dia.value}")
    
# obter membro pelo valor
dia_por_valor = DiaDaSemana(3)
print(dia_por_valor)

# obter um membro pelo nome
dia_por_nome = DiaDaSemana["DOMINGO"]
print(dia_por_nome)

# pode ser atribuido valores automaticamente

class StatusPedido(Enum):
    PENDENTE = auto()
    PROCESSANDO = auto()
    ENVIADO = auto()
    ENTREGUE = auto()
    CANCELADO = auto()

print(StatusPedido.PENDENTE.value)
print(StatusPedido.PENDENTE.name)
print(StatusPedido.ENTREGUE.value)    