from tkinter import *


def PRINT():  # imprime o texto digitado na janela
    Print['text'] = entry.get()
    entry.delete(0, 'end')


# =============================== [ configurações da janela ] ====================
app = Tk()
app.geometry('720x480')
app.minsize(width=720, height=480)
app.maxsize(width=1280, height=720)
app.config(bg='blue')
# =============================== [ front - end ] =================================
Print = Label(app, text='texto digitado aqui', bg='blue', font='Arial 50 bold')
entry = Entry(app, font='Arial 40')
botao = Button(app, text='Sair', font='Arial 30', command=quit)
botao2 = Button(app, text='Imprimir', font='Arial 30', command=PRINT)
# =============================== [ posições na janela ] ==========================
botao.pack()
Print.pack()
entry.pack()
botao2.pack()

app.mainloop()  # loop da janela
