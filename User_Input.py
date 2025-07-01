# Programa baseado na funcao input() que permite que seu programa
# pause e espere a entrada do usuario. Ao pressionar enter, o programa 
# retorna de onde parou. 

# Sempre retorna uma string, mesmo que o usuario digite numeros ou seja,
# eh necessario que haja um type casting

# variavel = input("Seu prompt aqui: ") -> sintaxe

nome = input("Qual o seu nome: ")
print(f"Ola, {nome}")

idade_str = input("Qual sua idade: ") # ou int(input(. . .))
idade = int(idade_str)
print(f"Sua idade eh: {idade}")

primeiro_digito = float(input("Digite o primeiro numero: "))
segundo_digito = float(input("Digite o segundo digito: "))
soma = primeiro_digito + segundo_digito
print(f"a soma eh: {soma}")
media = (primeiro_digito + segundo_digito) / 2
print(f"A media eh: {media}")