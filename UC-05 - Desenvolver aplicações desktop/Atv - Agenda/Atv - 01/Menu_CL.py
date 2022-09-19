from Agenda_CL import *


class Menu:
    def __init__(self):
        self.ag = Agenda()
        while True:
            print(70 * '\033[34m=\033[m')
            opt = input('Selecione uma opção abaixo \n \033[34m1 - Novo Contato \n 2 - Mostrar Contatos \n '
                        '3 - Mudar Telefone\n 4 - Sair\033[m \nEntrada: ')
            print(70 * '\033[34m=\033[m')
            if opt == '1':
                self.ag.salvar_contatos()
                print('\033[31mSALVO!!!\033[m')
            elif opt == '2':
                self.ag.listar_contats()
            elif opt == '3':
                self.ag.Mudar_contats()
            elif opt == '4':
                break
            else:
                print(10 * '\n')
                print('\033[31mEntrada Errada\033[m')
        print('Cabo :>')
