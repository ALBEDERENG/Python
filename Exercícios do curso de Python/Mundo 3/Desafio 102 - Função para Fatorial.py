import os
import math
os.system('cls')

def fatorial(n,show=False):
    '''
    -->Calcula o fatorial de um número.
    Para n: O número a ser calculado.
    para show: (opcional) Mostrar ou não a conta.
    return: O valor do fatorial de um número.

    '''
    print("---"*30)
    c = 1
    for i in range(n,1,-1):
        c*=i
    if show == True:
        print(f"{i} x",end=" ")
        k = print(f"1 = {c}")
    elif show == False:
        k = print(f"{c}")
    return (k)
fatorial(2,True)
#help(fatorial)