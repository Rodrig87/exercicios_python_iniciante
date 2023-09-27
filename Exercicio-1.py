senha_correta = '123456'
tentativas = 1
senha = input("Digite sua senha: ")

while senha != senha_correta:
    print(f"Senha incorreta! Você possui {3-tentativas} tentativas")

    if tentativas > 2:
        print("Senha bloqueda!")
        break
    tentativas+=1
    senha = input("Digite sua senha: ")

else:
    print("Logado com sucesso!!")