from book import Book
from user import User, Librarian
from library import Library

FILENAME = "library_books.txt"

def main():
    library = Library()
    library.load_books(FILENAME)
    librarian = Librarian("Ms. Smith")
    user = User("Alice")

    while True:
        print("\n--- Library Menu ---")
        print("1. List books")
        print("2. Add book")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Save and exit")
        choice = input("Choose an option: ")

        if choice == "1":
            library.list_books()
        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            librarian.add_book(library, book)
        elif choice == "3":
            library.list_books()
            idx = input("Enter book number to borrow: ")
            if idx.isdigit() and 1 <= int(idx) <= len(library.books):
                book = library.books[int(idx)-1]
                user.borrow_book(book)
            else:
                print("Invalid selection.")
        elif choice == "4":
            if not user.books:
                print("You have no books to return.")
            else:
                print("Your borrowed books:")
                for i, book in enumerate(user.books, 1):
                    print(f"{i}. {book}")
                idx = input("Enter book number to return: ")
                if idx.isdigit() and 1 <= int(idx) <= len(user.books):
                    book = user.books[int(idx)-1]
                    user.return_book(book)
                else:
                    print("Invalid selection.")
        elif choice == "5":
            library.save_books(FILENAME)
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()