import os
import math
import random
os.system('cls')
print("Sou seu computador...")
n1 = random.randint(0,10)
print("Acabei de pensar em um número de 0 a 10\nSerá que você consegue advinhar qual foi?")
n = int(input("Qual o seu palpite? "))
i = 1
while n != n1:
    if n < n1:
        print("Mais... Tente mais uma vez")
        n = int(input("Qual o seu palpite? "))
        i += 1
    if n > n1:
        print("Menos... Tente mais uma vez")
        n = int(input("Qual o seu palpite? "))
        i += 1
print("Acertou com {} tentativas. Parabéns!".format(i))