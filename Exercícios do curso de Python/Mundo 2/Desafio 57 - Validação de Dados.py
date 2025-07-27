import os
import math
os.system('cls')
n = ((input("Informe seu sexo: [M/F] ")).upper()).strip()
#if n != "M" and n != "F":
#    while True:
#        if n == "M":
#            print("Sexo {} registrado com sucesso".format(n))
#            break
#        elif n == "F":
#            print("Sexo {} registrado com sucesso".format(n))
#            break
#        else:
#            n = ((input("Dados inválidos! Por favor, informe seu sexo: ")).upper()).strip()
#else:
#    print("Sexo {} registrado com sucesso".format(n))

while n not in "MmFf":
    n = ((input("Dados inválidos! Por favor, informe seu sexo: ")).upper()).strip()
print("Sexo {} registrado com sucesso".format(n))