# Dissecando uma variavel
a = input('Digite algo: ')
print('O tipo primitivo desse valor', type(a))
print('Só tem espaços?', a.isspace())
print('É numerico?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É aLfa numerico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está minuscula?', a.islower())
print('Está capitalizada?', a.istitle())