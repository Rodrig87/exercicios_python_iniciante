base = float(input("Digite o valor da base do triagulo: "))

while base == 0 :
    print("Você digitou 0, precisa digitar um número maior que 0")
    base = float(input("Digite o valor da base do triagulo: "))

altura = float(input("Digite o valor da altura do triagulo: "))

while altura == 0:
    print("Você digitou 0, precisa digitar um número maior que 0")
    altura = float(input("Digite o valor da altura do triagulo: "))

area = (base * altura) /2

print(area)
