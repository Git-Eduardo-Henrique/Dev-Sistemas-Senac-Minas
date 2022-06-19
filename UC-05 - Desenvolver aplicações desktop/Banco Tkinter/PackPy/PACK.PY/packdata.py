import mysql.connector as ms


class pack_data:
    def __init__(self):
        # conecta com o banco de dados
        self.conectar = ms.connect(host='localhost', user='root', password='q1w2e3', database='Banco_Pack_Py')
        self.cursor = self.conectar.cursor()
        self.func = ''
        self.cli = ''

    def Cadastrar(self, nome, cpf, data, genero, email, senha,saldo):
        # realiza o cadastro no banco de dados
        self.cursor.execute(f'INSERT INTO cliente (cpf, nome, dataNasc, genero, email, senha, saldo) VALUES'
                            f'("{cpf}","{nome}","{data}","{genero}","{email}","{senha}","{saldo}")')
        self.conectar.commit()

    def Check_func(self, entry_id, entry_senha):
        self.cursor.execute(f'SELECT * FROM func')
        self.func = self.cursor.fetchall()
        for funcionario in self.func:
            if entry_id == funcionario[0] and entry_senha == funcionario[1]:
                return True
            else:
                return False

    def Check_cli(self, entry_cpf, entry_senha):
        self.cursor.execute(f'SELECT * FROM cliente')
        self.cli = self.cursor.fetchall()
        for cliente in self.cli:
            print(cliente[1], cliente[5])
            print(entry_cpf, entry_senha)
            if entry_cpf == cliente[1] and entry_senha == cliente[5]:
                return True
            else:
                return False

    def Close(self):
        self.cursor.close()
        self.conectar.close()
