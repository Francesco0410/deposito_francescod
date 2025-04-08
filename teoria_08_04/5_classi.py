class Esempio(): #la prima lettera va scritto in maiuscola
    x = 10
    
#se voglio usare x devo creare un oggetto
oggetto1 = Esempio() #oggeto 1 è un oggetto della classe esempio
#non avendo nessun paramentro non scrivo init
oggetto1.x= 20 #per modificare l'attributo
print(oggetto1.x) #qua metterà 20

#la classe è univoca
#gli oggetti sono infiniti
#posso avere 
oggetto2= Esempio()
oggetto2.x= 50
print(oggetto2.x)

class Penna():
    altezza = 0
    larghezza = 0 #partono tutte a zero. Poi con il costruttore si decide quanto devono essere ogni penna che avrà ognuna un altezza, larghezza e ovviamente un nome. 
    
    #__init__ è il Costruttore, che è un metodo SPECIALE (inizializzare significa costruire)
    def __init__(self,h,l): #si chiama init e non la classe, non sa a quale riferirsi. 
        self.altezza = h
        self.larghezza = l


#self rappresenta l'oggetto stesso. Perchè altrimenti come lo capisce?
oggettopenna = Penna(10, 7)
bic = Penna(5,4)

print(oggettopenna.altezza)
print(oggettopenna.larghezza)

print(bic.altezza)
print(bic.larghezza)

