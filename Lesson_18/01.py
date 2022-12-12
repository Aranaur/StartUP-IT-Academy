import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='01237890',
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_first_db2")

mycursor.close()
mydb.close()