'''

Uma empresa decidiu dar uma gratificação de Natal a seus
funcionários, baseada no número de horas
extras e no número de horas que o funcionário
faltou ao trabalho.
O valor do prêmio é obtido pela consulta à tabela que se segue, na qual:
H = número de horas extras - (2/3 * (número de horas falta))

> = 2.400 500,00
1.800 2.400 400,00
1.200 1.800 300,00
600 1.200 200,00
< 600 100,00

'''
horasExtras = int(input('Digite o numero de horas extras que ele fez: '))
horasFalta = int(input('Digite o numero de horas que ele faltou: '))

horasFeitas = horasExtras - (2/3 * (horasFalta))
# print(horasFeitas)
horasMinutos = horasFeitas * 60
# print(horasMinutos)
if (horasFeitas > 0):
    if (horasMinutos >= 2400):
        print('O valor do premio é: 500,00')
    elif (horasMinutos > 1800 and horasMinutos < 2400):
        print('O valor do premio é: 400,00')
    elif (horasMinutos >= 1200 and horasMinutos < 1800):
        print('O valor do premio é: 300,00')
    elif (horasMinutos >= 600 and horasMinutos < 1200):
        print('O valor do premio é: 200,00')
    else:
        print('O valor do premio é: 100,00')
else:
    print('Digite um valor valido.')
