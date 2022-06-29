from System_CL import *


class ControlProd:
    def __init__(self):
        self.entrada = System()

    def almenta_Quant(self):
        prod = int(input('Informe o codigo do \033[34mProduto\033[m: '))
        for produto in range(len(self.entrada.lista_prod)):
            if prod == self.entrada.lista_prod[produto].cod:
                self.entrada.lista_prod[produto].quant += int(input('Novo valor para \033[34madicionar\033[m: '))
            else:
                pass

