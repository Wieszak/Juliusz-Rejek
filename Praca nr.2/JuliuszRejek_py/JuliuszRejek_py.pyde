def setup():
    size(500, 500)
    #global natezenie # nie używasz
    #natezenie = 0
    #global index # nie używasz
    #index = 0
    frameRate(120)
    global szerokosc
    global wysokosc
    szerokosc = 250 #zmienne po za funkcjami nie wiadomo kiedy się zadeklarują, jeżeli umieścimy je w setup, mamy pewność, że przy starcie programu.
    wysokosc = 500

def draw():
    fill(random(255), 0, 0) # ładne obejście x)
    rect(szerokosc, wysokosc, 35, 35)
    global wysokosc
    wysokosc += 1
    # lista = [] # nie używasz jej, to po co tworzyć?
    #global index
    global szerokosc
    szerokosc += 1
    if szerokosc > width/2: # teraz lepiej widać, że chodzi o środek szerokości, tylko zamiast 'szerokość' lepiej stan oddawałąby np. nazwa 'aktualna_szerokosc'
        wysokosc += -2
    if wysokosc < height/2:
            szerokosc += -2
def mousePressed():
    exit()
    
#1,25p, miały być powtórzone kolekcje do zmiany koloru, a tu w ogóle je pominąłeś
    
    
    


        
    
