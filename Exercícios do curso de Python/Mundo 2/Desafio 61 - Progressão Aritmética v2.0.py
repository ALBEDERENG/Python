import os
import math
os.system('cls')
print("Gerador de PA")
print("=-="*5)
n = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
i = 0
k = 0
while i < 10:
    i += 1
    k = n + (i - 1)*r
    print("{} ->".format(k),end=" ")

print("FIM")
    