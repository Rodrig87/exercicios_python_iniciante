num = int(input("Digite um número: "))
sucessor = num + 1
antecessor = num - 1
perg = int(input("Digite 1 para ver o antecessor - 2 para ver o antecessor - 3 para encerrar: "))

if perg >= 3 or perg <=0:
    print("Programa encerrado")
elif perg == 1:
    print(sucessor)
else:
    print(antecessor)

