import os
import math
os.system('cls')
n = input("Digite seu nome completo: ")
print("Muito prazer em te conhecer!")
n1 = n.split()
n2 = len(n1)
print("Seu primeiro nome é {}".format(n1[0]))
print("Seu último nome é {}".format(n1[n2-1]))