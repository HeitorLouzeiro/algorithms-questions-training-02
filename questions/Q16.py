'''

Uma empresa decide aplicar descontos nos seus preços
usando a tabela a seguir. Faça um programa que
receba o preço atual de um produto e seu código,
calcule e mostre o valor do desconto e o novo preço.

Até R$ 30,00 Sem desconto
Entre R$ 30,00 e R$ 100,00 10%
Acima de R$ 100,00 15%

'''

preco = float(input('Digite o preço do produto: '))

if (preco > 0 and preco < 30):
    print('Você não ganhará um desconto.')
    print('Você pagara %.2f' % preco)
elif (preco >= 30 and preco <= 100):
    desconto = preco * 0.10
    preco = preco - desconto
    print('Você ganhou um desconto de %.2f' % desconto)
    print('Você ira pagar %.2f' % preco)
elif (preco > 100):
    desconto = preco * 0.15
    preco = preco - desconto
    print('Você ganhou um desconto de %.2f' % desconto)
    print('Você ira pagar %.2f' % preco)
else:
    print('Digite um valor valido.')
