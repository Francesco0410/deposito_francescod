class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def muovi (self,nuova_x,nuova_y):
        if nuova_x > self.x and nuova_y > self.y:
            self.x = nuova_x #modifica la coordinata x
            self.y = nuova_y #modifica la coordinata y
            print(f"Le distanze adesso sono {self.x} e {self.y}")
        else:
            print(f"il valore è negativo")
    def distanza (self,diff_x,diff_y):
        diff_x = self.nuova_x- self.x
        diff_y = self.nuova_y - self.y
        print(f"La differenza delle x è:"{diff_x})
        print(f"La differenza delle y è:"{diff_y})
        
    