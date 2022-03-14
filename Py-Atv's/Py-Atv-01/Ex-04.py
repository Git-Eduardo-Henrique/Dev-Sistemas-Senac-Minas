# Elabore um programa que calcule o imc de uma pessoa

print(70 * '=')
pes = int(input('Digite seu peso (em Kg):'))
alt = float(input('Digite sua altura (em M): '))
print(70 * '=')
imc = pes / (alt * alt)
print(f'Seu IMC: {imc:.2f}')
print(70 * '=')
