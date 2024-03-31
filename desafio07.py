# Faça um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input('Uma distancia em metros: '))
cm = m * 100
mm = m * 1000
print('A media é de {} tem {} centimetros e {} milimetros.'.format(m, cm, mm))