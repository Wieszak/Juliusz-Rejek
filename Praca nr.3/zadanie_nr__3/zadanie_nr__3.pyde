def setup():
    size(400, 400)
    background(20, 74, 207)
    fill(100)
    textSize(200)
    textAlign(CENTER)
    text("J", width/2-50, height/2)
    text("R", width/2+50, height/2)
    
    noStroke()
    smooth()
    fill(255, 0, 0, 160)
    ellipse(210, 225, 200, 100) # do kształtów niestandardowych tego zaliczyć nie moge
    

def draw():
    if (mousePressed == True): # miało być na najechanie, a nie kliknięcie w dowolnym miejsu
        text("J", width/2-50, height/2)
        text("R", width/2+50, height/2)
        fill(204, 102, 0)
    else:
        fill(0)
        
    if keyPressed: #nie ma potrby dublowania, wszędzie, gdzie jest wytabowane pod obowiązuje
        if (keyCode == LEFT): # jednocześnie z zaznaczeniem miały działać strzałki
            fill(76)
            text("J", width/2-50, height/2)
            fill(144)
            text("R", width/2+50, height/2)
        if (keyCode == RIGHT):
            fill(76)
            text("R", width/2+50, height/2)
            fill(144)
            text("J", width/2-50, height/2)
        fill(0)
        if key == 'j' or key == 'J':
            text("J", width/2-50, height/2)
        if key == 'r' or key == 'R':
            text("R", width/2+50, height/2)

    # 1pkt    
