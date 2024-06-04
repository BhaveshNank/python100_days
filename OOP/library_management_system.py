'''Here we are assuming that the library also have some books 
and going to do some hard coding to put those book into the library

solution: 
1) create function signatures with pass in it only
2) try for one book only'''

class Library:

    def __init__(self, books, no_of_books):
        self.books = books
        self.no_of_books = int(no_of_books)

    def display_book(self): # where books is a dictionary
        self.books = books
        book_names = list(self.books.keys())
        print("\n".join(book_names))

    def addBook(self, key, value):
        self.books[key] = value
        self.no_of_books += 1

    def getNoOfBook(self): 
        print(self.no_of_books)  


books = {'Think like monk': 'Jay Shetty',
         'The richest man in Babylon' : 'George S. Clason',
         'The power of your Subconsious mind': 'Dr Joseph Murphy',
         'Handbook python with DSA' : 'Pranay Bhute'}

oxford_street = Library(books, 4)
oxford_street.display_book()
oxford_street.getNoOfBook()
oxford_street.addBook('Java - A beginners guide', 'Herbert Schildt')
print()
oxford_street.display_book()
oxford_street.getNoOfBook()