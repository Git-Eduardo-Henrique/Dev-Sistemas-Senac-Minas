from Contatos_CL import *


class Agenda:
    def __init__(self):
        self.listaCon = []

    def salvar_contatos(self):
        cod = int(input('Informe o \033[34mid\033[m: '))
        nome = str(input('Informe o \033[34mNome\033[m: '))
        tele = int(input('Informe o \033[34mTelefone\033[m: '))
        self.listaCon.append(Contato(cod=cod, nome=nome, tele=tele))

    def listar_contats(self):
        print(70 * '\033[34m=\033[m')
        for cont in range(len(self.listaCon)):
            print(f'id: {self.listaCon[cont].cod}\nnome: {self.listaCon[cont].nome} '
                  f'\ntele: {self.listaCon[cont].tele}')
            print(70 * '-')
        print(70 * '\033[34m=\033[m')

    def Mudar_contats(self):
        cont = 0
        muda = int(input('Qual id da pessoa que vc quer mudar? '))
        for contats in range(len(self.listaCon)):
            if muda == self.listaCon[contats].cod:
                novo = input('novo telefone: ')
                self.listaCon[contats].tele = int(novo)
            else:
                cont += 1
                if cont == len(self.listaCon):
                    print('ID nao encontrado')

