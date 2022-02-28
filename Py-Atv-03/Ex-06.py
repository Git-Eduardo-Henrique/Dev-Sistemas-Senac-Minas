compras = float
total = 0

print(60 * '\033[34m=\033[m')
while compras != 0:
    compras = float(input('Digito o \033[34mpreço\033[m da \033[34mmercadoria\033[m: R$ '))
    total += compras

print(60 * '\033[34m=\033[m')
print(f'total da compra: R${total}')
print(60 * '\033[34m=\033[m')
