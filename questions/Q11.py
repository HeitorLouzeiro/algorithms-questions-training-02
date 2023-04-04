'''
Faça um programa que receba o salário atual de um funcionário e,
usando a tabela a seguir, calcule e
mostre o valor do aumento e o novo salário.

Até R$ 300,00 15%
R$ 300,00 R$ 600,00 10%
R$ 600,00 R$ 900,00 5%
Acima de R$ 900,00 0%

'''
salario = float(input('Digite o seu salário: '))

if (salario > 0 and salario <= 300):
    aumento = salario * 0.15
    novosalario = salario + aumento
    print('Você ganhara um aumento de %.2f.' % aumento)
    print('Seu novo salário é %.2f .' % novosalario)

elif (salario > 300 and salario < 600):
    aumento = salario * 0.10
    novosalario = salario + aumento
    print('Você ganhara um aumento de %.2f.' % aumento)
    print('Seu novo salário é %.2f .' % novosalario)

elif (salario >= 600 and salario <= 900):
    aumento = salario * 0.05
    novosalario = salario + aumento
    print('Você ganhara um aumento de %.2f.' % aumento)
    print('Seu novo salário é %.2f .' % novosalario)

elif (salario > 900):
    print('Você não ganhará um aumento no salário.')
else:
    print('Digite um valor valido.')
