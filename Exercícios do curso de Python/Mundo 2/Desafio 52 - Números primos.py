import os
import math
os.system('cls')
n = int(input("Digite um número: "))
a = 0
for i in range(1, n+1):
    if n % i == 0:
        print("\033[1;33m{}\033[m".format(i),end=" ")
        a = a + 1
    if n % i != 0:
        print("\033[1;31m{}\033[m".format(i),end=" ")
print("\nO número {} foi divisível {} vezes".format(n,a))
if a == 2 or a == 1:
    print("E por isso ele É PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")
