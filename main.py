from sqlite3 import *

class DB:
	conn=connect('db.db')
	cur=conn.cursor()

	def create(subject):
		DB.cur.execute(f"CREATE TABLE IF NOT EXISTS {subject} (unit TEXT );")
		DB.conn.commit()

	def insert(data,table='Professor'):
		try:
			DB.cur.execute(f"INSERT INTO {table} VALUES (?)",data)
			DB.conn.commit()
		except Exception:
			pass


	def fetch(table:str='Professor',typ:str='normal',col:str=None,*arg):

		if typ=='normal':
			cmd=f'SELECT * FROM {table}'#fetch all 
		elif typ=='specific':
			cmd=f'SELECT {col} FROM {table}'#fetch specific col
		elif typ=='quiere':#fetch comparing data's 
			cmd=f'SELECT {col} FROM {table} WHERE {arg[0]}'

		data=DB.cur.execute(cmd)
		return data.fetchall()