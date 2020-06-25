from abc import ABCMeta, abstractmethod 
class Pet():
    __metaclass__=ABCMeta
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'

class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('how how', random(50, width-70), random(50, height-50))
        return 'how how'
    def gimmePaw(self):
        image(loadImage("piesel.png"), random(50, width-70), random(50, height-50))
    def __add__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
class Bunny(Pet):
    pass

class Pies(Pet):
     def __init__(self, name):
        self.name = name
     def speak(self):
        text('woof woof', random(50, width-70), random(50, height-50))
        return 'woof woof'
  
def setup():
    size(600,600)
    textSize(20)
    pero = Pies('Pero')
    brown = Dog('Brown')
    global list_of_pets
    list_of_pets = [brown, pero] 
    print(isinstance(pero, Pet))
    print(brown+pero)
   
def draw(): 
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Dog): 
            pet.gimmePaw()

# 1pkt, brak chodźby nadpisania odejmowania
