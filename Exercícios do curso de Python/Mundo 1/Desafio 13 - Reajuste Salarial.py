while True:
    n = float(input("Qual é o salário do Funcionário? R$"))
    np = n + (n * 15/100)
    print("Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}\n". format(n,np))
