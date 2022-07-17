from Data_CL import *


class BackEnd:  # classe para realizar o back end
    def __init__(self):
        self.data = Data()

    def cadastrar_produto(self, nome, quant, fabri, frame_cada, frame_menu):
        # cria uma janela para confirmar o cadastro de produtos
        if askyesno('Confirmar', 'Confirmar dados para o cadastro?'):
            self.data.cadastro_produto(nome=nome.get(), quant=quant.get(), fabri=fabri.get())
            nome.delete(0, 'end')
            quant.delete(0, 'end')
            fabri.delete(0, 'end')
            frame_cada.forget()
            frame_menu.pack()

    def cadastrar_fabricante(self, nome, frame_cada, frame_menu):
        # cria uma janela para confirmar o cadastro de fabricante
        if askyesno('Confirmar', 'Confirmar dados para o cadastro?'):
            self.data.cadastro_fabricante(nome=nome.get())
            nome.delete(0, 'end')
            frame_cada.forget()
            frame_menu.pack()

    def alterar_prod(self, cod, nome, frame_cada, frame_menu):  # cria uma janela para confirmar a alteração de produtos
        if askyesno('Confirmar', 'Confirmar alteração?'):
            self.data.altera_produtos(cod=cod.get(), valor=nome.get(), mudar='descricao')
            cod.delete(0, 'end')
            nome.delete(0, 'end')
            frame_cada.forget()
            frame_menu.pack()

    def listar(self, frame):  # lista todos os produtos
        self.data.listar(frame)
