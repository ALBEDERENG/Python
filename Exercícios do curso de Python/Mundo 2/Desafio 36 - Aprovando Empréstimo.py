import os
import math
os.system('cls')
n = float(input("Valor da casa: R$"))
n1 = int(input("Salário do comprador: R$"))
n2 = float(input("Quantos anos de finaciamento? "))
p = n / (n2*12)
if p >= (0.3 *n1):
    print("Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}".format(n,n2,p))
    print("Empréstimo NEGADO!")
else:
    print("Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}".format(n,n2,p))
    print("Empréstimo pode ser CONCEDIDO!")