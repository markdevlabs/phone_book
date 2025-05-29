import sqlite3

db = sqlite3.connect("phone_book.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user(
    name VARCHAR(200), TEXT,
    last_name VARCHAR(200), TEXT,
    phone_number INTEGER
    PRIMARY KEY
)""")

choose = 10000

print("<<< Hello! Welcome to phone book 2.0 >>>")
for i in range(choose):
    new_question = input('There you can(add, delete(all), show info, exit): ')
    if new_question == 'delete':
        cursor.execute("DELETE FROM user")
        print('Contact(s) successful deleted!')
    elif new_question == 'show info':
        cursor.execute("SELECT rowid, name, last_name, phone_number FROM user")
        print(cursor.fetchall())
    elif new_question == 'exit':
        print('Bye thanks for using!')
        break
    elif new_question == 'add':
        question1 = input('Please write your name: ')
        question2 = input('Please write your last name: ')
        question3 = input('Please write your phone number: ')
        cursor.execute("""INSERT INTO user(name, last_name, phone_number) VALUES (?, ?, ?)""", (question1, question2, question3))
    else:
        print('Sorry phone book dont have this command!')
db.commit()

db.close()

if '__name__' == '__light__':
    light()
