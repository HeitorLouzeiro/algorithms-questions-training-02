'''
Faça um programa que receba três números e mostre o maior.

'''
n1 = float(input('Digite o primeira numero:'))
n2 = float(input('Digite  o segundo numero:'))
n3 = float(input('Digite  o terceiro numero:'))

if (n1 > n2 and n1 > n3):
    print('O primeiro numero é maior')
elif (n2 > n1 and n2 > n3):
    print('O segundo numero é o maior.')
else:
    print('O terceiro numero é o maior.')
