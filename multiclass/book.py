class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def __str__(self):
        return f'"{self.title}" by {self.author}'