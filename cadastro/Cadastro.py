# biblioteca
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import DataBaser

# Janela
jan = Tk()
jan.title('Cadastro de Clientes.')
jan.geometry('700x460')
jan.configure(background='CornflowerBlue')
jan.resizable(width=False, height=False)

"""
image = tk.PhotoImage(file='imagens/imagenv3.png')
image= image.subsample(1,1)

labelimage = tk.Label(image=image)
labelimage.place(x=0, y=0, relwidth=1, relheight=1)
"""
# Widget
pessoais = Frame(jan, width=600, height=100, bg='Gainsboro')
pessoais.pack()
pessoais.place(x=55, y=35)
dados = Frame(jan, width=600, height=100, bg='Gainsboro')
dados.pack()
dados.place(x=55, y=140)
contato = Frame(jan, width=600, height=170, bg='Gainsboro')
contato.pack()
contato.place(x=55, y=245)
cadastroLabel = Label(jan, text='Cadastro de Pessoa Fisica.', font=(
    'Century Gothic', 15), bg='CornflowerBlue', fg='black')
cadastroLabel.place(x=50, y=5)

# =======> Dados pessoais
dadosLabel = Label(pessoais, text='Dados Pessoais', font=(
    'Century Gothic', 10), bg='Gainsboro', fg='black')
dadosLabel.place(x=0, y=0)

aviso1Label = Label(pessoais, text='**Coloque os "." e o "-"**',
                    font=('Century Gothic', 5), bg='Gainsboro', fg='red')
aviso1Label.place(x=340, y=15)
nomeLabel = Label(pessoais, text='Nome:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
nomeLabel.place(x=0, y=25)
NomeEntry = ttk.Entry(pessoais, width=35)
NomeEntry.place(x=55, y=28)
cpfLabel = Label(pessoais, text='CPF:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
cpfLabel.place(x=285, y=25)
cpfEntry = ttk.Entry(pessoais, width=17)
cpfEntry.place(x=329, y=28)
rgLabel = Label(pessoais, text='RG:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
rgLabel.place(x=450, y=25)
rgEntry = ttk.Entry(pessoais, width=17)
rgEntry.place(x=485, y=28)
dataLabel = Label(pessoais, text='Data de Nascimento:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
dataLabel.place(x=0, y=60)
dataEntry = ttk.Entry(pessoais, width=17)
dataEntry.place(x=160, y=62)
sexoLabel = Label(pessoais, text='Sexo:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
sexoLabel.place(x=295, y=60)
sexoEntry = ttk.Entry(pessoais, width=17)
sexoEntry.place(x=345, y=60)

# ====> Endereço
dadosLabel = Label(dados, text='Endereço:', font=(
    'Century Gothic', 10), bg='Gainsboro', fg='black')
dadosLabel.place(x=0, y=0)

ruaLabel = Label(dados, text='Rua:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
ruaLabel.place(x=0, y=25)
ruaEntry = ttk.Entry(dados, width=25)
ruaEntry.place(x=40, y=27)

bairroLabel = Label(dados, text='Bairro:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
bairroLabel.place(x=240, y=25)
bairroEntry = ttk.Entry(dados, width=25)
bairroEntry.place(x=300, y=27)

numeroLabel = Label(dados, text='Nº:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
numeroLabel.place(x=470, y=25)
numeroEntry = ttk.Entry(dados, width=8)
numeroEntry.place(x=500, y=27)

estadoLabel = Label(dados, text='UF:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
estadoLabel.place(x=0, y=60)
estadoEntry = ttk.Entry(dados, width=25)
estadoEntry.place(x=35, y=60)

CityLabel = Label(dados, text='Cidade:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
CityLabel.place(x=200, y=60)
CityEntry = ttk.Entry(dados, width=15)
CityEntry.place(x=265, y=60)

cepLabel = Label(dados, text='CEP:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
cepLabel.place(x=368, y=60)
cepEntry = ttk.Entry(dados, width=15)
cepEntry.place(x=415, y=60)


# ======> Contatos
ContatosLabel = Label(contato, text='Telefone:', font=(
    'Century Gothic', 10), bg='Gainsboro', fg='black')
ContatosLabel.place(x=0, y=0)

comecialLabel = Label(contato, text='Comercial:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
comecialLabel.place(x=0, y=30)
comecialEntry = ttk.Entry(contato, width=20)
comecialEntry.place(x=85, y=30)

reciLabel = Label(contato, text='Recidencial:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
reciLabel.place(x=0, y=60)
reciEntry = ttk.Entry(contato, width=20)
reciEntry.place(x=95, y=60)

cellLabel = Label(contato, text='Celular:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
cellLabel.place(x=0, y=90)
cellEntry = ttk.Entry(contato, width=20)
cellEntry.place(x=60, y=90)

whatsLabel = Label(contato, text='WhatsApp:', font=(
    'Century Gothic', 13), bg='Gainsboro', fg='black')
whatsLabel.place(x=0, y=120)
whatsEntry = ttk.Entry(contato, width=20)
whatsEntry.place(x=85, y=120)

emailLabel = Label(contato, text='E-mail:',
                   font=('Century Gothic', 13), bg='Gainsboro', fg='black')
emailLabel.place(x=300, y=30)
emailEntry = ttk.Entry(contato, width=25)
emailEntry.place(x=355, y=30)

# Botão Salve


def Salvar():
    Nome = NomeEntry.get()
    CPF = cpfEntry.get()
    RG = rgEntry.get()
    Data = dataEntry.get()
    Sexo = sexoEntry.get()
    Rua = ruaEntry.get()
    Bairro = bairroEntry.get()
    N = numeroEntry.get()
    UF = estadoEntry.get()
    Cidade = CityEntry.get()
    CEP = cepEntry.get()
    Comecial = comecialEntry.get()
    Recidencial = reciEntry.get()
    Cell = cellEntry.get()
    Whatsapp = whatsEntry.get()
    Email = emailEntry.get()
    if (Nome == '' or CPF == '' or RG == '' or Data == '' or Sexo == ''
            or Rua == '' or Bairro == '' or UF == '' or Cidade == '' or Cell == '' or Email == ''):
        messagebox.showerror(title='Register Erro',
                             message='Por Favor, Preencha Todos os Campos!')
    else:
        DataBaser.cursor.execute("""
        INSERT INTO Users(Nome, CPF, RG, Data, Sexo, Rua, Bairro, N, UF, Cidade, CEP, Comecial, Recidencial, Cell, Whatsapp, Email) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (Nome, CPF, RG, Data, Sexo, Rua, Bairro, N, UF, Cidade, CEP, Comecial, Recidencial, Cell, Whatsapp, Email))
        DataBaser.conn.commit()
        messagebox.showinfo(title='Register info',
                            message='Conta Criada com Sucesso!')


salveButton = ttk.Button(jan, text='Salvar', width=20, command=Salvar)
salveButton.place(x=200, y=430)


def Fechar():
    jan.quit()


sairButton = ttk.Button(jan, text='Sair', width=10, command=Fechar)
sairButton.place(x=380, y=430)

jan.mainloop()
