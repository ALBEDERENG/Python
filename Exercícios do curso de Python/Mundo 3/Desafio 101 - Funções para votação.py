import os
import math
os.system('cls')
from datetime import datetime
def voto():
    print("___"*30)
    n = int(input("Em que ano você nasceu? "))
    n1 = datetime.now().year
    if n1 - n >= 18:
        c =print(f"Com {n1 - n} anos: VOTO OBRIGATÓRIO")
    elif 16 <= n1 - n < 18:
        c=print(f"Com {n1 - n} anos: VOTO OPCIONAL")
    else:
        c=print(f"Com {n1 - n} anos: VOTO NEGADO")
    return c
voto()