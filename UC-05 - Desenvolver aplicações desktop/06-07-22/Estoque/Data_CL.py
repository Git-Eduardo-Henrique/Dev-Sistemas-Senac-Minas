import mysql.connector as mys


class Data:
    def __init__(self):
        self.database = mys.connect(host='localhost', user='root', password='q1w2e3', database='Agenda')
        self.cursor = self.database.cursor()

    def cadastro_produto(self, nome, quant):
        self.cursor.execute(f'insert into Produtos (descricao, quantidade) values ("{nome}", "{quant}")')
        self.database.commit()

    def cadastro_fabricante(self, nome):
        self.cursor.execute(f'insert into Produtos (nome) values ("{nome}")')
        self.database.commit()

