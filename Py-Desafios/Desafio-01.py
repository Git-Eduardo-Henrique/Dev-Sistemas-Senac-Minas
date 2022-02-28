print(60 * "\033[36m=\033[m")
contador = int(input('Quantos \033[36malunos?\033[m '))
print(60 * "\033[36m=\033[m")

pessoa = media = soma = 0
Nomes = []
Notas = []

for cont in range(0, contador):
    Nomes.append(str(input('Nome do \033[36maluno\033[m: ')))
    Notas.append(int(input('Nota do \033[36maluno\033[m: ')))
    print(60 * "\033[36m=\033[m")
    soma += Notas[cont]

media = soma / contador
print(f'a \033[36mmedia\033[m da turma foi: \033[36m{media:.2f}\033[m')
print(60 * "\033[36m=\033[m")

for pessoa in range(0, len(Nomes)):
    if Notas[pessoa] >= 6:
        print(f'Parabéns \033[36m{Nomes[pessoa]}\033[m')

print(60 * "\033[36m=\033[m")
