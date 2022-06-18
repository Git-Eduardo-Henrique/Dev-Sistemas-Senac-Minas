import mysql.connector as ms


class pack_data:
    def __init__(self, teste):
        self.teste = teste

    def Conexao(self):
        conectar = ms.connect()
