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
frame_1 = Frame(window, bg='gray')
frame_2 = Frame(window, bg='#778899')
Centigrados = Label(frame_1, text='C°', font='Arial 30', foreground='orange', bg='gray')
C_Entry = Entry(frame_1, font='Arial 30')
Convert = Button(frame_2, text='Converte °F', font='Arial 30', foreground='red', bg='gray', command=Converter)
resul = Label(frame_2, font='Arial 30', bg='gray')
# ==============================================================================================
# organiza os elementos na tela
frame_1.grid(row=0, column=0)
frame_2.grid(row=0, column=1)
Centigrados.grid(row=0, column=0, sticky=NSEW)
C_Entry.grid(row=0, column=1, sticky=NSEW)
Convert.grid(row=1, column=0, sticky=NSEW)
resul.grid(row=1, column=1, sticky=NSEW)
# ==============================================================================================
window.mainloop()   # ativa o loop da tela
