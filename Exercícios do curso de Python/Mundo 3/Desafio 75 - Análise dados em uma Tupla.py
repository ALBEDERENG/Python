import os
import math
os.system('cls')
count = 0
i = -1
n = int(input("Digite um número: "))
n1 = int(input("Digite um outro número: "))
n2 = int(input("Digite mais um número: "))
n3 = int(input("Digite um último número: "))
Tupla = (n,n1,n2,n3)
print(f"Você digitou os valores: {Tupla}")
print(f"O número 9 apareceu {Tupla.count(9)} vezes")
if 3 in Tupla:
    n4 = Tupla.index(3,0)
    print(f"O valor 3 se encontra na posição {n4+1}º posição")
else:
    print("O valor 3 não foi digitado")
print(f"Os valores pares digitados foram ",end="")
while i < 3:
    i +=1
    #print(i, "A")
    if Tupla[i] % 2 == 0 and i == 0:
        print(Tupla[i],end="")
        count += 1
    if Tupla[i] % 2 == 0 and i > 0:
        print(",",Tupla[i],end="")
        count += 1
if count == 0:
    print("não digitados")