#n = input("Informe um número: ")
#print("Analisando o número {}".format(n))
#print("Unidade: {}".format(n[3]))
#print("Dezena: {}".format(n[2]))
#print("Centena: {}".format(n[1]))
#print("Milhar: {}".format(n[0]))


#A seguinte alternativa forma visa trabalhar com o valor passado de str para int, com a possiblidade de realizar cálculos
n = int(input("Informe um número: "))
print("Analisando o número {}".format(n))
n1 = n // 1 % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
n4 = n // 1000 % 10 #Em n4, % 10 não é necessário
print("Unidade: {}".format(n1))
print("Dezena: {}".format(n2))
print("Centena: {}".format(n3))
print("Milhar: {}".format(n4))