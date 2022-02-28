# Faça um programa com uma função chamada
# somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas
# expressa em porcentagem e custo, que é o custo de um
# item antes do imposto. A função “altera” o valor de
# custo para incluir o imposto sobre vendas.

def somaImporto(taxaImposto, custo):
    valorfinal = custo + ((taxaImposto / 100) * custo)
    return valorfinal


print(60 * '\033[31m=\033[m')
item = float(input('Valor do \033[31mproduto\033[m: '))
print(60 * '\033[31m=\033[m')
print(f'valor do produto: \033[31mR${item:.2f}\033[m')
print(f'valor do produto + impostos: '
      f'\033[31mR${somaImporto(taxaImposto=7.5, custo=item):.2f}\033[m')
print(60 * '\033[31m=\033[m')
