from tkinter import *


def Escrever():
    print()




window = Tk()
window.config(bg='gray')
for linha1 in range(5):
    window.grid_rowconfigure(linha1, weight=1)
for linha in range(4):
    window.grid_columnconfigure(linha, weight=1)

zero = Button(window, text='0', font='Arial 30')
um = Button(window, text='1', font='Arial 30')
dois = Button(window, text='2', font='Arial 30')
tres = Button(window, text='3', font='Arial 30')
quatro = Button(window, text='4', font='Arial 30')
cinco = Button(window, text='5', font='Arial 30')
seis = Button(window, text='6', font='Arial 30')
sete = Button(window, text='7', font='Arial 30')
oito = Button(window, text='8', font='Arial 30')
nove = Button(window, text='9', font='Arial 30')
botao1 = Button(window, text='+', font='Arial 30')
botao2 = Button(window, text='-', font='Arial 30')
botao3 = Button(window, text='x', font='Arial 30')
botao4 = Button(window, text='%', font='Arial 30')
num1 = Label(window, text='num1', font='Arial 30', bg='gray')
num2 = Label(window, text='num2', font='Arial 30', bg='gray')
resul = Label(window, text='', font='Arial 30', bg='gray')

zero.grid(row=4, column=1, sticky=NSEW)
um.grid(row=1, column=0, sticky=NSEW)
dois.grid(row=1, column=1, sticky=NSEW)
tres.grid(row=1, column=2, sticky=NSEW)
quatro.grid(row=2, column=0, sticky=NSEW)
cinco.grid(row=2, column=1, sticky=NSEW)
seis.grid(row=2, column=2, sticky=NSEW)
sete.grid(row=3, column=0, sticky=NSEW)
oito.grid(row=3, column=1, sticky=NSEW)
nove.grid(row=3, column=2, sticky=NSEW)
num1.grid(row=1, column=3, sticky=NSEW)
num2.grid(row=2, column=3, sticky=NSEW)
resul.grid(row=3, column=3, sticky=NSEW)
botao1.grid(row=5, column=0, sticky=NSEW)
botao2.grid(row=5, column=1, sticky=NSEW)
botao3.grid(row=5, column=2, sticky=NSEW)
botao4.grid(row=5, column=3, sticky=NSEW)

window.mainloop()
