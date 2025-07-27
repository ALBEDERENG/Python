import os
import math
os.system('cls')
Lista = []
i = -1
while i < 4:
    i+=1
    #print(i)
    n = int(input("Digite um valor: "))
    Lista.append(n)
    if i == 0:
        n1 = Lista.index(n)
        #print(Lista)
        print("Adicionado ao final da lista...")
    if i > 0:
        if n == max(Lista):
            Lista.remove(n)
            Lista.append(n)
            #print(Lista)
            n1 = Lista.index(n)
            print("Adicionado ao final da lista...")
            c = n
        if n == min(Lista):
            Lista.remove(n)
            Lista.insert(0,n)
            #print(Lista)
            n1 = Lista.index(n)
            print(f"Adicionado na posição {n1} da lista...")
            c = n
        if n <= c and n != max(Lista) and n != min(Lista):
            Lista.remove(n)
            Lista.insert(n1,n)
            n1 = Lista.index(n)
            #print(Lista)
            print(f"Adicionado na posição {n1} da lista...")
            c = n
        if n > c and n != max(Lista) and n != min(Lista):
            Lista.remove(n)
            Lista.insert(n1+1,n)
            n1 = Lista.index(n)
            #print(Lista)
            print(f"Adicionado na posição {n1} da lista...")
            c=n
print("=-="*30)
print(f"Os valores digitados em ordem foram: {Lista}")