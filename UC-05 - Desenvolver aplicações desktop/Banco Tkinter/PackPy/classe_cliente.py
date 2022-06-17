class Cliente:
    def __init__(self, nome, cpf, dataNasc,numero):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc
        self.numero = numero

    def imprime_dados(self):
        self.nome= input(f'Digite seu nome:{self.nome}')

        self.cpf= input(f'Digite seu CPF:{self.cpf}')

        self.dataNasc= input(f'Digite sua data de nascimento:{self.dataNasc}')

        self.numero= input(f'Digite o número da conta: {self.numero}')

        print(f'Titular: {self.nome}')
        print(f'CPF:{self.cpf}')
        print(f'Data de nascimento:{self.dataNasc}')
        print(f'Número da conta: {self.numero}')
