num_lista = int(input("Digite quantos números você vai querer: "))
soma = 0


for x in range (1,num_lista+1):
    num = (int(input("Digite um número: ")))
    soma = soma + num
media = soma / num_lista

print(f"A soma total é de {soma} e a média é {media}")
