from packback import *
import posiciona


class FrontEnd:  # classe para toda a Front-end
    def __init__(self):
        back = Backend(teste='')  # variavel que guarda a classe de backend
        branco = '#ffffff'
        azul_esc = '#00357b'
        preto = '#0F0F10'
        # ==============================================================================================================
        # janela principal
        janela = Tk()
        janela.geometry('500x500')
        janela.resizable(False, False)
        '''janela.bind('<Button-1>', posiciona.inicio_place)
        janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, janela))
        janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))'''
        # ==============================================================================================================
        # frames de cada tela
        frame_i = Frame()
        frame_entrar = Frame(janela)
        frame_func = Frame(janela)
        frame_cliente = Frame(janela)
        frame_conta = Frame(janela)
        frame_cadastro = Frame(janela)
        # ==============================================================================================================
        # carrega os primeiros frames
        frame_i.pack()
        frame_entrar.pack()
        # ==============================================================================================================
        # variaveis para todas as imagens usadas
        seta_voltar = PhotoImage(file='Foto/seta voltar.png')
        inicio = PhotoImage(file='Foto/inicio.png')
        entrar = PhotoImage(file='Foto/entrar.png')
        func = PhotoImage(file='Foto/func.png')
        cadastro = PhotoImage(file='Foto/cadastro.png')
        user = PhotoImage(file='Foto/conta cliente.png')
        on_image = PhotoImage(file='Foto/olho aberto.png')
        off_image = PhotoImage(file='Foto/olho fechado.png')
        cliente = PhotoImage(file='Foto/user.png')
        # ==============================================================================================================
        # primeira tela (mostra a logo)
        lb_inicio = Label(frame_i, image=inicio, border=0)
        lb_inicio.pack()
        # ==============================================================================================================
        # tela seleção de login
        # labels
        lb_entrar = Label(frame_entrar, image=entrar, border=0)
        # botões
        bt_func = Button(frame_entrar, text='FAZER LOGIN', bg=branco, font='arial 15 bold', bd=0,
                         command=lambda: [frame_cliente.pack(), frame_entrar.forget(), frame_func.forget()])

        bt_cli = Button(frame_entrar, text='LOGIN (FUNC)', bg=branco, font='arial 15 bold', bd=0,
                        command=lambda: [frame_func.pack(), frame_entrar.forget(), frame_cliente.forget()])
        # posicionamento na tela
        lb_entrar.pack()
        bt_func.place(width=155, height=42, x=247, y=146)
        bt_cli.place(width=157, height=47, x=251, y=354)
        # ==============================================================================================================
        # tela funcionário
        # labels
        lb_func = Label(frame_func, image=func, border=0)
        # Entry's
        en_func = Entry(frame_func, font='arial 12 bold', bd=0, fg=branco, bg=azul_esc)
        en_senha = Entry(frame_func, font='arial 12 bold', bg=azul_esc, bd=0, fg=branco, show='*')
        # botões
        bt_voltar_func = Button(frame_func, image=seta_voltar, bg=azul_esc, bd=0, activebackground=azul_esc,
                                command=lambda: [frame_entrar.pack(), frame_func.forget()])

        bt_entrar_func = Button(frame_func, text='Entrar', font='arial 13 bold', bg=branco, bd=0)
        bt_entrar_func.config(command=lambda: [frame_cadastro.pack(), frame_func.forget()])
        # posicionamento na tela
        lb_func.pack()
        bt_entrar_func.place(width=70, height=33, x=381, y=443)
        en_senha.place(width=293, height=22, x=25, y=180)
        bt_voltar_func.place(width=38, height=36, x=2, y=9)
        en_func.place(width=293, height=23, x=24, y=122)
        # ==============================================================================================================
        # tela cadastro
        # labels
        lb_cada = Label(frame_cadastro, image=cadastro, border=0)
        # Entry's
        en_nome_co = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto)
        en_cpf_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto)
        en_datanasc_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto)
        en_email_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto)
        en_senha_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto, show='*')
        en_confirma_cadas = Entry(frame_cadastro, font='Arial 10 bold', bg=branco, border=0, fg=preto, show='*')
        # botões
        bt_voltar_cadas = Button(frame_cadastro, image=seta_voltar, bg=azul_esc, bd=0, activebackground=azul_esc,
                                 command=lambda: [frame_func.pack(), frame_cadastro.forget()])
        # check buttons
        check_m = Checkbutton(frame_cadastro, bg=azul_esc, command=lambda: check_f.deselect())
        check_f = Checkbutton(frame_cadastro, bg=azul_esc, command=lambda: check_m.deselect())
        check_aceito = Checkbutton(frame_cadastro, bg=azul_esc)
        check_email = Checkbutton(frame_cadastro, bg=azul_esc)
        # posionamento na tela
        lb_cada.pack()
        en_nome_co.place(width=220, height=24, x=10, y=87)
        en_cpf_cadas.place(width=220, height=24, x=10, y=142)
        en_datanasc_cadas.place(width=220, height=24, x=10, y=200)
        en_email_cadas.place(width=220, height=24, x=266, y=91)
        en_senha_cadas.place(width=220, height=24, x=266, y=144)
        en_confirma_cadas.place(width=220, height=24, x=266, y=197)
        bt_voltar_cadas.place(width=38, height=36, x=2, y=9)
        check_m.place(width=7, height=6, x=13, y=270)
        check_f.place(width=6, height=7, x=113, y=268)
        check_aceito.place(width=6, height=4, x=263, y=243)
        check_email.place(width=8, height=9, x=263, y=265)
        # ==============================================================================================================
        # tela conta
        # labels
        lb_user = Label(frame_conta, image=user, border=0)
        # botoes
        bt_voltar_conta = Button(frame_conta, image=seta_voltar, bg='#1E90FF', bd=0, activebackground=azul_esc,
                                 command=lambda: [frame_cliente.pack(), frame_conta.forget()])
        # check_buttons
        check_aberto = Checkbutton(frame_conta, bg=azul_esc, image=on_image, selectimage=off_image,
                                   indicatoron=False, bd=0)
        # posionamento na tela
        lb_user.pack()
        bt_voltar_conta.place(width=38, height=36, x=2, y=9)
        check_aberto.place(width=30, height=22, x=175, y=130)
        # ==============================================================================================================
        # tela cliente login
        # labels
        lb_cliente = Label(frame_cliente, image=cliente, border=0)
        # Entry's
        en_cliente_user = Entry(frame_cliente, font='arial 12 bold', bg=branco, border=0, fg=preto)
        en_cliente_senha = Entry(frame_cliente, font='arial 12 bold', bg=branco, border=0, fg=preto, show='*')
        # botões
        bt_voltar_cliente = Button(frame_cliente, image=seta_voltar, bg=azul_esc, bd=0, activebackground=azul_esc,
                                   command=lambda: [frame_entrar.pack(), frame_cliente.forget()])

        bt_entrar_cliente = Button(frame_cliente, text='Entrar', bg=azul_esc, font='arial 19 bold', bd=0, fg=branco,
                                   command=lambda: [frame_conta.pack(), frame_entrar.forget(), frame_cliente.forget()])
        # posionamento na tela
        lb_cliente.pack()
        en_cliente_user.place(width=217, height=19, x=139, y=160)
        en_cliente_senha.place(width=219, height=17, x=137, y=228)
        bt_voltar_cliente.place(width=38, height=36, x=2, y=9)
        bt_entrar_cliente.place(width=215, height=46, x=141, y=337)
        # ==============================================================================================================
        # loop da janela e outros
        janela.after(500, frame_i.forget())  # Tempo de duração
        janela.bind('<KeyRelease>', back.Formatacao(senha_func=en_senha))
        janela.mainloop()
