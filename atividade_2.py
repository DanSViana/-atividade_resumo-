'''Crie um programa que receba o peso (em gramas) de um bebê recém-nascido, e indique se o bebê está normal ou se precisa ficar internado, caso o bebê tenha menos que 2500g.
'''
peso_str = input('Informe o peso do bebê em gramas: ')

peso = float(peso_str)

if peso < 2500:
    print('O bebê precisa ficar internado.')
else:
    print('O bebê está com o peso normal.')
