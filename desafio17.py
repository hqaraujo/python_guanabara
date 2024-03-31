""" Crie um programa que leia um ângulo qualquer e msotre na tela o valor do seno, cosseno e 
tangente desse ângulo """
import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print("O angulo de {} tem o seno de {:.2f}".format(an, seno))
co = math.cos(math.radians(an))
print('O angulo de {} tem o cosseno de {:.2f}'.format(an, co))
tang = math.tan(math.radians(an))
print('O Ângulo de {} tem a tangente de {:.2f}'.format(an, tang))
