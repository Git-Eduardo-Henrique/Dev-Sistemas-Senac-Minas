import mysql.connector as mys
from time import sleep


class Data:
    def __init__(self):
        # conexao com o banco de dados
        self.conectar = mys.connect(host='localhost', user='root', password='q1w2e3', database='crud')
        self.cursor = self.conectar.cursor()

    def linha(self):  # cria uma linha no terminal
        print(60 * '\033[34m=', '\033[m')

    def pula(self):
        print(15 * '\n')

    def create(self):  # cadastra uma pessoa no banco de dados
        self.pula()
        self.linha()

        nome = input('digite o seu \033[34mnome\033[m: ')
        data = input('digite a sua\033[34mdata de nascimento (ano,mes e dia)\033[m: ')
        self.cursor.execute(f'Insert into pessoas (nome, datanasc) values ("{nome}", "{data}")')
        self.conectar.commit()

    def read(self):  # mostra todos os contatos
        self.pula()

        self.cursor.execute('SELECT * FROM pessoas')
        lista = self.cursor.fetchall()
        for pes in lista:
            self.linha()
            print(f'\033[34mCodigo\033[m: {pes[0]} \n\033[34mNome\033[m: {pes[1]}\n\033[34mDatanasc\033[m: {pes[2]} ')
        sleep(3)
        self.pula()

    def update(self):  # muda o nome de um usuario
        self.pula()
        self.linha()

        ids = int(input('id para \033[34malterar\033[m: '))
        nome_novo = str(input('Novo \033[34mnome de usuario\033[m: '))
        self.cursor.execute(f"update pessoas set nome = '{nome_novo}' where id = {ids}")
        self.conectar.commit()

        self.pula()

    def deletar(self):
        self.pula()
        id_d = input('id para \033[34mdeletar\033[m: ')
        self.cursor.execute(f'delete from pessoas where id = {id_d}')
        self.conectar.commit()

    def close(self):  # encerra a conexao com o banco
        self.cursor.close()
        self.conectar.close()
