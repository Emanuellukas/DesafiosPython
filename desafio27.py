print("======== Desafio 27 ========")
#Lê o nomme de uma pessoa, mostrando o primeiro e o último nome separadamente

#nome = input("Digite seu nome completo: ")
nome = "Lucas Emanuel da Silva Nunes"

print("Seu primeiro nome é: {}".format(nome.split()[0]))
print("Seu último nome é: {}".format(nome.split()[-1]))
