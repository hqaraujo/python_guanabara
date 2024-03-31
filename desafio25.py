""" Faça um programa que leia uma frase pelo 
teclado e mostre:
Quantas vezes apareceu a letra "A"
Em que posição ela apareceu na primeira vez
Em que posição ela apareceu a útima vez """

frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('A letra "A" aparece {} vezez na frase.'.format(frase.count('A')))
print('A primera letra "A" apareceu na posiçao {}'.format(frase.find('A')+1))
print('A letra "A" apareceu na {} posição.'.format(frase.rfind('A')+1))