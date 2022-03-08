from classes import *
from Classe_Conta import *
from time import sleep

cliente = {}
conta = {}
# ===========================================================================
# variaveis da conta
print(60 * '\033[34m=\033[m')
cliente["nome"] = str(input('Digite seu \033[34mnome\033[m: '))
cliente["cpf"] = str(input('Digite seu \033[34mcpf\033[m: '))
cliente["data"] = str(input('Digite sua \033[34mdata de nascimento\033[m: '))
c0 = CLiente(nome=cliente["nome"], cpf=cliente["cpf"], datanasc=cliente["data"])
print(60 * '\033[34m=\033[m')
print('Conta criada com \033[34msucesso\033[m!')
# ===========================================================================
# loop do menu
c1 = Conta(titular=c0, numero='1333567')
while True:
    # menu
    print(60 * '\033[34m=')
    print('1. checar extrato da conta')
    print('2. Efetuar deposito')
    print('3. Efetuar saque')
    print('4. Sair')
    print(60 * '\033[34m=\033[m')
    # =======================================================================
    # loop do seletor de opção
    cliente["opc"] = int(input('Oque vc deseja fazer? '))
    print(60 * '\033[34m=\033[m')
    while cliente["opc"] < 1 or cliente["opc"] > 4:
        cliente["opc"] = int(input('Oque vc deseja fazer? '))
        print(60 * '\033[34m=\033[m')
    # =======================================================================
    # efetua cada solicitação do ususario
    if cliente["opc"] == 1:
        print(60 * '\033[34m=\033[m')
        c0.Imprimir()
        c1.Estrato()
        print(60 * '\033[34m=\033[m')
        sleep(2)
    elif cliente["opc"] == 2:
        print(60 * '\033[34m=\033[m')
        conta["deposito"] = float(input('valor do \033[34mdeposito\033[m: '))
        c1.Deposito(deposito=conta["deposito"])
        print(60 * '\033[34m=\033[m')
        sleep(2)
    elif cliente["opc"] == 3:
        print(60 * '\033[34m=\033[m')
        conta["saque"] = float(input('Quanto voce deseja \033[34msacar\033[m: '))
        c1.Saque(saque=conta["saque"])
        print(60 * '\033[34m=\033[m')
        sleep(2)
    else:
        break
    # =======================================================================
print(60 * '\033[34m=\033[m')

# ===========================================================================
