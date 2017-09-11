print("======== Desafio 22 ========")
#Lê o nome completo de uma pessoa e exibe:
# . O nome com todas as letras maiúsculas
# . O nome com todas minúsculas
# . Quantas letras ao todo (sem considerar espaços)
# . Quantas letras tem o primeiro nome

#nome = input("Digite seu nome completo: ").strip()
nome = "Lucas Emanuel da Silva Nunes"
letras = len(nome) - nome.count(' ')  # serve para facilitar nas funções extras
dividido = nome.split()  # também serve para facilitar nas funções extras
print("Seu nome em maiúsculo: ", nome.upper())
print("Seu nome em minúsuculo: ",nome.lower())
print("Número de letras no seu nome: {}".format(letras))
print("Primeiro nome: {}. Ele tem {} letras".format(dividido[0], len(dividido[0])))
