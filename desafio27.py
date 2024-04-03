""" Ecreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuario
tetar descobror qual foi  o número escolhido pelo computador.
O programa deverá escrever na tela se o usuario venceu ou perdeu. """
from random import randint
computador = randint(0, 5) #Faz o computador sortear os numeros 
print('-=-' * 20)
print('Vou pensar num número entre 0 e 5. Tente advinhar...')
print('-=-' * 10)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta advinhar
if computador == jogador:
    print('PArabens, pensamos no mesmo numero')
else:
    print('Errou, eu pesnei no numero {}, e não no número {} que voce digitou.'.format(computador, jogador))

