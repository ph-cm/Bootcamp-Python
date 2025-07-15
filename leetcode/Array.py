# Colecao ordenada de elementos. Permitem acesso por indice O(1), mas inserçoes/remocoes
# no meio sao O(N)-> os elementos precisam ser deslocados
# Adicionar/remover no final é O(1)

# Ocorrencia:
#     -Problemas de busca e ordenacao
#     -Sliding window
#     -Armazenar dados sequenciais
#     -Matrizes

arr = [1, 2, 3, 4, 5]

print(arr[0])
print(arr[2])

arr.insert(1, 99) # O(N)
arr.pop(2) # O(N)

arr.append(6) # O(1) amortizado
arr.pop() # O(1) amortizado

sub_arr = arr[1:4]
