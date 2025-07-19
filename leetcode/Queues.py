# Estrutura FIFO (First-In First-Out), o modulo collections.deque eh a 
# implementecao mais eficiente de uma fila em python, pois append e popleft sao O(1).
# Listas comuns usam insert(0, x) e pop(0) que sao O(N) e nao ideais para filas grandes.

# Uso:
#     - BFS(Breadth-First Search) em grafos/arvores
#     - Agendamento de tarefas
#     - Simulacoes

from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
print(queue)

front_element = queue[0]
print(front_element)

dequeue_element = queue.popleft()
print(dequeue_element)
print(queue)

