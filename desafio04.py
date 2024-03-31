# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

n = int(input('Digite um número: '))
a = n + 1
s = n - 1
print('O número digitado foi {}, o seu sucessor é {}, e seu antecessor é {}.'.format(n, a, s))