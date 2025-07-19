# Estrutura de dado hierarquica composta por nós(um nó raiz, nós fihos, folhas):
#     - Arvore binaria: cada no tem no maximo dois filhos(esquerdo e direito)
#     - BST (Binary Search Tree): arvore binaria onde os nós a esquerda sao menores que o pai, e os nos a direita sao maiores
#     - Trie (Prefix Tree): Usada para armazenar strings e otimizar buscas por prefixo

# Uso:
#     - Problemas de travessia (in-order, pre-order, post-order)
#     - Busca, inercao, remocao eficiente em BSTs
#     - Representar hierarquias
#     - Autocompletar(tries)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Travessia in-order(esquerda, raiz, direita)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val)
        inorder_traversal(node.right)
    
inorder_traversal(root)