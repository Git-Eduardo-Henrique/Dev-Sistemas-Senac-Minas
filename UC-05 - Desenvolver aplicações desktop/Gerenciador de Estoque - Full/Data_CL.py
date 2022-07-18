import mysql.connector as mys
from tkinter.messagebox import *
from Salvar_CL import *


class Data:  # faz a conexão com o banco de dados e usa seus dados
    def __init__(self):  # cria a conexão
        self.database = mys.connect(host='localhost', user='root', password='q1w2e3', database='Estoque')
        self.cursor = self.database.cursor()

    def cadastro_produto(self, nome, quant, fabri, valor):  # faz o cadastro do produto no banco
        try:
            produto = SalvarProd(nome, quant, fabri, valor)
            self.cursor.execute(f'insert into Produtos (descricao, quantidade, valor, codigo_fabri) '
                                f'values ("{produto.nome}", "{produto.quant}", "{produto.valor}", "{produto.fra}")')
            self.database.commit()
            showinfo('Cadastrado', 'Produto cadastrado com sucesso')
        except:
            showerror('Erro de id', 'fabricante desconhecido, verifique e tente novamente')

    def cadastro_fabricante(self, nome, cnpj):  # faz o cadastro do fabricante no banco
        fabricante = SalvarFabri(nome, cnpj)
        self.cursor.execute(f'insert into Fabricantes (nome, cnpj) values ("{fabricante.nome}", "{fabricante.cnpj}")')
        self.database.commit()

    def listar(self, tabela):  # faz a listagem de todos os dados de todos os produtos
        self.cursor.execute('select Produtos.id,Produtos.descricao,Produtos.quantidade,Produtos.valor, Fabricantes.nome'
                            ' from Produtos, Fabricantes where Fabricantes.codigo = Produtos.codigo_fabri')
        produtos = self.cursor.fetchall()
        tabela.delete(*tabela.get_children())
        for prod in produtos:
            valores = [prod[0], prod[1], prod[2], prod[3], prod[4]]
            tabela.insert('', 'end', values=valores, tags='1')

    def altera_produtos(self, cod, desc, valor):  # altera o dado de descrição de um produto
        self.cursor.execute(f'update Produtos set descricao = "{desc}", valor = {valor} where id = {cod}')
        self.database.commit()

    def compra_venda(self, cod, mudar, quant):  # almenta ou diminui a quantidade de um produto
        self.cursor.execute(f'update Produtos set quantidade = quantidade {mudar} {quant} where id = {cod}')
        self.database.commit()

    def deletar_produtos(self, cod):  # deleta um determinado produto no banco de dados
        self.cursor.execute(f'delete from Produtos where id = "{cod}"')
        self.database.commit()
