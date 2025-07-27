import os
import math
os.system('cls')
Dado = {}
DadoIndividual = {}
ListaM = []
count = 0
soma = 0
k = -1
while True:
    count +=1
    DadoIndividual["Nome"]=input("Nome: ")
    while True:
        n = DadoIndividual["Sexo"]=(input("Sexo: [M/F] ").upper()).strip()
        if n not in "MmFf":
            print("Erro! Por favor digite apenas M ou F.")
        else:
            break
    if n in "Ff":
            ListaM.append(DadoIndividual["Nome"])
    DadoIndividual["Idade"]=int(input("Idade: "))
    soma += DadoIndividual["Idade"]
    média = soma / count
    while True:
        n1 = input("Quer continuar? ")
        if n1 not in "SsNn":
            print("Erro! Por favor digite apenas S ou N.")
        else:
            break
    Dado[count-1] = DadoIndividual.copy()
    if n1 in "Nn":
        break
print("-=-="*30)
#print(DadoIndividual)
#print(Dado)
print(f"A) Ao todo foram {count} pessoas.")
print(f"B) A média de idade é de {média:.2f} anos.")
print(f"C) As mulheres cadastradas foram ",end="")
for i in ListaM:
    print(i,end=" ")
print()
print(f"D) Lista das pessoas pessoas que estão acima da média: ")
while k < count-1:
    k += 1
    if Dado[k]["Idade"] > média:
        print(f"    nome = {Dado[k]["Nome"]};   sexo = {Dado[k]["Sexo"]};   idade = {Dado[k]["Idade"]};")
print("<< ENCERRADO >>")
