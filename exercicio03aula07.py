print("Entre com os nomes e coloque em ordem alfabéica crescente\n")
nomes=[]
qtde = int(input("Quantos nomes deseja inserir? "))
for i in range(qtde):
    nome = input(f"{i+1}º Nome: ")
    nomes.append(nome)

nomes.sort(reverse=True)
print(f"Nomes em ordem alfabética decrescente {nomes}")

nome_remover = input("Esolha um nome para remover da lista: ")
nomes.remove(nome_remover)
print(f"Nomes: {nomes}")
