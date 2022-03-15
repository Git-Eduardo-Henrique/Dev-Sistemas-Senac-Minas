from Classe_Conta import *
from Classe_Cliente import *
from Classe_Menu import *
from random import randint

contas = []
cliente = []
menu = Menu()
clientemult = 0

menu.menu_textos(parte=1)
cliente.append(CLiente(nome=str(input('digite seu \033[34mnome\033[m: ')),
                       cpf=str(input('digite seu \033[34mcpf\033[m:')),
                       datanasc=input('digite sua \033[34mdata na nascimento\033[m:')))
contas.append(Conta(titular=cliente[0], numero=randint(100000, 500000)))
menu.menu_textos(parte=3)

while True:
    menu.menu_textos(parte=2)
    opc1 = int(input('sua \033[34mopção\033[m: '))
    menu.Linha(Color='34')
    if opc1 == 1:
        clientemult += 1
        cliente.append(CLiente(nome=str(input('digite seu \033[34mnome\033[m: ')),
                               cpf=str(input('digite seu \033[34mcpf\033[m:')),
                               datanasc=input('digite sua \033[34mdata na nascimento\033[m:')))
        contas.append(Conta(titular=cliente[clientemult], numero=randint(100000, 500000)))
        menu.menu_textos(parte=3)

    elif opc1 == 2:
        menu.Imprimir_contas(lista=contas)
        while True:
            opc2 = str(input('Qual \033[34mconta\033[m voce deseja \033[34mentrar\033[m(enter = sair)? '))
            print(60 * '\033[34m=\033[m')
            if opc2 in "":
                break
            else:
                for num_conta in range(0, len(contas)):
                    if opc2 == contas[num_conta].titular:
                        print(f'Entrou na conta {contas[num_conta].titular} com sucesso')
                        menu.menu_textos(parte=4)
                        opc3 = int(input('sua \033[34mopção\033[m: '))
                        print(60 * '\033[34m=\033[m')
                        if opc3 == 1:
                            cliente[num_conta].Imprimir()
                            contas[num_conta].Extrato()
                        elif opc3 == 2:
                            menu.Imprimir_contas(lista=contas)
                            opc4 = str(input('Em qual conta \033[34mvoce\033[m deseja efetuar o \033['
                                             '34mdeposito\033[m? '))
                            print(60 * '\033[34m=\033[m')
                            for num_depo in range(0, len(contas)):
                                if opc4 == contas[num_depo].titular:
                                    depo = float(input('valor do \033[34mdeposito\033[m: R$'))
                                    print(60 * '\033[34m=\033[m')
                                    contas[num_depo].Deposito(deposito=depo)
                                    print(60 * '\033[34m=\033[m')
                        elif opc3 == 3:
                            saq = float(input('valor do \033[34mdeposito\033[m: R$'))
                            print(60 * '\033[34m=\033[m')
                            contas[num_conta].Saque(saque=saq)
                            print(60 * '\033[34m=\033[m')
                        elif opc3 == 4:
                            break
    elif opc1 == 3:
        break
