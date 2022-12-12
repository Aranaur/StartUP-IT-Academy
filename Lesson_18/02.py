import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='01237890',
    database = "my_first_db2"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE table student(id INT,  name VARCHAR(255))")

mycursor.close()
mydb.close()