num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 == num2:
    print("Números iguais")
elif num1 < num2:
    print(f"{num1} {num2}")
else:
    print(f"{num2} {num1}")