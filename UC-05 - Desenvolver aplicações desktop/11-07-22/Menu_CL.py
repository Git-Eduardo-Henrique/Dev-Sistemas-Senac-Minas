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
        self.frame_menu_cadas.pack()
        img2 = PhotoImage(file='Fotos/2.png')
        img_cadas_prod = PhotoImage(file='Fotos/botao_cadas_prod.PNG')
        menu_cadas = Label(self.frame_menu_cadas, image=img2)
        menu_cadas.pack()
        botao_menu_cadas = Button(self.frame_menu_cadas, image=img_menu_botao, bd=0, activebackground=self.fundo,
                                  bg=self.fundo, command=lambda: [self.frame_menu_ini.pack(),
                                                                  self.frame_menu_cadas.forget()])
        botao_menu_cadas.place(width=32, height=31, x=9, y=11)
        botao_cadas_prod = Button(self.frame_menu_cadas, image=img_cadas_prod, bd=0, activebackground=self.fundo,
                                  command=lambda: [])
        botao_cadas_prod.place(width=210, height=75, x=160, y=173)
        # ========================================================================================
        self.frame_menu_prod = Frame(self.window)
        self.frame_menu_prod.pack()
        img3 = PhotoImage(file='Fotos/3.png')
        menu_prod = Label(self.frame_menu_prod, image=img3)
        menu_prod.pack()
        botao_menu_cadas = Button(self.frame_menu_prod, image=img_menu_botao, bd=0, activebackground=self.branco,
                                  bg=self.branco, command=lambda: [self.frame_menu_ini.pack(),
                                                                   self.frame_menu_prod.forget()])
        botao_menu_cadas.place(width=32, height=31, x=9, y=11)
        # ========================================================================================

        self.window.mainloop()

    '''def rodar(self):
        # =====================================================================
            # menu de seleção
            print(20 * ' ', 'Lojão das fabricantes')
            print('selecione uma \033[34mopção:')
            print('1 - Cadastrar Produto    2 - Cadastrar Fabri'
                  '\n3 - Alterar / Deletar'
                  '              4 - Entrada de produtos'
                  '\n5 - Saida de produtos'
                  '    6 - Listar Produto'
                  '\n7 - Historico            8 - Sair')
            self.linha()
            opt = input('\033[mOpção: ')
            self.linha()
            # verifica qual foi a opção digitada
            # =====================================================================
            if opt.isnumeric():
                if int(opt) == 1:
                    # =====================================================================
                    # Cadastra os produtos
                    nome = str(input('Nome do \033[34mProduto\033[m: '))
                    quant = int(input('\033[34mQuantidade\033[m: '))
                    fra = int(input('Codigo do Fabricante do \033[34mProduto\033[m: '))
                    self.data.cadastro_produto(nome=nome, quant=quant, fabri=fra)
                    self.pula()
                    # =====================================================================
                elif int(opt) == 2:
                    # =====================================================================
                    # Cadastra fabricantes
                    nome = str(input('Nome da \033[34mFabricante\033[m: '))
                    self.data.cadastro_fabricante(nome)
                    # =====================================================================
                elif int(opt) == 3:
                    # =====================================================================
                    # menu de seleção
                    self.pula()
                    self.linha()
                    print('Opções: '
                          '\n\033[34m1 - Alterar nome'
                          '\n2 - Deletar produto\033[m')
                    self.linha()
                    a_opt = input('Sua Opção:')
                    self.linha()
                    # =====================================================================
                    if a_opt.isnumeric():
                        # ====================================================================
                        if int(a_opt) == 1:  # Altera o nome de um produto
                            cod = input('insira o \033[34mcodigo do produto\033[m: ')
                            valor = input('novo \033[34mnome do produto\033[m: ')
                            self.data.altera_produtos(cod=cod, mudar='descricao', valor=valor)
                        elif int(a_opt) == 2:  # Deleta um produto
                            cod2 = input('insira o \033[34mcodigo do produto\033[m: ')
                            self.data.deletar_produtos(cod=cod2)
                        else:
                            print('\033[31mOpção Invalida!\033[m')
                        # =====================================================================
                    else:
                        print('\033[31mdigite um numero!!!\033[m')
                    # =====================================================================
                    # =====================================================================
                elif int(opt) == 4:
                    cod = input('insira o \033[34mcodigo do produto\033[m: ')
                    quant = int(input('Quantidade \033[34mcomprada\033[m: '))
                    self.data.compra_venda(cod=cod, quant=quant, mudar='+')
                elif int(opt) == 5:
                    cod = input('insira o \033[34mcodigo do produto\033[m: ')
                    quant = int(input('Quantidade \033[34mvendida\033[m: '))
                    self.data.compra_venda(cod=cod, quant=quant, mudar='-')
                elif int(opt) == 6:
                    # =====================================================================
                    self.data.listar()
                    # =====================================================================
                elif int(opt) == 7:
                    # =====================================================================
                    # menu de seleção das opções de historico
                    while True:
                        self.pula()
                        self.linha()
                        print('Qual \033[34mhistorico\033[m Você deseja acessar?\033[34m'
                              '\n  1 - Compra'
                              '\n  2 - Venda \033[m')
                        self.linha()
                        # =====================================================================
                        # verifica as opções selecionadas
                        h_opt = input('Opção: ')
                        if h_opt.isnumeric():
                            if int(h_opt) == 1:
                                compra.historico_compra()
                                break
                            elif int(h_opt) == 2:
                                Venda.historico_compra()
                                break
                            else:
                                self.pula()
                                print('selecione uma opção \033[31mVALIDA\033[m')
                        else:
                            self.pula()
                            print('Digite um \033[31mNumero!!!!!!!!\033[m')
                        # =====================================================================
                    # =====================================================================

                elif int(opt) == 8:
                    break
                else:
                    self.pula()
                    print('selecione uma opção \033[31mVALIDA\033[m')
            else:
                self.pula()
                print('Digite um \033[31mNumero!!!!!!!!\033[m')
            # =====================================================================
        # ====================================================================='''
