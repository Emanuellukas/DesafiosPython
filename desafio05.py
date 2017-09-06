print("======== Desafio 05 ========")
#Ler um número inteiro e mostrar na tela o seu sucessor e seu antecessor

n1 = int(input("Digite um valor: "))
#Sucessor
ns = int(n1 + 1)
#Antecessor
na = int(n1 - 1)

print("O número sucessor a {} é {}, e seu antecessor é {}".format(n1, ns, na))