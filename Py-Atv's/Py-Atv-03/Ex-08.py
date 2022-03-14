print(60 * '\033[34m=\033[m')
print('''CALCULADORA DO PEDRINHO
1.SOMAR 2.SUBTRAIR 3.MULTIPLICAÇÃO 4.DIVISÃO 5.SAIR''')
print(60 * '\033[34m=\033[m')
opc = 6
while opc > 5:
    opc = int(input('Sua \033[34mopção\033[m: '))
    if opc > 5 or opc <= 0:
        print('\033[31mOPÇÃO INVALIDA!\033[m')
        print(60 * '\033[34m=\033[m')
    elif opc == 5:
        break
    else:
        print(60 * '\033[34m=\033[m')
        num1 = int(input('\033[34mPrimeiro\033[m Numero: '))
        num2 = int(input('\033[34mSegundo\033[m Numero: '))
        print(60 * '\033[34m=\033[m')
        if opc == 1:
            print(f'{num1} + {num2} = {num1 + num2}')
            print(60 * '\033[34m=\033[m')
        elif opc == 2:
            print(f'{num1} - {num2} = {num1 - num2}')
            print(60 * '\033[34m=\033[m')
        elif opc == 3:
            print(f'{num1} x {num2} = {num1 * num2}')
            print(60 * '\033[34m=\033[m')
        elif opc == 4:
            print(f'{num1} % {num2} = {num1 / num2}')
            print(60 * '\033[34m=\033[m')

print('CABO :)')