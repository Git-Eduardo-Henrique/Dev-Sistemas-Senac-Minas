# elabore um algortimo que leia o peso de uma pessoa em KG, calcule e imprima:
# A) o peso da pessoa em gramas
# B) o novo peso da pessoa, em gramas, se a pessoa engordar em 12%

print(70 * '=')
pes = int(input('Digite seu peso (em Kg): '))
print(70 * '=')
print(f'seu peso em gramas: {pes * 100}')
print(f'seu peso + 12%: {pes * 0.12 + pes}')
print(70 * '=')