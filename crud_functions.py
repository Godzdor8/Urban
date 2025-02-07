import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

def initiate_db_users():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

def add_user(username, email, age):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)", (username, email, age, 1000,))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchone()
    connection.commit()
    connection.close()
    if user is None:
        return False
    else:
        return True

#cursor.execute("INSERT INTO Products VALUES(?, ?, ?, ?)", (1, 'Яблоко', 'зеленое, кислое', 52,))
#cursor.execute("INSERT INTO Products VALUES(?, ?, ?, ?)", (2, 'Ананас', 'свежий, заморский', 228,))
#cursor.execute("INSERT INTO Products VALUES(?, ?, ?, ?)", (3, 'Клубника', 'мытая, крупная', 322,))
#cursor.execute("INSERT INTO Products VALUES(?, ?, ?, ?)", (4, 'Лимон', 'желтый, кислый', 123,))

def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM Products").fetchall()
    connection.close()
    return result


#initiate_db_users()
#add_user('dsa', 'dsadzcx', 32)
#print(is_included("dsa"))

connection.commit()
connection.close()