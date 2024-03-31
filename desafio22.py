""" Faça um programa que leia u número de 0 a 9999 e mostrena tela cada um dos digitos separados
EX: 
digite um nuúmero: 1834
unidade: 4
dezena: 3 
centena: 8
milhar: 1 """
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(""" O numero digitado foi {}, 
      A unidade é {},
      A dezena é {},
      A centena é {},
      E o milhar é {}. """.format(num, u, d, c, m))