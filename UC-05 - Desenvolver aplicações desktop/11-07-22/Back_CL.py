from Data_CL import *


class BackEnd:
    def __init__(self):
        self.data = Data()

    def cadastrar_produto(self, nome, quant, fabri, frame_cada, frame_menu):
        if askyesno('Confirmar', 'Confirmar dados para o cadastro?'):
            self.data.cadastro_produto(nome=nome.get(), quant=quant.get(), fabri=fabri.get())
            nome.delete(0, 'end')
            quant.delete(0, 'end')
            fabri.delete(0, 'end')
            frame_cada.forget()
            frame_menu.pack()

    def cadastrar_fabricante(self, nome, frame_cada, frame_menu):
        if askyesno('Confirmar', 'Confirmar dados para o cadastro?'):
            self.data.cadastro_fabricante(nome=nome.get())
            nome.delete(0, 'end')
            frame_cada.forget()
            frame_menu.pack()

    def alterar_prod(self, cod, nome, frame_cada, frame_menu):
        if askyesno('Confirmar', 'Confirmar alteração?'):
            self.data.altera_produtos(cod=cod.get(), valor=nome.get(), mudar='descricao')
            cod.delete(0, 'end')
            nome.delete(0, 'end')
            frame_cada.forget()
            frame_menu.pack()

    def listar(self, frame):
        self.data.listar(frame)
