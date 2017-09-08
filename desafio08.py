import math
print("======== Desafio 08 ========")
#Algoritimo que leia um valor em metros e os exiba convertido em centímetro e milímetros

valor = int(input("Digitem um valor em metros: "))
result = int(valor * 100)

print("Valor em centímetros: {}cm".format(result))
result = int(valor * 1000)
print("Valor em milímetros: {}mm".format(result))