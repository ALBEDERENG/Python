while True:
    n = float(input("Qual o preço do produto? R$"))
    nf = n - (n * (5/100))
    print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}\n".format(n,nf))
