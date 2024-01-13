
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.availability = True

class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def removeBook(self, book):
        self.books.remove(book)

    def checkAvailability(self, book):
        if book in self.books:
            if book.availability:
                print(book.name,"is available")
            else:
                print(book.name,"is unavailable ")
        else:
            print( "Book not found in the library.")

class Member:
    def __init__(self, name):
        self.name = name
        self.substatus = True

    def borrowBook(self, book):
        if book.availability and self.substatus:
            book.availability = False
            print(self.name," has borrowed",book.name,'book by',book.author) 
        else: 
            print("Book is unavailable for borrowing or member's subscription is inactive.")

    def returnBook(self, book):
        if not book.availability:
            book.availability = True
            print( f"{self.name} has returned {book.name } book by {book.author}.")
        else:
            print( "Book is already available.")

book1 = Book("java","rohit")
book2 = Book("python","PeakyMemers")

library = Library()
library.addBook(book1)
library.addBook(book2)

member1 = Member("Meghana")
member1.borrowBook(book1)
library.checkAvailability(book1)
member1.returnBook(book1)
library.checkAvailability(book1)
