import os
import math
os.system('cls')
def leiaInt (n):
    print("---"*30)
    while True:
        n1 = (input(n)).strip()
        n2 = n1.isnumeric()
        if n2 == False:
            print("ERRO! Digite um número inteiro válido.")
        else:
            n = n1
            return n
            break





n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")