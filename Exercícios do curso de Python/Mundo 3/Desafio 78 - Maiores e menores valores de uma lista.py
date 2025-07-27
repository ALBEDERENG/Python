import os
import math
os.system('cls')
Lista = []
count = -1
count1 = -1
for i in range(0,5):
    n = int(input(f"Digite um valor para posição {i}: "))
    Lista.append(n)
print(f"{"":=^30}")
print(f"Você digitou os valores: {Lista}")
print(f"O maior valor foi {max(Lista)} na posição ",end='')
while count <4:
    count += 1
    #print(count)
    if Lista[count] == max(Lista):
        print(count,end="... ")
print("")
print(f"O menor valor foi {min(Lista)} na posição ",end='')
while count1 <4:
    count1 += 1
    #print(count)
    if Lista[count1] == min(Lista):
        print(count1,end="... ")
