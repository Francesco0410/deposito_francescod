class Contatore():
    numero_istanze = 0 #questa è la variabile della classe. 
    def __init__(self): #oggetto è self (se stesso)
        Contatore.numero_istanze += 1 #qua serve a contare quanti oggetti hai creato
    @classmethod #questo decoratore permette alla classe di prendere di riferimento non se stessa come oggetto ma se stessa come classe. è legata al metodo della classe. 
    def mostra_num_istanze(cls): #cls può essere anche pippo
        print(f"Sono state create {cls.numero_istanze} istanze") #con f sta per format. 
    

#creazione di alcune istanze
#self serve per indicare il nome dell'oggetto/istanza. 
c1 = Contatore() #nelle parantesi non ci sono gli attributi perchè c1 non avrà attributi. VIsto che dopo self nella riga dove c'è init, dopo il self non c'è niente. 
c2 = Contatore()
c3 = Contatore()

#output
Contatore.mostra_num_istanze()
