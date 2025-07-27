while True:
    l = float(input("Largura da parede: "))
    h = float(input("Altura da parede: "))
    a = l * h #Área parede em m2
    #2 m2 --> 1 L de tinta
    t = a / 2
    print("Sua parede tem a dimensão de {}x{} e sua área é de {} m^2.".format(l,h,a))
    print("Para pintar essa parede, você precisará de {:.4f}L. \n".format(t))
    
    
