import mysql.connector as ms

class pack_data:
    def __init__(self, teste=False):
        self.conectar = ms.connect(host='localhost', user='root', password='q1w2e3', database='Banco')
        self.cursor = self.conectar.cursor()
        if teste:
            self.conectar.close()
            self.cursor.close()

    def Conexao(self):
        print(self.conectar)
        testezino = int(input('teste:'))
        if testezino == 1:
            teste = True
