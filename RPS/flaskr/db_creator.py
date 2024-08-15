import sqlite3

try:
    con = sqlite3.connect('database/rps_base')
    with open('schema.sql','r') as sql_file:
        schema = sql_file.read()
        con.executescript(schema)
        con.commit()
        con.close()
except Exception as e:
    print(e)