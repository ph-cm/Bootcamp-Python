# Colecoes nao ordenaas de elementos unicos. Permitem pesquisa,
# adicao e exxcludao em tempo medio O(1)

# Uso:
#     - Remover duplicatas.
#     - Verificar a presença de elementos rapidamente.
#     - Problemas de interseçao, uniao, diferenca
#     - Detectar ciclos em grafos/listas ligadas
    
s = {1, 2, 3}
s.add(4)
s.add(2)
print(s)

print(3 in s)
s.remove(1)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))