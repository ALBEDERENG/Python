import os
import math
os.system('cls')
n = int(input("Ano de nascimento: "))
n1 = 2017 - n
print("Quem nasceu em {} tem {} anos em 2017.".format(n,n1))
na = n + 18
if n1 < 18:
    print("Ainda faltam {} anos para o alistamento".format(na-2017))
    print("Seu alistamento será em {}.".format(na))
elif n1 > 18:
    print("Você já deveria ter se alistado há {} anos".format(2017 - na))
    print("Seu alistamento foi em {}.".format(na))
else:
    print("Você tem que se alistar IMEDIATAMENTE")