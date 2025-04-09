import numpy as np

dati = np.arange(10,50) #qua è un metodo e vanno tonde le parantesi
print("forma del tipo di dato", dati.dtype)

#per cambiare il tipo di dato, da intero a decimale
#np.array serve per generare un array 
#np.float64 o "float64" meglio il secondo però
dati_nuovo = np.array(dati, dtype = "float64") #qui potevi mettere ([10,49]) invece di dati e le parentesi quadrate sono proprio il range
print("array float:\n", dati_nuovo)
print("forma del tipo di dato nuovo", dati_nuovo.dtype)


print("forma dell'array", dati.shape)
print("ecco l'array:\n", dati) #\n serve per andare a capo quando vedi l'output