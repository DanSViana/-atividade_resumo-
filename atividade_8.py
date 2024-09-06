'''
Crie um programa em que o usuário informe uma quantidade desejada de números decimais de, no mínimo 0 e no máximo 10, e o programa calcula a média desses números.
'''
def calcular_media(lista_numeros):
  
    if len(lista_numeros) == 0:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

while True:
    quantidade_str = input('Digite a quantidade de números decimais (de 0 a 10): ')
    
    try:
        quantidade = int(quantidade_str)
        if 0 <= quantidade <= 10:
            break
        else:
            print('Por favor, digite um número entre 0 e 10.')
    except Exception as e:
        print('Entrada inválida. Por favor, digite um número inteiro.')

numeros = []

for i in range(quantidade):
    while True:
        numero_str = input(f'Digite o número decimal {i+1}: ')
        try:
            numero = float(numero_str)
            numeros.append(numero)
            break
        except Exception as e:
            print('Entrada inválida. Por favor, digite um número decimal.')

media = calcular_media(numeros)

print(f'\nA média dos números digitados é: {media:.2f}')
