import mysql.connector as mys
from System_CL import *


class Data:
    def __init__(self):
        self.database = mys.connect(host='localhost', user='root', password='q1w2e3', database='Estoque')
        self.cursor = self.database.cursor()

    def cadastro_produto(self, nome, quant, fabri):
        self.cursor.execute('select codigo from Fabricantes')
        veri = self.cursor.fetchall()

        for cod in veri:
            if fabri == cod[0]:
                produto = SalvarProd(nome, quant, fabri)
                self.cursor.execute(f'insert into Produtos (descricao, quantidade, codigo_fabri) '
                                    f'values ("{produto.nome}", "{produto.quant}", "{produto.fra}")')
                self.database.commit()

    def cadastro_fabricante(self, nome):
        fabricante = SalvarFabri(nome)
        self.cursor.execute(f'insert into Fabricantes (nome) values ("{fabricante.nome}")')
        self.database.commit()

    def listar(self):
        self.cursor.execute('select Produtos.id, Produtos.descricao,Produtos.quantidade, Fabricantes.nome '
                            'from Produtos, Fabricantes where Fabricantes.codigo = Produtos.codigo_fabri')
        produtos = self.cursor.fetchall()
        for prod in produtos:
            print(70 * '\033[34m=', '\033[m')
            print(f'codigo: {prod[0]}'
                  f'\nproduto: {prod[1]}'
                  f'\nquantidade: {prod[2]}'
                  f'\nfabricante: {prod[3]}')

    def altera_produtos(self, cod, mudar, valor):
        try:
            self.cursor.execute(f'update Produtos set {mudar} = "{valor}" where id = {cod}')
            self.database.commit()
        except:
            print('codigo não encontrado')
