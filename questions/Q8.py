'''

Faça um programa para calcular e mostrar o salário
reajustado de um funcionário. O percentual de aumento
encontra-se na tabela a seguir.
1- Até R$ 300,00 aumento 35%
2 -Acima de R$ 300,00 aumento 15%

'''
salario = float(input('Digite o salario do funcionario: '))

if (salario < 300):
    salario = salario + (salario * 0.35)
    print('O salario com aumento é: %.2f' % salario)
else:
    salario = salario + (salario * 0.15)
    print('O salario com aumento é: %.2f' % salario)
