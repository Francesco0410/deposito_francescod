import numpy as np #as np è convenzione, tutti lo chiamano np. 
#creazione di un array monodimensionale
arr = np.array([1,2,3,4,5,6])
print(arr)

#mentre questo è un array multidimensionale
#array è un metodo in questo caso. Ha le parentesi tonde, che sono del metodo le tonde. 
#la classe è numpy
arraymult = np.array([[1,2,3],[4,5,6]])   #Con le parantesi quadrate, vuol dire che c'è un contenitore che contiene due contenitori. Quello dentro ci sono i parametri
print(arraymult)


#utilizzi di altri metodi
print("forma dell'array:", arr.shape)     # ---> ci restituisce la forma e devi usarlo se vuoi avere il numero di colonne (prima le righe, poi colonne)
print("Dimensioni dell'array:", arr.ndim) # Output: 1.  --> con ndim si intende il numero di dimensioni (quante righe ha questa tabella)
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)  ---> sta per intero a 64 bit. 
print("Numero di elementi:", arr.size) # Output: 5  --> il totale dei numero di elementi  
print("Somma degli elementi:", arr.sum()) # Output: 15 
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5. 
print("Indice del valore massimo:", arr.argmax()) # Output: 4. ---> #argmax = da come risultato la posizione del numero massimo. 
