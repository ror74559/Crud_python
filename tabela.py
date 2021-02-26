import sqlite3

conexao = sqlite3.connect('registros.bd')


cursor = conexao.cursor()


string_sql = '''

				CREATE TABLE IF NOT EXISTS usuarios
				(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					nome VARCHAR(50) NOT NULL,
					apelido VARCHAR(50) NOT NULL,
					data_nasc DATE NOT NULL

				);

			 '''

cursor.execute(string_sql)



