from random import randint
from random import choice
print("======== Desafio 28 ========")
#Algorítimo que faz o computador "pensar" em um número inteiro entre 0 e 5, e pede para que
#  o usuário adivinhe qual foi o número escolhido. Exiba na tela se ele acertou ou não

numpc = int(randint(0, 5))
numu = int(input("Adivinhe o número (entre 0 e 5) que o computador gerou: "))

if numu > 5:
    print("Digite um número menor ou igual a 5, zé ruela!")
else:
    if numu == numpc:
        print("Mas que sorte! Você acertou!")
    else:
        print("Que azar, hein. Você errou.")