'''

Faça um programa que receba a idade e
o peso de uma pessoa. De acordo com a
tabela a seguir, verifique e mostre em
qual grupo de risco essa pessoa se encaixa.

IDADE
PESO
Até 60 Entre 60 e 90 (inclusive) Acima de 90
Menores que 20 9 8 7
De 20 a 50 6 5 4
Maiores que 50 3 2 1
'''

idade = int(input('Digite a sua idade: '))
peso = float(input('Digite a seu peso: '))

if (idade > 0 and idade < 20):
    if (peso > 0 and peso < 60):
        print('Você faz parte da categoria 9.')
    elif (peso >= 60 and peso <= 90):
        print('Você faz parte da categoria 8.')
    elif (peso > 90):
        print('Você faz parte da categoria 7.')
elif (idade >= 20 and idade <= 50):
    if (peso > 0 and peso < 60):
        print('Você faz parte da categoria 6.')
    elif (peso >= 60 and peso <= 90):
        print('Você faz parte da categoria 5.')
    elif (peso > 90):
        print('Você faz parte da categoria 4.')
elif (idade > 50):
    if (peso > 0 and peso < 60):
        print('Você faz parte da categoria 3.')
    elif (peso >= 60 and peso <= 90):
        print('Você faz parte da categoria 2.')
    elif (peso > 90):
        print('Você faz parte da categoria 1.')
else:
    print('Digite uma idade valida.')
