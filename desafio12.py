import math
print("======== Desafio 12 ========")
#Algoritimo mostra o valor do preço atual de acordo com o desconto

valor = float(input("Digite o valor original do produto: "))
desconto = float(input("Agora a porcentagem de desconto: "))
valordes = float((valor*desconto)/100)
result = float(valor-valordes)
print("O valor do produto (R${:.2f}) com desconto de {}% tem o valor final de: R${:.2f}".format(valor, desconto, result))