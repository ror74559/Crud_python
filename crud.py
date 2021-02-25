import pyodbc

server = 'RAF_RAF_EMM\SQLEXPRESS'
database ='crudpy'
username_pass = 'Trusted_Connection=yes'

#conexão
conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';'+username_pass)

#gerenciador de comandos do banco de dados
cursor = conexao.cursor()


def imprimir_dados(lista):
	for registro in lista:
		print('--------------------------------')
		print(f'id:{registro[0]}')
		print(f'nome:{registro[1]}')
		print(f'apelido:{registro[2]}')
		print(f'data de nascimento: {registro[3].day}/{registro[3].month}/{registro[3].year}')

def create(nome,apelido,data_nasc):
	string_sql = f'''

		insert into pessoas(nome,apelido,data_nac)

		values('{nome}','{apelido}','{data_nasc}');

		'''
	cursor.execute(string_sql)

	cursor.commit()

def retrieve():
	string_sql = '''

		select * from pessoas;

	'''

	cursor.execute(string_sql)

	imprimir_dados(cursor.fetchall())

	

def retrieve_id(id):
	string_sql = f'''

		select * from pessoas

		where id ={id};

	'''

	cursor.execute(string_sql)

	imprimir_dados(cursor.fetchall())

def update(id, nome = '',apelido= '',data_nasc = ''):

	lista ={'nome':nome, 'apelido':apelido, 'data_nac':data_nasc}

	print('registro antigo:')

	retrieve_id(id)

	print('-------------------------------------')

	print('registro atualizado')

	for registro in lista:

		if lista[registro] != '':

			string_sql = f'''

				update pessoas

				set {registro} = '{lista[registro]}'

				where id ={id};

			'''
			cursor.execute(string_sql)
			cursor.commit()

	retrieve_id(id)

	#imprimir_dados(cursor.fetchall())


def delete(id):
	print('Registro que será deletado:')
	retrieve_id(id)
	print('')
	confirmacao = str(input('Tem certeza que deseja excluir este registro? (s/n)')).lower()
	if confirmacao == 's':
		string_sql = f'''
					delete from pessoas
					where id = {id}

			'''
		cursor.execute(string_sql)
		cursor.commit()
		print('Registro deletado!')
		
	else:
		print('Deleção não foi efetuada.')
delete(9)
	






















































