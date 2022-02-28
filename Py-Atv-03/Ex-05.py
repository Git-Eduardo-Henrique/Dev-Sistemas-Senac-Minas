cont = 0
num = int(input('Digite um \033[34mnumero\033[m: '))

print(60 * '\033[34m=\033[m')
for cont in range(0, 11):
    print(f'{num} x {cont} = {num * cont}')

print(60 * '\033[34m=\033[m')