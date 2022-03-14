class Menu:
    def __init__(self,teste):
        self.teste = teste

    def Linha(self, Cor):
        print(60 * f'\033[{Cor}m=\033[m')

    def menu_principal(self):
        print('1. Criar conta')
        print('2. Entrar em uma conta')
        print('3. Sair')
        Menu.Linha(Cor='34')
