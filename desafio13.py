import math
print("======== Desafio 13 ========")
#Aumento no salário de acordo com a porcentagem

salario = float(input("Digite o seu salário atual: "))
aumento = float(input("Agora a porcentagem do aumento: "))
valoraumento = float((salario*aumento)/100)
novo = float(salario+valoraumento)
print("O seu salário que era R${:.2f} passa a ser R${:.2f}".format(salario, novo))