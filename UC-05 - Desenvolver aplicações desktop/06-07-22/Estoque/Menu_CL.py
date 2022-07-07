from Controlar_CL import *
from System_CL import *
from Data_CL import Data


class Menu:
    def __init__(self):
        self.data = Data()

    def linha(self):  # cria uma linha no terminal
        print(70 * '\033[34m=', '\033[m')

    def pula(self):  # da um grande espaço entre as linhas do terminal
        print(30 * '\n')

    def rodar(self):
        # objetos
        '''Fabi = SystemFabri()
        compra = CompraProd()
        Venda = VendaProd()
        compra.entrada = Loja
        Venda.entrada = Loja
        Loja.entrada = Fabi'''

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
                  '\n3 - Alterar'
                  '              4 - Entrada de produtos'
                  '\n5 - Saida de produtos'
                  '    6 - Listar Produto'
                  '\n7 - Historico            8 - Sair')
            self.linha()
            Opt = input('\033[mOpção: ')
            self.linha()
            # verifica qual foi a opção digitada
            # =====================================================================
            if Opt.isnumeric():
                if int(Opt) == 1:
                    nome = str(input('Nome do \033[34mProduto\033[m: '))
                    quant = int(input('\033[34mQuantidade\033[m: '))
                    fra = int(input('Codigo do Fabricante do \033[34mProduto\033[m: '))
                    self.data.cadastro_produto(nome=nome, quant=quant, fabri=fra)
                    self.pula()
                elif int(Opt) == 2:
                    nome = str(input('Nome da \033[34mFabricante\033[m: '))
                    self.data.cadastro_fabricante(nome)
                elif int(Opt) == 3:
                    Loja.alterar()
                    Loja.pula()
                elif int(Opt) == 4:
                    compra.compra_quant()
                elif int(Opt) == 5:
                    Venda.venda_quant()
                elif int(Opt) == 6:
                    Loja.listar()
                elif int(Opt) == 7:
                    # =====================================================================
                    # menu de seleção das opções de historico
                    while True:
                        Loja.pula()
                        Loja.linha()
                        print('Qual \033[34mhistorico\033[m Você deseja acessar?\033[34m'
                              '\n  1 - Compra'
                              '\n  2 - Venda \033[m')
                        Loja.linha()
                        # =====================================================================
                        # verifica as opções selecionadas
                        H_Opt = input('Opção: ')
                        if H_Opt.isnumeric():
                            if int(H_Opt) == 1:
                                compra.historico_compra()
                                break
                            elif int(H_Opt) == 2:
                                Venda.historico_compra()
                                break
                            else:
                                Loja.pula()
                                print('selecione uma opção \033[31mVALIDA\033[m')
                        else:
                            Loja.pula()
                            print('Digite um \033[31mNumero!!!!!!!!\033[m')
                        # =====================================================================
                    # =====================================================================

                elif int(Opt) == 8:
                    break
                else:
                    Loja.pula()
                    print('selecione uma opção \033[31mVALIDA\033[m')
            else:
                Loja.pula()
                print('Digite um \033[31mNumero!!!!!!!!\033[m')
            # =====================================================================
        # =====================================================================
