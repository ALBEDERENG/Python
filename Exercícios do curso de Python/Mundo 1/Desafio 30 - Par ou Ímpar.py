import os
import math
os.system('cls')
n = int(input("Me diga um número qualquer: "))
n1 = n % 2
if n1 == 0:
    print("O número {} é PAR".format(n))
else:
    print("O número {} é ÍMPAR".format(n))