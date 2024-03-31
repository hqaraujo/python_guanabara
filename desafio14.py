""" Escreva um programa que pergunte a quantidade de KM percorrido
 por um carro alugado e a quantidade de dias pelos quais ele foi
ele foi alugado. Calculeo preço a pagar, sabendo que o carro custa R$60 por dia e 
R%0,15 por KM rodado """
dias = int(input('Quantos dias ele de aluguel? '))
km = float(input('Quantos KM o carro percorreu? KM'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}'.format(pago))

