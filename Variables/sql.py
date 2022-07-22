import mysql.connector

conn = mysql.connector.connect(host = 'localhost',database = 'APIDevelop',user = 'root',password = 'root')

cursor = conn.cursor()

print(conn.is_connected())

mysql = "select * from CustomerInfo"
cursor.execute(mysql)

rows = cursor.fetchall()
print(type(rows))
print(rows)