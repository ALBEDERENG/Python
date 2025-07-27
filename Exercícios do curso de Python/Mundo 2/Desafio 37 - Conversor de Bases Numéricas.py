import os
import math
os.system('cls')
n = int(input("Digite um número inteiro: "))
print("[ 1 ] Converter para BINÁRIO")
print("[ 2 ] Converter para OCTAL")
print("[ 3 ] Converter para HEXADECIMAL")
n1 = int(input("Escolha uma das bases para conversão: "))
if n1 == 1:
    print("Sua opção: {}".format(n1))
    n2 = bin(n)
    print("{} convertido para BINÁRIO é igual a {}".format(n,n2[2:]))
elif n1 == 2:
    print("Sua opção: {}".format(n1))
    n2 = oct(n)
    print("{} convertido para OCTAL é igual a {}".format(n,n2[2:]))
elif n1 == 3:
    print("Sua opção: {}".format(n1))
    n2 = hex(n)
    print("{} convertido para HEXADECIMAL é igual a {}".format(n,n2[2:]))
