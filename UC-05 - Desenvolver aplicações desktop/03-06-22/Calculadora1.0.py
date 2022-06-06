from tkinter import *


def Calculadora(Car):
    if Car == '=':
        try:
            conta['text'] = str(eval(conta["text"]))
            conta['foreground'] = 'Green'
        except ZeroDivisionError:
            conta['text'] = 'Impossivel dividir 0 por 0'
            conta['foreground'] = 'orange'
        except SyntaxError:
            conta['text'] = 'Impossivel realizar conta!'
            conta['foreground'] = 'red'
    elif Car == 'CE' or Car == 'C':
        conta['text'] = ''
    elif Car == 'del':
        conta['text'] = conta['text'][:-1]
    else:
        if conta['text'] == 'Impossivel realizar conta!' or conta['text'] == 'Impossivel dividir 0 por 0':
            conta['text'] = ''
            conta['text'] += Car
            conta['foreground'] = 'Green'
        else:
            conta['text'] += Car
            conta['foreground'] = 'Green'


window = Tk()
window.geometry('600x550')
window.minsize(400, 350)
window.maxsize(800, 750)
window.config(bg='black')

window.bind('0', lambda event: Calculadora(Car='0'))
window.bind('1', lambda event: Calculadora(Car='1'))
window.bind('2', lambda event: Calculadora(Car='2'))
window.bind('3', lambda event: Calculadora(Car='3'))
window.bind('4', lambda event: Calculadora(Car='4'))
window.bind('5', lambda event: Calculadora(Car='5'))
window.bind('6', lambda event: Calculadora(Car='6'))
window.bind('7', lambda event: Calculadora(Car='7'))
window.bind('8', lambda event: Calculadora(Car='8'))
window.bind('9', lambda event: Calculadora(Car='9'))
window.bind('<Return>', lambda event: Calculadora(Car='='))
window.bind('<BackSpace>', lambda event: Calculadora(Car='del'))
window.bind('<Escape>', lambda event: Calculadora(Car='CE'))
window.bind('/', lambda event: Calculadora(Car='/'))
window.bind('*', lambda event: Calculadora(Car='*'))
window.bind('+', lambda event: Calculadora(Car='+'))
window.bind('-', lambda event: Calculadora(Car='-'))
window.bind('.', lambda event: Calculadora(Car='.'))

for linha in range(6):
    window.grid_rowconfigure(linha, weight=1)

for Coluna in range(4):
    window.grid_columnconfigure(Coluna, weight=1)

zero = Button(window, text='0', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='0'))
um = Button(window, text='1', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='1'))
dois = Button(window, text='2', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='2'))
tres = Button(window, text='3', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='3'))
quatro = Button(window, text='4', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='4'))
cinco = Button(window, text='5', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='5'))
seis = Button(window, text='6', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='6'))
sete = Button(window, text='7', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='7'))
oito = Button(window, text='8', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='8'))
nove = Button(window, text='9', font='Arial 30', bg='gray', command=lambda: Calculadora(Car='9'))
mais = Button(window, text='+', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='+'))
menos = Button(window, text='-', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='-'))
divisao = Button(window, text='*', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='*'))
Divisao = Button(window, text='/', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='/'))
virgula = Button(window, text='.', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='.'))
DelTudo = Button(window, text='CE', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='CE'))
igual = Button(window, text='=', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='='))
Del = Button(window, text='del', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='del'))
elevado = Button(window, text='x²', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='**'))
DelC = Button(window, text='C', font='Arial 30', bg='#484848', command=lambda: Calculadora(Car='C'))
conta = Label(window, text='', font='Arial 30', bg='black', foreground='green')

conta.grid(columnspan=4, sticky=NSEW)
DelTudo.grid(row=2, column=0, sticky=NSEW)
DelC.grid(row=2, column=1, sticky=NSEW)
Del.grid(row=2, column=2, sticky=NSEW)
Divisao.grid(row=2, column=3, sticky=NSEW)
sete.grid(row=3, column=0, sticky=NSEW)
oito.grid(row=3, column=1, sticky=NSEW)
nove.grid(row=3, column=2, sticky=NSEW)
divisao.grid(row=3, column=3, sticky=NSEW)
quatro.grid(row=4, column=0, sticky=NSEW)
cinco.grid(row=4, column=1, sticky=NSEW)
seis.grid(row=4, column=2, sticky=NSEW)
mais.grid(row=4, column=3, sticky=NSEW)
um.grid(row=5, column=0, sticky=NSEW)
dois.grid(row=5, column=1, sticky=NSEW)
tres.grid(row=5, column=2, sticky=NSEW)
menos.grid(row=5, column=3, sticky=NSEW)
zero.grid(row=6, column=1, sticky=NSEW)
virgula.grid(row=6, column=2, sticky=NSEW)
igual.grid(row=6, column=3, sticky=NSEW)
elevado.grid(row=6, column=0, sticky=NSEW)


window.mainloop()
