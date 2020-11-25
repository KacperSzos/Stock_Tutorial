import pymssql
conn = pymssql.connect(server='pmp-esmt.database.windows.net',
                       user='quants',
                       password='Portfolio1!',
                       database='pmptest')

cursor = conn.cursor()

cursor.execute('SELECT * FROM dbo.IEX_CLOUD_API_Test')

print(cursor.fetchall())

conn.close()