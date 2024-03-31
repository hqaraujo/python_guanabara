# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Digite o preço: R$'))
desc = preco - (preco * 5 / 100)
print('O valor digitado foi {:.2f}R$, com  desconto de 5% ele fica de {:.2f}R$.'.format(preco, desc))