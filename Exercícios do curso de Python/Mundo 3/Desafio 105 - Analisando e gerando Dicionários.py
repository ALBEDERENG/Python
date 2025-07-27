import os
import math
os.system('cls')
def notas(*resp,sit = False):
    print("---"*30)
    dados = {}
    count = 0
    #print(resp)
    dados["total"] = len(resp)
    dados["maior"]  = max(resp)
    dados["menor"]  = min(resp)
    dados["media"] = (sum(resp)/ len(resp))
    if sit == True:
        if dados["media"] >= 7:
            dados["situação"] = "APROVADO"
        elif 5 <=dados["media"] <7:
            dados["situação"] = "RECUPERAÇÃO"
        else:
            dados["situação"] = "REPROVADO"
    return dados





resp = notas(5.5,2.5,10,5,10,10,10,sit = True)
print(resp)