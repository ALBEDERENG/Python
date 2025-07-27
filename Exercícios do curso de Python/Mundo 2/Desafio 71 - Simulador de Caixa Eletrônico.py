import os
import math
os.system('cls')
print("==="*10)
print("{:^30}".format("BANCO CEV"))
print("==="*10)
n = int(input("Que valor você quer sacar? R$"))
while True:
    n1 = n // 50
    n2 = n % 50
    #print(n1)
    #print(n2)
    n3 = n2 // 20
    n4 = n2 % 20
    #print(n3)
    #print(n4)
    n5 = n4 // 10
    n6 = n4 % 10
    #print(n5)
    #print(n6)
    n7 = n6 // 1
    n8 = n6 % 1
    #print(n7)
    #print(n8)
    break
if n1 > 0:
    print("Total de {} cédulas de R$50".format(n1))
if n3 > 0:
    print("Total de {} cédulas de R$20".format(n3))
if n5 > 0:
    print("Total de {} cédulas de R$10".format(n5))
if n7 > 0:
    print("Total de {} cédulas de R$1".format(n7))
print("==="*10)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")