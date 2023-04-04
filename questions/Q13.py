'''
Faça um programa que receba o preço de um preco,
calcule e mostre, de acordo com as tabelas a seguir,
o novo preço e a classificação.
Tabela 1
Até R$ 50,00 5
Entre R$ 50,00 e R$ 100,00 10
Acima de R$ 100,00 15

Tabela 2
Até R$ 80,00 Barato
Entre R$ 80,00 e R$ 120,00 (inclusive) Normal
Entre R$ 120,00 e R$ 200,00 (inclusive) Caro
Maior que R$ 200,00 Muito caro

'''

preco = float(input('Digite o valor do produto: '))

if (preco > 0 and preco <= 50):
    novoPreco = preco + (preco * 0.05)
    print('O novo preço do preco é: %.2f' % novoPreco)
elif (preco > 50 and preco <= 100):
    novoPreco = preco + (preco * 0.10)
    print('O novo preço do preco é: %.2f' % novoPreco)
elif (preco > 100):
    novoPreco = preco + (preco * 0.15)
    print('O novo preço do preco é: %.2f' % novoPreco)
else:
    print('Digite um valor valido.')


if (novoPreco > 0 and novoPreco <= 80):
    print('Barato')
elif (novoPreco > 80 and novoPreco <= 120):
    print('Normal')
elif (novoPreco > 120 and novoPreco <= 200):
    print('Caro')
elif (novoPreco > 200):
    print('Muito Caro')
