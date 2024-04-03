""" Escreva um programa que pergunte o sálario de um funcionario e
calcule o valor do seu aumento.
Para saláriod superiores a R$1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%. """

salario = float(input('Qual é o seu salário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${}, passa a ganhar R${} agora.'.format(salario, novo))