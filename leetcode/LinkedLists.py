# Colecao de nos, onde cada no contem um valor e um ponteiro(referencia) par o proximo no.

# Uso:
#     Inverter listas ligadas
#     Detectar ciclos
#     Remover N-esimo no do final
#     Problemas que requerem inserções/remoções eficientes no meio da estrutura (diferente de arrays)
    
# Em python, nao ha implementacao nativa. É necessario criar classes: Node e LinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

current = head
while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")