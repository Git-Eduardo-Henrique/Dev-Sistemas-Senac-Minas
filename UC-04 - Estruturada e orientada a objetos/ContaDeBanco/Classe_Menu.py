class Menu:
    def Linha(self, Color):
        print(60 * f'\033[{Color}m=\033[m')

    def menu_textos(self, parte):
        obj = Menu()
        if parte == 1:
            obj.Linha(Color='34')
            print('Cadastre uma \033[34mconta\033[m para começar')
            obj.Linha(Color='34')
        elif parte == 2:
            obj.Linha(Color='34')
            print('1. Criar conta')
            print('2. Entrar em uma conta')
            print('3. Sair')
            obj.Linha(Color='34')
        elif parte == 3:
            obj.Linha(Color='34')
            print('Conta criada com \033[34msucesso\033[m!')
            obj.Linha(Color='34')
        elif parte == 4:
            obj.Linha(Color='34')
            print('1. Extrato')
            print('2. Deposito')
            print('3. Saque')
            print('4. Deslogar')
            obj.Linha(Color='34')

    def Imprimir_contas(self, lista):
        obj = Menu()
        for conta in lista:
            print(f'conta = {conta.titular}')
        obj.Linha(Color='34')
