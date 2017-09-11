print("======== Desafio 24 ========")
#Lê o nome de uma cidade e diz se aela começa ou não com a palavra Santo

cidade = input("Digite o nome da sua cidade: ")

print(cidade.split()[0])

#Usando if

if (cidade.split()[0] == "Santo"):
    print("Sua cidade tem a palavra Santo como primeiro nome!")
else:
    print("Sua cidade não tem a palavra Santo como primeiro nome!")