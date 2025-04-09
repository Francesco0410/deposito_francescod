import numpy as np
#dtype solo in alcuni casi devi scrivere il tipo di dato o 64 o 32

#shape porta il numero massimo di righe e colonne (se abbiamo dati (2,3) e (4,5,6,7) sarà 2 x 4)

#arange da 0 a 10
arr = np.arange(6,0,-1)  #funziona come il range di python (start, stop, step). Nello stop considera sempre il valore prima di quello che hai inserito
print("Ho creato array da 0 a 5 monodimensionale:", arr)

#reshape
reshaped_arr= arr.reshape((2,3))
print("Ho modicato la shape di arr:\n",reshaped_arr)

