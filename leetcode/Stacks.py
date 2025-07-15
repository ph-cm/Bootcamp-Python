# Estrutura LIFO (Last In First Out):
#     - Push: adicionar um elemento no topo
#     - Pop: Remover o elemento do topo
#     - Peek/Top: Ver o elemento do topo sem remover.
# Uma lista python pode atuar como uma pilha eficientemente usando append()
# para push e pop() para pop.

# Uso:
#     - Balanceamento de parenteses/chaves
#     - Avaliação de expressoes
#     - Backtracking em algoritmos
#     - DFS (Depth-First Search) iterativa

stack = []
stack.append(10)
stack.append(20)
print(stack)

top_element = stack[-1] #Peek
print(top_element)

popped_element = stack.pop()
print(popped_element)
print(stack)
