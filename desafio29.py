""" Crie um programa que leia um número inteiro e mostre
na tela se ele é PAR ou IMPAR """

num = int(input('Digite um número qualquer: '))
resultado = num % 2
if resultado == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar.'.format(num))