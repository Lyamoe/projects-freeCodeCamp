def contaSegundos (tempo):
    if tempo >= 86400:
        dias = tempo // 86400
        tempo = tempo % 86400
    else:
        dias = 0
    if  tempo >= 3600:
        horas = tempo // 3600
        tempo = tempo % 3600
    else:
        horas = 0
    if  tempo >= 60:
        minutos = tempo // 60
        tempo = tempo % 60
    else:
        minutos = 0
    segundos = tempo

    print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")

ent = int(input("Por favor, entre com o número de segundos que deseja converter:"))
contaSegundos(ent)