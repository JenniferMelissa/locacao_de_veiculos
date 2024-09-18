#Crie um programa de locação de veículo, que receba o cadastro de um usuário para que ele possa escolher entre 5 veículos previamente cadastrados no sistema, e no final o programa exibe os #dados do cliente e do carro que ele decidiu alugar.
#O algoritmo deve ser criado com base no conceito de Associação entre Classes visto na aula do dia 18/09/2024.

from modulo import *

if __name__ == '__main__':

    # Instanciando um cliente
    nome = input('Informe o nome do cliente: ')
    cpf = input('Informe o CPF do cliente: ')
    idade = int(input('Informe a idade do cliente: '))
    email = input('Informe o email do cliente: ')
    cliente1 = Cliente(nome, cpf, idade, email)

    # Instanciando carros
    carros = [
        Carro(2022, 1000, 'Azul', 'Gol'),
        Carro(2005, 1500, 'Preto', 'Celta'),
        Carro(2001, 900, 'Preto', 'Duster'),
        Carro(2019, 700, 'Branco', 'Corola'),
        Carro(2003, 800, 'Cinza', 'Cruze')
    ]

    # Exibindo detalhes dos carros
    print("\nCarros disponíveis para locação:")
    for i, carro in enumerate(carros, start=1):
        print(f"{i}. {carro.listar_carros()}")

    # Permitindo que o cliente escolha um carro
    escolha = int(input("\nEscolha o número do carro que deseja alugar: ")) - 1
    carro_escolhido = carros[escolha]

    # Associando o carro ao cliente
    cliente1.adicionar_carro(carro_escolhido)

    # Exibindo dados do cliente e do carro escolhido
    print("\nDados do cliente:")
    print(f"Nome: {cliente1.nome}")
    print(f"CPF: {cliente1.cpf}")
    print(f"Idade: {cliente1.idade}")
    print(f"Email: {cliente1.email}")

    print("\nCarro escolhido:")
    print(carro_escolhido.listar_carros())