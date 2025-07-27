import os
import math
os.system('cls')
print("=-"*20)
print("Analisador de triângulos")
print("=-"*20)
n = float(input("Primeiro segmento: "))
n1 = float(input("Segundo segmento: "))
n2 = float(input("Terceiro segmento: "))
if n < n1 + n2 and n1 < n + n2 and n2 < n1 + n:
    print("Os segmentos acima PODEM FORMAR um triângulo")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")