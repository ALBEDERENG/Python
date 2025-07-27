import os
import math
os.system('cls')
i = -1
j = -1
Conjunto = [["","",""],["","",""],["","",""]]
soma = 0
soma2 = 0
soma3 = 0
while i != 2:
    i += 1 
    n = int(input(f"Digite um valor para [0,{i}]: "))
    Conjunto[0][i] = n
i = -1
#print(Conjunto[0][1])
while i != 2:
    i += 1 
    n1 = int(input(f"Digite um valor para [1,{i}]: "))
    Conjunto[1][i] = n1
i=-1
while i != 2:
    i += 1 
    n2 = int(input(f"Digite um valor para [2,{i}]: "))
    Conjunto[2][i] = n2
i=-1
print("=-="*30)

print(f"[{Conjunto[0][0]}]   [{Conjunto[0][1]}]   [{Conjunto[0][2]}]\n[{Conjunto[1][0]}]   [{Conjunto[1][1]}]   [{Conjunto[1][2]}]\n[{Conjunto[2][0]}]   [{Conjunto[2][1]}]   [{Conjunto[2][2]}]")

print("=-="*30)

for k in Conjunto[0]:
    #print(k)
    if k % 2 ==0:
        #print(k)
        soma += k

for k in Conjunto[1]:
    #print(k)
    if k % 2 ==0:
        #print(k)
        soma += k

for k in Conjunto[2]:
    #print(k)
    if k % 2 ==0:
        #print(k)
        soma += k
print(f"A soma dos valores pares é {soma}")

while i != 2:
    i += 1
    soma3 += Conjunto[i][2]
i = -1
print(f"A soma dos valores da terceira coluna é {soma3}")

while i != 2:
    i += 1
    soma2 += Conjunto[1][i]
print(f"A soma dos valores da segunda linha é {soma2}")