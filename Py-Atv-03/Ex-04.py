password = ''

senha = str(input('Digite uma senha: '))
print(60 * '\033[34m=\033[m')

while password != senha:
    password = str(input('Digite \033[34msua\033[m senha: '))

print(60 * '\033[34m=\033[m')
print('acesso liberado')
print(60 * '\033[34m=\033[m')
