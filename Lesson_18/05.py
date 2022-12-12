import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='01237890',
    database = "my_first_db2"
)

mycursor = mydb.cursor()

mycursor.execute('INSERT INTO student (id, name) VALUES (01, "John")')
mycursor.execute('INSERT INTO employee (name, salary) VALUES ("John", 10000)')

mydb.commit()

mycursor.execute('SELECT * FROM student')
stud_result = mycursor.fetchall()

for i in stud_result:
    print(i)

mycursor.execute('SELECT * FROM employee')
empl_result = mycursor.fetchall()

for i in empl_result:
    print(i)

mycursor.close()
mydb.close()