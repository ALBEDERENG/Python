import os
import math
os.system('cls')
import random
import operator
Dado = {}
print("Valores sorteados: ")
maior = 0
count = 0
for i in range(0,4):
    #print(i)
    n = f"jogador{i+1}"
    Dado[n] = random.randint(0,6)
    #print(f"O jogador{i+1} tirou o número {Dado[i]}")
    if Dado[n] >= maior:
        maior = Dado[n]
for c,v in Dado.items():
    print(f"O {c} tirou o número {v}")
    #Lista.append(c)
    #Lista.append(v)
print()#Para dar espaço
print("== RANKING DOS JOGADORES ==")
#print(Lista)
ranking = sorted(Dado.items(),key=operator.itemgetter(1),reverse=True)

for j,k in ranking:
    count += 1
    print(f"{count}º lugar: {j} com {k}")
#print(ranking)


#print(Dado.values())
