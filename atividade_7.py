'''
Crie um programa onde o usuário possa digitar uma lista de nomes (quantos ele quiser) e no final exiba a lista de nomes em ordem alfabética na tela, mostrando também o número de nomes digitado pelo usuário.
'''
import os

nomes = []
print('Digite "fim", para finalizar')

while True:
    nome = input('Digite um nome: ')
    
    if nome.lower() == "fim":
        break

    nomes.append(nome)

nomes.sort()

print('\nLista de nomes em ordem alfabética:')
for nome in nomes:
    print(nome)

print('\nNúmero de nomes digitados:', len(nomes))

