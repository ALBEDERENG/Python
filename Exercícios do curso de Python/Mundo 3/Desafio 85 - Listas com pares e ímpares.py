import os
import math
os.system('cls')
i = 0
Listap = []
Listai = []
Conjunto = [Listap,Listai]
while i != 7:
    i += 1
    n = float(input(f"Digite o {i}º número: "))
    if n % 2 == 0:
        Listap.append(n)
    elif n % 2 != 0:
        Listai.append(n)
    #Conjunto.append(n)
    

print(f"Os valores pares foram: {sorted(Conjunto[0])}")
print(f"Os valores ímpares foram: {sorted(Conjunto[1])}")
print("=-="*30)
