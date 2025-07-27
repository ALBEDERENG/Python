import os
import math
os.system('cls')
print("Gerador de PA")
print("=-="*5)
n = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
i = 0
k = 0
y = 0
count = 0
j = 0
n1 = 1
while i < 10:
    i += 1
    k = n + (i - 1)*r
    print("{} ->".format(k),end=" ")
    count += 1
    if i == 10:
        print("PAUSA")
        while n1 > 0:    
            n1 = int(input("Quantos termos você quer mostrar a mais? "))
            while j < n1:
                j += 1
                k += r
                print("{} ->".format(k),end=" ")
                count += 1
            j = 0
            if n1 > 0:
                print("PAUSA")
            if n1 == 0:
                print("Progressão finalizada com {} termos".format(count))
#y += 1
#k = n + (y - i)*r
#print("{} ->".format(k),end=" ")
#count += 1
