'''
Faça um programa que receba dois números e execute uma das operações
listadas a seguir, de acordo com a escolha do usuário.
Se for digitada uma opção inválida, mostre mensagem de erro
e termine a execução do programa. As opções são:

a) O primeiro número elevado ao segundo número.
b) Raiz quadrada de cada um dos números.
c) Raiz cúbica de cada um dos números.

'''
# Para calcular raiz quadrada de um numero multiplicamos ele por 1/2
# Para calcular raiz cubica de um numero multiplicamos ele por 1/3

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo  numero: '))

print('\n1 - O primeiro número elevado ao segundo número.')
print('2 - Raiz quadrada de cada um dos números.')
print('3 - Raiz cúbica de cada um dos números. \n')

op = int(input('Selecione uma Opção: '))


if (op == 1):
    elevado = n1 ** n2
    print('O primeiro elevado pelo segundo: %.2f' % elevado)
elif (op == 2):
    raiz1 = n1 ** (1/2)
    raiz2 = n2 ** (1/2)
    print('A raiz quadrada do primeiro numero é: %.2f' % raiz1)
    print('A raiz quadrada do segundo numero é: %.2f' % raiz2)
elif (op == 3):
    raiz1 = n1 ** (1/3)
    raiz2 = n2 ** (1/3)
    print('A raiz cubica do primeiro numero é: %.2f' % raiz1)
    print('A raiz cubica do segundo numero é: %.2f' % raiz2)
else:
    print('Opção invalida.')
