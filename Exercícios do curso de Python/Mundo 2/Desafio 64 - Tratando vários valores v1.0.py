import os
import math
os.system('cls')
count = 0
s=0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    s +=n
    count += 1
    #print(s)
    if n == 999:
        s = s - 999
        count = count -1
        break
print("Você digitou {} números e a soma entre eles foi {}".format(count,s))
