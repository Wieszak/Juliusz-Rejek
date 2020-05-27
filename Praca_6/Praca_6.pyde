class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class KolorowyKwadrat(Kwadrat):
    def sketchKolorowy(self):
        Kwadrat.sketch(self, x, y)
    def sketchKolorowy(self, x, y, kolory):
         Kwadrat.sketch(self, x, y)
         fill(random(255), 0, 0)
         rect(self.x, self.y, self.bok, self.bok)
    
def setup():
    size(500, 500)
    malyKolorowyKwadrat = KolorowyKwadrat(30.0) 
    malyKolorowyKwadrat.sketchKolorowy(random(225), 125, 5) 
    malyKolorowyKwadrat.sketchKolorowy(random(143),268, 7) 
    duzyKolorowyKwadrat = KolorowyKwadrat(120.0)
    duzyKolorowyKwadrat.sketchKolorowy(random(275), 36, 15)
    duzyKolorowyKwadrat.sketch(random(250), 300) 
