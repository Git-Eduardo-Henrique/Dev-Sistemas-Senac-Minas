# elabore um programa que leia uma temperatura em graus centígrados e apresente-a convertida em graus  fahrenheit, a forma
# de conversão é: f = 9 * C + 32
#                    ---
#                     5

print(70 * '=')
C = int(input('Digite uma temperatura em Graus centígrados: '))
F = (C * 9/5) + 32
print(70 * '=')
print(F'{C}ºc = {F}ºf')
print(70 * '=')