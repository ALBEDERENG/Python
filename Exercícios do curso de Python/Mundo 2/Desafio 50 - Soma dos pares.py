import os
import math
os.system('cls')
j = 0
k = 0
for i in range(1,7):
    n = int(input("Digite o {} valor: ".format(i)))
    if n % 2 == 0 and n != 0:
        j = n + j
        k = k + 1
print("Você informou {} números pares e a soma foi {}".format(k,j))