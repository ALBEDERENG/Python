import os
import math
os.system('cls')
n = float(input("Qual a velocidade atual do carro? "))
if n >= 80:
    n1 = (n - 80) * 7
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print("Você deve pagar uma multa de R${}!".format(n1))
print("Tenha um bom dia! Dirija com segurança!")