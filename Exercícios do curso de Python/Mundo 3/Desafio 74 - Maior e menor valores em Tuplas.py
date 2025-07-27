import os
import math
os.system('cls')
import random
i = 0
Lista = []
while i <= 4:
    i += 1
    n = random.randint(0,10)
    Lista.append(n)
print(f"Os valores sorteados foram: {Lista}")
print(f"O maior número sorteado foi {max(Lista)}")
print(f"O menor número sorteado foi {min(Lista)}")
