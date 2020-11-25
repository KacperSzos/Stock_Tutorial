import pymssql
conn = pymssql.connect(server='SERVERNAME.database.windows.net',
                       user='USER',
                       password='PASSWORD',
                       database='DATABASE')

cursor = conn.cursor()

cursor.execute('SELECT * FROM dbo.TABLE')

print(cursor.fetchall())

conn.close()
