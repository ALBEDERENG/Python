import os
import math
os.system('cls')
'''
n = str(input("Digite a expressão: "))
n1 = n.count("(")
n2 = n.count(")")
if n1 == n2:
    print("Sua expressão está correta")
else:
    print("Sua expressão está errada")
'''
Listaabre = []
Listafecha =[]
n = str(input("Digite a expressão: "))
for i in n:
    if i == "(":
        Listaabre.append(i)
    elif i == ")":
        Listafecha.append(i)
if len(Listaabre) == len(Listafecha):
    print("Sua expressão está correta")
else:
    print("Sua expressão está errada")