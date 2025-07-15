# Colecao de pares-valor. Permitem pesquisa, inserção e exclusao em tempo medio O(1).
# No pior caso, O(N) (devido a colisoes de hash, mas raro com boas funcoes de hash)
# As chaves devem ser imutaveis.

# Usos:
#     -Contagem de frequencia de elementos(counter).
#     -Mapeamento de IDs para objetos
#     -Verificar se um elemento existe rapidamente.
#     -Memoization(otimização de funcoes recursivas)
#     -Problemas Two Sum, Group Anagrams, etc.
    
#criacao
d = {"a": 1, "b": 2}

#acesso
print(d["a"]) # O(1) medio
print(d.get("c", 0)) #acesso seguro

#insercao
d["c"] = 3
d["a"] = 10

#remocao
del d["b"]

#iteracao
for key, value in d.items():
    print(key, value)