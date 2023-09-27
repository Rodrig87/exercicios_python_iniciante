num = int(input("Digite um número: "))

while num == 0:
    num = int(input("Número inválido, digite novamente: "))

if num < 0:
    print("Esse número é negativo")
else:
    print("Esse número é positivo")