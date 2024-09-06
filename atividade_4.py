'''
Crie um programa que o usuário informa um número inteiro positivo, e o programa exibe na tela uma contagem regressiva.
'''
import os
import time

numero = int(input('Informe um nomero inteiro: '))

while numero >= 0:
    os.system('cls')
    print(f'{numero}...')
    numero -= 1
    time.sleep(1)
   
os.system('cls')