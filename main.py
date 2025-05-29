import sqlite3

connect = sqlite3.connect('store_info.db')

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user_store(
    product VARCHAR(200),
    price VARCHAR(200),
    have VARCHAR(10),
    ID PRIMARY KEY
)""")

def dont_have_table():
    print("You dont have any tables")

if '__name__' == '__main__':
    main()

