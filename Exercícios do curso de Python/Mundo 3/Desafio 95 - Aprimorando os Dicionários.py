import os
import math
os.system('cls')
Dado = {}
DadoIndividual = {}
ListaGols = []
count = 0
while True:
    soma = 0
    count += 1
    DadoIndividual["Nome"]=input("Nome do jogador: ")
    n = int(input("Quantas partidas jogou? "))
    for i in range(1,n+1):
        g = int(input(f"Quantos gols fez na partida {i}? "))
        ListaGols.append(g)
        DadoIndividual["Gols"] = ListaGols.copy()
        soma += g
    DadoIndividual["Soma"] = soma
    ListaGols=[]
    n1 = (input("Quer continuar? ").upper()).strip()
    Dado[count]=DadoIndividual.copy()
    if n1 in "Nn":
        break
count = 0
print("-=-"*30)
#print(" cod nome        gols    total")
print(f"{"cod":>4}    {"nome":<15}  {"gols":<15}  {"total":<15}")
print("---"*30)
#print(Dado)
for c in Dado:
    count+=1
    k = count-1
    print(f"{k:>4}   {Dado[count]["Nome"]:<15}  {Dado[count]["Gols"]}{"":7}   {Dado[count]["Soma"]}")
print("---"*30)
count = 0
#print(Dado)
while True:
    n2 = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if n2 == 999:
        break
    print(f"-- LEVANTAMENTO DO JOGADOR {Dado[n2+1]["Nome"]}:")
    for j in Dado[n2+1]["Gols"]:
        count+=1
        print(f"No jogo {count} fez {Dado[n2+1]["Gols"][count-1]} gols.")
    count=0
    print("---"*30)
print("<< VOLTE SEMPRE >>")