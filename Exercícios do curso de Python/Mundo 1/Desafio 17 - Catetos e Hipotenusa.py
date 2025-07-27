while True:
    import math
    co = float(input("Comprimento do cateto oposto "))
    ca = float(input("Comprimento do cateto adjacente "))
#H = raiz quadrada de (co^2 + ca^2)
    print("A hipotenusa vai medir {:.2f}.\n".format(math.sqrt((co**2)+(ca**2))))

