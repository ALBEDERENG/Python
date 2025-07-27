import os
import math
os.system('cls')
n = float(input("Qual o seu peso? (Kg) "))
n1 = float(input("Qual é sua altura? (m) "))
n2 = n / (n1**2)
print("O IMC dessa pessoa é de {:.1f}".format(n2))
if n2 < 18.5:
    print("Você está ABAIXO DO PESO normal")
elif 18.5 <= n2 < 25:
    print("PARABÉNS, você esta na faixa de PESO NORMAL")
elif 25 < n2 <= 30:
    print("Você está em estado de SOBREPESO")
elif 30 < n2 <= 40:
    print("Você está em OBESIDADE!")
else:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")