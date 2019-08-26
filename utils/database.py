from .connection import DatabaseConnection

def create_db():
   with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer )')
        #primary key means no two names will be created

def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0 )', (name, author))

def list_book():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books ')
        books = [{'name': row[0], 'author' : row[1], 'read' : row[2]} for row in cursor.fetchall()]
        return books

def list_book_order():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books ORDER BY name DESC ')
        books = [{'name': row[0], 'author' : row[1], 'read' : row[2]} for row in cursor.fetchall()]

    return books

def mark_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE book SET read=1 WHERE name=?', (name,))


def del_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM book where name =?', (name,))