import os
import math
os.system('cls')
count = 0
i = -1
while True:
    i += 1
    if i == 0:
        n = int(input("Quer ver a tabuada de qual valor? "))
    if i >= 1:
        print("---"*10)
        n = int(input("Quer ver a tabuada de qual valor? "))
        print("---"*10)
    if n < 0:
        break
    while count < 10:
        count +=1
        print(f"{n} x {count} = {n * count}")
    count = 0
print("PROGRAMA TABUADA ERRADO. Volte sempre!")
