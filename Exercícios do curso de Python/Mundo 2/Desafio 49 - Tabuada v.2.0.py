import os
import math
os.system('cls')
n = float(input("Digite um número para ver sua tabuada: "))
for i in range (1,11):
    print("{:.0f} x {} = {:.0f}".format(n, i,n*i))