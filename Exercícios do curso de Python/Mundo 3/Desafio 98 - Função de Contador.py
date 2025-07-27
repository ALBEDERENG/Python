import os
import math
import time
os.system('cls')
print("-="*30)
def contador(X,Y,Z):
    print(f"Contagem de {X} até {Y} de {Z} em {Z}")
    if Y > X:
        for i in range(X,Y+1,Z):
            print(i,end=" ",flush=True)
            time.sleep(0.5)
    elif X > Y:
        for i in range(X,Y-1,-Z):
            print(i,end=" ",flush=True)
            time.sleep(0.5)
    print("FIM!")
    print("-="*30)
contador(1,10,1)
contador(10,0,2)
print("Agora é sua vez de personalizar a contagem!")
X = int(input("Início: "))
Y = int(input("Fim: "))
Z = int(input("Passo: "))
print("-="*30)
contador(X,Y,Z)
