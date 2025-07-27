import os
import math
os.system('cls')
n = float(input("Qual é o salário do funcionário? "))
if n > 1250:
    n1 = n + (n*0.1)
else:
    n1 = n + (n*0.15)
print("Quem ganhava R${:.2f} passa a ganhar {:.2f} agora.".format(n,n1))
