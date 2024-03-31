"""Crie um programa que leia um número Real qualquer pelo teclado e moste
na tela a sua porção Inteira"""
from math import trunc
num = float(input('Digite um valor : '))
print('O número digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))