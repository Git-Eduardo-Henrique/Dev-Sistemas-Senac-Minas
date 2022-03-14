class CLiente:
    # guarda as informações do usuário e as imprime
    def __init__(self, nome, cpf, datanasc):
        self.nome = nome
        self.cpf = cpf
        self.datanasc= datanasc

    def Imprimir(self):
        # imprime as informações
        print(f'Nome: \033[34m{self.nome}\033[m | Cpf: \033[34m{self.cpf}\033[m'
              f' | Nascimento: \033[34m{self.datanasc}\033[m')





