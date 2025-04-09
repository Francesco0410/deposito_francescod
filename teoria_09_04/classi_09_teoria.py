class Automobile():                                #la classe
    num_ruote = 4                                #attributo della classe. Questo rimuove fisso per la classe
    def __init__(self,marca,modello):            #metodo costruttore
        self.marca = marca                       #attributo di istanza, questo cambierà per ogni auto ovviamente
        self.modello = modello                   #attributo di istanza, come marca il modello cambierà 
    def stampa_info(self):                       #metodo di istanza
        print("L'auto è una", self.marca, self.modello)

car = Automobile("Seat","Ibiza business")
print(car.marca)
print(car.modello)

car.stampa_info()

class Calcolatrice():              #metodo statico 
    @staticmethod               #decoratore
    def somma(a,b):             #somma è un metodo 
        return a+b              
risultato = Calcolatrice.somma(5,3)     #viene scritta la classe invece dell'oggetto. #la grande differenza sta nel fatto che viene richiamata la classe e non l'oggetto. 

print(risultato)
    


