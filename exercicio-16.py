horaInicio = int(input("Digite a hora do inicio do jogo: "))
horaFim = int(input("Digite a hora do fim do jogo: "))

if horaInicio <= horaFim:
    duracao = horaFim - horaInicio
    print(duracao)
else:
    duracao = 24 - horaInicio + horaFim
    print(f"O jogo teve duração de {duracao} horas")