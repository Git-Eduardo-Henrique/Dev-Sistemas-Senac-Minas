from Contatos_CL import *


class Agenda:
    def __init__(self):
        self.listaCon = []  # lista das informações
        # detalhes do terminal
        self.pula = 10 * '\n'
        self.linha = 70 * '\033[34m=\033[m'

    def salvar_contatos(self):
        print(self.pula)
        print(self.linha)

        # ======================== [informar dados ] =========================
        cod = len(self.listaCon) + 1  #
        print(f'\033[34mId\033[m do produto: \033[34m{cod}\033[m')
        nome = str(input('Informe o \033[34mNome\033[m: '))
        tele = int(input('Informe o \033[34mTelefone\033[m: '))
        # ========================= [salvar dados] ===========================
        self.listaCon.append(Contato(cod=cod, nome=nome, tele=tele))  # salva os dados na classe contato

        print(self.pula)
        print(self.linha)

    def listar_contats(self):
        print(self.pula)
        print(self.linha)
        # =================== [ lista todos os dados de contatos ] =========================
        for cont in range(len(self.listaCon)):
            print(f'id: {self.listaCon[cont].cod}\nnome: {self.listaCon[cont].nome} '
                  f'\ntele: {self.listaCon[cont].tele}')
            print(70 * '-')

    def Mudar_contats(self):
        if len(self.listaCon) == 0:
            print(self.pula)
            print(self.linha)
            print('\033[31mNenhum contato encontrado!!!\033[m')
        else:
            cont = 0
            print(self.pula)
            print(self.linha)
            # =================== [ verificador de contato ] ================
            muda = int(input('Qual \033[34mid\033[m da pessoa que vc quer \033[34mmudar\033[m? '))

            for contats in range(len(self.listaCon)):
                if muda == self.listaCon[contats].cod:  # modifica o contato
                    novo = int(input('\033[34mnovo telefone\033[m: '))
                    self.listaCon[contats].tele = novo
                    print(self.pula)
                else:  # id invalido
                    cont += 1
                    if cont == len(self.listaCon):
                        print(self.pula)
                        print(self.linha)
                        print('\033[31mID nao encontrado!!!\033[m')

