class Libro():
    def __init__(self,titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def visualizzare (self):
        print(f"Il titolo è {self.titolo}, l'autore è {self.autore} e le pagine sono {self.pagine}")

#prova1 = Libro("Nuovo libro per economia", "Francesco", 1)
#manca qualcosa 