def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("dopo l'esecuzione della funzione")
    return wrapper

#restituzione di una funzione modifica. Non si cambia il codice di prima quindi. 
@decoratore
def saluta(): #è la funzione modificata
    print("ciao")
saluta() #si mette la riga 9 e 10 al posto della 4. Cioè viene presa la definizione saluta come parametro. 