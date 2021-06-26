from mysql.connector import *

main_db = connect(
host="localhost",
user='root',
password='00101101',
database='data_lib'
)
root=main_db.cursor()

class DB:
	def insert(data:list):
		root.execute("INSERT INTO techid VALUES (%s,%s,%s,%s,%s,%s)",data)
		main_db.commit()

	def fetch(data='*'):
		if data =='*':
			root.execute('SELECT * FROM techid')
		else:
			root.execute(f'''SELECT * FROM techid 
			WHERE fname = '{data}' OR sname = '{data}' OR id = '{data}' OR subject = '{data}' OR 
			email = '{data}' OR class = '{data}'
			''')
		return root.fetchall()
	
	def delete():
		root.execute("DELETE FROM techid")
		main_db.commit()