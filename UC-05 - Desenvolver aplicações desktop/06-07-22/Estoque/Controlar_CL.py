from System_CL import Menu
from time import sleep


class CompraProd:
    # ==================================================================================
    def __init__(self):  # objetos e listas
        self.entrada = System()
        self.hist = []

    # ==================================================================================
    def compra_quant(self):  # almenta a quantidade de produtos
        self.entrada.pula()
        self.entrada.linha()
        # ==================================================================================
        # verifica se o codigo digitado existe
        prod = int(input('Informe o codigo do \033[34mProduto\033[m: '))
        self.entrada.linha()
        for produto in range(len(self.entrada.lista_prod)):
            if prod == self.entrada.lista_prod[produto].cod:
                quanti = int(input('Novo valor para \033[34madicionar\033[m: '))
                self.entrada.lista_prod[produto].quant += quanti
                self.hist.append(f'{quanti} de {self.entrada.lista_prod[produto].nome}')
                self.entrada.pula()
        # ==================================================================================
    # ==================================================================================

    def historico_compra(self):  # mostra o historico de compras
        self.entrada.pula()
        self.entrada.linha()
        for Compra in range(len(self.hist)):
            print(f'Compra: {self.hist[Compra]}')
        sleep(4)
    # ==================================================================================


class VendaProd:
    # ==================================================================================
    def __init__(self):  # objetos e listas
        self.entrada = System()
        self.hist = []

    # ==================================================================================
    def venda_quant(self):  # diminiu a quantidade no historico
        self.entrada.pula()
        self.entrada.linha()
        # ==================================================================================
        prod = int(input('Informe o codigo do \033[34mProduto\033[m: '))
        self.entrada.linha()
        # ==================================================================================
        # verifica se o produto existe
        for produto in range(len(self.entrada.lista_prod)):
            if prod == self.entrada.lista_prod[produto].cod:
                # ==================================================================================
                # cria um loop para caso não haja produtos para vender
                while True:
                    quant = int(input('Quantos produtos \033[34mvendidos?\033[m: '))
                    # ==================================================================================
                    # verifica se há produtos suficientes para efetuar a compra
                    if quant > self.entrada.lista_prod[produto].quant:
                        self.entrada.pula()
                        self.entrada.linha()
                        print('Quantidade \033[31minsuficiente\033[m para a venda!!')
                    else:
                        self.entrada.lista_prod[produto].quant -= quant
                        self.hist.append(f'{quant} de {self.entrada.lista_prod[produto].nome}')
                        self.entrada.pula()
                        print(f'foi retirado: \033[34m{quant}\033[m do produto: {self.entrada.lista_prod[produto].nome}'
                              f' | Restante: \033[34m{self.entrada.lista_prod[produto].quant}\033[m')
                        break
                    # ==================================================================================
                # ==================================================================================
        # ==================================================================================
    # ==================================================================================

    def historico_compra(self):  # mostra o historico de vendas
        self.entrada.pula()
        self.entrada.linha()
        for Venda in range(len(self.hist)):
            print(f'Venda: {self.hist[Venda]}')
        sleep(4)
