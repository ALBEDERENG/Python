import random
while True:
    n = str(input("Primeiro aluno: "))
    n1 = str(input("Segundo aluno: "))
    n2 = str(input("Terceiro aluno: "))
    n3 = str(input("Quarto aluno: "))

    print("O aluno escolhido foi {}\n".format(random.choice([n, n1, n2, n3])))
