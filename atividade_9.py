'''
Crie um programa onde o usuário cadastre uma quantidade desejada de eventos (nome do evento e classificação indicativa) e após o cadastro dos eventos, o usuário possa informar o nome e a idade, e se inscrever em um dos eventos. Caso o usuário não tenha idade mínima, o programa proíbe a inscrição e pede para o mesmo se inscrever em outro evento. Caso o usuário tenha a idade mínima, o programa inscreve o usuário exibindo a data da inscrição e encerra.
'''
from datetime import datetime

def cadastrar_eventos():
    eventos = []
    quantidade = int(input("Quantos eventos deseja cadastrar? "))
    
    for _ in range(quantidade):
        nome_evento = input("Nome do evento: ")
        classificacao = int(input("Classificação indicativa (idade mínima): "))
        eventos.append({'nome': nome_evento, 'classificacao': classificacao})
    
    return eventos

def listar_eventos(eventos):
    print("\nEventos disponíveis:")
    for i, evento in enumerate(eventos, start=1):
        print(f"{i}. {evento['nome']} (Idade mínima: {evento['classificacao']})")

def inscrever_usuario(eventos):
    listar_eventos(eventos)
    
    evento_index = int(input("\nEscolha o número do evento para se inscrever: ")) - 1
    if evento_index < 0 or evento_index >= len(eventos):
        print("Evento inválido.")
        return
    
    nome_usuario = input("Digite seu nome: ")
    idade_usuario = int(input("Digite sua idade: "))
    
    evento_selecionado = eventos[evento_index]
    
    if idade_usuario >= evento_selecionado['classificacao']:
        data_inscricao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nInscrição bem-sucedida!")
        print(f"Evento: {evento_selecionado['nome']}")
        print(f"Nome do usuário: {nome_usuario}")
        print(f"Data da inscrição: {data_inscricao}")
    else:
        print("\nIdade insuficiente para se inscrever neste evento.")
        print("Por favor, escolha um evento diferente.")
        inscrever_usuario(eventos)  # Permite tentar inscrição novamente

def main():
    print("Bem-vindo ao sistema de eventos!")
    eventos = cadastrar_eventos()
    inscrever_usuario(eventos)

if __name__ == "__main__":
    main()
