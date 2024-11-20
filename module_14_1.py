import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor     = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,                 
balance TEXT NOT NULL,          
email TEXT NOT NULL,               
age INTEGER,                 
balance INTEGER NOT NULL             
)
''')
#- целое число, первичный ключ
#- текст (не пустой)
#- текст (не пустой)
# - целое число
#- целое число (не пустой)

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
#for i in range (10):
#    cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES (?,?,?,?)",(f"User{i}",f"example{i}@gmail.com",f"{i*10}",1000))

#for i in [1,3,5,7,9]:
#    cursor.execute("UPDATE Users Set balance = ? WHERE username =?",(500,f"User{i}"))
#for i in [1,4,7,10]:
#    cursor.execute("DELETE FROM Users WHERE username =?", (f"User{i}",))
cursor.execute("SELECT * FROM Users WHERE age != ?",(60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя:{user[1]} | Почта: {user[2]} | Возраст:{user[3]} | Баланс:{user[4]}")


connection.commit()
connection.close()