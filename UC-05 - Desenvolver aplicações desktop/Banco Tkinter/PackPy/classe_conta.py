class Conta:
    def __init__(self,objetoo,objeto,num,saldo=0.0):
        self.titular = objetoo.nome
        self.nums = objeto.numero
        self.saldo = saldo
        self.num = num

    def extrato(self):
        print(f'Titular: {self.titular}\nSaldo: R${self.saldo}')

    def deposito(self,valor_1):
        self.saldo += valor_1
        print(f'Depositando: R${valor_1}\nNovo Saldo: R${self.saldo}')

    def saque(self, valor_2):
        if valor_2 > self.saldo:
            print('O valor ultrapassou o seu Saldo!')
        else:
            self.saldo -= valor_2
            print(f'Saque: {valor_2}\nSaldo Atual: R${self.saldo}')

    def transferencia(self,valor,conta):
        self.saldo -= valor
        conta.saldo += valor
        print('Transferindo...')

    def imprime_dados_2(self):
        print(f'Titular:{self.titular}\nNúmero da Conta: {self.nums}\nSaldo:R${self.saldo}')



