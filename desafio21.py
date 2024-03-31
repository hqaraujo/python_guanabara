""" Crie um programa que leia nom completo de uma pessoa e
mostre :
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo(sem considerar espaço)
Quantas letras tem o primeiro nome """

nome = str(input('Digite seu Nome: ')).strip()
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
