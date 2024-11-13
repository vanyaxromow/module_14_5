import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    """)
for i in range(1, 5):
    cursor.execute('INSERT OR REPLACE INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)',
                   (f'{i}', f'Продукт {i}', f'Описание {i}', i * 100))

    connection.commit()

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance NOT NULL
);
""")
connection.commit()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        return True
    else:
        return False


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    prod = cursor.fetchall()
    connection.close()
    return prod

# connection.commit()
# connection.close()
