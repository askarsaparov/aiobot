import sqlite3

# Connect to or create the database file (if it doesn't exist, it will be created)


def create_db():
    conn = sqlite3.connect('oplata.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS need_payment 
                ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                payment_date TEXT,
                amount INT
                );''')
    conn.commit()
    conn.close()

# create_db()


def insert_payment(payment_date, amount):
    conn = sqlite3.connect('oplata.sqlite')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO payment (payment_date, amount) VALUES (?, ?);''',
                   (payment_date, amount))
    conn.commit()
    conn.close()


def select_payments():
    conn = sqlite3.connect('oplata.sqlite')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM payment;''')
    payments = cursor.fetchall()
    conn.commit()
    conn.close()
    return payments


def select_need_payments():
    conn = sqlite3.connect('oplata.sqlite')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM need_payment;''')
    need_payments = cursor.fetchall()
    conn.commit()
    conn.close()
    return need_payments