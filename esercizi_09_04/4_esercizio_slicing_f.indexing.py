import numpy as np
arr = np.random.randint(10,51, size = 20)
print(arr)

#per visualizzare i primi 10
print(arr[:10])

#per visualizzare gli ultimi 5
print(arr[-5:])

#per estrarre gli elementi dall'indice 5 all'indice 15(escluso)
print("Elementi estratti:",arr[5:15])

#slicing per estrarre ogni terzo elemento dell'array
print(arr[:20:3])

#modificare tramite lo slicing gli elementi dall'indice 5 all'indice 10 escluso assegnando il valore 99
arr_2 = arr
arr_2[5:10]= 99 
print("Elementi mdificati:",arr_2)