import os
import math
os.system('cls')
n = float(input("Primeir nota: "))
n1 = float(input("Segunda nota: "))
n2 = (n + n1)/2
if n2 < 5:
    print("Tirando {} e {}, a média do aluno é {:.1f}".format(n,n1,n2))
    print("O aluno está REPROVADO.")
elif 5 <= n2 <= 6.9:
    print("Tirando {} e {}, a média do aluno é {:.1f}".format(n,n1,n2))
    print("O aluno está em RECUPERAÇÃO.")
else:
    print("Tirando {} e {}, a média do aluno é {:.1f}".format(n,n1,n2))
    print("O aluno está APROVADO.")