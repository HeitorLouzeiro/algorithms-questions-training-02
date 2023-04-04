'''
Faça um programa que receba dois números e execute as
operações listadas a seguir, de acordo com a escolha do usuário.

1-Média entre os números digitados
2-Diferença do maior pelo menor
3-Produto entre os números digitados
4-Divisão do primeiro pelo segundo

Se a opção digitada for inválida, mostre uma mensagem de erro
e termine a execução do programa.

Lembre-se de que, na operação 4, o segundo número deve ser diferente de zero.
'''

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o Segundo numero:'))

print('1: Media entre os numeros digitados.')
print('2: Diferença do maior pelo menor.')
print('3: Produto entre os numeros digitados.')
print('4: Divisão do primeiro pelo segundo.\n')

op = int(input('Selecione uma Opção: \n'))


if (op == 1):
    media = (n1 + n2)/2
    print('media: %.2f' % media)
elif (op == 2):
    dif = (n1 - n2)
    print('diferença: %.2f.' % dif)
elif (op == 3):
    mult = (n1 * n2)
    print('produto: %.2f' % mult)
elif (op == 4):
    if (n2 == 0):
        print('O segundo numero não pode ser igual a zero.')
    else:
        div = n1 / n2
        print('Divisão: %.2f' % div)
else:
    print('opção invalida.')
