class Historico:
    def __init__(self):
        self.trasacoes = []

    def transacoes_bancarias(self):
        print('Transações: ')
        for i in self.trasacoes:
            print('-',i)
