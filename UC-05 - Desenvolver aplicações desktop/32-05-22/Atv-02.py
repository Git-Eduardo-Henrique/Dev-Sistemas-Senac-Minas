from tkinter import *


def Converter():
    # ==============================================================================================
    # verifica se o que foi degitado é um numero decimal
    if C_Entry.get().replace('.', '', 1).isdigit():
        # ==============================================================================================
        # converte os graus
        f = float(C_Entry.get()) * 1.8 + 32
        resul['text'] = f'{f:.2f}'
        resul['foreground'] = 'orange'
        # ==============================================================================================
    else:
        # ==============================================================================================
        # caso não seja um numero irá mostra um erro na tela
        resul['text'] = 'digite um numero'
        resul['foreground'] = 'red'
        # ==============================================================================================
    # ==============================================================================================


# ==============================================================================================
# configurações da tela
window = Tk()
window.config(bg='gray')
# ==============================================================================================
# faz com que cada linha e coluna seja esticavel
for linha in range(2):
    window.grid_rowconfigure(linha, weight=1)
for coluna in range(2):
    window.grid_columnconfigure(coluna, weight=1)
# ==============================================================================================
# cria cada elemento da tela
Centigrados = Label(window, text='C°', font='Arial 30', foreground='orange', bg='gray')
C_Entry = Entry(window, font='Arial 30')
Convert = Button(window, text='Converte °F', font='Arial 30', foreground='red', bg='gray', command=Converter)
resul = Label(window, font='Arial 30', bg='gray')
# ==============================================================================================
# organiza os elementos na tela
Centigrados.grid(row=0, column=0, sticky=NSEW)
C_Entry.grid(row=0, column=1, sticky=NSEW)
Convert.grid(row=1, column=0, sticky=NSEW)
resul.grid(row=1, column=1, sticky=NSEW)
# ==============================================================================================
window.mainloop()   # ativa o loop da tela
