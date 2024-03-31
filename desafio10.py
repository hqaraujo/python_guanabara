"""Desenvolva um programa que leia a largura de uma arede em metros,
calcule a sua área e a quantidade de tinta necessaaria para pinta la, 
sabendo que cada litro de tinta, pinta uma área de 2m². """

largura = float(input('Qual a largura da parede?'))
altura = float(input('Qual a altura da parede?'))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e a sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, voçe precisará de {} litros de tinta'.format(tinta))