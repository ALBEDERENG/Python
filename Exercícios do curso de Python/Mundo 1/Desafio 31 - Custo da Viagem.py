import os
import math
os.system('cls')
n = float(input("Qual a distância de sua viagem? "))
print("Você está prestes a começar uma viagem de {}Km.".format(n))
if n > 200:
    print("E o preço da sua passagem será de R${}".format(n * 0.45))
else:
    print("E o preço da sua passagem será de R${}".format(n * 0.50))    