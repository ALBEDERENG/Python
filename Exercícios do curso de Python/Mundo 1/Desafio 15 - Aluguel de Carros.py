while True:
    nd = float(input("Quantos dias alugados? "))
    nkm = float(input("Quantos Km rodados? "))
    np = (60*nd) + (0.15*nkm)
    print("O total a pagar é de R${:.2f}\n".format(np))
