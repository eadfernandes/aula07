#...
#Construir um algoritmo qu tenha a entrada de números inteiros escolhidos pelo usuário. A quantidade será escolhida também, pelo usuário e o algoritmo mostrará:
#1 - uma lista com todos os números
#2 - uma lista com números ímpares
#3 - uma lista com os números em ordem crescente
#4 - uma lista com os números em ordem decrescente
#5 - uma lista com um número removido pelo usuário
#....
numeros=[]
qtde = int(input("Quantos números inteiros deseja inserir? "))
for i in range(qtde):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero) #append=acrescentar item na lista
print(f"Números digitados: {numeros}")

#Mostrar somente os números ímpares
print("Números ímpares")
for i in numeros:
    if i %2!=0:
        print(i)
#Números em ordem crescente
numeros.sort()
print(f"Números em ordem crescente {numeros}")
#Números em ordem decrescente
numeros.sort(reverse=True)
print(f"Números em ordem decrescente {numeros}")
#Remover um número
numero_r = int(input("Esolha um número para remover da lista: "))
numeros.remove(numero_r)
print(f"Números: {numeros}")
