import os
import math
os.system('cls')
Dados = {}
Dados[0]="Nome"
Dados[1]="Média"
Dados[2]="Situação"
Nome = input("Nome: ")
Média = float(input("Média: "))                                                         
print("-="*30)
print(f"- Nome é igual a {Nome}")
print(f"- Média é igual a {Média}")
if Média >= 7:
    Situação = "aprovado"
elif 5<=Média<7:
     Situação = "recuperação"
else:
     Situação = "reprovado"
print(f"- A situação é {Situação}")
