import mysql.connector as ms
from tkinter import *


class Backend:
    def __init__(self, teste):
        self.teste = teste

    '''def Conexao(self):
        conexao = ms.connect(host='localhost', user='root', password='q1w2e3', database='Banco')
        cursor = conexao.cursor()
        cursor.close()
        conexao.close()'''

    def Func_Senha(self, entry_senha, button, entry_func):
        if button['state'] == NORMAL:
            if entry_func.get() == '022.121.656-17' and entry_senha.get() == 'q1w2e3':
                button['state'] = DISABLED
        else:
            button['state'] = NORMAL



