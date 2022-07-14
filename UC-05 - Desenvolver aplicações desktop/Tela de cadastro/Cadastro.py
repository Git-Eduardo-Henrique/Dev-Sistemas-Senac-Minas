from tkinter import *
from tkinter.messagebox import askyesno


def Render(event=None):
    texto = CPF_Entry.get().replace('.', '').replace('-', '')[:11]
    tele = Tele_Entry.get()[:12]
    data = Data_Entry.get().replace('/', '')[:8]
    novo_texto = ''
    nova_data = ''

    if event.keysym.lower() == 'backspace':
        return

    for numeros in range(len(texto)):

        if not texto[numeros] in "0123456789":
            continue
        if numeros in [2, 5]:
            novo_texto += texto[numeros] + "."
        elif numeros == 8:
            novo_texto += texto[numeros] + "-"
        else:
            novo_texto += texto[numeros]

    for num in range(len(data)):
        if not data[num] in "0123456789":
            continue
        if num in [1, 3]:
            nova_data += data[num] + '/'
        else:
            nova_data += data[num]

    CPF_Entry.delete(0, "end")
    CPF_Entry.insert(0, novo_texto)
    Tele_Entry.delete(0, 'end')
    Tele_Entry.insert(0, tele)
    Data_Entry.delete(0, 'end')
    Data_Entry.insert(0, nova_data)


def Deleter():
    nome_Entry.delete(0, 'end')
    Data_Entry.delete(0, 'end')
    Tele_Entry.delete(0, 'end')
    CPF_Entry.delete(0, 'end')
    Check_Male.deselect()
    Check_Fame.deselect()

# ==========================================================================================================
window = Tk()
window.geometry('745x270')
window.resizable(False, False)
window.title('Gerenciador de Usúario')
window.iconbitmap('PyDados.ico')
window.bind('<KeyRelease>', Render)
# ==========================================================================================================
vd = '#17A589'  # cor verde
azma = '#0B5345'  # azul marrinho

frame_1 = Frame(window, bg=vd)
frame_2 = Frame(window, highlightbackground=vd, highlightthickness=1)
frame_3 = Frame(window, highlightbackground=vd, highlightthickness=1)
frame_4 = Frame(window, highlightbackground=vd, highlightthickness=1)
frame_1_2 = Frame(window, bg=vd)
frame_2_2 = Frame(window, highlightthickness=5)
# ==========================================================================================================
# frame 1
Text_Create = Label(frame_1, text='CADASTRO DE USÚARIO', font='SnapITC 20', bg=vd, fg='white', anchor=E, width=34)
# frame 2
Imagem_Nome = PhotoImage(file='avatar-2.png')
Text_dados = Label(frame_2, text='Dados Pessoais', font='SnapITC 13 italic', fg=vd)
Text_Nome = Label(frame_2, text='Nome:', font='SnapITC 10 italic', fg=azma, pady=3)
nome_Entry = Entry(frame_2, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2)
Imagem_Label_Nome = Label(frame_2, image=Imagem_Nome)
Imagem_Data = PhotoImage(file='baby.png')
Text_Data = Label(frame_2, text='Datanasc:', font='SnapITC 10 italic', fg=azma, pady=3)
Data_Entry = Entry(frame_2, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2)
Imagem_Label_Data = Label(frame_2, image=Imagem_Data)
Imagem_CPF = PhotoImage(file='carteira-de-identidade.png')
Text_CPF = Label(frame_2, text='CPF:', font='SnapITC 10 italic', fg=azma, pady=3)
CPF_Entry = Entry(frame_2, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2)
Imagem_Label_CPF = Label(frame_2, image=Imagem_CPF)
Imagem_Telefone = PhotoImage(file='chamada-telefonica.png')
Text_Tele = Label(frame_2, text='Telefone:', font='SnapITC 10 italic', fg=azma, pady=3)
Tele_Entry = Entry(frame_2, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2)
Imagem_Label_Tele = Label(frame_2, image=Imagem_Telefone)
Text_Sexo = Label(frame_2, text='Sexo:', font='SnapITC 10 italic', fg=azma, pady=3)
Check_Male = Checkbutton(frame_2, text='Masculino', font='SnapITC 10 italic', fg=vd,
                         command=lambda: Check_Fame.deselect())
Check_Fame = Checkbutton(frame_2, text='Feminino', font='SnapITC 10 italic', fg=vd,
                         command=lambda: Check_Male.deselect())
# frame 3
Text_Endereco = Label(frame_3, text='Endereço', font='SnapITC 13 italic', fg=vd)
Text_Rua = Label(frame_3, text='Rua:', font='SnapITC 10 italic', fg=azma, pady=4)
Rua_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2, width=35)
Text_N = Label(frame_3, text='N°:', font='SnapITC 10 italic', fg=azma, pady=4)
N_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2, width=5)
Text_Bairro = Label(frame_3, text='Bairro:', font='SnapITC 10 italic', fg=azma, pady=4)
Bairro_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2, width=20)
Text_Cidade = Label(frame_3, text='Cidade:', font='SnapITC 10 italic', fg=azma)
Cidade_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2, width=20)
Text_UF = Label(frame_3, text='Uf:', font='SnapITC 10 italic', fg=azma, pady=4)
UF_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2, width=5)
# frame 4
Gravar = Button(frame_4, text='CADASTRAR', width=20, height=1, foreground='white', highlightbackground=vd, bg=vd,
                command=lambda: askyesno('Confirmar', 'Salvar estes dados?'))
Limpar = Button(frame_4, text='DESLOGAR', width=20, height=1, foreground='white', bg=vd, highlightbackground=vd,
                command=lambda: [frame_1.grid_forget(), frame_2.grid_forget(), frame_3.grid_forget(),
                                 frame_4.grid_forget(), frame_1_2.grid(row=0, column=0),
                                 frame_2_2.grid(row=0, column=1)])
nulo = Label(frame_4, text='', width=29)
# ==========================================================================================================
# frame 1.2
Imagem_Fundo = PhotoImage(file='fundo.png')
Fundo = Label(frame_1_2, image=Imagem_Fundo)
# frame 2.2
Text_Login = Label(frame_2_2, text='Logar', font='SnapITC 20 italic', anchor=W, pady=20, fg=azma)
Text_CPF_Login = Label(frame_2_2, text='Digite seu CPF:', font='SnapITC 10 italic', pady=5, fg=azma)
CPF_Login_Entry = Entry(frame_2_2, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2)
Text_Senha = Label(frame_2_2, text='Digite sua senha:', font='SnapITC 10 italic', anchor=W, pady=5, fg=azma)
Senha_Entry = Entry(frame_2_2, font='SnapITC 10 italic', highlightbackground=vd, highlightthickness=2)
Logar = Button(frame_2_2, text='LOGAR', bg=vd, fg='white', highlightbackground=vd, pady=6,
               command=lambda: [(frame_1.grid(row=0, column=0, sticky=NSEW, columnspan=2),
                                 frame_2.grid(row=1, column=0, sticky=NSEW),
                                 frame_3.grid(row=1, column=1, sticky=NSEW),
                                 frame_4.grid(row=2, column=0, columnspan=2, sticky=NSEW),
                                 frame_1_2.grid_forget(), frame_2_2.grid_forget())])
# ==========================================================================================================
# frame 1.2
frame_1_2.grid(row=0, column=0, sticky=NSEW)
Fundo.grid()
# frame 2.2
frame_2_2.grid(row=0, column=1, sticky=NSEW)
Text_Login.grid(row=0, column=0)
Text_CPF_Login.grid(row=1, column=0)
CPF_Login_Entry.grid(row=1, column=1)
Text_Senha.grid(row=2, column=0)
Senha_Entry.grid(row=2, column=1)
Logar.grid(row=3, column=0, sticky=NSEW, columnspan=2)
# ==========================================================================================================
# frame 1
Text_Create.grid(row=0, column=0, sticky=NSEW)
# frame 2
Text_dados.grid(row=0, column=0, columnspan=3)
Imagem_Label_Nome.grid(row=1, column=0)
Text_Nome.grid(row=1, column=1)
nome_Entry.grid(row=1, column=2)
Imagem_Label_Data.grid(row=2, column=0)
Text_Data.grid(row=2, column=1)
Data_Entry.grid(row=2, column=2)
Imagem_Label_CPF.grid(row=3, column=0)
Text_CPF.grid(row=3, column=1)
CPF_Entry.grid(row=3, column=2)
Imagem_Label_Tele.grid(row=4, column=0)
Text_Tele.grid(row=4, column=1)
Tele_Entry.grid(row=4, column=2)
Text_Sexo.grid(row=5, column=0)
Check_Male.grid(row=5, column=1)
Check_Fame.grid(row=5, column=2)
# frame 3
Text_Endereco.grid(row=0, column=0, columnspan=5)
Text_Rua.grid(row=1, column=0, sticky=NSEW)
Rua_Entry.grid(row=1, column=1, sticky=NSEW, columnspan=3)
Text_N.grid(row=1, column=4)
N_Entry.grid(row=1, column=5)
Text_Bairro.grid(row=2, column=0, sticky=NSEW)
Bairro_Entry.grid(row=2, column=1)
Text_Cidade.grid(row=2, column=2, sticky=NSEW)
Cidade_Entry.grid(row=2, column=3, sticky=NSEW)
Text_UF.grid(row=2, column=4, sticky=NSEW)
UF_Entry.grid(row=2, column=5, sticky=NSEW)
# frame 4
nulo.grid(row=0, column=0)
Gravar.grid(row=0, column=1, sticky=NSEW)
Limpar.grid(row=0, column=2, sticky=NSEW)
# ==========================================================================================================
window.mainloop()
