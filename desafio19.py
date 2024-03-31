""" O mesmo professor do desafio anterior quer sortear a ordem
da apresentação de trabalhos dos alunos. Faça um programa que mostre a ordem sorteada. """

from random import shuffle
n1 = str(input("Primeiro aluno: "))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terçeiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)