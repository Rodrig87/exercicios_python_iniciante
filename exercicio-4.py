idade = int(input("Digite sua idade: "))
mes = int(input("Digite o mês do seu nascimento: "))
mes_atual = int(input("Digite o mês atual: "))
ano = 0

if mes >= mes_atual:
    ano = 2023 - idade - 1
else:
    ano = 2023 - idade

print(f"Você nasceu no ano de {ano}")