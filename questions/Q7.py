'''

Uma empresa decide dar um aumento de 30% aos funcionários
com salários inferiores a R$ 500,00.
Faça um programa que receba o salário do funcionário e
mostre o valor do salário reajustado ou uma mensagem,
caso ele não tenha direito ao aumento.

'''

salario = float(input('Digite o salario do funcionario: '))
if (salario < 500):
    salario = salario + (salario * 0.3)
    print('O salario com aumento é: %.2f' % salario)
else:
    print('O funcionario não tem direito ao aumento.')
