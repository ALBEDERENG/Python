import os
import math
os.system('cls')

def ficha():
    nome = str(input("Nome do jogador: "))
    gols = str(input("Número de Gols: "))
    if nome == "":
        nome = "<desconhecido>"
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print("---"*30)
    c = print(f"O jogador {nome} fez {gols} gol(s) no campeonato")
    return c
ficha()