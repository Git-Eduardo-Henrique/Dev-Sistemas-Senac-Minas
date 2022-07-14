import mysql.connector as mys


class Data:
    def __init__(self):
        self.conectar = mys.connect(host='localhost', user='root', password='q1w2e3', database='crud')
        self.cursor = self.conectar.cursor()

    def linha(self):
        print(60 * '\033[34m=', '\033[m')

    def create(self):
        nome = input('digite seu \033[34mnome\033[m: ')
        data = input('digite a \033[34mdata (ano,mes e dia)\033[m: ')
        self.cursor.execute(f'Insert into pessoas (nome, datanasc) values ("{nome}", "{data}")')
        self.conectar.commit()

    def read(self):
        self.cursor.execute('SELECT * FROM pessoas')
        lista = self.cursor.fetchall()

        for pes in lista:
            self.linha()
            print(f'\033[34mCodigo\033[m: {pes[0]} \n\033[34mNome\033[m: {pes[1]}\n\033[34mDatanasc\033[m: {pes[2]} ')

    def update(self):
        self.linha()
        nome_novo = str(input('Novo nome de usuario: '))
        ids = int(input('id para alterar: '))
        self.linha()
        self.cursor.execute(f"update pessoas set nome = '{nome_novo}' where id = {ids}")
        self.conectar.commit()

    def deletar(self):
        id_d = input('id para deletar: ')
        self.cursor.execute(f'delete from pessoas where id = {id_d}')
        self.conectar.commit()
        self.linha()

    def close(self):
        self.cursor.close()
        self.conectar.close()
