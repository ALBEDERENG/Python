import os
import math
os.system('cls')
cadastro = []
nomepeso = [" "," "]
maiornome = []
maiorpeso = [] #Acréscimo de uma variável X inicial para dar pop não de uma lista vazia
menornome = []
menorpeso = [] #Acréscimo de uma variável X inicial para dar pop não de uma lista vazia
count = 0
maior = 0
menor = float('inf')
n2 = 0
while n2 != "N":
    #========================================== Colocando listas dentro do cadastro
    n = input("Nome: ")
    nomepeso[0] = n
    n1 = float(input("Peso: "))
    nomepeso[1] = n1
    cadastro.append(nomepeso[:])
    count +=1
    #==========================================
    n2 = (input("Quer continuar: [S/N] ").upper()).strip()
'''
for c,v in enumerate(cadastro):
    print(f"{c} e {v}")
'''
for i in cadastro:
    maiorpeso.append(i[1])
    menorpeso.append(i[1])
    if i[1] == maior:
        maiornome.append(i[0])
    elif i[1] > maior:
        maiornome = []
        maiornome.append(i[0])
        maior = i[1]
    if i[1] == menor:
        menornome.append(i[0])
    elif i[1] < menor:
        menornome = []
        menornome.append(i[0])
        menor = i[1]

print("=-="*30)
print(f"Ao todo você cadastrou {count} pessoas.")
print(f"O maior peso foi {max(maiorpeso)} Kg. Peso de {maiornome}")
print(f"O menor peso foi {min(menorpeso)} Kg. Peso de {menornome}")