import os
import math
os.system('cls')
print("---"*10)
print("{:^30}".format("LOJA SUPER BARATÃO"))
print("---"*10)
count = 0
p = 0
M = 0
s = 0
m = float('inf')
m1 = 0
while True:
    count+=1
    n = (input("Nome do produto: ").upper()).strip()
    n1 = float(input("Preço: R$"))
    n2 = (input("Quer continuar? ").upper()).strip()
    if n1 > M:
        M = n1
    if n1 > 1000:
        p += 1
    if n1 < m:
        m = n1
        m1 = n
    s += n1
    if n2 == "N":
        break
print("---"*10,"FIM DO PROGRAMA","---"*10)
print("O total foi {:.2f}".format(s))
print("Temos {} produto custando mais de R$1000".format(p))
print("O produto mais barato foi {} que custa R${:.2f}".format(m1,m))


    
