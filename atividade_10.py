'''
Crie um programa em que o usuário cadastre quantos cursos ele quiser (nome do curso, duração do curso em horas, Período do dia, quantidade de vagas) e exiba na tela.
'''
def cadastrar_cursos():
    
    cursos = []

    print("Cadastro de Cursos")
    print("Quando terminar, digite 'fim' para o nome do curso.")

    while True:
        nome_curso = input("Digite o nome do curso: ")
        
        if nome_curso.lower() == 'fim':
            break

        while True:
            try:
                duracao = float(input("Digite a duração do curso em horas: "))
                if duracao <= 0:
                    print("A duração deve ser um número positivo. Tente novamente.")
                else:
                    break
            except Exception as e:
                print("Entrada inválida. Por favor, digite um número decimal.")

        periodo = input('Digite o período do dia (ex.: manhã, tarde, noite): ').strip()

        while True:
            try:
                vagas = int(input('Digite a quantidade de vagas: '))
                if vagas < 0:
                    print('A quantidade de vagas não pode ser negativa. Tente novamente.')
                else:
                    break
            except Exception as e:
                print('Entrada inválida. Por favor, digite um número inteiro.')

        curso = {
            'Nome': nome_curso,
            'Duração (horas)': duracao,
            'Período do dia': periodo,
            'Quantidade de vagas': vagas
        }

        cursos.append(curso)
        print('\nCurso cadastrado com sucesso!\n')

    return cursos

def exibir_cursos(cursos):
    
    if not cursos:
        print('Nenhum curso foi cadastrado.')
        return

    print('\nCursos Cadastrados:')
    for curso in cursos:
        print('\nNome do Curso:', curso['Nome'])
        print('Duração (horas):', curso['Duração (horas)'])
        print('Período do Dia:', curso['Período do dia'])
        print('Quantidade de Vagas:', curso['Quantidade de vagas'])

def main():
    cursos = cadastrar_cursos()
    exibir_cursos(cursos)

if __name__ == "__main__":
    main()
