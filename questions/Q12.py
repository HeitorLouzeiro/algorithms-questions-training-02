'''

Faça um programa que receba o salário bruto de
um funcionário e, usando a tabela a seguir, calcule e
mostre o valor a receber.

Até R$ 350,00 R$ 100,00
R$ 350,00 R$ 600,00 R$ 75,00
R$ 600,00 R$ 900,00 R$ 50,00
Acima de R$ 900,00 R$ 35,00

Sabe-se que este é composto pelo salário bruto acrescido de gratificação
e descontado o imposto de 7% sobre o salário.

'''

salario = float(input('Digite o seu salário: '))

if (salario > 0 and salario <= 350):
    salario = salario + 100
    salario = salario - (salario * 0.07)
    print('Seu salário é: %.2f' % salario)
elif (salario > 350 and salario < 600):
    salario = salario + 75
    salario = salario - (salario * 0.07)
    print('Seu salário é: %.2f' % salario)
elif (salario >= 600 and salario <= 900):
    salario = salario + 50
    salario = salario - (salario * 0.07)
    print('Seu salario é: %.2f' % salario)
elif (salario > 900):
    salario = salario + 35
    salario = salario - (salario * 0.07)
    print('Seu salario é: %.2f' % salario)
else:
    print('Digite um valor valido.')
