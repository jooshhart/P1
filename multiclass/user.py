class User:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow_book(self, book):
        if not book.checked_out:
            self.books.append(book)
            book.checked_out = True
            print(f"{self.name} borrowed {book}")
        else:
            print(f"{book} is already checked out.")

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)
            book.checked_out = False
            print(f"{self.name} returned {book}")
        else:
            print(f"{self.name} does not have {book}.")

# Inheritance: Librarian is a User with extra powers
class Librarian(User):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book):
        library.books.append(book)
        print(f"{self.name} added {book} to the library.")