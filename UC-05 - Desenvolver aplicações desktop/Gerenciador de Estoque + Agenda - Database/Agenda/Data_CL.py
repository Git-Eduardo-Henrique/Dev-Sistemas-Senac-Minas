import mysql.connector as mys
from Contatos_CL import Contato


class Data:  # conecta e edita o banco de dados de contatos
    def __init__(self):
        # conecta com o banco
        self.database = mys.connect(host='localhost', user='root', password='q1w2e3', database='Agenda')
        self.cursor = self.database.cursor()

    def novo_contato(self, nome, telefone, email):  # cria um novo contato no banco de dados
        contato = Contato(nome=nome, tele=telefone, email=email)
        self.cursor.execute(f'insert into Contato (nome, telefone, email) value ("{contato.nome}", "{contato.tele}", '
                            f'"{contato.email}")')
        self.database.commit()

    def mostra_contatos(self):  # mostra todos os contatos salvos
        self.cursor.execute(f'select * from Contato')
        contatos = self.cursor.fetchall()
        for con in contatos:
            print(70 * '\033[34m=', '\033[m')
            print(f'Codigo: {con[0]}'
                  f'\nNome: {con[1]}'
                  f'\nTelefone: {con[2]}'
                  f'\nEmail: {con[3]}')

    def editar(self, cod, mudar, valor):  # edita alguma informação de um contato
        self.cursor.execute(f'update Contato set {mudar} = "{valor}" where id = {cod}')
        self.database.commit()

    def excluir(self, cod):  # exclui um contato no banco de dados
        self.cursor.execute(f'delete from Contato where id = {cod}')
        self.database.commit()

    def close(self):  # fecha a conexão com o banco
        self.database.close()
        self.cursor.close()
