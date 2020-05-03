add_library("pdf")

def setup():
    global img
    global i
    size(198, 255)
    img=loadImage("zdjecie.jpg")
    i = loadImage("okulary.png") # lepiej wczytać raz niż co klatkę
    imageMode(CENTER)
    beginRecord(PDF, "pdfik.pdf")
    image(img, width/2, height/2)
    
def draw():
    global img
    global i
    if (mousePressed == True):
        image(i, width/2, 135, 140, 70)
        endRecord()
# brakuje wariantu
# 1,5p
