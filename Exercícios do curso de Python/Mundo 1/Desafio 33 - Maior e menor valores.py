import os
import math
os.system('cls')
n = input("Primeiro valor: ")
n1 = input("Segundo valor: ")
n2 = input("Terceiro valor: ")
if n < n1 and n < n2:
    print("O menor valor digitado foi {}".format(n))
    if n1 < n2:
        print("O maior valor digitado foi {}".format(n2))
    else:
        print("O maior valor digitado foi {}".format(n1))
else:
    if n > n1 and n < n2:
        print("O menor valor digitado foi {}".format(n1))
        print("O maior valor digitado foi {}".format(n2))
    else:
        if n > n2 and n < n1:
            print("O menor valor digitado foi {}".format(n2))
            print("O maior valor digitado foi {}".format(n1))
        else:
            if n > n2 and n > n1:
                print("O maior valor digitado foi {}".format(n))
                if n1 > n2:
                    print("O menor valor digitado foi {}".format(n2))
                else:
                    print("O menor valor digitado foi {}".format(n1))
if n == n1 == n2:
    print("Os três valores são iguais")