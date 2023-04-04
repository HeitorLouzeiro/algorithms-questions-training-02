'''
Faça um programa que receba duas notas, calcule e mostre
a média aritmética e a mensagem que se encontra na tabela a seguir:
media:
0,0 a 3,0 - Reprovado
3,0 a 7,0 - Exame
7,0 a 10,0 - Aprovado
'''
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

media = (n1+n2)/2
print('Sua media é: %.2f' % media)

if (media > 0 and media < 3):
    print('Reprovado')
elif (media >= 3 and media < 7):
    print('Exame')
else:
    print('Aprovado')
