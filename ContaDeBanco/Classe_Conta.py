class Conta:
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular.nome
        self.numero = numero
        self.saldo = saldo
        self.saldo_depo = []
        self.saldo_saq = []

    def Extrato(self):
        print(f'titular: {self.titular}'
              f'\nnumero: {self.numero}')
        print(60 * '\033[34m=\033[m')
        print(f'saldo: \033[32mR${self.saldo}\033[m')
        print(60 * '\033[34m=\033[m')
        for valor in self.saldo_depo:
            print(f'deposito = R${valor}')
        for valor2 in self.saldo_saq:
            print(f'saque = R${valor2}')
        print(60 * '\033[34m=\033[m')

    def Deposito(self, deposito):
        self.saldo += deposito
        print(f'Depositado: R${deposito}'
              f' Novo saldo: R${self.saldo}')
        self.saldo_depo.append(deposito)

    def Saque(self, saque):
        if self.saldo < saque:
            print('\033[31mvoce não possui saldo o suficiente para realizar o saque\033[m')
        else:
            self.saldo -= saque
            print(f'Sacado: \033[31m- R${saque}\033[m'
                  f' Saldo Restante: \033[32mR${self.saldo}\033[m')
            self.saldo_saq.append(saque)
