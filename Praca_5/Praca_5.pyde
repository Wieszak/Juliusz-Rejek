global cWidth
global cHeight
cWidth = 600
cHeight = 600
class Player(object): # nazwa klasy zwyczajowo z dużej litery, a dziedziczenie po object jest wskazane w pythonie ver. 2
    down = 0 # jako argument klasy będą wspólne dla wszystkich playerów - obiektów tej klasy
    left = 0
    right= 0
    up   = 0
    def __init__(self, x = 1000, y = 1000): #teraz są argumentami można je zmienić dla różnych playeró, a jeśli nie - zostaną defaultowe
        self.x = x
        self.y = y
        self.speed= 5
        self.h = 20
        self.w = 20
    def show(self):
        fill(0)
        rect(self.x,self.y,self.w,self.h)
    def update(self):
        self.x = self.x + (Player.right - Player.left)*self.speed
        self.y = self.y + (Player.down - Player.up)*self.speed
        if not (self.x >= 0):
            self.x = 0
        if not (self.x <= (cWidth - self.w)):
            self.x = (cWidth - self.w)
        if not (self.y >= 0):
            self.y = 0
        if not (self.y <= (cHeight - self.h)):
            self.y = (cHeight - self.h)


def setup():
    size(cWidth,cHeight)
    global p1, p2
    p1 = Player(200, 200) # miały być stworzone dwa obiekty, co zreztą uwidoczniłoby pewne problemy
    p2 = Player()
    
def draw():
    background(100)
    p1.show()
    p1.update()
    p2.show()
    p2.update()
    
def keyPressed():
    if keyCode == UP:
        Player.up=1
    if keyCode == DOWN:
        Player.down=1
    if keyCode == LEFT:
        Player.left=1
    if keyCode == RIGHT:
        Player.right=1
        
def keyReleased():
    if keyCode == UP:
        Player.up=0
    if keyCode == DOWN:
        Player.down=0
    if keyCode == LEFT:
        Player.left=0
    if keyCode == RIGHT:
        Player.right=0
        
# 1,75pkt
