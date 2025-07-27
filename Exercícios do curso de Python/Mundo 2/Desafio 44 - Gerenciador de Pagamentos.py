import os
import math
os.system('cls')
print("="*10+"LOJAS GUANABARA"+"="*10)
n = float(input("Preços das compras: R$ "))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
n1 = int(input("Qual é a opção? "))
if n1 == 1:
    n2 = n - 0.1*n
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(n,n2))
elif n1 == 2:
    n2 = n - 0.05*n
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(n,n2))
elif n1 == 3:
    n2 = n / 2
    print("Sua compra será parcelada em {:.1f}x de R${:.2f}".format(2,n2))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(n,n2*2))
elif n1 == 4:
    n3 = float(input("Quantas parcelas? "))
    n2 = (n + 0.2*n) / n3
    print("Sua compra será parcelada em {:.1f}x de R${:.2f}".format(n3,n2))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(n,n2*n3))