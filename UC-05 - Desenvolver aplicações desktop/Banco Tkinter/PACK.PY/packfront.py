from tkinter import *
from packback import *

Back = Backend()
Form = Format()
Data = DataVerificar()
con = Conta()


class Frontend:
    def __init__(self, janela):
        # cores
        self.branco = '#ffffff'
        self.azul_esc = '#00357b'
        self.preto = '#0F0F10'
        # janela e frames
        self.janela = janela
        self.frame_ini = Frame(self.janela)
        self.frame_menu = Frame(self.janela)
        self.frame_lo_cli = Frame(self.janela)
        self.frame_lo_func = Frame(self.janela)
        self.frame_cadastrar = Frame(self.janela)
        self.frame_conta = Frame(self.janela)
        self.frame_depo = Frame(self.janela)
        self.frame_saque = Frame(self.janela)
        self.frame_trans = Frame(self.janela)
        self.frame_ex = Frame(self.janela)
        # imgs / background
        self.seta_voltar = PhotoImage(file='Foto/seta voltar.png')
        self.inicio = PhotoImage(file='Foto/inicio.png')
        self.entrar = PhotoImage(file='Foto/entrar.png')
        self.func = PhotoImage(file='Foto/func.png')
        self.cadastro = PhotoImage(file='Foto/cadastro.png')
        self.user = PhotoImage(file='Foto/conta cliente.png')
        self.on_image = PhotoImage(file='Foto/olho aberto.png')
        self.off_image = PhotoImage(file='Foto/olho fechado.png')
        self.cliente = PhotoImage(file='Foto/user.png')
        self.depo = PhotoImage(file='Foto/Bt_Depósito.png')
        self.extra = PhotoImage(file='Foto/Bt_Extrato.png')
        self.sq = PhotoImage(file='Foto/bt_saque.png')
        self.tranfer = PhotoImage(file='Foto/bt_transferencia.png')
        self.deposito = PhotoImage(file='Foto/Depósito.png')
        self.saque = PhotoImage(file='Foto/Saque.png')
        self.transferencia = PhotoImage(file='Foto/Transferencia.png')
        self.extrato = PhotoImage(file='Foto/Extrato.png')

    def Conteiner(self):
        # carrega os primeiros frames
        self.frame_ini.pack()
        self.frame_menu.pack()
        # ==============================================================================================================
        # primeira tela (mostra a logo)
        lb_inicio = Label(self.frame_ini, image=self.inicio, border=0)
        lb_inicio.pack()
        # ==============================================================================================================
        # tela seleção de login
        # labels
        lb_entrar = Label(self.frame_menu, image=self.entrar, border=0)
        # botões
        bt_func = Button(self.frame_menu, text='FAZER LOGIN', bg=self.branco, font='arial 15 bold', bd=0,
                         command=lambda: [self.frame_lo_cli.pack(), self.frame_menu.forget(),
                                          self.frame_lo_func.forget()])
        bt_cli = Button(self.frame_menu, text='LOGIN (FUNC)', bg=self.branco, font='arial 15 bold', bd=0,
                        command=lambda: [self.frame_lo_func.pack(), self.frame_menu.forget(),
                                         self.frame_lo_cli.forget()])
        # posicionamento na tela
        lb_entrar.pack()
        bt_func.place(width=155, height=42, x=247, y=146)
        bt_cli.place(width=157, height=47, x=251, y=354)
        # ==============================================================================================================
        # tela funcionário
        # labels
        lb_func = Label(self.frame_lo_func, image=self.func, border=0)
        # Entry's
        en_func = Entry(self.frame_lo_func, font='arial 12 bold', bd=0, fg=self.branco, bg=self.azul_esc)
        en_senha = Entry(self.frame_lo_func, font='arial 12 bold', bg=self.azul_esc, bd=0, fg=self.branco, show='*')
        # botões
        bt_voltar_func = Button(self.frame_lo_func, image=self.seta_voltar, bg=self.azul_esc, bd=0,
                                activebackground=self.azul_esc,
                                command=lambda: [self.frame_menu.pack(), self.frame_lo_func.forget()])
        bt_entrar_func = Button(self.frame_lo_func, text='Entrar', font='arial 13 bold', bg=self.branco, bd=0)
        bt_entrar_func.config(
            command=lambda: Back.Entrar_func(en_func.get(), en_senha.get(), self.frame_cadastrar, self.frame_lo_func))
        # checks
        check_senha_func = Checkbutton(self.frame_lo_func, bg=self.azul_esc, image=self.off_image,
                                       selectimage=self.on_image, indicatoron=False, bd=0,
                                       command=lambda: Back.Mostrar_senha(en_senha), selectcolor=self.azul_esc)
        # posicionamento na tela
        lb_func.pack()
        bt_entrar_func.place(width=70, height=33, x=381, y=443)
        en_senha.place(width=293, height=22, x=25, y=180)
        bt_voltar_func.place(width=38, height=36, x=2, y=9)
        en_func.place(width=293, height=23, x=24, y=122)
        check_senha_func.place(width=30, height=22, x=290, y=170)
        # ==============================================================================================================
        # tela cadastro
        # labels
        lb_cada = Label(self.frame_cadastrar, image=self.cadastro, border=0)
        # Entry's
        en_nome_co = Entry(self.frame_cadastrar, font='Arial 10 bold', bg=self.branco, border=0, fg=self.preto)
        en_cpf_cadas = Entry(self.frame_cadastrar, font='Arial 10 bold', bg=self.branco, border=0, fg=self.preto)
        en_datanasc_cadas = Entry(self.frame_cadastrar, font='Arial 10 bold', bg=self.branco, border=0, fg=self.preto)
        en_email_cadas = Entry(self.frame_cadastrar, font='Arial 10 bold', bg=self.branco, border=0, fg=self.preto)
        en_senha_cadas = Entry(self.frame_cadastrar, font='Arial 10 bold', bg=self.branco, border=0,
                               fg=self.preto, show='*')
        en_confirma_cadas = Entry(self.frame_cadastrar, font='Arial 10 bold', bg=self.branco, border=0,
                                  fg=self.preto, show='*')
        # botões
        bt_voltar_cadas = Button(self.frame_cadastrar, image=self.seta_voltar, bg=self.azul_esc, bd=0,
                                 activebackground=self.azul_esc, command=lambda:
            [self.frame_lo_func.pack(), self.frame_cadastrar.forget()])
        bt_cadastro = Button(self.frame_cadastrar, text='CADASTRAR', font='Arial 15 bold ', bg=self.azul_esc,
                             fg=self.branco,
                             command=lambda: Back.Cadastrar(en_cpf_cadas, en_nome_co, en_datanasc_cadas, en_email_cadas,
                                                            en_senha_cadas, en_confirma_cadas, check_m, check_f,
                                                            check_ac,
                                                            check_email, self.frame_lo_func, self.frame_cadastrar))
        # check buttons
        check_m = Checkbutton(self.frame_cadastrar, bg=self.azul_esc, command=lambda: check_f.deselect())
        check_f = Checkbutton(self.frame_cadastrar, bg=self.azul_esc, command=lambda: check_m.deselect())
        check_ac = Checkbutton(self.frame_cadastrar, bg=self.azul_esc)
        check_email = Checkbutton(self.frame_cadastrar, bg=self.azul_esc)
        # posionamento na tela
        lb_cada.pack()
        en_nome_co.place(width=220, height=24, x=10, y=87)
        en_cpf_cadas.place(width=220, height=24, x=10, y=142)
        en_datanasc_cadas.place(width=220, height=24, x=10, y=200)
        en_email_cadas.place(width=220, height=24, x=266, y=91)
        en_senha_cadas.place(width=220, height=24, x=266, y=144)
        en_confirma_cadas.place(width=220, height=24, x=266, y=197)
        bt_voltar_cadas.place(width=38, height=36, x=2, y=9)
        bt_cadastro.place(width=160, height=55, x=286, y=287)
        check_m.place(width=7, height=6, x=13, y=270)
        check_f.place(width=6, height=7, x=113, y=268)
        check_ac.place(width=6, height=4, x=263, y=243)
        check_email.place(width=8, height=9, x=263, y=265)
        # ==============================================================================================================
        # tela conta
        # labels
        lb_user = Label(self.frame_conta, image=self.user, border=0)
        lb_nome_user = Label(self.frame_conta, text='', font='Arial 15 bold', bg=self.azul_esc, fg=self.branco, bd=0)
        lb_saldo = Label(self.frame_conta, text='0', font='Arial 10 bold', bg=self.azul_esc, fg=self.branco, bd=0)
        # botoes
        bt_voltar_conta = Button(self.frame_conta, image=self.seta_voltar, bg=self.azul_esc, bd=0,
                                 activebackground=self.azul_esc,
                                 command=lambda: [self.frame_lo_cli.pack(), self.frame_conta.forget()])
        bt_deposito = Button(self.frame_conta, image=self.depo, bd=0, activebackground=self.azul_esc,
                             command=lambda: [self.frame_depo.pack(), self.frame_conta.forget()])
        bt_extrato = Button(self.frame_conta, image=self.extra, bd=0, activebackground=self.azul_esc,
                            command=lambda: [self.frame_ex.pack(), self.frame_conta.forget()])
        bt_saque = Button(self.frame_conta, image=self.sq, bd=0, activebackground=self.azul_esc,
                          command=lambda: [self.frame_saque.pack(), self.frame_conta.forget()])
        bt_transfer = Button(self.frame_conta, image=self.tranfer, bd=0, activebackground=self.azul_esc,
                             command=lambda: [self.frame_trans.pack(), self.frame_conta.forget()])

        # check_buttons
        check_saldo = Checkbutton(self.frame_conta, bg=self.azul_esc, image=self.off_image, selectimage=self.on_image,
                                  indicatoron=False, bd=0, selectcolor=self.azul_esc)
        # posionamento na tela
        lb_user.pack()
        bt_voltar_conta.place(width=38, height=36, x=2, y=9)
        bt_deposito.place(width=155, height=68, x=183, y=204)
        bt_extrato.place(width=144, height=37, x=297, y=93)
        check_saldo.place(width=30, height=22, x=175, y=130)
        lb_nome_user.place(width=60, height=18, x=111, y=65)
        lb_saldo.place(width=25, height=11, x=74, y=129)
        bt_saque.place(width=148, height=66, x=18, y=206)
        bt_transfer.place(width=316, height=49, x=19, y=287)
        # ==============================================================================================================
        # tela cliente login
        # labels
        lb_cliente = Label(self.frame_lo_cli, image=self.cliente, border=0)
        # Entry's
        en_cliente_user = Entry(self.frame_lo_cli, font='arial 12 bold', bg=self.branco, border=0, fg=self.preto)
        en_cliente_senha = Entry(self.frame_lo_cli, font='arial 12 bold', bg=self.branco, border=0, fg=self.preto,
                                 show='*')
        # botões
        bt_voltar_cliente = Button(self.frame_lo_cli, image=self.seta_voltar, bg=self.azul_esc, bd=0,
                                   activebackground=self.azul_esc,
                                   command=lambda: [self.frame_menu.pack(), self.frame_lo_cli.forget()])
        bt_entrar_cliente = Button(self.frame_lo_cli, text='Entrar', bg=self.azul_esc, font='arial 19 bold', bd=0,
                                   fg=self.branco,
                                   command=lambda: [
                                       Back.Entrar_cli(en_cliente_user.get(), en_cliente_senha.get(), self.frame_conta,
                                                       self.frame_menu, self.frame_lo_cli)])
        # checks
        check_senha_us = Checkbutton(self.frame_lo_cli, bg=self.branco, image=self.off_image, selectimage=self.on_image,
                                     indicatoron=False, bd=0, command=lambda: Back.Mostrar_senha(en_cliente_senha))
        # posionamento na tela
        lb_cliente.pack()
        en_cliente_user.place(width=217, height=19, x=139, y=160)
        en_cliente_senha.place(width=219, height=17, x=137, y=228)
        bt_voltar_cliente.place(width=38, height=36, x=2, y=9)
        bt_entrar_cliente.place(width=215, height=46, x=141, y=337)
        check_senha_us.place(width=30, height=22, x=335, y=228)
        # ==============================================================================================================
        # tela deposito
        lb_depo = Label(self.frame_depo, image=self.deposito, border=0)
        lb_depo.pack()
        en_valor_depo = Entry(self.frame_depo, font='arial 12 bold', bd=0, fg=self.azul_esc, bg=self.branco)
        bt_confirma = Button(self.frame_depo, text='confirmar', bd=0, bg=self.azul_esc, fg=self.branco,
                             font='arial 19 bold',
                             command=lambda: Back.Depo(en_cliente_user.get(), en_valor_depo.get(), self.frame_conta,
                                                       self.frame_depo, en_valor_depo))
        bt_voltar_deposito = Button(self.frame_depo, image=self.seta_voltar, bg=self.azul_esc, bd=0,
                                    activebackground=self.azul_esc,
                                    command=lambda: [self.frame_conta.pack(), self.frame_depo.forget()])
        en_valor_depo.place(width=216, height=17, x=140, y=157)
        bt_confirma.place(width=208, height=39, x=143, y=281)
        bt_voltar_deposito.place(width=38, height=36, x=2, y=9)
        # ==============================================================================================================
        # tela saque
        lb_saque = Label(self.frame_saque, image=self.saque, border=0)
        lb_saque.pack()
        bt_voltar_saque = Button(self.frame_saque, image=self.seta_voltar, bg=self.azul_esc, bd=0,
                                 activebackground=self.azul_esc,
                                 command=lambda: [self.frame_conta.pack(), self.frame_saque.forget()])
        en_saque = Entry(self.frame_saque, font='arial 12 bold', bd=0, fg=self.azul_esc, bg=self.branco)

        bt_confirma_saque = Button(self.frame_saque, text='confirmar', bd=0, bg=self.azul_esc, fg=self.branco,
                                   font='arial 19 bold',
                                   command=lambda: Back.Saque(en_cliente_user.get(), en_saque.get(), self.frame_conta,
                                                              self.frame_saque, en_saque))
        bt_voltar_saque.place(width=38, height=36, x=2, y=9)
        en_saque.place(width=217, height=16, x=138, y=160)
        bt_confirma_saque.place(width=212, height=43, x=141, y=277)
        # ==============================================================================================================
        # Tela Tranferencia
        lb_transfer = Label(self.frame_trans, image=self.transferencia, bd=0)
        lb_transfer.pack()
        bt_voltar_transfer = Button(self.frame_trans, image=self.seta_voltar, bg=self.azul_esc, bd=0,
                                    activebackground=self.azul_esc,
                                    command=lambda: [self.frame_conta.pack(), self.frame_trans.forget()])
        bt_confirma_transfer = Button(self.frame_trans, text='confirmar', bd=0, bg=self.azul_esc, fg=self.branco,
                                      font='arial 19 bold')

        bt_voltar_transfer.place(width=38, height=36, x=2, y=9)
        bt_confirma_transfer.place(width=208, height=38, x=148, y=351)
        # ==============================================================================================================
        # Tela Extrato
        lb_extrato = Label(self.frame_ex, image=self.extrato, bd=0)
        lb_extrato.pack()
        bt_voltar_extrato = Button(self.frame_ex, image=self.seta_voltar, bg=self.azul_esc, bd=0,
                                   activebackground=self.azul_esc,
                                   command=lambda: [self.frame_conta.pack(), self.frame_ex.forget()])

        bt_voltar_extrato.place(width=38, height=36, x=2, y=9)

        # ==============================================================================================================
    def Formatar_func(event=None):
        # frame funcionario
        func_senha = en_senha.get().replace('.', '').replace('-', '')[:11]
        func_id = en_func.get()[:6]
        nova_senha = ''
        novo_id = ''
        # frame usuario
        usu_senha = en_cliente_senha.get()[:8]
        cliente_cpf = en_cliente_user.get().replace('.', '').replace('-', '')[:11]
        cpf_novo = ''
        # frame cadastro
        cpf_cnpj = en_cpf_cadas.get().replace('.', '').replace('-', '')[:11]
        data = en_datanasc_cadas.get().replace('/', '')[:8]
        senha = en_senha_cadas.get()[:8]
        co_senha = en_confirma_cadas.get()[:8]
        nova_data = ''
        novo_cpf = ''
        # frame deposito
        quant = en_valor_depo.get()
        quant_novo = ''
        # frame saque
        quant_saque = en_saque.get()
        quant_novo_saque = ''

        if event.keysym.lower() == 'backspace':
            return
        for numero in range(len(func_senha)):
            if not func_senha[numero].isnumeric():
                continue
            if numero in [2, 5]:
                nova_senha += func_senha[numero] + '.'
            elif numero == 8:
                nova_senha += func_senha[numero] + '-'
            else:
                nova_senha += func_senha[numero]

            for id in range(len(func_id)):
                if not func_id[id].isnumeric():
                    continue
                else:
                    novo_id += func_id[id]

            for numero_c in range(len(cliente_cpf)):
                if not cliente_cpf[numero_c].isnumeric():
                    continue
                if numero_c in [2, 5]:
                    cpf_novo += cliente_cpf[numero_c] + '.'
                elif numero_c == 8:
                    cpf_novo += cliente_cpf[numero_c] + '-'
                else:
                    cpf_novo += cliente_cpf[numero_c]

            for num in range(len(data)):
                if not data[num].isnumeric():
                    continue
                if num in [1, 3]:
                    nova_data += data[num] + '/'
                else:
                    nova_data += data[num]

            for cpf_num in range(len(cpf_cnpj)):
                if not cpf_cnpj[cpf_num].isnumeric():
                    continue
                if cpf_num in [2, 5]:
                    novo_cpf += cpf_cnpj[cpf_num] + '.'
                elif cpf_num == 8:
                    novo_cpf += cpf_cnpj[cpf_num] + '-'
                else:
                    novo_cpf += cpf_cnpj[cpf_num]

            if not quant.isnumeric():
                pass
            else:
                quant_novo += quant

            if not quant_saque.isnumeric():
                pass
            else:
                quant_novo_saque += quant_saque

            # deletes
            en_senha.delete(0, 'end')
            en_func.delete(0, 'end')
            en_cliente_user.delete(0, 'end')
            en_cliente_senha.delete(0, 'end')
            en_datanasc_cadas.delete(0, 'end')
            en_cpf_cadas.delete(0, 'end')
            en_senha_cadas.delete(0, 'end')
            en_confirma_cadas.delete(0, 'end')
            en_valor_depo.delete(0, 'end')
            en_saque.delete(0, 'end')
            # inserts
            en_senha.insert(0, nova_senha)
            en_func.insert(0, func_id)
            en_cliente_user.insert(0, cpf_novo)
            en_cliente_senha.insert(0, usu_senha)
            en_datanasc_cadas.insert(0, nova_data)
            en_cpf_cadas.insert(0, novo_cpf)
            en_senha_cadas.insert(0, senha)
            en_confirma_cadas.insert(0, co_senha)
            en_valor_depo.insert(0, quant_novo)
            en_saque.insert(0, quant_novo_saque)

# janela.after(3000, frame_i.forget)
