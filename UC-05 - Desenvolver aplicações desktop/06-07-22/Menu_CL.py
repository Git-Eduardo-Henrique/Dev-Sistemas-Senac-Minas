from Data_CL import *


class Menu:
    def __init__(self):
        self.data = Data()

    def linha(self):
        print(70 * '\033[34m=\033[m')

    def pula(self):
        print(30 * '\n')

    def rodar(self):
        # ===========================================================================================================
        while True:
            # ===========================================================================================================
            # menu principal
            self.linha()
            opt = input('Selecione uma opção abaixo \n \033[34m1 - Novo Contato \n 2 - Mostrar Contatos \n '
                        '3 - Editar Contato\n 4 - Excluir Contato\n 5 - Sair \033[m\nEntrada: ')
            self.linha()
            # ===========================================================================================================
            if opt.isnumeric():
                # ===========================================================================================================
                if opt == '1':
                    # Adicionar Contato
                    self.pula()
                    self.linha()
                    nome = input('\033[34mNome\033[m: ')
                    tele = input('\033[34mTelefone\033[m: ')
                    email =input('\033[34mEmail\033[m: ')
                    self.data.novo_contato(nome=nome, telefone=tele, email=email)

                    self.pula()
                    self.linha()
                    print('\033[31mSALVO!!!\033[m')
                    self.linha()
                # ===========================================================================================================
                # Mostrar contatos
                elif opt == '2':
                    self.pula()
                    self.data.mostra_contatos()
                # ===========================================================================================================
                # Alterar contato
                elif opt == '3':
                    self.pula()
                    self.linha()
                    print('\033[34m1 - Alterar Telefone'
                          '\n2 - Alterar Email'
                          '\n3 - Alterar Nome\033[m')
                    self.linha()
                    mud = input('Opção: ')
                    # ===========================================================================================================
                    # verifica opção digitada
                    if mud.isnumeric() and int(mud) < 4:
                        self.pula()
                        cod = int(input('\033[34mCodigo do contato: \033[m'))
                        muda = ''
                        valor = ''
                        self.linha()
                        # ===========================================================================================================
                        # editar telefone
                        if mud == '1':
                            valor = input('Digite o \033[34mnovo telefone\033[m: ')
                            muda = 'telefone'
                        # ===========================================================================================================
                        # editar email
                        elif mud == '2':
                            valor = input('Digite o \033[34mnovo email\033[m: ')
                            muda = 'email'
                        # ===========================================================================================================
                        # editar nome
                        elif mud == '3':
                            valor = input('Digite o \033[34mnovo nome\033[m: ')
                            muda = 'nome'
                        # ===========================================================================================================
                        # salvar mudanças
                        self.data.editar(cod=cod, mudar=muda, valor=valor)
                    else:
                        self.pula()
                        print('\033[31mDIGITE UM NUMERO VALIDO!\033[m')
                    # ===========================================================================================================
                # ===========================================================================================================
                # Excluir arquivo
                elif opt == '4':
                    self.pula()
                    self.linha()
                    dele = input('\033[34mCodigo do contato: \033[m')
                    self.data.excluir(cod=dele)
                # ===========================================================================================================
                # fechar programa
                elif opt == '5':
                    self.data.close()
                    break
                # ===========================================================================================================
                else:
                    self.pula()
                    print('\033[31mEntrada Errada\033[m')
                # ===========================================================================================================
            else:
                self.pula()
                print('\033[31mDIGITE UM NUMERO!\033[m')
        # ===========================================================================================================
        print('Cabo :>')
