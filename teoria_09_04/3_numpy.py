import numpy as np
arr = np.array ([0,1,2,3,4,5,6,7,8,9])
print(arr)

#come tagliare gli elementi (slicing) 

#indicizzare serve per riportare pezzi di elementi. 
print(arr[2])

#slicing
print(arr[2:4])

#boolean indexing
#print(arr[arr > 3])
#3 è l'indice non il numero

#slicing sulle righe e colonne e misto
arr_2 = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])
print(arr_2)

#slicing sulle righe
print(arr_2[1:3])
#sulle colonne
print(arr_2[:, 1:3])
#slicing misto
print(arr_2[1:, 2:3])


#per lo slicing ci sono quello base, quello con passo
#con passo
print(arr[1:8:2])

#omettere start e stop
print(arr[:5])
print(arr[5:])

#utilizzare indici negativi
print(arr[-5:]) #stamperà cinque numeri, li parte a prendere dal fondo. Però li scrive in ordine. Questo parte da 5
print(arr[:-5]) #prende i numeri dall'inizio.  Questo finisce a 5. 

#fancy indexing

arr_4 = np.array([10,20,30,40,50])
#utilizzare indici dell'array
indici = np.array([1,3])
print(arr_4[indici])

#utilizzare lista di indici
indices = [0,2,4]
print(arr_4[indices])