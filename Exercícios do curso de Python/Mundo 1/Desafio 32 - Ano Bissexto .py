import os
import math
os.system('cls')
n = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
n1 = n % 4
n2 = n % 100
n3 = n % 400
if n1 == 0:
    if n2 == 0:
        if n3 == 0:
            print("O ano {} É BISSEXTO".format(n))
        else:
            print("O ano {} NÃO É BISSEXTO".format(n))
    else:
        print("O ano {} É BISSEXTO".format(n))
else:
    print("O ano {} NÃO É BISSEXTO".format(n))

#if ano % 4 == 0 and % 100 != 0 or ano % 400 ==0:
    #print("O ano {} é BISSEXTO".format(ano))
#else:
    #print("O ano {} NÃO é BISSEXTO".format(ano))