from System_CL import *


class ControlProd:
    def __init__(self):
        self.teste = None

    def almenta_Quant(self):
        prod = input('Informe o codigo do \033[34mProduto\033[m: ')
        if prod.isnumeric():
            for produto in range(len(System().lista_prod)):
                if int(prod) == System().lista_prod[produto].cod:
                    quant = input('Novo valor para \033[34madicionar\033[m: ')
                    System().lista_prod[produto].quant += quant

        else:
            System().pula()
            System().linha()
            print('Digite um \033[31mCodigo Valido!!!!\033[m')

