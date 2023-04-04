'''

Faça um programa que receba o salário de um funcionário e,
usando a tabela a seguir, calcule e mostre o novo salário.

Até R$ 300,00 50%
R$ 300,00 <= R$ 500,00 aumento de 40%
R$ 500,00 <= R$ 700,00 aumento de 30%
R$ 700,00 <= R$ 800,00 aumento de 20%
R$ 800,00 <= R$ 1.000,00 aumento de 10%
Acima de R$ 1.000,00 aumento de 5%

'''
salario = float(input('Digite o seu salário: '))

if (salario > 0 and salario <= 300):
    salario = salario + (salario * 0.50)
    print('Seu novo salário é: %.2f' % salario)
elif (salario > 300 and salario <= 500):
    salario = salario + (salario * 0.40)
    print('Seu novo salário é: %.2f' % salario)
elif (salario > 500 and salario <= 700):
    salario = salario + (salario * 0.30)
    print('Seu novo salário é: %.2f' % salario)
elif (salario > 700 and salario <= 800):
    salario = salario + (salario * 0.20)
    print('Seu novo salário é: %.2f' % salario)
elif (salario > 800 and salario <= 1000):
    salario = salario + (salario * 0.10)
    print('Seu novo salário é: %.2f' % salario)
elif (salario > 1000):
    salario = salario + (salario * 0.05)
    print('Seu novo salário é: %.2f' % salario)
else:
    print('Digite um valor valido.')
