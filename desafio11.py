import math
print("======== Desafio 11 ========")
#Lê a largura e a altura de uma parede em metros, calcula a sua área e a quantidade
#de tinta necessária para pintála, sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Agora a largura: "))

area = altura*largura
mlata = int(2**2) #quantos metros uma lata pinta em m²
qtdlata = int(area/mlata)

print("Sua área é {}m²".format(area))
print("Sabendo que cada litro pinta 2m², você precisará de {} litros para pintar"
      "totalmente a parede.".format(qtdlata))