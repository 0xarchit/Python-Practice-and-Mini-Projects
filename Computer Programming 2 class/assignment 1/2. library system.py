'''
2. Simple Menu-Driven Program: Library
You are tasked to create a menu-driven Python program to manage a simple Library system.
The program should allow the following options:
• Add a book
• View all books
• Search for a book
• Exit
Write a Python program using classes to implement this. Each book should have attributes
like title, author, and ISBN number.
Instructions: Use a class Book and methods to add and display book details.
Scenario: Consider each book as an object of the Book class.
'''

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        book = Book(title, author, isbn)
        self.books.append(book)
        print("Book added successfully!")

    def view_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def search_for_book(self):
        if not self.books:
            print("No books in the library.")
        else:
            title = input("Enter book title to search: ")
            for book in self.books:
                if book.title.lower() == title.lower():
                    print(book)
                    return
            print("Book not found.")


lib = Library()
while True:
            print("\nLibrary Menu:")
            print("1. Add a book")
            print("2. View all books")
            print("3. Search for a book")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                lib.add_book()
            elif choice == "2":
                lib.view_all_books()
            elif choice == "3":
                lib.search_for_book()
            elif choice == "4":
                print("Exiting the library system.")
                break
            else:
                print("Invalid choice. Please try again.")