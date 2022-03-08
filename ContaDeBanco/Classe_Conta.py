class Conta:
    from classes import CLiente

    def __init__(self, titular, numero, saldo=0):
        self.titular = titular.nome
        self.numero = numero
        self.saldo = saldo

    def Estrato(self):
        print(f'titular: {self.titular}'
              f' saldo: {self.saldo}')

    def Deposito(self, deposito):
        self.saldo += deposito
        print(f'Depositado: {deposito}'
              f' Novo saldo: {self.saldo}')

    def Saque(self, saque):
        if self.saldo < saque:
            print('\033[31mVOCE NAO PODE EFUTUAR O SAQUE\033[m')
        else:
            self.saldo -= saque
            print(f'Saqueado: {saque}'
                  f' Saldo Restante: {self.saldo}')
