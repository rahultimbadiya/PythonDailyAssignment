import mysql.connector

#this statement will authenticate server and then connect with the database
db = mysql.connector.connect(host="localhost", user="root", password="root@123", database="student")

cursor = db.cursor() #this will create the cursor to execute the queries

#This query create the table in the database with given column
sql1 = "CREATE TABLE student_data (student_id INT NOT NULL AUTO_INCREMENT, student_name VARCHAR(15),PRIMARY KEY (student_id))"
#This query insert the data to the database with given values
sql2 = "INSERT INTO student_data(student_id,student_name) VALUES(1,'Rahul'),(2,'Ketul'),(3,'Raj')"
#This query update the row in the database with given id
sql3 = "UPDATE student_data SET student_name=('Bhavik') WHERE student_id=3"
#This query delete the row from the database with given id
sql4 = "DELETE FROM student_data WHERE student_id=3"

cursor.execute(sql1) #this executes the query
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)

data = cursor.fetchall() #this statement fetch all data from database

for val in data:
    print(val) # this will print tha fetched data from database to console

db.commit() #commit all changes
db.close() #close the connection from database

