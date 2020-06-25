def setup():

    global img
    size(1200/2, 1600/2)
    noFill()

def draw():
 
    global img
    img = loadImage("wisz.png")
    try:
        image(img, 50,100, 500,500) 
        f = open("wisz.png")
        if f.name == 'wisz.png':
            raise Exception


    except:
        print ("Error!")
        rect(20, 75,555,555)
        stroke(255,0,0,90)
    
    else:
        rect(20, 75,555,555)
        stroke(0,0,255,90)

# 0,25pkt i przeanalizuj co się pozmieniałam, że działa
