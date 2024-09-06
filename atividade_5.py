'''
Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice informado pelo usuário.
'''
# lista de nomes
nomes = ['Catarina', 'Joaquina', 'Franscisca', 'Sebastiana', 'Florentina', 'Josefina', 'Betina', 'Juscicleyto', 'Birubiru', 'Jurema'
]

indice = int(input("Informe um número inteiro: "))

if 0 <= indice < len(nomes):
    
    print("O nome no índice", indice, "é", nomes[indice])
else:
    
    print("Número do índice inválido, tente outro.")
