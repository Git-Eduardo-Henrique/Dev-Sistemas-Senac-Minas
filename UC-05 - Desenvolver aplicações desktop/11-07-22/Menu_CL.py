from Data_CL import Data
from tkinter import *
import posiciona


class Menu:
    def __init__(self):
        self.data = Data()
        self.fundo = '#728BB7'
        self.branco = '#ffffff'
        self.window = Tk()
        self.window.geometry('960x540')
        self.window.resizable(False, False)
        # ========================================================================================
        self.window.bind('<Button-1>', posiciona.inicio_place)
        self.window.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, self.window))
        self.window.bind('<Button-2>', lambda arg: posiciona.para_geometry(self.window))
        # ========================================================================================
        img_menu_botao = PhotoImage(file='Fotos/menu.png')
        img_voltar_botao = PhotoImage(file='Fotos/voltar.png')
        self.frame_menu_ini = Frame(self.window)
        self.frame_menu_ini.pack()
        img1 = PhotoImage(file='Fotos/1.png')
        img_botao_cadas = PhotoImage(file='Fotos/botao_cadas.PNG')
        img_botao_prod = PhotoImage(file='Fotos/botao_prod.PNG')

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
        self.frame_menu_cadas = Frame(self.window)
        img2 = PhotoImage(file='Fotos/2.png')
        img_cadas_prod = PhotoImage(file='Fotos/botao_cadas_prod.PNG')
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
        # ========================================================================================
        self.frame_menu_prod = Frame(self.window)
        img3 = PhotoImage(file='Fotos/3.png')
        menu_prod = Label(self.frame_menu_prod, image=img3)
        menu_prod.pack()
        botao_menu_cadas = Button(self.frame_menu_prod, image=img_menu_botao, bd=0, activebackground=self.branco,
                                  bg=self.branco, command=lambda: [self.frame_menu_ini.pack(),
                                                                   self.frame_menu_prod.forget()])
        botao_menu_cadas.place(width=32, height=31, x=9, y=11)
        # ========================================================================================
        self.frame_cadas_prod = Frame(self.window)
        img4 = PhotoImage(file='Fotos/4.png')
        cadas_prod = Label(self.frame_cadas_prod, image=img4)
        cadas_prod.pack()
        botao_menu = Button(self.frame_cadas_prod, image=img_menu_botao, bd=0, activebackground=self.fundo,
                            bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(), self.frame_cadas_prod.forget()])
        botao_menu.place(width=32, height=31, x=9, y=11)
        botao_voltar = Button(self.frame_cadas_prod, image=img_voltar_botao, bd=0, activebackground=self.fundo,
                              bg=self.fundo, command=lambda: [self.frame_cadas_prod.forget(),
                                                              self.frame_menu_cadas.pack()])
        botao_voltar.place(width=32, height=31, x=40, y=12)
        # ========================================================================================

        self.window.mainloop()
