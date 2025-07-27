import os
import math
import random
os.system('cls')
print("=-"*10)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*10)
count = 0
j = 0
while True:
    count += 1
    n = int(input(("Diga um valor: ")))
    n1 = (input(("Par ou ímpar: [P/I] ")).upper()).strip()
    n2 = random.randint(0,10)
    s = (n + n2)%2
    if s == 0:
        pi = "PAR"
        i = "P"
    if s != 0:
        pi = "ÍMPAR"
        i = "I"
    if n1 == i:
        print("---"*10)
        print("Você jogou {} e o computador jogou {}. Total de {} DEU {}".format(n,n2,n + n2,pi))
        print("---"*10)
        print("Você VENCEU!\nVamos jogar novamente...")
        print("=-=-"*10)
        j += 1
    if n1 != i:
        print("---"*10)
        print("Você jogou {} e o computador jogou {}. Total de {} DEU {}".format(n,n2,n + n2,pi))
        print("---"*10)
        print("Você PERDEU!")
        print("=-=-"*10)
        print("GAME OVER! Você venceu {} vez".format(j))
        break
    