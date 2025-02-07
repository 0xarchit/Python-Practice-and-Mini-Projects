import sqlite3
import sys
import csv

db_conn = sqlite3.connect('test.db')
db_cursor = db_conn.cursor()
print("connected")

def print_db():
    try:
        result = db_cursor.execute("SELECT * FROM employees;")
        for row in result:
            print("id: ", row[0])
            print("name: ", row[1])
            print("age: ", row[2])
            print("salary: ", row[3])
    except:
        print("Error: unable to fetch data")

try:
    db_conn.execute("create table if not exists employees(ID INTEGER PRIMARY KEY, f_name TEXT NOT NULL, age INT NOT NULL, salary REAL);")
    db_conn.commit()
    print("created")

except sqlite3.Error as e:
    print(e)

db_conn.execute("Insert into employees(f_name, age, salary) values ('John', 25, 50000.0);")
db_conn.commit()
print("Entered")

print_db()

try:
    db_conn.execute("Update employees set salary = 60000.0 where ID = 1;")
    db_conn.commit()
except:
    print("Error: unable to update data")


print_db()

try:
    db_conn.execute("Delete from employees where ID = 1;")
    db_conn.commit()
except:
    print("Error: unable to delete data")

print_db()

db_conn.rollback()

print_db()

try:
    db_conn.execute("alter table employees add column 'image' blob default null;")
    db_conn.commit()
except:
    print("Error: unable to alter table")

db_cursor.execute("pragma table_info(employees)")
row_names = [nameTuple[1] for nameTuple in db_cursor.fetchall()]
print(row_names)

db_cursor.execute('select count(*) from employees;')
print(db_cursor.fetchall()[0][0])

with db_conn:
    db_conn.row_factory = sqlite3.Row
    db_cursor = db_conn.cursor()
    db_cursor.execute("select * from employees;")
    rows = db_cursor.fetchall()
    for row in rows:
        print(row['ID'], row['f_name'], row['age'], row['salary'])
        

print_db()
