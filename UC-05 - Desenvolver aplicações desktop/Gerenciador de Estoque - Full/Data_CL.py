import mysql.connector as mys
from tkinter.messagebox import *
from Salvar_CL import *


class Data:
    def __init__(self):
        self.database = mys.connect(host='localhost', user='root', password='q1w2e3', database='Estoque')
        self.cursor = self.database.cursor()

    def cadastro_produto(self, nome, quant, fabri):
        try:
            produto = SalvarProd(nome, quant, fabri)
            self.cursor.execute(f'insert into Produtos (descricao, quantidade, codigo_fabri) '
                                f'values ("{produto.nome}", "{produto.quant}", "{produto.fra}")')
            self.database.commit()
        except:
            showerror('Erro de id', 'fabricante desconhecido, verifique e tente novamente')

    def cadastro_fabricante(self, nome):
        fabricante = SalvarFabri(nome)
        self.cursor.execute(f'insert into Fabricantes (nome) values ("{fabricante.nome}")')
        self.database.commit()

    def listar(self, tabela):
        self.cursor.execute('select Produtos.id, Produtos.descricao,Produtos.quantidade, Fabricantes.nome '
                            'from Produtos, Fabricantes where Fabricantes.codigo = Produtos.codigo_fabri')
        produtos = self.cursor.fetchall()
        for prod in produtos:
            valores = [prod[0], prod[1], prod[2], prod[3]]
            tabela.insert('', 'end', values=valores, tags='1')

    def altera_produtos(self, cod, mudar, valor):
        self.cursor.execute(f'update Produtos set {mudar} = "{valor}" where id = {cod}')
        self.database.commit()

    def compra_venda(self, cod, mudar, quant):
        self.cursor.execute(f'update Produtos set quantidade = quantidade {mudar} {quant} where id = {cod}')
        self.database.commit()

    def deletar_produtos(self, cod):
        self.cursor.execute(f'delete from Produtos where id = "{cod}"')
        self.database.commit()
