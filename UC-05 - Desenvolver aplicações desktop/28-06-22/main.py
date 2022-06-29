from Controlar_CL import *

Loja = System()
Control = ControlProd()
while True:
    Loja.linha()
    Opt = input('selecione uma \033[34mopção: '
                '\n 1 - Cadastrar'
                '\n 2 - Listar'
                '\n 3 - Alterar'
                '\n 4 - Entrada de produtos'
                '\n 5 - Sair'
                '\n\033[mOpção: ')
    if Opt.isnumeric():
        if int(Opt) == 1:
            Loja.cadastro()
            Loja.pula()
        elif int(Opt) == 2:
            Loja.listar()
        elif int(Opt) == 3:
            Loja.alterar()
            Loja.pula()
        elif int(Opt) == 4:
            Control.almenta_Quant()
        elif int(Opt) == 5:
            break
        else:
            Loja.pula()
            print('selecione uma opção \033[31mVALIDA\033[m')
    else:
        Loja.pula()
        print('Digite um \033[31mNumero!!!!!!!!\033[m')
