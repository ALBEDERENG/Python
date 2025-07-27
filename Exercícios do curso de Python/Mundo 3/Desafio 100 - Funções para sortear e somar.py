import os
import math
import random
import time
os.system('cls')
Lista = []
def sorteador(list):
    for i in range(0,6):
        j = random.randint(0,5)
        list.append(j)
    print("Sorteando 5 valores da lista:",end=" ")
    for k in list:
        print(f"{k}",end=" ",flush = "True")
        time.sleep(0.5)
    print("PRONTO!")

def somadorp(list):
    soma = 0
    for l in list:
        if l % 2 ==0:
            soma += l
    print(f"Somando os valores pares de {list}, temos {soma}")


sorteador(Lista)
somadorp(Lista)

    