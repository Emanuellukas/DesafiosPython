print("======== Desafio 34 ========")
#Lê o salário de um funcionário e calcula o valor do seu aumento
#Salário superior a R$1250.00 = 10%
#Salário inferior ou igual a R$1250.00 = 15%

salario = float(input("Digite o seu salário (use '.' para valores decimais): "))

if salario > 1250.00:
    aumento = (salario*10)/100
    salario += aumento
else:
    aumento = (salario*15)/100
    salario += aumento

print("Seu novo salário é: R${:.2f}".format(salario))