import os
import math
os.system('cls')
n = input("Digite uma frase: ")
n1 = n.upper()
#print(n1)
n2 = n1.split()
#print(n2)
n3 = "".join(n2)
#print(n3)
inverso=""
for i in range(len(n3) - 1,-1,-1):
    inverso += n3[i]
print("O inverso de {} é {}".format(n3,inverso))
if inverso == n3:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é palíndromo!")