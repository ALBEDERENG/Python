import os
import math
os.system('cls')
os.system('cls')
for i in range(1,6):
    n = float(input("Peso da {} pessoa: ".format(i)))
    if i == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    

print("O maior peso lido foi {:.1f} Kg".format(maior))
print("O menor peso lido foi {:.1f} Kg".format(menor))