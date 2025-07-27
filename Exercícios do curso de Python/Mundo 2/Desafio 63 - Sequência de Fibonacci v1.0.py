import os
import math
os.system('cls')
print("---"*10)
print("Sequência de Fibonacci")
print("---"*10)
n = int(input("Quantos termos você quer mostrar? "))
print("~~~~"*10)
i = 0
j = 0
k = 1
while i < n:
    y = j + k
    j = k
    k = y
    i+=1
    print("{} ->".format(y),end=" ")
print("FIM")
    