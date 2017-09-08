import math
print("======== Desafio 10 ========")
#Algoritimo que diga quantos dólares vocÊ pode comprar de acordo com o valor que possui em reais

print("Descubra quantos dólares você pode comprar!")
reais = float(input("Digite quantos reais você quer trocar: "))
pdolar = float(3.27)
result = float(reais/pdolar)

print("Com R${:.2f} você vai adquirir U${:.2f}.".format(reais,result))


