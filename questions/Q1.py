'''
Faça um programa que receba quatro notas de um aluno, calcule e mostre
a média aritmética das notas e a mensagem de aprovado
ou reprovado, considerando para aprovação média 7.

'''

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
n4 = float(input('Digite a quarta nota:'))

media = (n1+n2+n3+n4)/4
print('Sua media é: %.2f' % media)

if (media >= 7):
    print('Aprovado')
else:
    print('Reprovado')
