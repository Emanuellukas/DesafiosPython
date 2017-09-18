from math import sqrt

print("======== Desafio 06 ========")
#Algorítimo que lê um número e mostra o seu dobro, triplo e sua ráiz quadrada

n1 = int(input("Digite um valor: "))
#Dobro
d = int(n1 * 2)
#Triplo
t = int(n1 * 3)
#Raíz
r = sqrt(n1)

print("O dobro de {} é {}, seu triplo equivale a {} e sua raíz quadrada equivale a {}".format(n1, d, t, r))

#Maneiras diferentes de exibir na tela o mesmo resultado
print("O dobro de", n1, "é", d, ", seu triplo é", t, "e sua raíz quadrada equivale a", r)
print("O dobro de {} é".format(n1), d, ", seu triplo é", t, "e sua raíz quadrada equivale a", r)

