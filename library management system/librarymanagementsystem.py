class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Available Copies: {book.available_copies}")

    def borrow_book(self, book_id):
        book = next((b for b in self.books if b.book_id == book_id), None)

        if book and book.available_copies > 0:
            book.available_copies -= 1
            self.borrowed_books.append(book)
            print("\nBook borrowed successfully.")
        elif book and book.available_copies == 0:
            print("\nSorry, the book is currently not available.")
        else:
            print("\nBook not found.")

    def display_borrowed_books(self):
        print("\nBorrowed Books:")
        for book in self.borrowed_books:
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

def main():
    library = Library()

    book1 = Book(1, "Introduction to Python", "John Doe", 5)
    book2 = Book(2, "Data Structures and Algorithms", "Jane Smith", 3)

    library.add_book(book1)
    library.add_book(book2)

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Display Borrowed Books")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book_id = int(input("Enter Book ID to borrow: "))
            library.borrow_book(book_id)
        elif choice == "3":
            library.display_borrowed_books()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
