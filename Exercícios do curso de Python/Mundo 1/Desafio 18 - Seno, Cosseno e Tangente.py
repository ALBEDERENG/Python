while True:
    import math
    n = float(input("Digite o ângulo que você deseja: "))
    print("O ângulo de {} tem o SENO de {:.2f}".format(n,math.sin(math.radians(n))))
    print("O ângulo de {} tem o COSSENO de {:.2f}".format(n,math.cos(math.radians(n))))
    print("O ângulo de {} tem a TANGENTE de {:.2f}\n".format(n,math.tan(math.radians(n))))
