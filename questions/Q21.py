'''

Faça um programa que receba o preço de um produto e
seu código de origem e mostre sua procedência.
A procedência obedece à tabela a seguir.
codigos de origem.
1 Sul
2 Norte
3 Leste
4 Oeste
5 ou 6 Nordeste
7 ou 8 ou 9 Sudeste
10 a 20 Centro-oeste
21 a 30 Nordeste

'''

preco = float(input('Digite o valor do produto: '))
codigo = int(input('Digite o codigo do produto:'))

if (codigo == 1):
    print('Esse Codigo é do sul.')
elif (codigo == 2):
    print('Esse Codigo é do norte.')
elif (codigo == 3):
    print('Esse Codigo é do leste.')
elif (codigo == 4):
    print('Esse Codigo é do oeste.')
elif (codigo == 5 or codigo == 6):
    print('Esse Codigo é do nordeste.')
elif (codigo == 7 or codigo == 8 or codigo == 9):
    print('Esse Codigo é do sudeste.')
elif (codigo >= 10 and codigo <= 20):
    print('Esse Codigo é do centro-oeste.')
elif (codigo >= 21 and codigo <= 30):
    print('Esse Codigo é do nordeste.')
else:
    print('codigo invalido')
