while True:
    num = int(input("Digite um número: "))

    perg = input("Digite 1 para ver o sucessor - 2 para ver o antecessor - 3 para encerrar: ")
    if perg == '1':
        print(num+1)
    elif perg == '2':
        print (num-1)
    else:
        break
