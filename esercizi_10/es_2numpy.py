import numpy as np
class Gestionearray:
    def __init__(self, start, stop, num_elements):
        self.arr = np.linspace(start, stop, num_elements)
        self.arr_2 = np.random.rand(num_elements) #perchè rand genera tra 0 e 1, quindi serve mettere il numero di elementi che ti servono quindi metti quell'attributo 
    
    
    def operazioni(self):
        self.somm_elem = self.arr + self.arr_2 #qua fa la somma degli elementi, qunidi c'è un nuovo array
        self.arr_3 = np.sum(self.somm_elem)  #qui fa la somma dell'array 
        self.mag_5_arr_3 = np.sum (self.somm_elem[self.somm_elem > 5])  #qui fa la somma dei valori che sono maggiori di 5
        return self.arr_3, self.mag_5_arr_3

        
    def stampa_info(self):
        print(f"Gli Array originali sono {self.arr} e \n {self.arr_2} e le somme calcolate sono {self.arr_3} e \n {self.mag_5_arr_3}")
    
    
    
test = Gestionearray(0,10,50)

test.operazioni()
test.stampa_info()

