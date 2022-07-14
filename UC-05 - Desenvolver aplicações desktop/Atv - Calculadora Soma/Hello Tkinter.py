from tkinter import *


# Back-End
# comando
def PRINT():
    Print['text'] = entry.get()


# Front-End
# janela
app = Tk()
app.geometry('1280x720')
app.minsize(width=720, height=480)
app.maxsize(width=1960, height=1080)
app.config(bg='blue')

# widgets
Print = Label(app, text='Hello World', bg='blue', font='Arial 50 bold')
entry = Entry(app, font='Arial 40')
botao = Button(app, text='Sair', font='Arial 30', command=quit)
botao2 = Button(app, text='Imprimir', font='Arial 30', command=PRINT)

# organizar widgets
botao.pack()
Print.pack()
entry.pack()
botao2.pack()

# executar janela
app.mainloop()
