import os
import math
os.system('cls')
n = 0
n1 = 0
print("-="*10)
Lista = "Corinthians", "Palmeiras", "Santos","Grêmio","Cruzeiro","Flamengo","Vasco","Chapecoense","Atlético"

print(f"Lista de times do Brasileirão: {Lista}")
print("-="*10)
print(f"Os 5 primeiros são {Lista[0:5]}")
print("-="*10)
print(f"Os 4 últimos times são {Lista[-4:]}")
print("-="*10)
print(f"Times em ordem alfabética: {sorted(Lista)}")
print("-="*10)
print(f"O Chapecoense está na {Lista.index("Chapecoense")}º posição")
