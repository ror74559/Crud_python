import sqlite3

#conexão
conexao = sqlite3.connect('registros.bd')

#gerenciador de comandos do banco de dados
cursor = conexao.cursor()


def imprimir_dados(lista):
	for registro in lista:
		print('--------------------------------')
		print(f'id:{registro[0]}')
		print(f'nome:{registro[1]}')
		print(f'apelido:{registro[2]}')
		print(f'data de nascimento: {registro[3]}')
		print('--------------------------------')
		

def create(nome,apelido,data_nasc):
	string_sql = f'''

		INSERT INTO usuarios(nome,apelido,data_nasc)

		VALUES('{nome}','{apelido}','{data_nasc}');

		'''
	cursor.execute(string_sql)

	conexao.commit()

	

def retrieve():
	string_sql = '''

		SELECT * FROM usuarios;

	'''

	cursor.execute(string_sql)

	imprimir_dados(cursor.fetchall())

	

def retrieve_id(id):
	string_sql = f'''

		SELECT * FROM usuarios

		WHERE id ={id};

	'''

	cursor.execute(string_sql)

	imprimir_dados(cursor.fetchall())

def update(id, nome = '',apelido= '',data_nasc = ''):

	lista ={'nome':nome, 'apelido':apelido, 'data_nasc':data_nasc}

	print('registro antigo:')

	retrieve_id(id)

	print('-------------------------------------')

	print('registro atualizado')

	for registro in lista:

		if lista[registro] != '':

			string_sql = f'''

				UPDATE usuarios

				SET {registro} = '{lista[registro]}'

				WHERE id ={id};

			'''
			cursor.execute(string_sql)
			conexao.commit()

	retrieve_id(id)

	imprimir_dados(cursor.fetchall())


def delete(id):
	print('Registro que será deletado:')
	retrieve_id(id)
	print('')
	confirmacao = str(input('Tem certeza que deseja excluir este registro? (s/n)')).lower()
	if confirmacao == 's':
		string_sql = f'''
					DELETE FROM usuarios
					WHERE id = {id};

			'''
		cursor.execute(string_sql)
		conexao.commit()
		print('Registro deletado!')
		
	else:
		print('Deleção não foi efetuada.')


retrieve()
	






















































