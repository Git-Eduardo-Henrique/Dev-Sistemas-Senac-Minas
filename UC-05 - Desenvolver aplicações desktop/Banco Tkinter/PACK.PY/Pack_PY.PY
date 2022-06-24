import posiciona
from packfront import *
from packback import *
from packdata import *
Data = DataVerificar()
Conta = Conta()
Back = Backend()
# programa principal
janela = Tk()
janela.geometry('500x500')
janela.resizable(False, False)
janela.title('PackPy')
janela.iconbitmap('Foto/logo.PNG.ico')
# bind
janela.bind('<Button-1>', posiciona.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, janela))
janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))
janela.bind('<KeyRelease>', Formatar_func)
# loop
# janela.after(3000, frame_i.forget)
janela.mainloop()
Data.Close()
Conta.Close()
