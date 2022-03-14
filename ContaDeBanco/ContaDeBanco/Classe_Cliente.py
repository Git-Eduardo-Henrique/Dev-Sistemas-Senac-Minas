class CLiente:
    # guarda as informações do usuário e as imprime
    def __init__(self, nome, cpf, datanasc):
        self.nome = nome
        self.cpf = cpf
        self.datanasc= datanasc

    def Imprimir(self):
        # imprime as informações
        print(f'Nome: {self.nome} Cpf: {self.cpf} Nascimento: {self.datanasc}')





