from Data_CL import *


class BackEnd:  # classe para realizar o back end
    def __init__(self):
        self.data = Data()

    def login(self, nome, codigo, frame1, frame2):
        if self.data.login(nome=nome.get(), codigo=codigo.get()):
            showinfo('Login Realizado', 'Login efetuado com sucesso!')
            frame1.forget()
            frame2.pack()
        else:
            showerror('Erro Login', 'Funcionario desconhecido, tente novamente!')

    def cadastrar_produto(self, nome, quant, fabri, valor, frame_cada, frame_menu):
        # cria uma janela para confirmar o cadastro de produtos
        if askyesno('Confirmar', 'Confirmar dados para o cadastro?'):
            self.data.cadastro_produto(nome=nome.get(), quant=quant.get(), fabri=fabri.get(), valor=valor.get())
            nome.delete(0, 'end')
            quant.delete(0, 'end')
            fabri.delete(0, 'end')
            frame_cada.forget()
            frame_menu.pack()

    def cadastrar_fabricante(self, nome, cnpj, frame_cada, frame_menu):
        # cria uma janela para confirmar o cadastro de fabricante
        if askyesno('Confirmar', 'Confirmar dados para o cadastro?'):
            self.data.cadastro_fabricante(nome=nome.get(), cnpj=cnpj.get())
            nome.delete(0, 'end')
            frame_cada.forget()
            frame_menu.pack()

    def alterar_prod(self, cod, nome, valor, frame_cada, frame_menu):  # cria uma janela para confirmar a alteração de produtos
        if askyesno('Confirmar', 'Confirmar alteração?'):
            self.data.altera_produtos(cod=cod.get(), desc=nome.get(), valor=valor.get())
            cod.delete(0, 'end')
            nome.delete(0, 'end')
            valor.delete(0, 'end')
            frame_cada.forget()
            frame_menu.pack()

    def deletar_prod(self, cod, frame1, frame2):
        if askyesno('Confirmar', 'Confirmar alteração?'):
            self.data.deletar_produtos(cod=cod.get())
            frame1.forget()
            frame2.pack()
            cod.delete(0, 'end')

    def compra_venda(self, cod, mudar, quant, table, frame1, frame2):
        if askyesno('Confirmar', 'Confirmar alteração?'):
            self.data.compra_venda(cod=cod, mudar=mudar, quant=quant, table=table)
            cod.delete(0, 'end')
            quant.delete(0, 'end')
            frame1.forget()
            frame2.pack()

    def listar(self, frame):  # lista todos os produtos
        self.data.listar(frame)

    def listar_fabri(self, tabela):
        self.data.listar_fabri(tabela=tabela)
