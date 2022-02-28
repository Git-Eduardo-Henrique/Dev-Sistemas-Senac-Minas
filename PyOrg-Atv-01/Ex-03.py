def SomaThree(n1, n2, n3):
    return n1 + n2 + n3


numeros = []
for num in range(0,3):
    numeros.append(int(input('digite um numero: ')))
print(f'a soma dos numeros é: {SomaThree(numeros[0], numeros[1], numeros[2])}')
