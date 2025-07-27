import os
import math
os.system('cls')
count = 0
Lista = []
Listap =[]
Listai = []
while True:
    n = int(input("Digite uma valor: "))
    count+=1
    Lista.append(n)
    if n%2==0:
        Listap.append(n)
    else:
        Listai.append(n)
    p = (input("Quer continuar? [S/N] ").upper()).strip()
    if p == "N":
        break
print("=-="*30)
print(f"A lista completa é {Lista}")
print(f"A lista de pares é {Listap}")
print(f"A lista de ímpares é {Listai}")