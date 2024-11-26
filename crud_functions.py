import sqlite3
import random

connection = sqlite3.connect("my_db.db")
cursor = connection.cursor()


def initiate_db1():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,                 
    title TEXT NOT NULL,          
    description TEXT ,               
    price INTEGER NOT NULL             
    )
    ''')
    connection.commit()


def initiate_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,                 
    username TEXT NOT NULL,          
    email TEXT NOT NULL,               
    age  INTEGER NOT NULL,
    balance INTEGER NOT NULL             
    )
    ''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON Users (id)")
    connection.commit()


def add_user(username, email, age):
    if not is_included(username):
        connection = sqlite3.connect("my_db.db")
        cursor = connection.cursor()
        cursor.execute(f'''
        INSERT INTO Users (username,email,age,balance) VALUES('{username}','{email}','{age}',1000) 
        ''')
        connection.commit()
    else:
        pass


#for i in range(1, 5):
#    cursor.execute("INSERT INTO Products (title,description,price) VALUES(?,?,?)",
#                   (f"product{i}", f"description{i}", f"{i * 100}"))


def is_included(username):
    connection = sqlite3.connect("my_db.db")
    cursor = connection.cursor()
    message = ''
    chek_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if chek_user.fetchone() is None:
        message = False
    else:
        message = True
    return message
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("my_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    return products
    connection.commit()


initiate_db1()
initiate_db()

#add_user(username="Pand", email="jkgjkrgb", age=40,)
connection.commit()
connection.close()
