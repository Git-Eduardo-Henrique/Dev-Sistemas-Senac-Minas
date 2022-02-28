def MediaList(list):
    soma = 0
    for num in range(len(list)):
        soma += list[num]
    media = soma / len(list)
    return media


ListaDeNum = [1, 2, 3, 4, 5]
print(f'A media da lista é {MediaList(list=ListaDeNum)}')
