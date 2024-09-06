'''
Crie um programa onde o usuário informa um número inteiro, e o programa informa se o número e par ou ímpar.
'''
# Solicita ao usuário que digite um número inteiro
numero_str = input('Informe um número inteiro: ')

numero = int(numero_str)

if numero % 2 == 0:
    print('É par.')
else:
    print('É ímpar.')
