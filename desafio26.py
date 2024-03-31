""" Faça um progra,a que leia o nome completo de uma
pessoa, moxtrando em seguida o primeiro nome separadamente.
EX: Ana Maria de Souza
primeiro = Ana
último = Souza """

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))