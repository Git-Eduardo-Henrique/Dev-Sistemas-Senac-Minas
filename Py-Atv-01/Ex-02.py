# elabore um algortimo que leia dois numeros inteiros e imprima a seguinte sáida: dividendo, divisor, quociente, resto

num = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

print(30 * '=')
print(f'{num} % {num2} = {num / num2}')
print(30 * '=')
print(f'dividendo: {num}')
print(f'divisor: {num2}')
print(f'quociente: {num/ num2}')
print(f'resto: {num % num2}')
print(30 * '=')