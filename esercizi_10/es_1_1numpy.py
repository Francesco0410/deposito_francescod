import numpy as np
arr = np.linspace(0,1,12) #array di valori tra 0 e 1, 12 numeri
print(arr)

arr_2 = arr.reshape(3,4) #modifica, array con 3 righe e 4 colonne

arr_3 = np.random.rand(3,4) #numeri randomici 3 righe e 4 colonne

print(arr_3)
somma_arr_2= np.sum(arr_2)
somma_arr_3 = np.sum(arr_3)

print(f"somma 1 e 2 sono rispettivamente {somma_arr_2} e {somma_arr_3}")

class Generaarray:
    def __init__(self, start, stop, num_elements, rows, cols):
        self.arr = np.linspace(start, stop, num_elements)
        self.arr_2 = self.arr.reshape(rows, cols)
        self.arr_3 = np.random.rand(rows, cols)
    
    def calcola_som(self):
        somma_arr_2 = np.sum(self.arr_2)
        somma_arr_3 = np.sum(self.arr_3)
        return somma_arr_2, somma_arr_3
    
    def stampa_info(self):
        print(f"la somma dell'array 2 è: {somma_arr_2} e dell'array 3 è: {somma_arr_3}")
    
    

nuov_arr = Generaarray (0,1,12,3,4)
nuov_arr.stampa_info()