import os
import math
os.system('cls')
Lista = []
a = int(input("Digite um valor: "))
Lista.append(a)
print("Valor adicionado com sucesso...")
while True:
    n1 = ((input("Quer continuar? ")).upper()).strip()
    if n1 == "N":
        break
    n = int(input("Digite um valor: "))
    if n in Lista:
        print("Valor duplicado! Não vou adicionar...")
    else:
        Lista.append(n)
        print("Valor adicionado com sucesso...")
print("-=-"*30)
print(f"Você digitou os valores: {sorted(Lista)}")
    