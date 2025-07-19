# Conjunto de vertices(nos) e arestas(conexoes entre nos)
#     direcionado/nao direcionado: arestas tem direcao ou nao
#     ponderado/nao ponderado:arestas tem um pseo ou custo

# Representacao:
#     lista de adjacencia: dicionario onde chave = nó e os valores sao lisats de seus vizinhos(mais comum e eficiene)
#     matriz de adjacencia: matriz onde adj[i][j] é 1 se houver uma aresta de i para j, e 0 caso contarrio(melhor em garfos densos ou quando precisa saber se uma aresta existe)

# Uso:
#     caminho mais curto
#     alcance
#     ciclos
#     componentes conectados
#     topologia sort
    
#representacao por lista de adjacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'c': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# BFS (Breadth first search)- usando fila
from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(graph, 'A')

#dfs - usando pilha ou recursao
def dfs_iterafive(graph, start_node):
    visited = set()
    stack = [start_node]
    visited.add(start_node)
    
    while stack:
        node = stack.pop()
        print(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

dfs_iterafive(graph, 'A')
    
