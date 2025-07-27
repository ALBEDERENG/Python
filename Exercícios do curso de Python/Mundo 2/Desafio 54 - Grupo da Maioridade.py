import os
import math
j = 0 #Menor de idade
k = 0
os.system('cls')
for i in range(1,8):
    n = int(input("Em que ano a {} pessoa nasceu? ".format(i)))
    if 2017 - n < 21: 
        j = j + 1
    elif 2017 - n >= 21:
        k = k + 1
print("Ao todo tivemos {} pessoas maiores de idade".format(k))
print("E também tivemos {} pessoas menores de idade".format(j))