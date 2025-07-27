import os
import math
os.system('cls')
n = float(input("Primeiro segmento: "))
n1 = float(input("Segundo segmento: "))
n2 = float(input("Terceiro segmento: "))

if n2 != max(n,n1,n2):
    tmp = n2
    if n == max(n,n1,n2):
        n2 = max(n,n1,n2)
        n = tmp
    elif n1 == max(n,n1,n2):
        n2 = max(n,n1,n2)
        n1 = tmp
print(n)
print(n1)
print(n2)
if n + n1 > n2:
    print("Pode ser formar um triângulo")
    if n != n1 != n2:
        print("Os segmentos PODEM FORMAR um triângulo ESCALÊNO!")
    elif n == n1 == n2:
        print("Os segmentos PODEM FORMAR um triângulo EQUILÁTERO!")
    elif n == n1 != n2 or n == n2 != n1 or n1 == n2 != n:
        print("Os segmentos PODEM FORMAR um triângulo ISÓSCELES")
else:
    print("Não pode ser formar um triângulo")

