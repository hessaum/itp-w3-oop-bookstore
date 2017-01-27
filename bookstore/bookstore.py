class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def get_books(self):
        return self.books
    
    def add_book(self, book):
        self.books.append(book)

    def search_books(self, title=None, author=None):
        result = []
        for book in self.books:
            if ((title != None) and (title.lower() in book.title.lower())) or\
            ((author != None) and (author == book.author)):
                result.append(book)
        return result

"""
    def search_books(self, book_title):
        return [book for book in self.books if book_title in book.title.lower()]
"""

class Author(object):
    def __init__(self, author, nationality):
        self.name = author
        self.nationality = nationality
        self.books = []
    
    #returns a boolean value if equal
    def __eq__(self, other):
        return self.name == other.name and self.nationality == other.nationality
        
    def get_books(self):
        return self.books


class Book(object):
    def __init__(self, bookname, author):
       self.title = bookname
       self.author = author
       #appends this current isntance of the Book class to the isntance  
       #of the Author class
       author.books.append(self)
