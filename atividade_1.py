'''
Crie um programa que peça para que o usuário digite um número, em seguida o converta para float, exibindo em tela tanto o número em si quanto seu tipo de dado.
'''
try:
    entrada = input('Informe um número: ')

    numero = float(entrada)

    print('Número digitado:', numero)
    print('Tipo de dado:', type(numero))
except Exception as e:
    print(f'Não foi possível realizar a operação. {e}.')
