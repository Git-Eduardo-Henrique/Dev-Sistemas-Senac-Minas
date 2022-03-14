from Classe_Conta import *
from Classe_Cliente import *
from random import randint

# =======================================================================================
# contas e cliente são listas para guardar as informações do usuário
# clientemult variavel para mudar o valor do numero do cliente de acordo com a conta
contas = []
cliente = []
clientemult = 0 
# =======================================================================================
# parte para cadastrar a primeira conta e guardar suas informações
print(60 * '\033[34m=\033[m')
print('Cadastre uma \033[34mconta\033[m para começar')
print(60 * '\033[34m=\033[m')
cliente.append(CLiente(nome=str(input('digite seu \033[34mnome\033[m: ')),
                       cpf=str(input('digite seu \033[34mcpf\033[m:')),
                       datanasc=input('digite sua \033[34mdata na nascimento\033[m:')))
contas.append(Conta(titular=cliente[0], numero=randint(100000, 500000)))
print(60 * '\033[34m=\033[m')
print('Conta criada com \033[34msucesso\033[m!')
print(60 * '\033[34m=')
# ========================================================================================
# loop do menu
while True:
    # menu principal e variavel para selecionar a opção desejada
    print('1. Criar conta')
    print('2. Entrar em uma conta')
    print('3. Sair')
    print(60 * '\033[34m=\033[m')
    opc1 = int(input('sua \033[34mopção\033[m: '))
    print(60 * '\033[34m=\033[m')
    # ====================================================================================
    # inicia o cadastro caso o usuário selecione 1
    if opc1 == 1:
        # cadastra uma nova conta e guarda suas informações
        clientemult += 1  # usuado para a conta na linha 40 condizer com o cliente
        cliente.append(CLiente(nome=str(input('digite seu \033[34mnome\033[m: ')),
                               cpf=str(input('digite seu \033[34mcpf\033[m:')),
                               datanasc=input('digite sua \033[34mdata na nascimento\033[m:')))
        contas.append(Conta(titular=cliente[clientemult], numero=randint(100000, 500000)))
        print('Conta criada com \033[34msucesso\033[m!')
        print(60 * '\033[34m=\033[m')
    # =================================================================================
    # Permite o usuário entrar em uma conta caso o mesmo selecione 2
    elif opc1 == 2:
        # mostra o nome das contas cadastradas na tela
        # =================================================================================
        for conta in contas:
            print(f'conta = {conta.titular}')
        print(60 * '\033[34m=\033[m')
        # =================================================================================
        # loop caso o usuário erre o nome da conta
        while True:
            # =================================================================================
            # seleciona qual conta o usuario deseja entrar
            opc2 = str(input('Qual \033[34mconta\033[m voce deseja \033[34mentrar\033[m(enter = sair)? '))
            print(60 * '\033[34m=\033[m')
            # =================================================================================
            # se o usuário digitar "s" ele sai da opção de escolher conta
            if opc2 in "":
                break
            else:
                # verifica se a conta digitada condiz com alguma conta existente
                for num_conta in range(0, len(contas)):
                    if opc2 == contas[num_conta].titular:
                        # =================================================================================
                        # mostra o menu de possiveis ações da conta
                        print(f'Entrou na conta {contas[num_conta].titular} com sucesso')
                        print(60 * '\033[34m=\033[m')
                        print('1. Extrato')
                        print('2. Deposito')
                        print('3. Saque')
                        print('4. Deslogar')
                        print(60 * '\033[34m=\033[m')
                        # seleciona uma opção
                        opc3 = int(input('sua \033[34mopção\033[m: '))
                        print(60 * '\033[34m=\033[m')
                        # =================================================================================
                        # se o usuário selecionar a opções 1 irá emitir um extrato
                        if opc3 == 1:
                            cliente[num_conta].Imprimir()
                            contas[num_conta].Extrato()
                        # se o usuário selecionar a opções 2 irá começar o deposito
                        elif opc3 == 2:
                            # mostra o nome das contas cadastradas na tela
                            for conta2 in contas:
                                print(f'conta = \033[34m{conta2.titular}\033[m')
                            print(60 * '\033[34m=\033[m')
                            # seleciona qual conta o usuario deseja efetuar o deposito
                            opc4 = str(input('Em qual conta \033[34mvoce\033[m deseja efetuar o \033['
                                             '34mdeposito\033[m? '))
                            print(60 * '\033[34m=\033[m')
                            # verifica se a conta digitada condiz com alguma conta existente
                            for num_depo in range(0, len(contas)):
                                if opc4 == contas[num_depo].titular:
                                    # parte para digitar o valor e efetuar o deposito
                                    depo = float(input('valor do \033[34mdeposito\033[m: R$'))
                                    print(60 * '\033[34m=\033[m')
                                    contas[num_depo].Deposito(deposito=depo)
                                    print(60 * '\033[34m=\033[m')
                        # se o usuário selecionar a opções 3 irá começar o saque
                        elif opc3 == 3:
                            # parte para digitar o valor e efetuar o saque
                            saq = float(input('valor do \033[34mdeposito\033[m: R$'))
                            print(60 * '\033[34m=\033[m')
                            contas[num_conta].Saque(saque=saq)
                            print(60 * '\033[34m=\033[m')
                        # se  o usuário selecionar a opções 4 irá fechar o menu
                        elif opc3 == 4:
                            break
                        # =================================================================================
    # ==================================================================================
    # fecha o programa
    elif opc1 == 3:
        break
    # ===================================================================================
# =======================================================================================
# Cabo :D
