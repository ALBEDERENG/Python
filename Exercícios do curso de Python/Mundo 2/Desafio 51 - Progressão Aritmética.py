import os
import math
os.system('cls')
print("="*30)
print("10 TERMOS DE UMA PA")
print("="*30)
n = int(input("Primeiro termo: "))
r = int(input("Razão: "))
a = 0
for i in range(1, 11):
    a = n + (i - 1)*r
    print(a , end="->")
print("ACABOU")

#2 4 6 8 10