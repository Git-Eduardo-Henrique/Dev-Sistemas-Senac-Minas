print(70 * '=')
pes = int(input('Digite seu peso (em Kg):'))
alt = float(input('Digite sua altura (em M): '))
print(70 * '=')
imc = pes / (alt * alt)
print(f'Seu IMC: {imc:.2f}')
print(70 * '=')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < imc <= 25:
    print('Saudável')
elif 25 < imc <= 30:
    print('Peso em excesso')
elif 30 < imc <= 35:
    print('Obsidade Grau 1')
elif 35 < imc <= 40:
    print('Obsidade Grau 2')
elif imc >= 40:
    print('Obsidade Grau 3')
