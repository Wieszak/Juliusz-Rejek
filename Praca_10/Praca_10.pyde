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

def setup():
    size(220,100)
    global library, Madzia, Juliusz
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Koralina"]
    library = Library(books) 
    Madzia = Customer()
    Juliusz = Customer() #w programowaniu chodzi o to, aby nie powielać! Po to są klasy, by mnożyć ich obiekty i nie trzeba było pisać funkcjonalności wielokrotnie.
    
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
            library.lendBook(Juliusz.requestBook("Koralina")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            library.addBook(Juliusz.returnBook()) # tu też nie trzeba powielać warunków        
            
class ZadanieDziesiate(unittest.TestCase):

    def test_JR(self): # zapomniałąm nadmienić, że testy muszą się zaczynać tym przedrostkiem
        Juliusz = Customer()
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books) # to przypisanie, a powinno być porónanie i to najlepiej przez asercję


    def test_JR_2(self): # lepszą nazwą byłoby np. test_wypożyczenia
        Juliusz = Customer()
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books)
        library.lendBook(Juliusz.requestBook("Harry Potter"))
        self.assertEqual(["Naocznosc", "Sens Sztuki"], library.availableBooks)
        self.assertEqual(Juliusz.book, "Harry Potter")
        self.assertTrue(Juliusz.haveBook)

    def test_JR_3(self): # lepszą nazwą byłoby np. test_dodania_ksiazki
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books)
        library.addBook("Marsjanin")
        self.assertEqual(["Naocznosc", "Sens Sztuki", "Harry Potter", "Marsjanin"], library.availableBooks)
        
if __name__ == '__main__':
    unittest.main()
    
#1,25pkt
