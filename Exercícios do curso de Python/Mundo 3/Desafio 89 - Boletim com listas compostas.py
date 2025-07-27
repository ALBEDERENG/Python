import os
import math
os.system('cls')
Conjunto = []
Lista = ["","",""]
count = -1
i=-1
while True:
    n = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    count += 1
    Lista[0]=n
    Lista[1]=n1
    Lista[2]=n2
    Conjunto.append(Lista[:])
    p = (input("Quer continuar? [S/N] ").upper()).strip()
    if p == "N":
        break
print("-="*30)
print("{:<5}".format("No"),end="")
print("{:^10}".format("Nome"),end="")
print("{:>10}".format("MÉDIA"))
print("---"*30)
while i != count:
    i+=1
    print("{:<5}".format(i),end="")
    print("{:^10}".format(Conjunto[i][0]),end="")
    print("{:>10}".format((Conjunto[i][1] + Conjunto[i][2])/2))
print("---"*30)
while True:
    p1 = int(input("Mostrar nota de qual aluno? (999 interrompe): "))
    if p1 == 999:
        break
    print(f"Notas do {Conjunto[p1][0]} são {Conjunto[p1][1]} e {Conjunto[p1][2]}")
    print("---"*30)