# ========= Bibliotecas ==============
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser
import sys
from cadastro import *

# ========= Criar janelas ============
janela = Tk()
janela.title("Painel de Acesso. ")
janela.geometry('600x300')
janela.configure(background='white')
janela.resizable(width=False, height=False)
janela.attributes('-alpha', 0.9)
janela.iconbitmap(default='icones/LogoIcon.ico')

# ===== Imagens ========

logo = PhotoImage(file='icones/logo.png')

# ====== Widget =========
LeftFrame = Frame(janela, width=200, height=300,
                  bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack(side=LEFT)

RigntFrame = Frame(janela, width=395, height=300,
                   bg='MIDNIGHTBLUE', relief='raise')
RigntFrame.pack(side=RIGHT)

# ========= Logo da empresa ==========
LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=30, y=100)

# ===== Usuário ======
UserLabel = Label(RigntFrame, text="Username:", font=(
    'Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RigntFrame, width=30)
UserEntry.place(x=150, y=110)

# ===== Senha =====
PassLabel = Label(RigntFrame, text='Password: ', font=(
    "Century Gothic", 20), bg='MIDNIGHTBLUE', fg='white')
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RigntFrame, width=30, show='•')
PassEntry.place(x=150, y=160)


def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (User, Pass))
    print("Selecionou")
    verifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in verifyLogin and Pass in verifyLogin):
            messagebox.showinfo(title='Login Info.',
                                message='Acesso Confirmado, Bem vindo!')
        janela.destroy()
        from cadastro import Cadastro

    except:
        messagebox.showinfo(
            title='login Info', message='Acesso Negado, Verifique se está cadastrado no sistema!')


# ===== Botão ======
LoginButton = ttk.Button(RigntFrame, text='Login', width=30, command=Login)
LoginButton.place(x=100, y=220)


def Register():
    # Removendo Botão de Login
    LoginButton.destroy
    RegisterButton.destroy
    # Add botão de cadastro
    NomeLabel = Label(RigntFrame, text='Name:', font=(
        'Century Gothic', 20),  bg='MIDNIGHTBLUE', fg='white')
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RigntFrame, width=40)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RigntFrame, text='E-mail:',
                       font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
    EmailLabel.place(x=5, y=50)

    EmailEntry = ttk.Entry(RigntFrame, width=40)
    EmailEntry.place(x=100, y=60)

    def RegisterToDataBaser():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == '' or Email == '' or User == '' or Pass == ''):
            messagebox.showerror(title='Register Erro',
                                 message='Por Favor, Preencha Todos os Campos!')
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title='Register info',
                                message='Conta Criada com Sucesso!')

    Register = ttk.Button(RigntFrame, text='Register',
                          width=30, command=RegisterToDataBaser)
    Register.place(x=100, y=220)

    def BackToLogin():
        # Removendo Widget de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailEntry.place(x=5000)
        EmailLabel.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        # Trazendo os Botão de Login
        LoginButton.place(x=100)
        RegisterButton.place(x=130)

    Back = ttk.Button(RigntFrame, text='Back', width=20, command=BackToLogin)
    Back.place(x=130, y=250)


RegisterButton = ttk.Button(
    RigntFrame, text='Register', width=20, command=Register)
RegisterButton.place(x=130, y=250)

janela.mainloop()
