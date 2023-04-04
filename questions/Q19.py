'''

Faça um programa que receba a altura e o sexo de
uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas (onde h é a altura):
para homens: (72.7 * h) - 58.
 para mulheres: (62.1 * h) - 44.7.

'''

altura = float(input('Digite sua altura:'))

# lower trasforma tudo em letra minuscula
sexo = input(
    '\nDigite seu sexo (M) para masculino ou (F) para feminino: ').lower()

if (sexo == 'm'):
    peso = (72.7 * altura) - 58
    print('Seu peso ideal é: %.2f' % peso)
elif (sexo == 'f'):
    peso = (61.1 * altura) - 44.7
    print('Seu peso ideal é: %.2f' % peso)
else:
    print('Opção invalida.')
