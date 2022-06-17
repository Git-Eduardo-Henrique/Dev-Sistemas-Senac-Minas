from classe_cliente import *
from classe_conta import *

# instanciar um objeto
c1 = Cliente('','','','')
print('='*70)
print('<Cadastro>')
# objeto.metodo()
c1.imprime_dados()
print('='*70)
c2 = Conta(c1,c1,c1)
while True:
    print('1.Criar um novo Cadastro\n2.Acesso Cliente')
    r= input('')
    if (r == '1'):
        # instanciar um objeto
        c1 = Cliente('', '', '', '')
        print('<Cadastro>')
        # objeto.metodo()
        c1.imprime_dados()
        print('=' * 70)
    if (r == '2'):
        print('<Conta>')
        print('1- Depósito')
        print('2- Saque')
        print('3- Extrato')
        print('4- Sair')
        resposta=input('')
        if resposta == '1':
            c2.deposito(float(input('Digite o Valor para depósito:R$')))
            c2.extrato()
            print('=' * 70)
        elif resposta == '2':
            c2.saque(float(input('Digite o Valor para saque:R$')))
            c2.extrato()
            print('=' * 70)
        elif resposta == '3':
            print('<Extrato>')
            c2.imprime_dados_2()
            print('=' * 70)
        elif resposta == '4':
            print('Obrigado por dar preferência ao nosso Banco')
            break
        else:
            print('Número digitado inválido')