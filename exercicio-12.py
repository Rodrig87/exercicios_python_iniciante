eleitor = int(input("Digite o número de eleitores: "))
branco = int(input("Digite a quantidade de votos brancos: "))
valido = int(input("Digite a quantidade de votos válidos: "))
nulos = int(input("Digite a quantidade de votos nulos: "))

vbranco = (branco / eleitor)*100
vvalido = (valido / eleitor)*100
vnulos = (nulos / eleitor)*100

votos = print(f"{vbranco}% de votos brancos\n{vvalido}% de votos válidos\n{vnulos}% de votos brancos")


