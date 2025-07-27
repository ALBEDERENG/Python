import os
import math
os.system('cls')
n = input("Qual é o seu nome completo? ")
print("Seu nome tem Silva? {}".format((((n.lower()).title()).find("Silva"))!=-1))