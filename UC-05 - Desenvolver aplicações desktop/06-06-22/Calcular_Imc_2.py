from tkinter import *


def Calcular(limpa=False):  # efetua o calculo de imc
    # ====================================================================================================
    # verifica se o que foi degitado é um numero decimal
    if AlturaEntry.get().replace('.', '', 1).isdigit() and PesoEntry.get().replace('.', '', 1).isdigit():
        # ==============================================================================================
        # verifica o imc e mostra na tela
        imc = float(PesoEntry.get()) / (float(AlturaEntry.get()) * float(AlturaEntry.get()))
        resul['text'] = f'{imc:.2f}'
        resul['foreground'] = 'purple'
        # ==============================================================================================
        # verifica o grau de imc e mostra na tela
        if imc < 18.5:
            saude['text'] = 'Abaixo do peso'
            saude['foreground'] = 'red'
        elif 18.5 < imc <= 25:
            saude['text'] = 'Saudável'
            saude['foreground'] = 'green'
        elif 25 < imc <= 30:
            saude['text'] = 'Peso em excesso'
            saude['foreground'] = 'green'
        elif 30 < imc <= 35:
            saude['text'] = 'Obsidade Grau 1'
            saude['foreground'] = 'pink'
        elif 35 < imc <= 40:
            saude['text'] = 'Obsidade Grau 2'
            saude['foreground'] = 'red'
        elif imc >= 40:
            saude['text'] = 'Obsidade Grau 3'
            saude['foreground'] = 'red'
        # ==============================================================================================
    # caso não seja um numero irá mostra um erro na tela
    else:
        resul['text'] = 'DIGITE APENAS NUMEROS!'
        resul['foreground'] = 'red'
        saude['text'] = ''
    if limpa:
        resul['text'] = ''
        saude['text'] = ''

    # ====================================================================================================


# Front-End
# ==============================================================================================
# configurações da tela
window = Tk()
window.bind('<Return>', lambda event: Calcular())
# ==============================================================================================
# faz com que cada linha e coluna seja esticavel
for linha in range(4):
    window.grid_rowconfigure(linha, weight=1)
for coluna in range(2):
    window.grid_columnconfigure(coluna, weight=1)
# ==============================================================================================
# cria cada elemento da tela
frame_1 = Frame(window, bg='gray')
frame_2 = Frame(window, bg='#778899')
Peso = Label(frame_1, text='Peso:', font='Arial 30', bg='gray')
Altura = Label(frame_1, text='Altura:', font='Arial 30', bg='gray')
PesoEntry = Entry(frame_1, font='Arial 30')
AlturaEntry = Entry(frame_1, font='Arial 30')
Imc = Button(frame_2, text='Calcular Imc', font='Arial 30', bg='gray', command=Calcular)
limpar = Button(frame_2,  text='Limpar', font='Arial 30', bg='gray', command=lambda: Calcular(limpa=True))
resul = Label(frame_2, text='', font='Arial 30', bg='#778899')
saude = Label(frame_2, text='', font='Arial 30', bg='#778899')
# ==============================================================================================
# organiza os elementos na tela
frame_1.grid(row=0, column=0, sticky=NSEW)
frame_2.grid(row=0, column=1, sticky=NSEW)
Peso.grid(row=0, column=0, sticky=NSEW)
PesoEntry.grid(row=0, column=1, sticky=NSEW)
Altura.grid(row=1, column=0, sticky=NSEW)
AlturaEntry.grid(row=1, column=1, sticky=NSEW)
Imc.grid(row=0, column=0, sticky=NSEW)
limpar.grid(row=0, column=1, sticky=NSEW)
resul.grid(row=1, column=0, sticky=NSEW)
saude.grid(row=2, column=0, sticky=NSEW)
# ==============================================================================================
window.mainloop()  # ativa o loop da tela
