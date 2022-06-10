from tkinter import *


def render(frame, line, colum):
    for linha in range(line):
        frame.grid_rowconfigure(linha, weight=1)
    for coluna in range(colum):
        frame.grid_columnconfigure(coluna, weight=1)


window = Tk()
window.geometry('735x270')
render(frame=window, line=4, colum=2)
# ==========================================================================================================

frame_1 = Frame(window, bg='#17A589')
frame_2 = Frame(window, highlightbackground="#17A589", highlightthickness=1)
frame_3 = Frame(window, highlightbackground="#17A589", highlightthickness=1)
frame_4 = Frame(window, highlightbackground="#17A589", highlightthickness=1)
frame_5 = Frame(window, highlightbackground="#17A589", highlightthickness=1)
render(frame=frame_1, line=1, colum=1)
render(frame=frame_2, line=6, colum=3)
render(frame=frame_3, line=3, colum=6)
render(frame=frame_4, line=1, colum=2)
render(frame=frame_5, line=2, colum=1)
# ==========================================================================================================

# frame 1
Text_Create = Label(frame_1, text='CREATE ACCOUNT', font='SnapITC 20', bg='#17A589', foreground='white', anchor=E, width=30)

# frame 2
Imagem_Nome = PhotoImage(file='avatar-2.png')
Text_dados = Label(frame_2, text='Dados Pessoais', font='SnapITC 13 italic', foreground='#17A589')
Text_Nome = Label(frame_2, text='Nome:', font='SnapITC 10 italic', foreground='#0B5345', pady=3)
nome_Entry = Entry(frame_2, font='SnapITC 10 italic', highlightbackground="#17A589", highlightthickness=2)
Imagem_Label_Nome = Label(frame_2, image=Imagem_Nome)

Imagem_Data = PhotoImage(file='baby.png')
Text_Data = Label(frame_2, text='Datanasc:', font='SnapITC 10 italic', foreground='#0B5345', pady=3)
Data_Entry = Entry(frame_2, font='SnapITC 10 italic', highlightbackground="#17A589", highlightthickness=2)
Imagem_Label_Data = Label(frame_2, image=Imagem_Data)

Imagem_CPF = PhotoImage(file='carteira-de-identidade.png')
Text_CPF = Label(frame_2, text='CPF:', font='SnapITC 10 italic', foreground='#0B5345', pady=3)
CPF_Entry = Entry(frame_2, font='SnapITC 10 italic', highlightbackground="#17A589", highlightthickness=2)
Imagem_Label_CPF = Label(frame_2, image=Imagem_CPF)

Imagem_Telefone = PhotoImage(file='chamada-telefonica.png')
Text_Tele = Label(frame_2, text='Telefone:', font='SnapITC 10 italic', foreground='#0B5345', pady=3)
Tele_Entry = Entry(frame_2, font='SnapITC 10 italic', highlightbackground="#17A589", highlightthickness=2)
Imagem_Label_Tele = Label(frame_2, image=Imagem_Telefone)

Text_Sexo = Label(frame_2, text='Sexo:', font='SnapITC 10 italic', foreground='#0B5345', pady=3)
Check_Male = Checkbutton(frame_2, text='Masculino', font='SnapITC 10 italic', foreground='#17A589')
Check_Fame = Checkbutton(frame_2, text='Feminino', font='SnapITC 10 italic', foreground='#17A589')

# frame 3
Text_Endereco = Label(frame_3, text='Endereço', font='SnapITC 13 italic', foreground='#17A589')
Text_Rua = Label(frame_3, text='Rua:', font='SnapITC 10 italic', foreground='#0B5345', pady=4)
Rua_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground="#17A589", highlightthickness=2, width=35)
Text_N = Label(frame_3, text='N°:', font='SnapITC 10 italic', foreground='#0B5345', pady=4)
N_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground="#17A589", highlightthickness=2, width=5)
Text_Bairro = Label(frame_3, text='Bairro:', font='SnapITC 10 italic', foreground='#0B5345', pady=4)
Bairro_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground="#17A589", highlightthickness=2, width=20)
Text_Cidade = Label(frame_3, text='Cidade:', font='SnapITC 10 italic', foreground='#0B5345')
Cidade_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground="#17A589", highlightthickness=2, width=20)
Text_UF = Label(frame_3, text='Uf:', font='SnapITC 10 italic', foreground='#0B5345', pady=4)
UF_Entry = Entry(frame_3, font='SnapITC 10 italic', highlightbackground="#17A589", highlightthickness=2, width=5)

# frame 4
Gravar = Button(frame_4, text='CADASTRAR', width=20, height=1, foreground='#17A589', highlightbackground="#17A589")
Limpar = Button(frame_4, text='LIMPAR DADOS', width=20, height=1, foreground='#17A589',
                highlightbackground="#17A589")

# frame 5
Text_Alter = Label(frame_5, text='ou\n faça login em uma conta registrada', font='SnapITC 13 italic', foreground='#17A589')
SingIN = Button(frame_5, text='SIGN IN', bg='#17A589')

# ==========================================================================================================
frame_1.grid(row=0, column=0, sticky=NSEW, columnspan=2)
Text_Create.grid(row=0, column=0, sticky=NSEW)

frame_2.grid(row=1, column=0, sticky=NSEW)
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

frame_3.grid(row=1, column=1, sticky=NSEW)
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

frame_4.grid(row=2, column=0, columnspan=2, sticky=NSEW)
Gravar.grid(row=0, column=0, sticky=NSEW)
Limpar.grid(row=0, column=1, sticky=NSEW)
Limpar.grid(row=0, column=2, sticky=NSEW)

frame_5.grid(row=3, column=0, columnspan=2, sticky=NSEW)
Text_Alter.grid(row=0, column=0, sticky=NSEW)
SingIN.grid(row=1, column=0)
# ==========================================================================================================

window.mainloop()
