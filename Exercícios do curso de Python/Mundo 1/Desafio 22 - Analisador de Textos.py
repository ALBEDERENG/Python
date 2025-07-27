n = input("Digite seu nome completo: ")
print("Analisando seu nome...")
print("Seu nome em maiúsculo é {}".format(n.upper()))
print("Seu nome em minúsculo é {}".format(n.lower()))
print("Seu nome possui {} letras".format(len(n)-n.count(" ")))
n1 = n.split()
n2 = n1 [0]
print("Seu primeiro nome é {} e ele tem {} letras".format(n2,len(n2)))