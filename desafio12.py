# Calcule o salario do funcionario com acrescimo de 15% de aumento
salario = float(input("QUAl o seu salario? R$ "))
novo = salario + (salario * 15 / 100)
print('O seu salario antigo era de {:.2f}R$, com o reajuste de 15% vai para {:.2f}R$'.format(salario, novo))