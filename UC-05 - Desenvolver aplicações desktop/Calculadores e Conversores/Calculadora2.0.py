from tkinter import *


def Calculadora(car):
    if car == 'del':  # deleta um numero
        conta['text'] = conta['text'][:-1]
    elif car == 'CE' or car == 'C':  # deleta tudo oque foi digitado
        conta['text'] = ''
    else:  # deleta as mensagens de erro quando algo é digitado
        if conta['text'] == 'Conta Invalida!!!' or conta['text'] == 'Impossivel dividir por 0':
            conta['text'] = ''
            conta['text'] += car
            conta['foreground'] = 'black'
        else:
            conta['text'] += car
            conta['foreground'] = 'black'


def Resul():
    entrada = conta['text']
    historico = last['text']
    entrada_mod = entrada.replace('+', '|').replace('-', '|').replace('*', '|').replace('/', '|').replace('**', '|')
    entrada_full = entrada_mod.split('|')
    controle = True
    for Numero in range(len(entrada_full)):
        if not entrada_full[Numero].replace('.', '1', 1).isnumeric():
            controle = False
    if controle:
        try:
            conta['text'] = str(eval(entrada))
            conta['foreground'] = 'Blue'
            last['text'] = entrada
            historico += f'\n{last["text"]} = {float(conta["text"]):.2f}'
            last['text'] = historico
        except ZeroDivisionError:
            conta['text'] = 'Impossivel dividir por 0'
            conta['foreground'] = 'orange'
    else:
        conta['text'] = 'Conta Invalida!!!'
        conta['foreground'] = 'red'


# ==================================== [ configurações da janela ] ==============================
window = Tk()
window.geometry('800x550')
window.minsize(400, 350)
window.maxsize(800, 750)
window.config(bg='#483D8B')

window.bind('0', lambda event: Calculadora(car='0'))
window.bind('1', lambda event: Calculadora(car='1'))
window.bind('2', lambda event: Calculadora(car='2'))
window.bind('3', lambda event: Calculadora(car='3'))
window.bind('4', lambda event: Calculadora(car='4'))
window.bind('5', lambda event: Calculadora(car='5'))
window.bind('6', lambda event: Calculadora(car='6'))
window.bind('7', lambda event: Calculadora(car='7'))
window.bind('8', lambda event: Calculadora(car='8'))
window.bind('9', lambda event: Calculadora(car='9'))
window.bind('<Return>', lambda event: Calculadora(car='='))
window.bind('<BackSpace>', lambda event: Calculadora(car='del'))
window.bind('<Escape>', lambda event: Calculadora(car='CE'))
window.bind('/', lambda event: Calculadora(car='/'))
window.bind('*', lambda event: Calculadora(car='*'))
window.bind('+', lambda event: Calculadora(car='+'))
window.bind('-', lambda event: Calculadora(car='-'))
window.bind('.', lambda event: Calculadora(car='.'))

for linha in range(6):
    window.grid_rowconfigure(linha, weight=1)

for Coluna in range(5):
    window.grid_columnconfigure(Coluna, weight=1)

# =================================== [ front-end ] =====================================
zero = Button(window, text='0', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='0'))
um = Button(window, text='1', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='1'))
dois = Button(window, text='2', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='2'))
tres = Button(window, text='3', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='3'))
quatro = Button(window, text='4', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='4'))
cinco = Button(window, text='5', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='5'))
seis = Button(window, text='6', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='6'))
sete = Button(window, text='7', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='7'))
oito = Button(window, text='8', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='8'))
nove = Button(window, text='9', font='Arial 30', bg='#B0C4DE', command=lambda: Calculadora(car='9'))
mais = Button(window, text='+', font='Arial 30', bg='#1E90FF', command=lambda: Calculadora(car='+'))
menos = Button(window, text='-', font='Arial 30', bg='#1E90FF', command=lambda: Calculadora(car='-'))
divisao = Button(window, text='x', font='Arial 30', bg='#1E90FF', command=lambda: Calculadora(car='*'))
Divisao = Button(window, text='÷', font='Arial 30', bg='#1E90FF', command=lambda: Calculadora(car='/'))
virgula = Button(window, text='.', font='Arial 30', bg='#1E90FF', command=lambda: Calculadora(car='.'))
DelTudo = Button(window, text='CE', font='Arial 30', bg='#1E90FF', command=lambda: Calculadora(car='CE'))
igual = Button(window, text='=', font='Arial 30', bg='#1E90FF', command=Resul)
Del = Button(window, text='«', font='Arial 30', bg='#1E90FF', command=lambda: Calculadora(car='del'))
elevado = Button(window, text='+-', font='Arial 30', bg='#1E90FF', command=lambda: Calculadora(car='**'))
DelC = Button(window, text='C', font='Arial 30', bg='#1E90FF', command=lambda: Calculadora(car='C'))
conta = Label(window, text='', font='Arial 30', bg='#778899', foreground='black')
histo = Label(window, text='historico:', font='Arial 30', bg='#483D8B', foreground='black')
last = Label(window, text='', font='Arial 30', bg='#483D8B', foreground='white')
# ================================== [ posições na janela ] ===============================
conta.grid(columnspan=4, sticky=NSEW)
DelTudo.grid(row=1, column=0, sticky=NSEW)
DelC.grid(row=1, column=1, sticky=NSEW)
Del.grid(row=1, column=2, sticky=NSEW)
Divisao.grid(row=1, column=3, sticky=NSEW)
sete.grid(row=2, column=0, sticky=NSEW)
oito.grid(row=2, column=1, sticky=NSEW)
nove.grid(row=2, column=2, sticky=NSEW)
divisao.grid(row=2, column=3, sticky=NSEW)
quatro.grid(row=3, column=0, sticky=NSEW)
cinco.grid(row=3, column=1, sticky=NSEW)
seis.grid(row=3, column=2, sticky=NSEW)
mais.grid(row=3, column=3, sticky=NSEW)
um.grid(row=4, column=0, sticky=NSEW)
dois.grid(row=4, column=1, sticky=NSEW)
tres.grid(row=4, column=2, sticky=NSEW)
menos.grid(row=4, column=3, sticky=NSEW)
zero.grid(row=5, column=1, sticky=NSEW)
virgula.grid(row=5, column=2, sticky=NSEW)
igual.grid(row=5, column=3, sticky=NSEW)
elevado.grid(row=5, column=0, sticky=NSEW)
histo.grid(row=0, column=4, sticky=NSEW)
last.grid(row=1, column=4, rowspan=3)

window.mainloop()
