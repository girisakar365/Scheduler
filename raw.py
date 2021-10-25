from sqlite3 import *

class PhotoLib:

	conn=connect('db.db')
	cur=conn.cursor()

	def insert(img,oid=None,cmd='ins'):
		with open(f'FrontEnd/Image/{img}.png','rb') as pic:
			if cmd=='ins':
				PhotoLib.cur.execute("INSERT INTO plib(img) VALUES (?)",[Binary(pic.read())])
				PhotoLib.conn.commit()
			else:
				PhotoLib.cur.execute("UPDATE plib set img=(?) WHERE id={}".format(oid),[Binary(pic.read())])
				PhotoLib.conn.commit()

	def get(oid):
		data=PhotoLib.cur.execute('SELECT * FROM plib WHERE id=?',[oid])
		return data.fetchall()[0][1]
    

class Cache:
	conn=connect('db.db')
	cur=conn.cursor()

	def cache(data):
		try: #Managing unique string error
			Cache.cur.execute("INSERT INTO cache(sq) VALUES (?)",[data])
			Cache.conn.commit()
		except Exception:
			pass

	def switch(col, data):
			Cache.cur.execute(f'UPDATE switch SET {col} = (?)',[data])
			Cache.conn.commit()

	def fetch(table,col):
		data=Cache.cur.execute(f'SELECT {col} FROM {table}')
		for data in data.fetchall(): return next(iter(data))

	def update(col,data):
		data=Cache.cur.execute(f'UPDATE mgSub SET {col} = (?)',[data])
		Cache.conn.commit()

	def delete():
		data=Cache.cur.execute('DELETE FROM cache')
		Cache.conn.commit()