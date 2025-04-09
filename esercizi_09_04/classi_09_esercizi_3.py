class Libro():
    def __init__(self,titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def visualizzare_libro (self):
        print(f"Il titolo è {self.titolo}, l'autore è {self.autore} e le pagine sono {self.pagine}")
        
class Biblioteca():
    numero_libri = []
    def __init__(self):
        self.numero_libri = []  #questa è una lista
    
    def aggiungere_libro(self,titolo, autore, pagine):
        nuovo_libro= Libro(titolo,autore,pagine)
        self.numero_libri.append(nuovo_libro)
    
    def numero_libri_stampa(self):
        print(f"Nella biblioteca ci sono:")
        for libri in self.numero_libri:
            libri.visualizzare_libro()
            
biblioteca = Biblioteca() #creazione di biblioteca fuori dal menu
        
while True:
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci l'autore: ")
    pagine = int(input("inserisci il numero delle pagine "))
    
    
    biblioteca.aggiungere_libro(titolo, autore, pagine)
    biblioteca.numero_libri_stampa()
    
    inserire = input("vuoi inserire un altro libro?")
    if inserire.lower == "si":
        continue
    else:
        break

