from Controlar_CL import *
from System_CL import *

# objetos
Loja = System()
Fabi = SystemFabri()
compra = CompraProd()
Venda = VendaProd()
compra.entrada = Loja
Venda.entrada = Loja
Loja.entrada = Fabi

# loop principal
# =====================================================================
while True:
    # menu de seleção
    Loja.linha()
    print(20 * ' ', 'Lojão das fabricantes')
    Loja.linha()
    print('selecione uma \033[34mopção:')
    Loja.linha()
    print('1 - Cadastrar Produto    2 - Cadastrar Fabri'
          '\n3 - Alterar'
          '              4 - Entrada de produtos'
          '\n5 - Saida de produtos'
          '    6 - Listar Produto'
          '\n7 - Historico            8 - Sair')
    Loja.linha()
    Opt = input('\033[mOpção: ')
    Loja.linha()
    # verifica qual foi a opção digitada
    # =====================================================================
    if Opt.isnumeric():
        if int(Opt) == 1:
            Loja.cadastro()
            Loja.pula()
        elif int(Opt) == 2:
            Fabi.cadastro()
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
