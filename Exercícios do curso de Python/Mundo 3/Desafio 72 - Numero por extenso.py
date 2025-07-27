import os
import math
os.system('cls')
n = int(input("Digite um número entre 0 e 20: "))
while n not in range(0,21):
    n = int(input("Tente novamente. Digite um número entre 0 e 20: "))

conjunto = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "desesseis", "desessete", "dezoito", "dezenove", "vinte")
print(f"Você digitou o número {conjunto[n]}")