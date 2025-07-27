Ent = input("Digite algo ")
print ("O tipo primitivo desse valor é", type (Ent))

t1 = Ent.isalnum()
t2 = Ent.isnumeric()
t3 = Ent.isalpha()
t4 = Ent.isupper()
t5 = Ent.islower()
t6 = Ent.istitle()

print ("Só tem espaços?", t1)
print ("É um número?", t2)
print ("É alfabético?", t3)
print ("Está em maiúsculas?", t4)
print ("Está em minúsculas?", t5)
print ("Está capitalizada?", t6)

