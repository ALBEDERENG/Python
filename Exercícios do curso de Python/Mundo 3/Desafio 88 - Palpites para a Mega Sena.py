import os
import math
import random
os.system('cls')
print("---"*10)
print("{:^30}".format("JOGO NA MEGASSENA"))
print("---"*10)
n = 1
while True:
    i = -1
    j = -1
    n = int(input("Quantos jogos você quer que eu sorteie? "))
    if n == 0:
        break
    print("-=-=-=SORTEANDO {} JOGOS=-=-=-".format(n))
    Conjunto = []
    Lista = ["","","","","",""]
#print(len(Lista))

    while j != n-1:
        j+=1
        while i != 5:
            i+=1
            Lista[i] = random.randint(0,60)
        Conjunto.append(Lista[:])
        i = -1
        print(f"Jogo {j+1}: {Conjunto[j]}")

    print("-=-=-= < BOA SORTE > =-=-=-")
#print(Lista)
