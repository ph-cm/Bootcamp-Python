# Gerenciar recursos externos(arquivos, conexoes de banco de dados, locks) de forma segura e eficiente.
# Sem o with eh necessario gerenciar explicitamente a abertura e o fechamento de recursos:
f = open("meu_arquivo.txt", "w")
try:
    f.write("Ola,mundo")
except Exception as e:
    print(f"Erro: {e}")
finally:
    f.close()

#usando with
with open("meu_arquivo.txt", "w") as f:
    f.write("Ola com with")

print("Arquivo gravado e fechado automaticamente")

with open("meu_arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)