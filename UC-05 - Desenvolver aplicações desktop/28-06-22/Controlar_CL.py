from System_CL import System


class CompraProd:
    def __init__(self):
        self.entrada = System()

    def compra_quant(self):
        self.entrada.pula()
        self.entrada.linha()
        prod = int(input('Informe o codigo do \033[34mProduto\033[m: '))
        self.entrada.linha()
        for produto in range(len(self.entrada.lista_prod)):
            if prod == self.entrada.lista_prod[produto].cod:
                self.entrada.lista_prod[produto].quant += int(input('Novo valor para \033[34madicionar\033[m: '))
                self.entrada.pula()


class VendaProd:
    def __init__(self):
        self.entrada = System()

    def venda_quant(self):
        self.entrada.pula()
        self.entrada.linha()
        prod = int(input('Informe o codigo do \033[34mProduto\033[m: '))
        self.entrada.linha()
        for produto in range(len(self.entrada.lista_prod)):
            if prod == self.entrada.lista_prod[produto].cod:
                while True:
                    quant = int(input('Quantos produtos \033[34mvendidos?\033[m: '))
                    if quant > self.entrada.lista_prod[produto].quant:
                        self.entrada.pula()
                        self.entrada.linha()
                        print('Quantidade \033[31minsuficiente\033[m para a venda!!')
                    else:
                        self.entrada.lista_prod[produto].quant -= quant
                        self.entrada.pula()
                        print(f'foi retirado: \033[34m{quant}\033[m do produto: {self.entrada.lista_prod[produto].nome}'
                              f' | Restante: \033[34m{self.entrada.lista_prod[produto].quant}\033[m')
                        break
