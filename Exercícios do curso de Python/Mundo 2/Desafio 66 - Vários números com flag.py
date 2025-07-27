import os
import math
os.system('cls')
count = 0
s = 0
while True:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break
    count += 1
    s += n
print(f"A soma dos {count} valores foi {s}!")
