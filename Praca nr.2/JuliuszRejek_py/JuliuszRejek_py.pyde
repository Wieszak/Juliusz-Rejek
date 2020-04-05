szerokosc = 250
wysokosc = 500

def setup():
    size(500, 500)
    global natezenie
    natezenie = 0
    global index
    index = 0
    frameRate(120)
    global szerokosc
    global wysokosc


def draw():
    fill(random(255), 0, 0)
    rect(szerokosc, wysokosc, 35, 35)
    global wysokosc
    wysokosc += 1
    lista = []
    global index
    global szerokosc
    szerokosc += 1
    if szerokosc > 250:
        wysokosc += -2
    if wysokosc < 250:
            szerokosc += -2
def mousePressed():
    exit()
    
    
    


        
    
