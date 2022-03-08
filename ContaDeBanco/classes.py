class CLiente:
    def __init__(self, nome, cpf, datanasc):
        self.nome = nome
        self.cpf = cpf
        self.datanasc= datanasc

    def Imprimir(self):
        print(f'Nome: {self.nome} Cpf: {self.cpf} Nascimento: {self.datanasc}')





