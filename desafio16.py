""" Faça um programa que leia o comprimetnto do cateto
opsoto e do cateto adjacente de um triângulo,
e mostre o comprimento da hipotenusa"""


"""co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""

import math
co = float(input('Comprimento do catetito oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa dos catetos é {:.2f}'.format(hi))