import random
n = str(input("Primeiro aluno: "))
n1 = str(input("Segundo aluno: "))
n2 = str(input("Terceiro aluno: "))
n3 = str(input("Quarto aluno: "))
lista = [n, n1, n2, n3]
random.shuffle(lista)
print ("A ordem de apresentação será\n{}".format(lista))
