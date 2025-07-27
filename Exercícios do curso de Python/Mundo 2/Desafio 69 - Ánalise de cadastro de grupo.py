import os
import math
os.system('cls')
count = 0
m = 0
f = 0
i = 0
j = 0
while True:
    count += 1
    print("---"*10)
    print("CADASTRE UM PESSOA")
    print("---"*10)
    n = int(input("Idade: "))
    n1 = (input("Sexo: [M/F] ").upper()).strip()
    if n1 == "M":
        m += 1
    if n1 == "F":
        f += 1
        if n < 20:
            j += 1
    if n > 18:
        i += 1
    print("---"*10)
    n2 = (input("Quer continuar? [S/N] ").upper()).strip()
    if n2 == "N":
        print("O total de pessoas com mais de 18 anos: {}".format(i))
        print("Ao todo temos {} homens cadastrados".format(m))
        print("E temos {} mulheres com menos de 20 anos".format(j))
        break