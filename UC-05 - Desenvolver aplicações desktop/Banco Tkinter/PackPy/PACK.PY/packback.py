from tkinter import *
from tkinter.messagebox import showwarning


class Backend:
    def __init__(self, teste):
        self.teste = teste

    def Formatacao(self, senha_func):
        senha_f = senha_func.get()[:8]
        senha_func.delete(0, 'end')
        senha_func.insert(0, senha_f)
