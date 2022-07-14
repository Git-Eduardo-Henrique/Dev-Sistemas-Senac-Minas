from Data_CL import Data
import tkinter as tk


class Menu:
    def __init__(self):
        self.data = Data()

    def linha(self):  # cria uma linha no terminal
        print(70 * '\033[34m=', '\033[m')

    def pula(self):  # da um grande espaço entre as linhas do terminal
        print(30 * '\n')

    def rodar(self):
        # loop principal
        # =====================================================================
        while True:
            # menu de seleção
            self.linha()
            print(20 * ' ', 'Lojão das fabricantes')
            self.linha()
            print('selecione uma \033[34mopção:')
            self.linha()
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
        # =====================================================================
