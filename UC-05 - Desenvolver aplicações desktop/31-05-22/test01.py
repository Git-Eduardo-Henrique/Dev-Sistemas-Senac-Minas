from tkinter import *


def Calculadora(Car):
    if Car == '=':
        resul['text'] = conta['text']
        conta['text'] = ''
    elif Car == 'CE':
        conta['text'] = ''
    else:
        conta['text'] += Car






window = Tk()
window.geometry('350x300')
window.minsize(200, 150)
window.maxsize(600, 550)
window.config(bg='gray')

zero = Button(window, text='0', font='Arial 30', command=lambda: Calculadora(Car='0'))
um = Button(window, text='1', font='Arial 30', command=lambda: Calculadora(Car='1'))
dois = Button(window, text='2', font='Arial 30', command=lambda: Calculadora(Car='2'))
tres = Button(window, text='3', font='Arial 30', command=lambda: Calculadora(Car='3'))
quatro = Button(window, text='4', font='Arial 30', command=lambda: Calculadora(Car='4'))
cinco = Button(window, text='5', font='Arial 30', command=lambda: Calculadora(Car='5'))
seis = Button(window, text='6', font='Arial 30', command=lambda: Calculadora(Car='6'))
sete = Button(window, text='7', font='Arial 30', command=lambda: Calculadora(Car='7'))
oito = Button(window, text='8', font='Arial 30', command=lambda: Calculadora(Car='8'))
nove = Button(window, text='9', font='Arial 30', command=lambda: Calculadora(Car='9'))
botao1 = Button(window, text='+', font='Arial 30', command=lambda: Calculadora(Car='+'))
botao2 = Button(window, text='-', font='Arial 30', command=lambda: Calculadora(Car='-'))
botao3 = Button(window, text='x', font='Arial 30', command=lambda: Calculadora(Car='x'))
botao4 = Button(window, text='%', font='Arial 30', command=lambda: Calculadora(Car='%'))
botao5 = Button(window, text='=', font='Arial 30', command=lambda: Calculadora(Car='='))
botao6 = Button(window, text='CE', font='Arial 30', command=lambda: Calculadora(Car='CE'))
conta = Label(window, text='', font='Arial 30', bg='gray')
resul = Label(window, text='', font='Arial 30', bg='gray')


conta.grid(row=0, column=1, sticky=NSEW)
resul.grid(row=1, column=1, sticky=NSEW)
zero.grid(row=5, column=1, sticky=NSEW)
um.grid(row=2, column=0, sticky=NSEW)
dois.grid(row=2, column=1, sticky=NSEW)
tres.grid(row=2, column=2, sticky=NSEW)
quatro.grid(row=3, column=0, sticky=NSEW)
cinco.grid(row=3, column=1, sticky=NSEW)
seis.grid(row=3, column=2, sticky=NSEW)
sete.grid(row=4, column=0, sticky=NSEW)
oito.grid(row=4, column=1, sticky=NSEW)
nove.grid(row=4, column=2, sticky=NSEW)
botao1.grid(row=2, column=3, sticky=NSEW)
botao2.grid(row=3, column=3, sticky=NSEW)
botao3.grid(row=4, column=3, sticky=NSEW)
botao4.grid(row=5, column=3, sticky=NSEW)
botao5.grid(row=5, column=2, sticky=NSEW)
botao6.grid(row=5, column=0, sticky=NSEW)

window.mainloop()
