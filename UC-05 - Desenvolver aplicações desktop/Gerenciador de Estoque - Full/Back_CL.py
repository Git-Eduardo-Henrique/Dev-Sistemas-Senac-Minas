from Data_CL import *


class BackEnd:  # classe para realizar o back end
    def __init__(self):
        self.data = Data()

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

    def listar(self, frame):  # lista todos os produtos
        self.data.listar(frame)
