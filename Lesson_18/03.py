import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='01237890',
    database = "my_first_db2"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE table employee(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255),salary INT(6))")

mycursor.close()
mydb.close()