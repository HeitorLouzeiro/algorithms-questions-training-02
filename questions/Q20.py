'''
Faça um programa que receba a idade de um nadador
e mostre sua categoria, usando as regras a seguir.
Para idade inferior a 5, deverá mostrar mensagem.

Infantil 5 a 7
Juvenil 8 a 10
Adolescente 11 a 15
Adulto 16 a 30
Sênior Acima de 30

'''
idade = int(input('Digite a sua idade:'))

if (idade < 5):
    print('')
elif (idade >= 5 and idade <= 7):
    print('Você está na categoria infantil.')
elif (idade >= 8 and idade <= 10):
    print('Você está na categoria Juvenil.')
elif (idade >= 11 and idade <= 15):
    print('Você está na categoria Adolescente.')
elif (idade >= 16 and idade <= 30):
    print('Você está na categoria Adulto.')
elif (idade > 30):
    print('Você está na categoria Sênior.')
else:
    print('Digite uma idade valida.')
