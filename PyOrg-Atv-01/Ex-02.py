def imprimeLinha(numero):
    for n in range(1, numero + 1):
        print(('  {} ').format(n), end='')
    print()


def imprimeSequencia(numero):
    for numero in range(numero + 1):
        imprimeLinha(numero)


numero = input('Digite um número: ')
imprimeSequencia(int(numero))
