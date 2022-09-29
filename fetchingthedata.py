import mysql.connector as c

con = c.connect(host='localhost',
                user='root',
                passwd='Ankit@8285',
                database='ironman')

cursor = con.cursor()

query = 'select * from jarvis'
cursor.execute(query)

# data = cursor.fetchone()
# data = cursor.fetchmany(3)
data = cursor.fetchall()
print(data)