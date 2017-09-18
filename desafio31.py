print("======== Desafio 31 ========")
#Pergunta a distância de uma viagem em Km. Calcula o preço da passagem, cobrando R$0.50 por Km
#para viagens de até 200Km e R$0.45 para viagens mais longas

dist = int(input("Digite a distância da viagem em Km (apenas números): "))

if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45

print("O preço da sua passagem será: R${:.2f}".format(preco))