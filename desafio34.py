""" Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triangulo """

print("Digite os comprimentos das três retas:")
a = float(input("Comprimento da primeira reta: "))
b = float(input("Comprimento da segunda reta: "))
c = float(input("Comprimento da terceira reta: "))
if a + b > c and a + c > b and b + c > a:
     print("As medidas fornecidas podem formar um triângulo.")
else:
    print("As medidas fornecidas não podem formar um triângulo.")

