import sqlite3

# A4
connect = sqlite3.connect("user.db")
# Рука с карандашом
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (100) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')
connect.commit()
# CRUD Create - Read - Update - Delete

def create_user(name, age, hobby):
    # cursor.execute(f'INSERT INTO users(age, name, hobby) VALUES("{age}", "{name}", "{hobby}")')

    cursor.execute(
        'INSERT INTO users(age, name) VALUES(?,?)',
        (age, name)
    )

    connect.commit()
    print(f"user {name} added!")

create_user("ARDAGER", 26, "Бегать!!!!")

def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    # print(users)
    for i in users:
        print(f"name: {i[0]}, age: {i[1]} hobby:{i[2]}")

# get_users()


def update_user(hobby, rowid):
    cursor.execute(
        'UPDATE users SET hobby=? WHERE rowid=?',
        (hobby, rowid)
    )
    connect.commit()
    print(f'updated user {rowid}')


# update_user("Бегать!!", 3)

# get_users()


def delete_user(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid=?',
        (rowid,)
    )
    connect.commit()
    print(f"user deleted {rowid}!!")


# delete_user(2)
#
#
# get_users()
