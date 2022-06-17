from classe_cliente import *
from classe_conta import *

p1= Cliente(nome='Matheus', cpf='12345678', dataNasc='01/04/2004')
c1= Conta(p1, num='123-4')

p2= Cliente(nome='Pedro', cpf='0102030405', dataNasc='08/03/2003')
c2= Conta(p2,num='123-6')

c1.extrato()
c1.deposito(500)
print('=' * 70)
c2.extrato()
print('=' * 70)
c1.transferencia(50,c2)
c2.extrato()
print('=' * 70)
c1.extrato()
