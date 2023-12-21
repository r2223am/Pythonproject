import mysql.connector

conn = mysql.connector.connect(host= 'localhost', database= 'dvd_collection', user= 'root', password='Boss#23')

cursor = conn.cursor()
print(conn.is_connected())

mysql = "select * from movies"
cursor.execute(mysql)
rows = cursor.fetchall()
print(type(rows))
print(rows)
