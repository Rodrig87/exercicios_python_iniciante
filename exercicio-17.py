maca = int(input("Digite a quantidade de maças que você deseja comprar: "))

if maca < 12:
    valor = 1.3
    valorTotal = maca * valor
    print(f"Você comprou {maca} maças, o valor total foi de R${valorTotal}")
else:
    valor = 1
    valorTotal = maca * valor
    print(f"Você comprou {maca} maças, o valor total foi de R${valorTotal}")