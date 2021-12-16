from sqlite3 import *

class DB:
    conn = connect("3ZH9iusR.db")
    cur = conn.cursor()

    def create(subject):
        DB.cur.execute(f"CREATE TABLE IF NOT EXISTS {subject} (unit TEXT, tpp INTEGER);")
        DB.conn.commit()

    def insert(data, table="Professor"):
        if table == "Professor":
            try:
                DB.cur.execute(f"INSERT INTO {table} VALUES ({'?,?,?,?,?,?'});", data)

            except Exception:
                pass

        else:
            DB.cur.execute(f"INSERT INTO {table} VALUES ({'?'});", [data])

        DB.conn.commit()

    def fetch(table: str = "Professor", typ: str = "normal", col: str = None, *arg):

        if typ == "normal":
            cmd = f"SELECT * FROM {table}"  # fetch all
        elif typ == "specific":
            cmd = f"SELECT {col} FROM {table}"  # fetch specific col
        elif typ == "quiere":  # fetch comparing data's
            cmd = f"SELECT {col} FROM {table} WHERE {arg[0]}"
        elif typ == 'filter':
            cmd = f'''SELECT * FROM {table} 
            WHERE fname = '{col}' OR sname = '{col}' OR id = '{col}' OR subject = '{col}' OR 
            email = '{col}' OR class = '{col}'
            '''
        elif typ == 'delete':
            cmd = f'''DELETE FROM {table} WHERE fname = '{col}' OR sname = '{col}' OR id = '{col}' OR subject = '{col}' OR 
            email = '{col}' OR class = '{col}'
            '''

        data = DB.cur.execute(cmd)
        DB.conn.commit()
        return data.fetchall()

class Password:

    conn = connect("9Zr6ucDt.db")
    cur = conn.cursor()

    def insert(table, data):
        Password.cur.execute(f'UPDATE "{table}" SET "00101101" = (?)',[data])
        Password.conn.commit()

    def fetch(table):
        data=Password.cur.execute(f'SELECT * FROM "{table}"')
        for data in data.fetchall(): return next(iter(data))