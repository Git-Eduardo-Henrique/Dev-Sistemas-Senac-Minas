from tkinter import *
from tkinter.ttk import Combobox

def formatado(event = None):
    texto = en_CPF.get().replace('.','').replace('-', '')[:11]
    tele = en3.get()[:12]
    data = en4.get().replace('/', '')[:8]
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
        if num in [1,3]:
            nova_data += data[num] + '/'      
        else:
            nova_data += data[num]    


    en_CPF.delete(0, "end")
    en_CPF.insert(0, novo_texto) 

    en3.delete(0, 'end')
    en3.insert(0, tele)

    en4.delete(0, 'end')
    en4.insert(0, nova_data)



SENAC = Tk()
SENAC.geometry('950x494')
SENAC.config(bg='white')
SENAC.resizable(FALSE, FALSE)
SENAC.title('Login')
SENAC.bind('<KeyRelease>',formatado)

Bg = PhotoImage(file='sus.png')
Fundo = Label(SENAC, image= Bg, border=0)
Fundo.place(x=0, y=0)

Fra_login= Frame(SENAC, borderwidth=5, bg='#D1D5D5')

fr0 = Frame(SENAC)
fr1 = Frame(SENAC, bg='#D1D5D5', borderwidth=5)
fr2 = Frame(SENAC, bg='#D1D5D5')
fr3 = Frame(SENAC, bg='#D1D5D5')

lista_estado = ['MG','ES','RJ','SP','PR','SC','RS','MS','GO','BA','SE','AL','PE','PB','RN','CE','PI','MA','TO','PA','AP','RR','AM','RO','AC','MT','DF']

var = StringVar()
estado = Combobox(fr2, textvariable=var, values=lista_estado, font='verdana 19',)

Text_Cadastro = Label(fr0, text='Cadastro de Funcionário', font='Verdana 25', width = 45)
lb1 = Label(fr1, text='Dados Pessoais', font='Verdana 15 bold', anchor=W, bg='#D1D5D5', foreground='#9128CC')
Text_Nome = Label(fr1, text='Nome:', font='Verdana 15', bg='#D1D5D5', anchor=W)
lb3 = Label(fr1, text='CPF:', font='Verdana 15', anchor=W, bg='#D1D5D5')
lb4 = Label(fr1, text='Telefone:', font='Verdana 15', anchor=W, bg='#D1D5D5')
lb5 = Label(fr1, text='Data Nasc:', font='Verdana 15', anchor=W, bg='#D1D5D5')
lb_sexo = Label(fr1, text='Sexo:', font='Verdana 15', anchor=W, bg='#D1D5D5')
Check_Fame = Checkbutton(fr1, text='Feminino', bg='#D1D5D5', anchor=W, font='Verdana 15',command= lambda: Check_Male.deselect())
Check_Male = Checkbutton(fr1, text='Masculino', bg='#D1D5D5', anchor=W, font='Verdana 15',command=lambda: Check_Fame.deselect())
lb6 = Label(fr2, text='Endereço', font='Verdana 15 bold', bg='#D1D5D5', height=2, foreground='#9128CC')
lb7 = Label(fr2, text='Rua:', font='Verdana 15', anchor=W, bg='#D1D5D5')
lb8 = Label(fr2, text='Bairro:', font='Verdana 15', anchor=W, bg='#D1D5D5')
lb9 = Label(fr2, text='N°:', font='Verdana 15', anchor=W, bg='#D1D5D5')
lb10 = Label(fr2, text='UF:', font='Verdana 15', anchor=W, bg='#D1D5D5')
lb11 = Label(fr2, text='Cidade:', font='Verdana 15', anchor=W, bg='#D1D5D5')
en1 = Entry(fr1, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en_CPF = Entry(fr1, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en3 = Entry(fr1, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en4 = Entry(fr1, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en5 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en6 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en7 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en8 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en9 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
bt1 = Button(fr3, text='Cadastrar', font='Verdana 12 bold', bg='#9128CC', width=15, borderwidth=10)
bt2 = Button(fr3, text='Sair', font='Verdana 12 bold', bg='#9128CC', width=15,borderwidth=10, command= lambda:[Fra_login.place(x=360, y=120),
fr0.grid_forget(), fr1.grid_forget(), fr2.grid_forget(), fr3.grid_forget(), SENAC.title('Login')])


Butb= '#6BBC00'
Fon= 'Verdana 15'
EnLingu = Label(Fra_login)
Log = Label(Fra_login, text='Logar',font='Verdana 25 bold')
Mensa = Label(Fra_login, text='Use uma conta registrada',font=Fon)
Email = Label(Fra_login, text='E-mail',font=Fon)
Pass = Label(Fra_login, text='Senha',font=Fon)
Log_in = Button(Fra_login, text= 'Entrar',font='Verdana 15 bold', bg='#9128CC', borderwidth=10, command=lambda: [fr0.grid(row=0, column=0, sticky=NSEW, columnspan=2), 
fr1.grid(row=1, column=0, sticky=NSEW), fr2.grid(row=1, column=1, sticky=NSEW), fr3.grid(row=2, column=0, sticky=NSEW, columnspan=2), Fra_login.grid_forget(),SENAC.title('Cadastro')])
Enty1 = Entry(Fra_login, font=Fon)
Enty2 = Entry(Fra_login, font=Fon,show='*')


Fra_login.place(x=360, y=120)
Log.grid(row=0, column=0, sticky=NSEW, columnspan=1)
Mensa.grid(row=1, column=0, sticky=NSEW, columnspan=1)
Email.grid(row=2, column=0, sticky=NSEW) 
Enty1.grid(row=3, column=0, sticky=NSEW)
Pass.grid(row=4, column=0, sticky=NSEW)
Enty2.grid(row=5, column=0, sticky=NSEW)
Log_in.grid(row=7, column=0, sticky=NSEW, columnspan=1)



Text_Cadastro.grid(row=0, column=0)

lb1.grid(row=0, column=0)
Text_Nome.grid(row=1, column=0, sticky=EW)
lb3.grid(row=3, column=0,sticky=EW)
lb4.grid(row=5, column=0, sticky=EW)
lb5.grid(row=7, column=0, sticky=EW)
lb6.grid(row=0, column=0, sticky=EW)
lb7.grid(row=2, column=0, sticky=EW)
lb8.grid(row=4, column=0, sticky=EW)
lb9.grid(row=6, column=0, sticky=EW)
lb10.grid(row=8, column=0, sticky=EW)
lb11.grid(row=10, column=0, sticky=EW)
lb_sexo.grid(row=11, column=0, sticky=EW)
Check_Fame.grid(row=12, column=0, sticky=EW)
Check_Male.grid(row=12, column=1, sticky=EW)

en1.grid(row=2, column=0, sticky=EW)
en_CPF.grid(row=4, column=0, sticky=EW)
en3.grid(row=6, column=0, sticky=EW)
en4.grid(row=8, column=0, sticky=EW)
en5.grid(row=3, column=0, sticky=EW)
en6.grid(row=5, column=0, sticky=EW)
en7.grid(row=7, column=0, sticky=EW)
estado.grid(row=9, column=0, sticky=EW)
en9.grid(row=11, column=0, sticky=EW)

bt1.grid(row=0,column=1)
bt2.grid(row=0, column=2)


SENAC.mainloop()