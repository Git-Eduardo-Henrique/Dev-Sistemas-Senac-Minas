from tkinter import *


def Escrever_1():
    conta['text'] = '1'



window = Tk()
window.geometry('350x300')
window.minsize(200, 150)
window.maxsize(600, 550)
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
botao5 = Button(window, text='=', font='Arial 30')
botao6 = Button(window, text=',', font='Arial 30')
conta = Label(window, text='conta:', font='Arial 30', bg='gray')
resul = Label(window, text='Resultado:', font='Arial 30', bg='gray')

conta.grid(row=0, column=0, sticky=NSEW)
resul.grid(row=1, column=0, sticky=NSEW)
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
