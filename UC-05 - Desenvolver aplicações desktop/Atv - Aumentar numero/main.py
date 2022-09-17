from tkinter import *


def Aumentar():  # almenta em um digito o contador
    if num['text'] != 10:
        num['text'] += 1


def Diminuir():  # diminui em um digito o contador
    if num['text'] != -10:
        num['text'] -= 1


# ======================= [ configurações da janela } =======================
window = Tk()
window.geometry('500x300')
window.grid_rowconfigure(0, weight=1)
for linha in range(3):
    window.grid_columnconfigure(linha, weight=1)
# atalhos de teclado
window.bind('-', lambda event: Diminuir())
window.bind('+', lambda event: Aumentar())
# ============================= [ front end ] ================================
menos = Button(window, text='-', font='Arial 50', bg='blue', command=Diminuir)
mais = Button(window, text='+', font='Arial 50', bg='green', command=Aumentar)
num = Label(window, text=0, font='Arial 50', bg='gray')
# ======================== [ posições na janela ] ============================
menos.grid(row=0, column=0, sticky=NSEW)
num.grid(row=0, column=1, sticky=NSEW)
mais.grid(row=0, column=2, sticky=NSEW)

window.mainloop()
