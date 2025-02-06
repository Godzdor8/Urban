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


#initiate_db()

connection.commit()
connection.close()