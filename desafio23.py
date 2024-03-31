""" Crie um programa que leia o noome de 
uma cidade e diga se ela começa ou não com o nome "santo" """

cidade = str(input('Em qual cidade voce nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')