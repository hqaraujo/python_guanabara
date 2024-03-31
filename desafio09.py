# Quanto dinheiro tem na carteira e  msotre quantos dollares ela pode comprar.

real = float(input('Digite o valor que voce tem: R$ '))
dolar = real / 4.98
euro = real / 5.39
print('Com R${:.2f} voce pode comprar US${:.2f} dolares ou {:.2f} euros'.format(real, dolar, euro))

