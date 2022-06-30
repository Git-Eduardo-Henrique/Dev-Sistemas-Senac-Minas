from Controlar_CL import *
from System_CL import *

Loja = System()
Fabi = System_Fabri()
compra = CompraProd()
Venda = VendaProd()
compra.entrada = Loja
Venda.entrada = Loja
Loja.entrada = Fabi

while True:
    Loja.linha()
    print(20 * ' ', 'Lojão dos fabricantes')
    Loja.linha()
    print('selecione uma \033[34mopção:')
    Loja.linha()
    print('1 - Cadastrar Produto  4 - Entrada de produtos'
          '\n2 - Cadastrar Fabri'
          '      5 - Saida de produtos'
          '\n3 - Alterar'
          '     6 - Listar Produto'
          '\n7 - Sair')
    Loja.linha()
    Opt = input('\033[mOpção: ')
    Loja.linha()
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
            break
        else:
            Loja.pula()
            print('selecione uma opção \033[31mVALIDA\033[m')
    else:
        Loja.pula()
        print('Digite um \033[31mNumero!!!!!!!!\033[m')
