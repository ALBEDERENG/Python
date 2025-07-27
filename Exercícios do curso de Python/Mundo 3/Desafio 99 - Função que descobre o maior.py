import os
import math
os.system('cls')
def maior(list):
    print("-="*30)
    print("Analisando os valores passados...")
    if list == []:
        print("Foram informados 0 valores ao todo")
        print("O maior valor informado foi 0")
    else:
        for i in list:
            print(f"{i}",end=" ") 
        print(f"foram informados {len(list)} valores ao todo.")
        print(f"O maior valor informado foi {max(list)}.")


Lista = [2,9,4,5,7,1]
maior(Lista)
Lista1 = [4,7,9]
maior(Lista1)
Lista2 = [1,2]
maior(Lista2)
Lista3 = [6]
maior(Lista3)
Lista4 = []
maior(Lista4)