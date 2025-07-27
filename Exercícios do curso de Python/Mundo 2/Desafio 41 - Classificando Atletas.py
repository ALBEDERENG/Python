import os
import math
os.system('cls')
n = int(input("Ano de Nascimento: "))
n1 = 2017 - n
print("O atleta tem {} anos.".format(n1))
if n1 <= 9:
    print("Classificação: MIRIM")
elif 9 < n1 <= 14:
    print("Classificação: INFANTIL")
elif 14 < n1 <= 19:
    print("Classificação: JÚNIOR")
elif 19 < n1 <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")