#semantica delle funzioni, ovvero come si scrive
def nomedellafunzione():
    pass #pass serve per non far crashare il programma, in quanto non è stata scritta nessuna funzione

def primafunzione():
    print("Ciao")
    
#funzione con parametri
def secondafunzione(x,y,z):
    #sono i placeholder, sono i contenitori delle variabili
    risultato = x + y + z
    print(risultato)
    
secondafunzione(1,2,3) 
#bisogna scrivere i 3 dati in questo caso al posto dei placeholder.

def salutare(nome):
    print("Ciao", nome)
    
salutare("Francesco")

def funzione_3(x): #def funzione_alt()
    return 2*x     #x = input()
                    #return 2*x 

print(funzione_3(4))
#secondafunzione l'avevamo definita prima ed è una somma. Hai fatto una funzione, con altre funzioni. 
secondafunzione(funzione_3(4), funzione_3(4), funzione_3(4))


#funzione con parametri standard
def funzione_standard(x = 1):
    return x+x #serve per evitare che qualcuno sbagli. Si usa raramente.
