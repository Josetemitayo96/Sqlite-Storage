from utils import database

USER_CHOICE = """
ENTER:
- 'a' to add a new book
- 'l' to list all books
- 'o' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            prompt_list_book()
        elif user_input == 'o':
            prompt_list_book_order()
        elif user_input == 'r':
            prompt_mark_read()
        elif user_input == 'd':
            prompt_del_book()
        else:
            print("Unkown command")
        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input("Enter the new book name")
    author = input("Enter the new book author")

    database.add_book(name, author)

def prompt_list_book():
    books = database.list_book()
    for book in books:
        read = 'YES' if book['read'] is True else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

def prompt_list_book_order():
    books = database.list_book_order()
    for book in books:
        read = 'YES' if book['read'] is True else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

def prompt_mark_read():
    name = input("Enter the name of the book")

    database.mark_book(name)

def prompt_del_book():
    name = input("Enter the name of the book")

    database.del_book(name)

database.create_db()

menu()




