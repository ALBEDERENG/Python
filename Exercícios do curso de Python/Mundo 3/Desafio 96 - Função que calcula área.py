import os
import math
os.system('cls')
print(f"{"Controle de terrenos":^30}")
print("-"*30)
def area(L,C):
    area = L*C
    print(f"A área do terreno {L}x{C} é de {area}m^2")


L = float(input("LARGURA (m): "))
C = float(input("COMPRIMENTO (m): "))
area(L,C)