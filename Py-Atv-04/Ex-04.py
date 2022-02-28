def Product(x, y, z):
    Conta = x * y * z
    return Conta


num = []
for numero in range(0, 3):
    num.append(int(input(f'Digite o {numero + 1}° numero: ')))
print(Product(num[1], num[2], num[3]))
