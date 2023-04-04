'''

Faça um programa que receba:
o código do produto comprado; e
a quantidade comprada do produto.
Calcule e mostre:
o preço unitário do produto comprado, seguindo a Tabela I;
o preço total da nota;
o valor do desconto, seguindo a Tabela II e
aplicado sobre o preço total da nota;
e o preço final da nota depois do desconto.

tabela 1
Código PrEço
1 a 10 R$ 10,00
11 a 20 R$ 15,00
21 a 30 R$ 20,00
31 a 40 R$ 30,00

tabela 2
Até R$ 250,00 5%
Entre R$ 250,00 e R$ 500,00 10%
Acima de R$ 500,00 15%

'''

codigo = int(input('Digite o codigo do produto: '))
qtd = int(input('Digite a quantidade comprada: '))

if (codigo > 0 and codigo <= 10):
    preco = 10.00
elif (codigo > 10 and codigo <= 20):
    preco = 15.00
elif (codigo > 20 and codigo <= 30):
    preco = 20.00
elif (codigo > 30 and codigo <= 40):
    preco = 30.00
else:
    print('Digite um codigo valido.')

precoTotal = preco * qtd

if (precoTotal > 0 and precoTotal <= 250):
    desconto = precoTotal * 0.05
elif (precoTotal > 250 and precoTotal <= 500):
    desconto = precoTotal * 0.10
elif (precoTotal > 500):
    desconto = precoTotal * 0.15
else:
    print('Digite um valor valido.')

precoFinal = precoTotal - desconto

print('O preço unitário do produto é: %.2f' % preco)
print('O preço total da nota é: %.2f' % precoTotal)
print('O valor do desconto é: %.2f' % desconto)
print('O preço final da nota é: %.2f' % precoFinal)
