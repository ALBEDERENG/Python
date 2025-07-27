import os
import math
os.system('cls')
for i in range(0,10):
    if i % 3 == 0 and i % 2 != 0:
        i += i
        print(i)
        print()
print("A soma de todos os {} valores solicitados é {}".format(i,i))