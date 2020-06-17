import sqlite3

conn = sqlite3.connect('UserData.db')

new = sqlite3.connect('UserData.db')

new = new.cursor()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name  TEXT NOT NULL,
    Email  TEXT NOT NULL,
    User TEXT NOT NULL,
    Password  TEXT NOT NULL
);
""")

new.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nome	TEXT NOT NULL,
	CPF	TEXT NOT NULL,
	RG	TEXT NOT NULL,
	Data	TEXT NOT NULL,
	Sexo	TEXT NOT NULL,
	Rua	TEXT NOT NULL,
	Bairro	TEXT NOT NULL,
	N	TEXT NOT NULL,
	UF	TEXT NOT NULL,
	Cidade	TEXT NOT NULL,
	CEP	TEXT NOT NULL,
	Comecial	TEXT NOT NULL,
	Recidencial	TEXT NOT NULL,
	Cell	TEXT NOT NULL,
	Whatsapp	TEXT NOT NULL,
	Email	TEXT NOT NULL
);
""")


print('Conectado ao Bandco de Dados')
