def setup():
    size(800, 600)
    global natezenie
    natezenie = 0
    global index
    index = 0
    frameRate(8)
    global szerokosc
    szerokosc = 0
    global wysokosc
    wysokosc = 0

def draw():
    fill(random(255), 0, 0)
    rect(wysokosc, szerokosc, 100, 100)
    global wysokosc
    wysokosc = wysokosc + 1
    lista = []
    global index
    
def mousePressed():
    exit()
    


        
    
