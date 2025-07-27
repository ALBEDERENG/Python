import os
import math
os.system('cls')
c = 0
count = 0
j = ""
s = 0
ma = 0
n = 0
me = float("inf")
while True:
    n = int(input("Digite um número: "))
    c += n
    n1 = (input("Quer continuar? [S/N]").upper()).strip()
    if n >= ma:
        ma = n
    count += 1
    if n <= me:
        me = n
    e = c / count
    if n1 == "S":
        continue
    elif n1 == "N":
        print("Você digitou {} números e a média foi {:.1f}.".format(count,e))
        print("O maior valor foi {} e o menor foi {}".format(ma,me))
        break

    #j = j + str(n) + ' '
    #print(j)
    #k1 = (j.split())
    #k2 = " ".join(k1)
    #print(k2)
    #s += int(k2[count-1])
    #print("A soma é {}".format(s))