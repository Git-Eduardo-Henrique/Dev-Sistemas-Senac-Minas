
print(60 * '=')
media = float(input('Digite a \033[34;40mmedia\033[m: '))
print(60 * '=')
if media > 6:
    print('\033[34mAprovado!\033[m')
elif 6 > media > 5:
    print('\033[34mRecuperação!\033[m')
elif media < 5:
    print('\033[31mREPROVADO!\033[m')
