print("O usuário agora escolhe os números")
numeros = []
quantidade = int(input("Quantos números você quer digitar na lista? "))
for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero) #append=acrescentar item na lista
print(f"Números digitados: {numeros}")

#Mostrar somente os números pares
print("Números pares")
for i in numeros:
    if i %2==0:
        print(i)
