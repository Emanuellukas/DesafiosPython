print("======== Desafio 29 ========")
#Lê a velocidade de um carro, se ele ultrapassar 80Km/h, exibir que ele foi multado
#Calcular a multa com R$7.00 a cada Km ultrapassado

vel = int(input("Digite a velocidade (apenas números) em Km/h: "))

if vel > 80:
    km = vel - 80
    multa = km * 7
    print("Você foi multado, e o valor da multa equivale a R${:.2f}.".format(multa))
else:print("Velocidade adequada. Sem multa.")
