# Faça um programa que converta da notação de 24 horas
# para a notação de 12 horas. Por exemplo, o programa
# deve converter 14:25 em 2:25 P.M. A entrada é dada em dois
# inteiros. Deve haver pelo menos duas funções: uma para fazer
# a conversão e uma para a saída. Registre a informação A.M./P.M.
# como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
# efetuar as conversões terá um parâmetro formal para registrar se
# é A.M. ou P.M. Inclua um loop que permita que o usuário repita
# esse cálculo para novos valores de entrada todas as vezes que
# desejar.

def Notacao(horas):
    if 13 <= horas < 23:
        convert = horas - 12
    elif horas > 23:
        convert = 0
    else:
        convert = horas
    return convert


def Saida(horas):
    if horas < 13 or horas == 24:
        return 'A.M'
    else:
        return 'P.M'


# ======================================================================
while True:
    print(60 * '\033[32m=\033[m')
    agora = float(input('Digite as \033[32mhoras\033[m (em notação de 24h): '))
    # ======================================================================
    print(60 * '\033[32m=\033[m')
    print(f'Horas em \033[32mnotação\033[m de 12H: '
          f'\033[32m{Notacao(agora):.2f}{Saida(agora)}\033[m')
    print(60 * '\033[32m=\033[m')
    # ======================================================================
    sn = 'w'
    while sn not in 'SsnN':
        sn = str(input('Deseja \033[32mcontinuar\033[m? '))
    if sn in 'Nn':
        break
    # ======================================================================
# ======================================================================
