import unittest

class Library(): 
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): 
        if requestedBook in self.availableBooks: 
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): 
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): 
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer(): 
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
        
class JulekR():
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False


def setup():
    size(220,100)
    global library, Madzia, Juliusz
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Koralina"]
    library = Library(books) 
    Madzia = Customer()
    Juliusz = JulekR()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) 
    rect(100,40,100,20) 
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked(): 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            
def mouseClicked():
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Juliusz.requestBook("Koralina")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Juliusz.returnBook())
            
class ZadanieDziesiate(unittest.TestCase):

    def JR(self):
        self.Juliusz = Customer()
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        self.library = Library(books) 


    def JR_2(self):
        self.library.lendBook(self.Juliusz.requestBook("Harry Potter"))
        self.assertEqual(["Naocznosc", "Sens Sztuki"], self.library.availableBooks)
        self.assertEqual(self.Juliusz.book, "Harry Potter")
        self.assertTrue(self.Juliusz.haveBook)

    def JR_3(self):
        self.library.addBook("Marsjanin")
        self.assertEqual(["Naocznosc", "Sens Sztuki", "Harry Potter", "Marsjanin"], self.library.availableBooks)
