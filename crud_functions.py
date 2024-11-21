import sqlite3

connection = sqlite3.connect("my_db.db")
cursor = connection.cursor()

# def initiate_db():
cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,                 
    title TEXT NOT NULL,          
    description TEXT ,               
    price INTEGER NOT NULL             
    )
    ''')


# for i in range(1, 5):
#    cursor.execute("INSERT INTO Products (title,description,price) VALUES(?,?,?)",
#                   (f"product{i}", f"description{i}", f"{i * 100}"))


def get_all_products():
    connection = sqlite3.connect("my_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    return products
    connection.commit()


connection.commit()
connection.close()
