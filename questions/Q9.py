'''
Um banco concederá um crédito especial aos seus clientes,
de acordo com o saldo médio no último ano.
Faça um programa que receba o saldo médio de um cliente
e calcule o valor do crédito, de acordo com a tabela a seguir.
Mostre o saldo médio e o valor do crédito.

R$ 400,00 valor do credito é 30% do saldo médio
R$ 300,00 até R$ 400,00 valor do credito é 25% do saldo médio
R$ 200,00 até R$ 300,00 valor do credito é 20% do saldo médio
R$ 200,00 valor do credito é 10% do saldo médio

'''

saldoMedio = float(input('Digite o saldo medio do cliente: '))

if (saldoMedio > 400):
    valorCredito = saldoMedio * 0.3
    print('Saldo Medio: %.2f' % saldoMedio)
    print('O seu valor de crédito é : %.2f' % valorCredito)

elif (saldoMedio > 300 and saldoMedio <= 400):
    valorCredito = saldoMedio * 0.25
    print('Saldo Medio: %.2f' % saldoMedio)
    print('O seu valor de crédito é : %.2f' % valorCredito)

elif (saldoMedio > 200 and saldoMedio <= 300):
    valorCredito = saldoMedio * 0.2
    print('Saldo Medio: %.2f' % saldoMedio)
    print('O seu valor de crédito é : %.2f' % valorCredito)

elif (saldoMedio > 0 and saldoMedio <= 200):
    valorCredito = saldoMedio * 0.1
    print('Saldo Medio: %.2f' % saldoMedio)
    print('O seu valor de crédito é : %.2f' % valorCredito)
else:
    print('Digite um valor valido.')
