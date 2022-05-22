# Exemplo04:Faça um programa que leia os números inteiros digitados pelo usuário até
# queo usuário digite 0 (condição para finalizaro loop).Ao final,mostre a soma de todos os números digitados
N = 1
soma = 0

print(60 * '\033[34m=\033[m')
while N != 0:
    N = int(input('Digite um numero (0 para parar):'))
    soma += N
    if soma >= 20:
        break
print(60 * '\033[34m=\033[m')
print(f'Soma dos numeros: \033[34m{soma}\033[m')
print(60 * '\033[34m=\033[m')
