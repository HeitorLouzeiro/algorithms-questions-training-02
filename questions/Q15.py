'''

Uma agência bancária possui dois tipos de investimentos,
conforme o quadro a seguir. Faça um programa que receba
o tipo de investimento e seu valor, calcule e mostre o
valor corrigido após um mês de investimento,
de acordo com o tipo de investimento.

1 - Poupança 3%
2 - Fundos de renda fixa 4%

'''

valor = float(input('Digite o valor a ser depositado: '))

print('1 - Poupança 3% ')
print('2 - Fundos de renda fixa 4% ')

op = int(input('Selecione uma Opção: '))

if (op == 1):
    valor = valor + (valor * 0.03)
    print('Na poupança você irá ganhar: %.2f .' % valor)
elif (op == 2):
    valor = valor + (valor * 0.04)
    print('Na renda fixa você irá ganhar: %.2f .' % valor)
else:
    print('Opção invalida.')
