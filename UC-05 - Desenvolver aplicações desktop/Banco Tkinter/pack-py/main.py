from packfront import *
from packback import *
from packdata import *
from os import getcwd

diretorio = getcwd() 

# Objetos
Data = DataVerificar()
Conta = Conta()
Back = Backend()

# programa principal
janela = Tk()
janela.geometry('500x500')
janela.resizable(False, False)
janela.title('PackPy')
janela.iconbitmap(f'{diretorio}\\images\\logo.ico')
Front = Frontend(janela=janela)
Front.Conteiner()

# loop
janela.mainloop()
Data.Close()
Conta.Close()
