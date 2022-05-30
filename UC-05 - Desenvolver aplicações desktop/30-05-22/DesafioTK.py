from tkinter import *


def somar():
    if Num_1.get().isnumeric() and Num_2.get().isnumeric():
        Resul['text'] = float(Num_1.get()) + float(Num_2.get())
        Resul['foreground'] = 'black'
    else:
        Resul['text'] = 'Valor Invalido'
        Resul['foreground'] = 'red'


window = Tk()
window.geometry('1280x720')
window.minsize(width=720, height=480)
window.maxsize(width=1960, height=1080)
window.config(bg='gray')

Text_calc = Label(window, text='Super Calculadora Telecurso 2000', font='Arial 30', bg='gray')
Text_Num_1 = Label(window, text='Numero 1', font='Arial 30', bg='gray')
Text_Num_2 = Label(window, text=' + Numero 2', font='Arial 30', bg='gray')
Text_Resul = Label(window, text='Resultado: ', font='Arial 30', bg='gray')
Resul = Label(window, text=' ', font='Arial 30', bg='gray', foreground='black')

Botao = Button(text='somar', font='Arial 20', command=somar)

Num_1 = Entry(window, font='Arial 30')
Num_2 = Entry(window, font='Arial 30')

Text_calc.pack()
Text_Num_1.pack()
Num_1.pack()
Text_Num_2.pack()
Num_2.pack()
Botao.pack()
Text_Resul.pack()
Resul.pack()

window.mainloop()
