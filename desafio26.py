print("======== Desafio 26 ========")
#Importando abaixo uma biblioteca de tempo para um teste
from time import sleep

#Lê uma frase qualquer e:
# . Quantas vezes a letra "A" aparece
# . Em que posição aparece pela primeira vez
# . Em que posução ela aparece a última vez

#frase = input("Digite uma frase qualquerm, de preferência uma frase longa: ")
frase = "O Arthur trabalha na Life Tecnologia e Consultoria"
print("Analisando a frase...")

def tempo():
    sleep(0.2)
    print("Na sua frase a letra 'a' aparece {} vezes.".format(frase.lower().count('a')))
    print("A letra 'a' aparece pela primeira vez na posição {}.".format(frase.lower().find('a')))
    print("E ela aparece pela última vez na posição {}.".format(frase.rfind('a')))

print(tempo())