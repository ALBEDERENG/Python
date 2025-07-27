import os
import math
os.system('cls')
Dado = {}
Lista = []
soma = 0
count=0
a = Dado["Nome"] = input("Nome do jogador: ")
n = int(input(f"Número de partidas {Dado["Nome"]} jogou? "))
for i in range(0,n):
    n1 = int(input(f"   Quantos gols na partida {i}? "))
    n2 = Lista.append(n1)
    soma += n1
Dado["Gols"]=Lista
Dado["total"]=soma
print("-="*30)
print(Dado)
print("-="*30)
for c,v in Dado.items():
    print(f"O campo {c} tem o valor {v}")
print("-="*30)
print(f"O jogador {a} jogou {len(Lista)} partidas")
for count in range(0,len(Lista)):
    print(f"    =>Na partida {count}, fez {Dado["Gols"][count]} gols.")
print(f"Foi um total de {soma} gols.")