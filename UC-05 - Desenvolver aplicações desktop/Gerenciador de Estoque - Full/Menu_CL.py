from Back_CL import *
from tkinter import *
from tkinter import ttk


class Menu:
    def __init__(self):
        self.back = BackEnd()
        self.fundo = '#728BB7'
        self.branco = '#ffffff'
        self.window = Tk()
        self.window.geometry('960x540')
        self.window.resizable(False, False)
        self.window.title('PagMenos')
        # ========================================================================================
        # menu principal
        img_menu_botao = PhotoImage(file='Imagens/menu.png')
        img_voltar_botao = PhotoImage(file='Imagens/voltar.png')
        self.frame_menu_ini = Frame(self.window)
        self.frame_menu_ini.pack()
        img1 = PhotoImage(file='Imagens/1.png')
        img_botao_cadas = PhotoImage(file='Imagens/botao_cadas.PNG')
        img_botao_prod = PhotoImage(file='Imagens/botao_prod.PNG')

        menu = Label(self.frame_menu_ini, image=img1)
        menu.pack()

        botao_cadas = Button(self.frame_menu_ini, image=img_botao_cadas, bd=0, activebackground=self.fundo,
                             command=lambda: [self.frame_menu_cadas.pack(), self.frame_menu_ini.forget(),
                                              self.frame_menu_prod.forget()])
        botao_cadas.place(width=140, height=45, x=517, y=325)

        botao_prod = Button(self.frame_menu_ini, image=img_botao_prod, bd=0, activebackground=self.fundo,
                            command=lambda: [self.frame_menu_prod.pack(), self.frame_menu_ini.forget(),
                                             self.frame_menu_cadas.forget()])
        botao_prod.place(width=138, height=50, x=789, y=326)
        # ========================================================================================
        # menu cadastro
        self.frame_menu_cadas = Frame(self.window)
        img2 = PhotoImage(file='Imagens/2.png')
        img_cadas_prod = PhotoImage(file='Imagens/botao_cadas_prod.PNG')
        img_cadas_fabri = PhotoImage(file='Imagens/botao_cadas_fabri.PNG')
        menu_cadas = Label(self.frame_menu_cadas, image=img2)
        menu_cadas.pack()
        botao_menu = Button(self.frame_menu_cadas, image=img_menu_botao, bd=0, activebackground=self.fundo,
                            bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(),
                                                            self.frame_menu_cadas.forget()])
        botao_menu.place(width=32, height=31, x=9, y=11)
        # botão de selecionar o cadastro do produto
        botao_cadas_prod = Button(self.frame_menu_cadas, image=img_cadas_prod, bd=0, activebackground=self.fundo,
                                  command=lambda: [self.frame_menu_cadas.forget(), self.frame_cadas_prod.pack()])
        botao_cadas_prod.place(width=200, height=70, x=165, y=170)
        botao_cadas_fabri = Button(self.frame_menu_cadas, image=img_cadas_fabri, bd=0, activebackground=self.fundo,
                                   command=lambda: [self.frame_menu_cadas.forget(), self.frame_cadas_fabri.pack()])
        botao_cadas_fabri.place(width=200, height=70, x=165, y=315)
        # ========================================================================================
        # menu produtos
        self.frame_menu_prod = Frame(self.window)
        img3 = PhotoImage(file='Imagens/3.png')
        img_prod_listar = PhotoImage(file='Imagens/botao_prod_listar.PNG')
        img_prod_alterar = PhotoImage(file='Imagens/botao_prod_alterar.PNG')
        menu_prod = Label(self.frame_menu_prod, image=img3)
        menu_prod.pack()
        botao_menu_cadas = Button(self.frame_menu_prod, image=img_menu_botao, bd=0, activebackground=self.branco,
                                  bg=self.branco, command=lambda: [self.frame_menu_ini.pack(),
                                                                   self.frame_menu_prod.forget()])
        botao_prod_listar = Button(self.frame_menu_prod, image=img_prod_listar, bd=0, activebackground=self.fundo,
                                   bg=self.fundo, command=lambda: [self.frame_menu_prod.forget(),
                                                                   self.frame_prod_listar.pack()])
        botao_prod_alterar = Button(self.frame_menu_prod, image=img_prod_alterar, bd=0, activebackground=self.fundo,
                                    bg=self.fundo, command=lambda: [self.frame_menu_prod.forget(),
                                                                    self.frame_prod_alterar.pack()])
        botao_prod_listar.place(width=230, height=79, x=420, y=245)
        botao_menu_cadas.place(width=32, height=31, x=9, y=11)
        botao_prod_alterar.place(width=196, height=70, x=730, y=247)
        # ========================================================================================
        # cadastro produtos
        self.frame_cadas_prod = Frame(self.window)
        img4 = PhotoImage(file='Imagens/4.png')
        img_confirmar = PhotoImage(file='Imagens/botao_confirma.PNG')
        cadas_prod = Label(self.frame_cadas_prod, image=img4)
        cadas_prod.pack()

        entry_nome = Entry(self.frame_cadas_prod, font='Arial 15 bold', bd=0)
        entry_quant = Entry(self.frame_cadas_prod, font='Arial 15 bold', bd=0)
        entry_id = Entry(self.frame_cadas_prod, font='Arial 15 bold', bd=0)

        botao_menu = Button(self.frame_cadas_prod, image=img_menu_botao, bd=0, activebackground=self.fundo,
                            bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(), self.frame_cadas_prod.forget()])
        botao_menu.place(width=32, height=31, x=9, y=11)
        botao_voltar = Button(self.frame_cadas_prod, image=img_voltar_botao, bd=0, activebackground=self.fundo,
                              bg=self.fundo, command=lambda: [self.frame_cadas_prod.forget(),
                                                              self.frame_menu_cadas.pack()])
        botao_confirma = Button(self.frame_cadas_prod, image=img_confirmar, bd=0, activebackground=self.fundo,
                                bg=self.fundo, command=lambda: self.back.cadastrar_produto(entry_nome, entry_quant,
                                                                                           entry_id,
                                                                                           self.frame_cadas_prod,
                                                                                           self.frame_menu_cadas))
        entry_id.place(width=77, height=25, x=475, y=234)
        entry_nome.place(width=409, height=26, x=129, y=178)
        entry_quant.place(width=137, height=23, x=168, y=234)
        botao_voltar.place(width=32, height=31, x=40, y=12)
        botao_confirma.place(width=122, height=42, x=420, y=313)
        # ========================================================================================
        # cadastro fabricante
        self.frame_cadas_fabri = Frame(self.window)
        img5 = PhotoImage(file='Imagens/5.png')
        cadas_fabri = Label(self.frame_cadas_fabri, image=img5)
        cadas_fabri.pack()
        entry_nome_fabri = Entry(self.frame_cadas_fabri, font='Arial 15 bold', bd=0)
        botao_menu_cadas = Button(self.frame_cadas_fabri, image=img_menu_botao, bd=0, activebackground=self.fundo,
                                  bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(),
                                                                  self.frame_cadas_fabri.forget()])
        botao_menu_cadas.place(width=32, height=31, x=9, y=11)
        botao_voltar = Button(self.frame_cadas_fabri, image=img_voltar_botao, bd=0, activebackground=self.fundo,
                              bg=self.fundo, command=lambda: [self.frame_cadas_fabri.forget(),
                                                              self.frame_menu_cadas.pack()])
        botao_confirma_fabri = Button(self.frame_cadas_fabri, image=img_confirmar, bd=0, activebackground=self.fundo,
                                      bg=self.fundo, command=lambda: self.back.cadastrar_fabricante(entry_nome_fabri,
                                                                                                    self.frame_cadas_fabri,
                                                                                                    self.frame_menu_cadas))
        botao_confirma_fabri.place(width=116, height=40, x=422, y=272)
        entry_nome_fabri.place(width=420, height=23, x=130, y=178)
        botao_voltar.place(width=32, height=31, x=40, y=12)
        # ========================================================================================
        # tela de listagem
        self.frame_prod_listar = Frame(self.window)
        img6 = PhotoImage(file='Imagens/6.png')
        prod_listar = Label(self.frame_prod_listar, image=img6)
        prod_listar.pack()
        botao_menu_cadas = Button(self.frame_prod_listar, image=img_menu_botao, bd=0, activebackground=self.fundo,
                                  bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(),
                                                                  self.frame_prod_listar.forget()])
        botao_menu_cadas.place(width=32, height=31, x=0, y=11)
        botao_voltar = Button(self.frame_prod_listar, image=img_voltar_botao, bd=0, activebackground=self.fundo,
                              bg=self.fundo, command=lambda: [self.frame_prod_listar.forget(),
                                                              self.frame_menu_prod.pack()])
        botao_voltar.place(width=32, height=31, x=30, y=12)
        # ====================================================================================
        # =============================================================================
        tabela = ttk.Treeview(self.frame_prod_listar, columns=["id", "nome", "quant", "fabri"], selectmode='browse',
                              show='headings')
        tabela.place(width=823, height=475, x=65, y=69)
        # ==============================================================================
        rolar = ttk.Scrollbar(self.frame_prod_listar, orient='vertical', command=tabela.yview())
        rolar.place(height=470, x=886, y=70)
        # ==============================================================================
        tabela.config(xscrollcommand=rolar.set)
        tabela.column("id", width=10)
        tabela.column("nome", width=150)
        tabela.column("quant", width=30)
        tabela.column("fabri", width=150)
        tabela.heading("id", text='Id')
        tabela.heading("nome", text='Nome do produto')
        tabela.heading("quant", text='Quantidade')
        tabela.heading("fabri", text='Fabricante')
        self.back.listar(tabela)
        # ==============================================================================
        # ========================================================================================
        # tela de alterar produto
        self.frame_prod_alterar = Frame(self.window)
        img7 = PhotoImage(file='Imagens/7.png')
        img_botao_alterar = PhotoImage(file='Imagens/botao_alterar.PNG')
        prod_alterar = Label(self.frame_prod_alterar, image=img7)
        prod_alterar.pack()

        entry_id_prod = Entry(self.frame_prod_alterar, font='Arial 15 bold', bd=0)
        entry_novo_nome = Entry(self.frame_prod_alterar, font='Arial 15 bold', bd=0)

        botao_menu_cadas = Button(self.frame_prod_alterar, image=img_menu_botao, bd=0, activebackground=self.branco,
                                  bg=self.branco, command=lambda: [self.frame_menu_ini.pack(),
                                                                   self.frame_prod_alterar.forget()])
        botao_menu_cadas.place(width=32, height=31, x=9, y=11)
        botao_voltar = Button(self.frame_prod_alterar, image=img_voltar_botao, bd=0, activebackground=self.branco,
                              bg=self.branco, command=lambda: [self.frame_prod_alterar.forget(),
                                                               self.frame_menu_prod.pack()])
        botao_confirma_fabri = Button(self.frame_prod_alterar, image=img_botao_alterar, bd=0, activebackground=self.fundo,
                                      bg=self.fundo, command=lambda: self.back.alterar_prod(entry_id_prod, entry_novo_nome,
                                                                                                    self.frame_prod_alterar,
                                                                                                    self.frame_menu_prod))
        botao_confirma_fabri.place(width=125, height=40, x=785, y=270)
        entry_novo_nome.place(width=425, height=22, x=490, y=190)
        entry_id_prod.place(width=81, height=25, x=557, y=145)
        botao_voltar.place(width=32, height=31, x=40, y=12)
        # ========================================================================================
        self.window.mainloop()

