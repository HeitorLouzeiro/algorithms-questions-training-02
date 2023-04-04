'''

O preço ao consumidor de um carro novo é a
soma do custo de fábrica com a porcentagem do
distribuidor e dos impostos, ambos aplicados
ao custo de fábrica. As porcentagens encontram-se
na tabela a seguir.
Até R$ 12.000,00 5 isento
Entre R$ 12.000,00 e R$ 25.000,00 10 15
Acima de R$ 25.000,00 15 20
Faça um programa que receba o custo de fábrica de um carro
e mostre o preço ao consumidor.

'''

custoFabrica = float(input('Digite o custo de fabrica do carro: '))

if (custoFabrica > 0 and custoFabrica <= 12000):
    custoConsumidor = custoFabrica + (custoFabrica * 0.05)
    print('O custo ao consumidor é: %.2f' % custoConsumidor)
elif (custoFabrica > 12000 and custoFabrica <= 25000):
    custoConsumidor = custoFabrica + \
        (custoFabrica * 0.1) + (custoFabrica * 0.15)
    print('O custo ao consumidor é: %.2f' % custoConsumidor)
elif (custoFabrica > 25000):
    custoConsumidor = custoFabrica + \
        (custoFabrica * 0.15) + (custoFabrica * 0.2)
    print('O custo ao consumidor é: %.2f' % custoConsumidor)
else:
    print('Digite um valor valido.')
