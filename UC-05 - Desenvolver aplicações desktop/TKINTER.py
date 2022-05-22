from tkinter import *
def imprimir():
    print('nome %s' %nome.get())

tela = Tk()

tela.title('SUS')

tela.geometry('1280x720')
tela.configure(background='purple')

text = Label(tela, text='NAME', background='purple', foreground='white')
text.place(x=100, y=50, height='200', width='100')

nome = Entry(tela)
nome.place(x=100, y=50)

button = Button(tela, text='SER SUS', background='blue', foreground='black', command=tela.destroy)
button2 = Button(tela, text='Imprimir', background='blue', foreground='black', command=imprimir)
button.place(x=100, y=70)
button2.place(x=150, y=70)

tela.mainloop()
