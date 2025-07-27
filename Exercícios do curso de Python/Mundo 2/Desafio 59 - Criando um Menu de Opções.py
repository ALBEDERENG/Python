import os
import math
os.system('cls')
n = float(input("Primeiro valor: "))
n1 = float(input("Segundo valor: "))
while True:
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair do programa")
    p = int(input(">"*10+"Qual é a sua opção? "))
    if p == 1:
        print("A soma entre {:.1f} e {:.1f} é {:.1f}".format(n,n1,n+n1))
        print("=-"*10+"\n")
    elif p == 2:
        print("O resultado de {:.1f} x {:.1f} é {:.1f}".format(n,n1,n*n1))
        print("=-"*10+"\n")
    elif p == 3:
        print("Entre {} e {} o número {} é maior".format(n,n1,max(n,n1)))
        print("=-"*10+"\n")
    elif p == 4:
        print("Informe os números novamente:")
        n = float(input("Primeiro valor: "))
        n1 = float(input("Segundo valor: "))
        print("=-"*10+"\n")
    elif p == 5:
        print("Fim do programa. Volte sempre!")
        break
    else:
        print("Opção inválida. Tente novamente")
        print("=-"*10+"\n")
              
