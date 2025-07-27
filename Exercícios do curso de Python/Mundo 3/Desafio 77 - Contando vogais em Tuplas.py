import os
import math
os.system('cls')
Palavras = ("APRENDER","PROGRAMAR","LINGUAGEM","PYTHON","CURSO","GRÁTIS")
for i in Palavras:
    print(f"\nNa palavra {i} temos ", end="")
    for letra in i:
        if letra.lower() in "aáâeéêiíoóôuúû":
            print(letra,end="")