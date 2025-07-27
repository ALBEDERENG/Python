import os
import math
os.system('cls')
print(f"{"":-^30}")
print(f"{"LISTA DE PREÇOS":^30}")
print(f"{"":-^30}")
TO = ("Lápis", "Borracha", "Caderno", "Estojo",
      "Tranferidor", "Compasso","Mochila","Canetas"
      ,"Livros")
TP = (1.75,2.00,15.90,25.00,4.20,9.99,120.32,22.30,34.90)
for i in range(len(TO)):
    print(f"{TO[i]:.<30} R$ {TP[i]}")
print(f"{"":-^30}")