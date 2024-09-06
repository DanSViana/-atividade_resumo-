'''
Crie um programa com funções para calcular a área de 4 figuras geométricas (quadrado, círculo, triângulo e trapézio).
'''

def mostrar_menu():
    print('1 - Calcular quadrado.')
    print('2 - Calcular triângulo.')
    print('3 - Calcular círculo.')
    print('4 - Calcular trapézio.')
    print('5 - Sair do programa.')

def calcular_quadrado(b, h):
    result = b * h
    return result

def calcular_triangulo(b, h):
    result = (b * h)/2
    return result

def calcular_circulo(r):
    result = 3.14*(r**2)
    return result

def calcular_trapézio(b, h):
    result = (b + h) . h/2
    return result

while True:
    mostrar_menu()

    opcao = input('Opção desejada: ')

    match opcao:
        case '1':
            b = float(input('Informe o valor da base: ').replace(',', '.'))
            h = float(input('Informe o valor da altura: ').replace(',', '.'))
            print(f'Área do quadrado: {calcular_quadrado(b, h)}.')
            continue
        case '2':
            b = float(input('Informe o valor da base: ').replace(',', '.'))
            h = float(input('Informe o valor da altura: ').replace(',', '.'))
            print(f'Área do triangulo: {calcular_triangulo(b, h)}.')
            continue
        case '3':
            r = float(input('Informe o valor da base: ').replace(',', '.'))
            print(f'Área do circulo: {calcular_circulo(r)}.')
            continue 
        case '5':
            print('Programa encerrado.')
            break
        case _:
            print('Opção invalida.')