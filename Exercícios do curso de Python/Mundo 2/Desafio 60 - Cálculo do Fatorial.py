import os
import math
os.system('cls')
n = int(input("Digite um número para\ncalcular seu Fatorial: "))
i = 0
k = 1
print("{}! =".format(n),end=" ")
n = n + 1
while n != 2:
    n += -1
    k *= n
    print(str(n) + " x",end=" ")
print("1 = {}".format(k))