print("======== Desafio 33 ========")
#Lê 3 números e diz qual é o maior e qual é o menor

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O maior valor é {}".format(n1))
elif n2 > n1 and n2 > n3:
    print("O maior valor é {}".format(n2))
else: print("O maior valor é {}".format(n3))