from packback import *
import posiciona


class FrontEnd:
    def __init__(self):
        back = Backend(teste='')
        janela = Tk()
        janela.geometry('500x500')
        janela.resizable(False, False)

        janela.bind('<Button-1>', posiciona.inicio_place)
        janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, janela))
        janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))

        frame_i = Frame()
        frame_entrar = Frame(janela)
        frame_func = Frame(janela)
        frame_cliente = Frame(janela)
        frame_conta = Frame(janela)
        frame_cadastro = Frame(janela)

        frame_i.pack()
        frame_entrar.pack()

        seta_voltar = PhotoImage(file='seta voltar.png')
        # foto tela inicio
        inicio = PhotoImage(file='inicio.png')
        lb_inicio = Label(frame_i, image=inicio, border=0)
        lb_inicio.pack()

        # tela entrar
        entrar = PhotoImage(file='entrar.png')
        lb_entrar = Label(frame_entrar, image=entrar, border=0)
        lb_entrar.pack()

        bt_func = Button(frame_entrar, text='FAZER LOGIN', bg='#ffffff', font='arial 15 bold',  bd=0,
                         command=lambda: [frame_cliente.pack(), frame_entrar.forget(), frame_func.forget()])
        bt_func.place(width=155, height=42, x=247, y=146)
        bt_cli = Button(frame_entrar, text='LOGIN (FUNC)', bg='#ffffff', font='arial 15 bold', bd=0,
                        command=lambda: [frame_func.pack(), frame_entrar.forget(), frame_cliente.forget()])
        bt_cli.place(width=157, height=47, x=251, y=354)

        # tela funcionário
        func = PhotoImage(file='func.png')
        lb_func = Label(frame_func, image=func, border=0)
        lb_func.pack()

        en_func = Entry(frame_func, font='arial 12 bold', bd=0, fg='white', bg='#00357b')
        en_func.place(width=293, height=23, x=24, y=122)

        en_senha = Entry(frame_func, font='arial 12 bold', bg='#00357b', bd=0, fg='white', show='*')
        en_senha.place(width=293, height=22, x=25, y=180)

        bt_voltar_func = Button(frame_func, image=seta_voltar, bg='#00357b', bd=0, activebackground='#00357b',
                                command=lambda: [frame_entrar.pack(), frame_func.forget()])
        bt_voltar_func.place(width=38, height=36, x=2, y=9)
        bt_entrar_func = Button(frame_func, text='Entrar', font='arial 13 bold', bg='#ffffff', bd=0,
                                command=lambda: [frame_cadastro.pack(), frame_func.forget(),
                                                 back.Func_Senha(button=bt_entrar_func, entry_senha=en_senha,
                                                                 entry_func=en_func)])
        bt_entrar_func.place(width=70, height=33, x=381, y=443)

        # tela cadastro
        cadastro = PhotoImage(file='cadastro.png')
        lb_cada = Label(frame_cadastro, image=cadastro, border=0)
        bt_voltar_cadas = Button(frame_cadastro, image=seta_voltar, bg='#00357b', bd=0, activebackground='#00357b',
                                 command=lambda: [frame_func.pack(), frame_cadastro.forget()])
        bt_voltar_cadas.place(width=38, height=36, x=2, y=9)

        en_nome_co = Entry(frame_cadastro, font='Arial 10 bold', bg='#ffffff', border=0, fg='black')
        en_nome_co.place(width=220, height=24, x=10, y=87)

        en_cpf_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg='#ffffff', border=0, fg='black')
        en_cpf_cadas.place(width=220, height=24, x=10, y=142)

        en_datanasc_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg='#ffffff', border=0, fg='black')
        en_datanasc_cadas.place(width=220, height=24, x=10, y=200)

        en_email_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg='#ffffff', border=0, fg='black')
        en_email_cadas.place(width=220, height=24, x=266, y=91)

        en_senha_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg='#ffffff', border=0, fg='black', show='*')
        en_senha_cadas.place(width=220, height=24, x=266, y=144)

        en_confirma_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg='#ffffff', border=0, fg='black', show='*')
        en_confirma_cadas.place(width=220, height=24, x=266, y=197)

        check_m = Checkbutton(frame_cadastro, bg='#00357b', command=lambda: check_f.deselect())
        check_m.place(width=7, height=6, x=13, y=270)

        check_f = Checkbutton(frame_cadastro, bg='#00357b', command=lambda: check_m.deselect())
        check_f.place(width=6, height=7, x=113, y=268)

        check_aceito = Checkbutton(frame_cadastro, bg='#00357b')
        check_aceito.place(width=6, height=4, x=263, y=243)

        check_email = Checkbutton(frame_cadastro, bg='#00357b')
        check_email.place(width=8, height=9, x=263, y=265)
        lb_cada.pack()

        # tela conta
        user = PhotoImage(file='conta cliente.png')
        lb_user = Label(frame_conta, image=user, border=0)
        bt_voltar_conta = Button(frame_conta, image=seta_voltar, bg='#1E90FF', bd=0, activebackground='#00357b',
                                 command=lambda: [frame_cliente.pack(), frame_conta.forget()])
        bt_voltar_conta.place(width=38, height=36, x=2, y=9)
        on_image = PhotoImage(file='olho aberto.png')
        off_image = PhotoImage(file='olho fechado.png')

        check_aberto = Checkbutton(frame_conta, bg='#00357b', image=on_image, selectimage=off_image,
                                   indicatoron=False, bd=0)
        check_aberto.place(width=30, height=22, x=175, y=130)
        
        lb_user.pack()

        # tela cliente login
        cliente = PhotoImage(file='user.png')
        lb_cliente = Label(frame_cliente, image=cliente, border=0)
        lb_cliente.pack()

        en_cliente_user = Entry(frame_cliente, font='arial 12 bold', bg='#ffffff', border=0, fg='black')
        en_cliente_user.place(width=217, height=19, x=139, y=160)

        en_cliente_senha = Entry(frame_cliente, font='arial 12 bold', bg='#ffffff', border=0, fg='black', show='*')
        en_cliente_senha.place(width=219, height=17, x=137, y=228)

        bt_voltar_cliente = Button(frame_cliente, image=seta_voltar, bg='#00357b', bd=0, activebackground='#00357b',
                                   command=lambda: [frame_entrar.pack(), frame_cliente.forget()])
        bt_voltar_cliente.place(width=38, height=36, x=2, y=9)

        bt_entrar_cliente = Button(frame_cliente, text='Entrar', bg='#00357b', font='arial 19 bold', bd=0, fg='White', 
                                   command=lambda: [frame_conta.pack(), frame_entrar.forget(), frame_cliente.forget()])
        bt_entrar_cliente.place(width=215, height=46, x=141, y=337)

        # Tempo de duração
        janela.after(500, frame_i.forget())
        janela.mainloop()
