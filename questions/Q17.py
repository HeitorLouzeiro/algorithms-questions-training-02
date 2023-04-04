'''
Faça um programa que verifique a validade de uma
senha fornecida pelo usuário. A senha é 4531.
O programa deve mostrar uma mensagem
de permissão de acesso ou não.

'''

senha = 4531

validsenha = int(input('Digite a senha para acessar: '))

if (validsenha == senha):
    print('Acesso liberado!')
else:
    print('Acesso negado!')
