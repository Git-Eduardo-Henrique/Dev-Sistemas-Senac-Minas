from Agenda_CL import *


class Menu:
    def __init__(self):
        self.ag = Agenda()

    def linha(self):
        print(70 * '\033[34m=\033[m')

    def pula(self):
        print(10 * '\n')

    def Rodar(self):
        while True:
            self.linha()
            opt = input('Selecione uma opção abaixo \n \033[34m1 - Novo Contato \n 2 - Mostrar Contatos \n '
                        '3 - Mudar Telefone\n 4 - Sair\033[m \nEntrada: ')
            self.linha()
            if opt == '1':
                self.ag.salvar_contatos()
                self.pula()
                self.linha()
                print('\033[31mSALVO!!!\033[m')
                self.linha()
            elif opt == '2':
                self.pula()
                self.ag.listar_contats()
            elif opt == '3':
                self.pula()
                self.ag.Mudar_contats()
                self.pula()
            elif opt == '4':
                break
            else:
                self.pula()
                print('\033[31mEntrada Errada\033[m')
        print('Cabo :>')
