def setup():
    size(800, 600)
    background(255, 10, 20)
def draw():
    line(mouseX, mouseY, 500, 500)
    print(mouseX, mouseY, mousePressed)
    rect(100, 100, 100, 100)
    rect(50, 40, 80, 80)
    if mousePressed:
        rect(width/2, height/2, 250, 250)
        rect(70, 20, 70, 70)
        line(500, 900, 500, 500)
        circle(350, 350, 100)
