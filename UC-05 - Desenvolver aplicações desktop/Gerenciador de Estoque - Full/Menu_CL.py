from Back_CL import *
from tkinter import *
from tkinter import ttk
import posiciona
import webbrowser as web


class Menu:  # classe que cria todo o front end
    def __init__(self):
        # =======================================================================================
        # tela principal
        self.window = Tk()
        self.window.geometry('960x540')
        self.window.resizable(False, False)
        self.window.title('PagMenos')
        self.window.iconbitmap('Imagens/pagmenos.ico')
        self.window.bind('<Button-1>', posiciona.inicio_place)
        self.window.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, self.window))
        self.window.bind('<Button-2>', lambda arg: posiciona.para_geometry(self.window))
        # =======================================================================================
        # objetos e outras variaveis uteis
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('arial', 15, 'bold'))
        self.back = BackEnd()
        self.fundo = '#728BB7'
        self.branco = '#ffffff'
        # ========================================================================================
        # frames
        self.frame_menu_ini = Frame(self.window)
        self.frame_menu_ini.pack()
        self.frame_menu_cadas = Frame(self.window)
        self.frame_menu_prod = Frame(self.window)
        self.frame_cadas_prod = Frame(self.window)
        self.frame_cadas_fabri = Frame(self.window)
        self.frame_prod_listar = Frame(self.window)
        self.frame_prod_alterar = Frame(self.window)
        # ========================================================================================
        # imagens
        img1 = PhotoImage(file='Imagens/1.png')
        img2 = PhotoImage(file='Imagens/2.png')
        img3 = PhotoImage(file='Imagens/3.png')
        img4 = PhotoImage(file='Imagens/4.png')
        img5 = PhotoImage(file='Imagens/5.png')
        img6 = PhotoImage(file='Imagens/6.png')
        img7 = PhotoImage(file='Imagens/7.png')
        img_menu_botao = PhotoImage(file='Imagens/menu.png')
        img_voltar_botao = PhotoImage(file='Imagens/voltar.png')
        img_botao_cadas = PhotoImage(file='Imagens/botao_cadas.PNG')
        img_botao_prod = PhotoImage(file='Imagens/botao_prod.PNG')
        img_cadas_prod = PhotoImage(file='Imagens/botao_cadas_prod.PNG')
        img_cadas_fabri = PhotoImage(file='Imagens/botao_cadas_fabri.PNG')
        img_prod_listar = PhotoImage(file='Imagens/botao_prod_listar.PNG')
        img_prod_alterar = PhotoImage(file='Imagens/botao_prod_alterar.PNG')
        img_confirmar = PhotoImage(file='Imagens/botao_confirma.PNG')
        img_recarrega = PhotoImage(file='Imagens/recarregar.PNG')
        img_botao_alterar = PhotoImage(file='Imagens/botao_alterar.PNG')
        img_github = PhotoImage(file='Imagens/github.png')
        img_insta = PhotoImage(file='Imagens/instagram.png')
        img_twitter = PhotoImage(file='Imagens/twitter.png')
        img_face = PhotoImage(file='Imagens/facebook.png')
        # ==========================================================================================
        # MENU PRINCIPAL
        # ----------------------------------------------------------------------------------------
        #  Labels
        menu = Label(self.frame_menu_ini, image=img1)
        # ----------------------------------------------------------------------------------------
        #  Buttons
        botao_cadas = Button(self.frame_menu_ini, image=img_botao_cadas, bd=0, activebackground=self.fundo,
                             command=lambda: [self.frame_menu_cadas.pack(), self.frame_menu_ini.forget(),
                                              self.frame_menu_prod.forget()])

        botao_prod = Button(self.frame_menu_ini, image=img_botao_prod, bd=0, activebackground=self.fundo,
                            command=lambda: [self.frame_menu_prod.pack(), self.frame_menu_ini.forget(),
                                             self.frame_menu_cadas.forget()])
        botao_github = Button(self.frame_menu_ini, image=img_github, bd=0, activebackground=self.fundo, bg=self.fundo,
                              command=lambda: web.open('https://github.com/Git-Eduardo-Henrique'))
        botao_insta = Button(self.frame_menu_ini, image=img_insta, bd=0, activebackground=self.fundo, bg=self.fundo,
                             command=lambda: web.open('https://www.instagram.com'))
        botao_twitter = Button(self.frame_menu_ini, image=img_twitter, bd=0, activebackground=self.fundo, bg=self.fundo,
                               command=lambda: web.open('https://twitter.com/?lang=pt-br'))
        botao_face = Button(self.frame_menu_ini, image=img_face, bd=0, activebackground=self.fundo, bg=self.fundo,
                            command=lambda: web.open('https://pt-br.facebook.com'))
        # ----------------------------------------------------------------------------------------
        #  Posições
        botao_cadas.place(width=140, height=45, x=510, y=325)
        botao_prod.place(width=138, height=50, x=780, y=326)
        botao_insta.place(x=530, y=460)
        botao_face.place(x=578, y=460)
        botao_github.place(x=626, y=460)
        botao_twitter.place(x=674, y=460)
        menu.pack()
        # ----------------------------------------------------------------------------------------
        # ============================================================================================
        # MENU CADASTRO
        # ----------------------------------------------------------------------------------------
        #  Labels
        menu_cadas = Label(self.frame_menu_cadas, image=img2)
        # ----------------------------------------------------------------------------------------
        #  Buttons
        botao_menu = Button(self.frame_menu_cadas, image=img_menu_botao, bd=0, activebackground=self.fundo,
                            bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(),
                                                            self.frame_menu_cadas.forget()])
        botao_cadas_prod = Button(self.frame_menu_cadas, image=img_cadas_prod, bd=0, activebackground=self.fundo,
                                  command=lambda: [self.frame_menu_cadas.forget(), self.frame_cadas_prod.pack()])
        botao_cadas_fabri = Button(self.frame_menu_cadas, image=img_cadas_fabri, bd=0, activebackground=self.fundo,
                                   command=lambda: [self.frame_menu_cadas.forget(), self.frame_cadas_fabri.pack()])
        # ----------------------------------------------------------------------------------------
        # Posições
        botao_cadas_fabri.place(width=200, height=70, x=165, y=315)
        botao_cadas_prod.place(width=200, height=70, x=165, y=170)
        botao_menu.place(width=32, height=31, x=9, y=11)
        menu_cadas.pack()
        # ----------------------------------------------------------------------------------------
        # ==========================================================================================
        # MENU PRODUTOS
        # ----------------------------------------------------------------------------------------
        #  Labels
        menu_prod = Label(self.frame_menu_prod, image=img3)
        # ----------------------------------------------------------------------------------------
        #  Buttons
        botao_menu_cadas = Button(self.frame_menu_prod, image=img_menu_botao, bd=0, activebackground=self.branco,
                                  bg=self.branco, command=lambda: [self.frame_menu_ini.pack(),
                                                                   self.frame_menu_prod.forget()])
        botao_prod_listar = Button(self.frame_menu_prod, image=img_prod_listar, bd=0, activebackground=self.fundo,
                                   bg=self.fundo, command=lambda: [self.frame_menu_prod.forget(),
                                                                   self.frame_prod_listar.pack(),
                                                                   self.back.listar(tabela)])
        botao_prod_alterar = Button(self.frame_menu_prod, image=img_prod_alterar, bd=0, activebackground=self.fundo,
                                    bg=self.fundo, command=lambda: [self.frame_menu_prod.forget(),
                                                                    self.frame_prod_alterar.pack()])
        # ----------------------------------------------------------------------------------------
        #  Posições
        botao_prod_listar.place(width=230, height=79, x=420, y=245)
        botao_menu_cadas.place(width=32, height=31, x=9, y=11)
        botao_prod_alterar.place(width=196, height=70, x=730, y=247)
        menu_prod.pack()
        # ----------------------------------------------------------------------------------------
        # ============================================================================================
        # CADASTRO DE PRODUTOS
        # ----------------------------------------------------------------------------------------
        #  Labels
        cadas_prod = Label(self.frame_cadas_prod, image=img4)
        # ----------------------------------------------------------------------------------------
        #  Entry's
        entry_nome = Entry(self.frame_cadas_prod, font='Arial 15 bold', bd=0)
        entry_quant = Entry(self.frame_cadas_prod, font='Arial 15 bold', bd=0)
        entry_id = Entry(self.frame_cadas_prod, font='Arial 15 bold', bd=0)
        entry_valor = Entry(self.frame_cadas_prod, font='Arial 15 bold', bd=0)
        # ----------------------------------------------------------------------------------------
        # Button's
        botao_menu = Button(self.frame_cadas_prod, image=img_menu_botao, bd=0, activebackground=self.fundo,
                            bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(), self.frame_cadas_prod.forget()])
        botao_menu.place(width=32, height=31, x=9, y=11)
        botao_voltar = Button(self.frame_cadas_prod, image=img_voltar_botao, bd=0, activebackground=self.fundo,
                              bg=self.fundo, command=lambda: [self.frame_cadas_prod.forget(),
                                                              self.frame_menu_cadas.pack()])
        botao_confirma = Button(self.frame_cadas_prod, image=img_confirmar, bd=0, activebackground=self.fundo,
                                bg=self.fundo, command=lambda: self.back.cadastrar_produto(entry_nome, entry_quant,
                                                                                           entry_id, entry_valor,
                                                                                           self.frame_cadas_prod,
                                                                                           self.frame_menu_cadas))
        # ----------------------------------------------------------------------------------------
        #  Posições
        entry_id.place(width=75, height=24, x=199, y=281)
        entry_nome.place(width=409, height=26, x=129, y=176)
        entry_quant.place(width=137, height=23, x=168, y=234)
        entry_valor.place(width=117, height=26, x=414, y=232)
        botao_voltar.place(width=32, height=31, x=40, y=12)
        botao_confirma.place(width=122, height=42, x=420, y=313)
        cadas_prod.pack()
        # ----------------------------------------------------------------------------------------
        # ==========================================================================================
        # CADASTRO DE FABRICANTE
        # ----------------------------------------------------------------------------------------
        #  Labels
        cadas_fabri = Label(self.frame_cadas_fabri, image=img5)
        # ----------------------------------------------------------------------------------------
        #  Entry's
        entry_nome_fabri = Entry(self.frame_cadas_fabri, font='Arial 15 bold', bd=0)
        entry_cnpj = Entry(self.frame_cadas_fabri, font='Arial 15 bold', bd=0)
        # ----------------------------------------------------------------------------------------
        #  Button's
        botao_menu_cadas = Button(self.frame_cadas_fabri, image=img_menu_botao, bd=0, activebackground=self.fundo,
                                  bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(),
                                                                  self.frame_cadas_fabri.forget()])
        botao_menu_cadas.place(width=32, height=31, x=9, y=11)
        botao_voltar = Button(self.frame_cadas_fabri, image=img_voltar_botao, bd=0, activebackground=self.fundo,
                              bg=self.fundo, command=lambda: [self.frame_cadas_fabri.forget(),
                                                              self.frame_menu_cadas.pack()])
        botao_confirma_fabri = Button(self.frame_cadas_fabri, image=img_confirmar, bd=0, activebackground=self.fundo,
                                      bg=self.fundo,
                                      command=lambda: self.back.cadastrar_fabricante(entry_nome_fabri,  entry_cnpj,
                                                                                     self.frame_cadas_fabri,
                                                                                     self.frame_menu_cadas))
        # ----------------------------------------------------------------------------------------
        #  Posições
        botao_confirma_fabri.place(width=116, height=40, x=422, y=272)
        entry_cnpj.place(width=356, height=26, x=132, y=223)
        entry_nome_fabri.place(width=420, height=23, x=130, y=178)
        botao_voltar.place(width=32, height=31, x=40, y=12)
        cadas_fabri.pack()
        # ==========================================================================================
        # TELA DE LISTAGEM
        # ----------------------------------------------------------------------------------------
        #  Label's
        prod_listar = Label(self.frame_prod_listar, image=img6)
        # ----------------------------------------------------------------------------------------
        #  Button's
        botao_menu_cadas = Button(self.frame_prod_listar, image=img_menu_botao, bd=0, activebackground=self.fundo,
                                  bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(),
                                                                  self.frame_prod_listar.forget()])
        botao_menu_cadas.place(width=32, height=31, x=0, y=11)
        botao_voltar = Button(self.frame_prod_listar, image=img_voltar_botao, bd=0, activebackground=self.fundo,
                              bg=self.fundo, command=lambda: [self.frame_prod_listar.forget(),
                                                              self.frame_menu_prod.pack()])
        botao_recarregar = Button(self.frame_prod_listar, image=img_recarrega, bd=0, activebackground='black',
                                  bg='black', command=lambda: [self.back.listar(tabela)])
        # ----------------------------------------------------------------------------------------
        #  Treeview
        tabela = ttk.Treeview(self.frame_prod_listar, columns=["id", "nome", "quant", "valor", "fabri"],
                              selectmode='browse', show='headings')
        rolar = ttk.Scrollbar(self.frame_prod_listar, orient='vertical', command=tabela.yview())
        tabela.config(xscrollcommand=rolar.set)
        tabela.column("id", width=2)
        tabela.column("nome", width=70)
        tabela.column("quant", width=30)
        tabela.column("valor", width=30)
        tabela.column("fabri", width=70)
        tabela.heading("id", text='Id')
        tabela.heading("nome", text='Nome do produto')
        tabela.heading("quant", text='Quantidade')
        tabela.heading("valor", text='Valores')
        tabela.heading("fabri", text='Fabricante')
        # ----------------------------------------------------------------------------------------
        #  Posições
        prod_listar.pack()
        tabela.place(width=823, height=475, x=65, y=69)
        botao_voltar.place(width=32, height=31, x=30, y=12)
        rolar.place(height=470, x=886, y=70)
        botao_recarregar.place(width=54, height=49, x=811, y=23)
        # ----------------------------------------------------------------------------------------
        # ==========================================================================================
        # ALTERAR PRODUTO
        # ----------------------------------------------------------------------------------------
        #  Labels
        prod_alterar = Label(self.frame_prod_alterar, image=img7)
        # ----------------------------------------------------------------------------------------
        #  Entry's
        entry_id_prod = Entry(self.frame_prod_alterar, font='Arial 15 bold', bd=0)
        entry_novo_nome = Entry(self.frame_prod_alterar, font='Arial 15 bold', bd=0)
        entry_novo_valor = Entry(self.frame_prod_alterar, font='Arial 15 bold', bd=0)
        # ----------------------------------------------------------------------------------------
        # Button's
        botao_menu_cadas = Button(self.frame_prod_alterar, image=img_menu_botao, bd=0, activebackground=self.branco,
                                  bg=self.branco, command=lambda: [self.frame_menu_ini.pack(),
                                                                   self.frame_prod_alterar.forget()])
        botao_menu_cadas.place(width=32, height=31, x=9, y=11)
        botao_voltar = Button(self.frame_prod_alterar, image=img_voltar_botao, bd=0, activebackground=self.branco,
                              bg=self.branco, command=lambda: [self.frame_prod_alterar.forget(),
                                                               self.frame_menu_prod.pack()])
        botao_confirma_fabri = Button(self.frame_prod_alterar, image=img_botao_alterar, bd=0,
                                      activebackground=self.fundo, bg=self.fundo,
                                      command=lambda: self.back.alterar_prod(entry_id_prod, entry_novo_nome,
                                                                             entry_novo_valor, self.frame_prod_alterar,
                                                                             self.frame_menu_prod))
        # ----------------------------------------------------------------------------------------
        #  Posições
        botao_confirma_fabri.place(width=125, height=40, x=785, y=270)
        entry_novo_nome.place(width=425, height=22, x=490, y=190)
        entry_id_prod.place(width=81, height=25, x=552, y=147)
        entry_novo_valor.place(width=108, height=25, x=798, y=146)
        botao_voltar.place(width=32, height=31, x=40, y=12)
        prod_alterar.pack()
        # ----------------------------------------------------------------------------------------
        # ==========================================================================================
        self.window.mainloop()
