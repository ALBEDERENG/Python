import os
import math
os.system('cls')
count = 0
Lista = []
while True:
    n = int(input("Digite uma valor: "))
    count+=1
    Lista.append(n)
    Lista.sort(reverse=True)
    p = (input("Deseja continuar? [S/N] ").upper()).strip()
    if p == "N":
        break
print("=-="*30)
print(f"Você digitou {count} elementos")
print(f"Os valores em ordem decrescente são {Lista}")
if 5 in Lista:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")
