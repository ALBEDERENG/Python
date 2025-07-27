import os
import math
from datetime import datetime
os.system('cls')
Dado = {}
Dado["Nome"] = input("Nome: ")
n1 = int(input("Ano de nascimento: "))
Dado["Idade"] = datetime.now().year - n1
Dado["Ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if Dado["Ctps"] != 0:
    Dado["contratação"]= int(input("Ano de contratação: "))
    Dado["salário"]=float(input("Salário: R$"))
    Dado["aposentadoria"] = Dado["Idade"] + ((Dado["contratação"] + 35) - datetime.now().year)
print("-=-="*30)
for c,v in Dado.items():
    print(f" - {c} tem o valor {v}")
#if n2 == 0:
