import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='01237890',
    database = "my_first_db2"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE student ADD PRIMARY KEY (id)")

mycursor.close()
mydb.close()