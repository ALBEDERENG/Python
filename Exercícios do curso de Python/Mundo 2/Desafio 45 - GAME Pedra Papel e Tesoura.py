import os
import math
import random
os.system('cls')
print("Suas opções: ")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")
n = int(input("Qual é a sua jogada? "))
n1 = int(random.randint(0,2))
print("JO")
print("KEN")
print("PO!!!")
print("-="*10)
if n == 0 and n1 == 0:
    print("Computador jogou pedra")
    print("Jogador jogou pedra")
    print("-="*10)
    print("EMPATOU!")
if n == 1 and n1 == 1:
    print("Computador jogou papel")
    print("Jogador jogou papel")
    print("-="*10)
    print("EMPATOU!")
if n == 2 and n1 == 2:
    print("Computador jogou tesoura")
    print("Jogador jogou tesoura")
    print("-="*10)
    print("EMPATOU!")
elif n == 0 and n1 == 1:
    print("Computador jogou papel")
    print("Jogador jogou pedra")
    print("-="*10)
    print("COMPUTADOR VENCEU")
elif n == 1 and n1 == 0:
    print("Computador jogou pedra")
    print("Jogador jogou papel")
    print("-="*10)
    print("JOGADOR VENCEU")
elif n == 0 and n1 == 2:
    print("Computador jogou tesoura")
    print("Jogador jogou pedra")
    print("-="*10)
    print("JOGADOR VENCEU")
elif n == 2 and n1 == 0:
    print("Computador jogou pedra")
    print("Jogador jogou tesoura")
    print("-="*10)
    print("COMPUTADOR VENCEU")
elif n == 1 and n1 == 2:
    print("Computador jogou tesoura")
    print("Jogador jogou papel")
    print("-="*10)
    print("COMPUTADOR VENCEU")
elif n == 2 and n1 == 1:
    print("Computador jogou papel")
    print("Jogador jogou tesoura")
    print("-="*10)
    print("JOGADOR VENCEU")