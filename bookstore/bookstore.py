class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
      
    def get_books(self):
        return self.books
        
    def add_book(self, book):
        self.books.append(book)
        
    def search_books(self, title=None, author=None):
        rtn_list = []
        if not author and not title:
            print("oh no")
        elif author == None:
            for book in self.books:
                if title.lower() in book.title.lower():
                    rtn_list.append(book)
        elif title == None:
            for book in self.books:
                if author.name.lower() in book.author.name.lower():
                    rtn_list.append(book)
        else:
            for book in self.books:
                if title.lower() in book.title.lower() and author.name.lower() in book.author.name.lower():
                    rtn_list.append(book)
                    
        return rtn_list
    
        

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.titles = []
        
    def get_books(self):
        return self.titles
        
        


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.titles.append(self)
        
        
        
        
#my_bookstore.books[0].author.name