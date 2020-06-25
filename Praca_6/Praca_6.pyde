class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class KolorowyKwadrat(Kwadrat):
    def sketchKolorowy(self, x, y):
         fill(random(255), 0, 0) # albo kolorujez randomowo, albo przekazujesz argument z koleorem i go używasz
         Kwadrat.sketch(self, x, y) # to wystarczy, wywoływałeś to samo 4ry razy różnym zapisem
    
def setup():
    size(500, 500)
    malyKolorowyKwadrat = KolorowyKwadrat(30.0) 
    malyKolorowyKwadrat.sketchKolorowy(random(225), 125) 
    malyKolorowyKwadrat.sketchKolorowy(random(143),268) 
    duzyKolorowyKwadrat = KolorowyKwadrat(120.0)
    duzyKolorowyKwadrat.sketchKolorowy(random(275), 36)
    duzyKolorowyKwadrat.sketch(random(250), 300)
    
# po za tym, że już u kogoś widziałam identyczne absurdalne błędy, co nie może być przypadkiem, 
# 1pkt
