import os
import math
os.system('cls')
m = 0
s = 0
soma = 0
for i in range(1,2):
    print("--"*4,"{} PESSOA".format(i), "--"*4,)
    n = str(input("Nome: ").strip())
    n1 = int(input("Idade: ").strip())
    n2 = (input("Sexo [M/F]: ").upper()).strip()
    if i == 1:
        m = n1
        nome = n
        #print(m)
    if n1 > m and n2 == "M":
        m = n1
        nome = n
    else:
        if n2 == "F" and n1 < 20:
            s = s + 1
            #print("Números de pessoas do sexo feminino B: {}".format(s))
    soma += n1
    media = (soma)/i
#print(m)
#print(nome)
#print(s)
print("A média de idade do grupo é de {}".format(media))
print("O homem mais velho do grupo tem {} anos e se chama {}".format(m,nome))
print("Ao todo são {} mulheres com menos de 20 anos".format(s))