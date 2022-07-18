class SalvarProd:  # Classe para salvar as informações dos produtos
    def __init__(self, nome, quant, fra, valor):
        self.nome = nome
        self.quant = quant
        self.fra = fra
        self.valor = valor


class SalvarFabri:  # Classe para salvar as informações dos fabricantes
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
