from Class_Data import *


Crud = Data()  # banco de dados
while True:  # menu principal
    Crud.linha()
    print('1 - Cadastrar usuario'
          '\n2 - Modificar Nome'
          '\n3 - Deletar usuario'
          '\n4 - Listar usuarios'
          '\n\033[34m5 - Sair\033[m')
    Crud.linha()
    opt = input('Opção: ')
    if opt.isnumeric():
        # ================================================================================================
        if int(opt) == 1:
            # Create
            Crud.create()
        # ================================================================================================
        elif int(opt) == 2:
            # Update
            Crud.update()
        # ================================================================================================
        elif int(opt) == 3:
            # Delete
            Crud.deletar()
        # ================================================================================================
        elif int(opt) == 4:
            # Read
            Crud.read()
        # ================================================================================================
        elif int(opt) == 5:
            Crud.close()
            Crud.pula()
            print('Programa encerrado!!!')
            break
        else:
            Crud.pula()
            print('\033[31mDigite uma opção valida\033[m')
    else:
        Crud.pula()
        print('\033[31mDIGITE UM NUMERO')
