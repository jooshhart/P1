from book import Book

class Library:
    def __init__(self):
        self.books = []

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for idx, book in enumerate(self.books, 1):
                status = "Checked out" if book.checked_out else "Available"
                print(f"{idx}. {book} - {status}") 
    def save_books(self, filename): #a command called "open is used, and filename is used"
        with open(filename, "w") as f:
            for book in self.books:
                # Format: title|author|checked_out
                f.write(f"{book.title}|{book.author}|{book.checked_out}\n")

    def load_books(self, filename):
        self.books = []
        try:
            with open(filename, "r") as f:
                for line in f:
                    title, author, checked_out = line.strip().split("|")
                    book = Book(title, author)
                    book.checked_out = checked_out == "True"
                    self.books.append(book)
        except FileNotFoundError:
            pass  # No file yet, start with empty library