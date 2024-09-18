#Crie um programa de locação de veículo, que receba o cadastro de um usuário para que ele possa escolher entre 5 veículos previamente cadastrados no sistema, e no final o programa exibe os #dados do cliente e do carro que ele decidiu alugar.
#O algoritmo deve ser criado com base no conceito de Associação entre Classes visto na aula do dia 18/09/2024.

class Cliente:
    def __init__(self, nome, cpf, idade, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__email = email
        self.carro_cadastrado = []

    # Métodos de acesso (getters e setters) para os atributos
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def adicionar_carro(self, carro):
        if carro not in self.carro_cadastrado:
            self.carro_cadastrado.append(carro)
            carro.adicionar_cliente(self)

    def listar_carros(self):
        lista = []
        for carro in self.carro_cadastrado:
            lista.append(carro.nome)
        return lista
    
class Carro:
    def __init__(self, ano, preco, cor, fabricante):
        self.__ano = ano
        self.__preco = preco
        self.__cor = cor
        self.__fabricante = fabricante
        self.cliente_cadastrado = []

    #metodos de acesso 
    @property
    def ano(self):
        return self.__ano
        
    @ano.setter
    def ano(self, ano):
         self.__ano = ano

    @property
    def preco(self):
        return self.__preco
        
    @preco.setter
    def preco(self, preco):
         self.__preco = preco

    @property
    def cor(self):
        return self.__cor
        
    @cor.setter
    def cor(self, cor):
         self.__cor= cor

    @property
    def fabricante(self):
        return self.__fabricante
        
    @fabricante.setter
    def fabricante(self, fabricante):
         self.__fabricante = fabricante

     #METODO DE ACAO
    def adicionar_cliente(self, cliente):
        if cliente not in self.cliente_cadastrado:
            self.cliente_cadastrado.append(cliente)
            cliente.adicionar_carro(self)

    def listar_clientes(self):
        lista = []
        for cliente in self.cliente_cadastrado:
            lista.append(cliente.nome)
        return lista
    
    def listar_carros(self):
        return f"{self.__fabricante} {self.__cor} {self.__ano} - R${self.__preco}"