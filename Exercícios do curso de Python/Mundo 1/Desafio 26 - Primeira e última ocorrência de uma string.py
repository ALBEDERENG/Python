import os
import math
os.system('cls')
n = input("Digite uma frase: ")
print("A letra A aparece {} vezes na frase.".format(((n.strip()).upper()).count("A")))
print("A primeira letra A apareceu na posição {}".format(int(((n.strip()).upper()).find("A")) + 1))
print("A última letra A apareceu na posição {}".format(int(((n.strip()).upper()).rfind("A")) + 1))