import mysql.connector


class BlackDB:
    def __init__(self):  # conexões com o banco e outros
        self.conexao = mysql.connector.connect(host='localhost', user='root', password='q1w2e3', database='blackmegb')
        self.mycursor = self.conexao.cursor()

    def cadas_user(self, nome, sobrenome, nome_exibicao, email, senha, jogos):  # cadastro de usuarios no banco
        comando_sql = f'insert into Usuarios (nome, sobrenome, nome_exibicao, email, senha, total_jogos) values ' \
                      f'("{nome}", "{sobrenome}", "{nome_exibicao}", "{email}", "{senha}", "{jogos}")'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()

    def check_user(self, entry_email, entry_senha):  # verificador de email e senha de cada usuario
        self.mycursor.execute('select email,senha from Usuarios')
        user = self.mycursor.fetchall()
        verifica = False
        for usuarios in user:
            if entry_email == usuarios[0] and entry_senha == usuarios[1]:
                verifica = True
            else:
                pass
        if verifica:
            return True
        else:
            return False

    def delete_accont(self, email):  # deleta uma conta no banco de dados
        self.mycursor.execute(f'select id from Usuarios where email = "{email}"')
        codigo = self.mycursor.fetchall()
        self.mycursor.execute(f'delete from Usuarios where id = "{codigo[0][0]}" ')
        self.conexao.commit()

    def info_user(self, email):  # cria uma lista com as principais informações
        self.mycursor.execute(f'select nome_exibicao, nome, sobrenome, email, total_jogos from Usuarios where email = "{email}"')
        infos = self.mycursor.fetchall()
        lista = []
        for info in infos:
            lista.append(info[0])
            lista.append(info[1])
            lista.append(info[2])
            lista.append(info[3])
            lista.append(info[4])
        return lista

    def jogos_add(self, mn, email_lb):
        self.mycursor.execute(f'select id from Usuarios where email = "{email_lb}"')
        id_usu = self.mycursor.fetchall()

        for usu in id_usu:
            print(f'update Usuarios set total_jogos {mn} 1 where id = {usu[0]}')
            self.mycursor.execute(f'update Usuarios set total_jogos = total_jogos {mn} 1 where id = {usu[0]}')
            self.conexao.commit()

