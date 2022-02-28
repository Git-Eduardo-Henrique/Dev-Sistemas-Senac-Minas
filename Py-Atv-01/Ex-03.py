# elabore um algortimo que leia 3 numeros reais e imprima o valor de y sabendo que:
# y = n1 +    n2     + 2 * (n1 - n2)
#          ---------
#           n3 + n1

print(30 * '=')
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
y = n1 + (n2 /(n3 + n1)) + (2 * (n1 - n2))
print(30 * '=')
print(f'resultado: {y}')
print(30 * '=')
