from Salvar_CL import *


class System:
    def __init__(self):
        self.cont = 0
        self.lista_prod = []
        self.entrada = System_Fabri()

    def linha(self):
        print(70 * '\033[34m=', '\033[m')

    def pula(self):
        print(30 * '\n')

    def cadastro(self):
        self.pula()
        self.linha()
        print(f'Codigo do produto {self.cont + 1}')
        self.linha()
        self.cont += 1
        nome = str(input('Nome do \033[34mProduto\033[m: '))
        quant = int(input('\033[34mQuantidade\033[m: '))

        fra = int(input('Codigo do Fabricante do \033[34mProduto\033[m: '))
        for fabri in range(len(self.entrada.list_fabi)):
            if fra == int(self.entrada.list_fabi[fabri].cod):
                self.lista_prod.append(SalvarProd(cod=self.cont, nome=nome, quant=quant,
                                                  fra=self.entrada.list_fabi[fabri].nome))
            else:
                print('Fabricante desconhecido')

        self.linha()

    def alterar(self):
        self.linha()
        prod = input('Informe o codigo do \033[34mProduto\033[m: ')
        self.linha()
        if prod.isnumeric():
            for Prodi in range(len(self.lista_prod)):
                if int(prod) == int(self.lista_prod[Prodi].cod):
                    muda = input('novo \033[34mnome\033[m: ')
                    self.lista_prod[Prodi].nome = muda
        else:
            self.pula()
            self.linha()
            print('Digite um \033[31mCodigo Valido!!!!\033[m')

    def listar(self):
        self.linha()
        prod = input('Informe o codigo do \033[34mProduto\033[m (0 = Mostrar Todos): ')
        self.linha()
        if prod.isnumeric():
            if int(prod) == 0:
                for produto in range(len(self.lista_prod)):
                    self.linha()
                    print(f'Codigo Produto: \033[34m{self.lista_prod[produto].cod}\033[m'
                          f'\nProduto: \033[34m{self.lista_prod[produto].nome}\033[m'
                          f'\nQuantidade: \033[34m{self.lista_prod[produto].quant}\033[m'
                          f'\nFabricante: \033[34m{self.lista_prod[produto].fra}\033[m')
            else:
                for codigo in range(len(self.lista_prod)):
                    if int(prod) == int(self.lista_prod[codigo].cod):
                        self.pula()
                        self.linha()
                        print(f'Codigo Produto: \033[34m{self.lista_prod[codigo].cod}\033[m'
                              f'\nProduto: \033[34m{self.lista_prod[codigo].nome}\033[m'
                              f'\nQuantidade: \033[34m{self.lista_prod[codigo].quant}\033[m'
                              f'\nFabricante: \033[34m{self.lista_prod[codigo].fra}\033[m')
        else:
            self.pula()
            self.linha()
            print('Digite um \033[31mNumero!!!!\033[m')


class System_Fabri:
    def __init__(self):
        self.list_fabi = []
        self.cont = 0

    def linha(self):
        print(70 * '\033[34m=', '\033[m')

    def pula(self):
        print(30 * '\n')

    def cadastro(self):
        print(f'Codigo do frabicante {self.cont + 1}')
        self.cont += 1
        nome = str(input('Nome da \033[34mFabricante\033[m: '))
        self.list_fabi.append(SalvarFabri(cod=self.cont, nome=nome))
