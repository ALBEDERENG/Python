import os
import math
import random
os.system('cls')
print("=-"*20)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
print("=-"*20)
n1 = random.randint(0,5)
n = int(input("Em que número eu pensei? "))
print ("PROCESSANDO...")
if n == n1:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}".format(n1,n))