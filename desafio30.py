""" Desenvolva um proframa que pergunte a distância de uma viagem 
em Km. Calcule o preço da passagem, cobrando R$0,50 por 
Km para viagnes de até 200Km e R$0,45 para viagens mais longas. """

distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de {:.2f}.'.format(preço))
   