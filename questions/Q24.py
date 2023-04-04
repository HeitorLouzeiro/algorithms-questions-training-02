'''

Faça um programa que receba o preço, a categoria
(1 — limpeza; 2 — alimentação; ou 3 — vestuário)
e a situação
(R — produtos que necessitam de refrigeração;
e N — produtos que não necessitam de refrigeração).
Calcule e mostre:
O valor do aumento, usando as regras que se seguem.
PrEço CATEgori A PErCENTuAL dE AuMENTo
preco <= 25
1 5%
2 8%
3 10%
preco > 25
1 12%
2 15%
3 18%

O produto que preencher pelo menos um dos seguintes requisitos
pagará imposto equivalente a 5% do preço; caso contrário,
pagará 8%.
Os requisitos são:
Categoria: 2
Situação: R

O novo preço, ou seja, o preço mais aumento menos imposto.
A classificação, usando as regras a seguir.
< = R$ 50,00 Barato
Entre R$ 50,00 e R$ 120,00 Normal
> = R$ 120,00 Caro

'''
preco = float(input('Digite o preco do produto: '))
print('1 — limpeza; 2 — alimentação; ou 3 — vestuário')
categoria = int(input('Digite a categoria do produto: '))
print('\nR- Produtos que necessitam de refrigeração')
print('N - Produtos que não necessitam de refrigeração')
# lower transformar tudo em minusculo
situacao = input('Digite a situacao do produto: ').lower()

# Calcula o percentual de aumento
if (preco <= 25):
    if (categoria == 1):
        aumento = preco * 0.05
    elif (categoria == 2):
        aumento = preco * 0.08
    elif (categoria == 3):
        aumento = preco * 0.1
    else:
        print('Categoria invalida!')
elif (preco > 25):
    if (categoria == 1):
        aumento = preco * 0.12
    elif (categoria == 2):
        aumento = preco * 0.15
    elif (categoria == 3):
        aumento = preco * 0.18
    else:
        print('Categoria invalida!')

# Calcula o valor do imposto.
if categoria == 2 or situacao == "R":
    imposto = preco * 0.05
else:
    imposto = preco * 0.08

# Calcula o novo preço.
novoPreco = preco + aumento - imposto

# Classifica o produto
if novoPreco <= 50:
    classificacao = "Barato"
elif novoPreco <= 120:
    classificacao = "Normal"
else:
    classificacao = "Caro"

print('O valor do aumento é: %.2f' % aumento)
print('O valor do imposto é: %.2f' % imposto)
print('O novo preço é: %.2f' % novoPreco)
print('A classificação é: %s' % classificacao)
